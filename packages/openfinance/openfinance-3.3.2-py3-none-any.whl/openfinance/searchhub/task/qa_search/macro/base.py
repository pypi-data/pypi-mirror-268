from typing import Any, List, Optional, Sequence, Tuple, Dict

from pydantic import Field

from langchain.agents.agent import Agent, AgentExecutor, AgentOutputParser
from openfinance.searchhub.task.qa_search.macro.prompt import FORMAT_INSTRUCTIONS, PREFIX, SUFFIX
from openfinance.searchhub.task.qa_search.macro import MACRO_ECONOMY
from openfinance.searchhub.task.qa_search.macro.output_parser import StockOutputParser
from openfinance.searchhub.task.qa_search.base import IntentExecutor


from langchain.base_language import BaseLanguageModel
from langchain.callbacks.base import BaseCallbackManager
from langchain.chains.llm import LLMChain
from langchain.prompts.prompt import PromptTemplate
from langchain.schema import AgentAction
from langchain.agents.tools import Tool
from langchain.tools.base import BaseTool
from langchain.agents.utils import validate_tools_single_input
from langchain.callbacks.manager import (
    AsyncCallbackManagerForChainRun,
    AsyncCallbackManagerForToolRun,
    CallbackManagerForChainRun,
    CallbackManagerForToolRun,
    Callbacks,
)
from langchain.schema import (
    AgentAction,
    AgentFinish,
    BaseMessage,
    BaseOutputParser,
)
from langchain.input import get_color_mapping



class StockMacroAgent(Agent):
    """Agent for the StockInformation chain."""

    output_parser: AgentOutputParser = Field(default_factory=StockOutputParser)

    @classmethod
    def _get_default_output_parser(cls, **kwargs: Any) -> AgentOutputParser:
        return StockOutputParser()

    @property
    def _agent_type(self) -> str:
        """Return Identifier of agent type."""
        return "StockFundamentalAgent"

    @property
    def observation_prefix(self) -> str:
        """Prefix to append the observation with."""
        return "Observation: "

    @property
    def llm_prefix(self) -> str:
        """Prefix to append the llm call with."""
        return "Thought:"

    @classmethod
    def create_prompt(
        cls,
        tools: Sequence[BaseTool],
        prefix: str = PREFIX,
        suffix: str = SUFFIX,
        format_instructions: str = FORMAT_INSTRUCTIONS,
        input_variables: Optional[List[str]] = None,
    ) -> PromptTemplate:
        """Create prompt in the style of the zero shot agent.

        Args:
            tools: List of tools the agent will have access to, used to format the
                prompt.
            prefix: String to put before the list of tools.
            suffix: String to put after the list of tools.
            input_variables: List of input variables the final prompt will expect.

        Returns:
            A PromptTemplate with the template assembled from the pieces here.
        """
        tool_strings = "\n".join([f"{tool.name}: {tool.description}" for tool in tools])
        tool_names = ", ".join([tool.name for tool in tools])
        format_instructions = format_instructions.format(tool_names=tool_names)
        template = "\n\n".join([prefix, tool_strings, format_instructions, suffix])
        print(template)
        if input_variables is None:
            input_variables = ["input", "agent_scratchpad"]
        return PromptTemplate(template=template, input_variables=input_variables)

    @classmethod
    def from_llm_and_tools(
        cls,
        llm: BaseLanguageModel,
        tools: Sequence[BaseTool],
        callback_manager: Optional[BaseCallbackManager] = None,
        output_parser: Optional[AgentOutputParser] = None,
        prefix: str = PREFIX,
        suffix: str = SUFFIX,
        format_instructions: str = FORMAT_INSTRUCTIONS,
        input_variables: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> Agent:
        """Construct an agent from an LLM and tools."""
        cls._validate_tools(tools)
        prompt = cls.create_prompt(
            tools,
            prefix=prefix,
            suffix=suffix,
            format_instructions=format_instructions,
            input_variables=input_variables,
        )
        llm_chain = LLMChain(
            llm=llm,
            prompt=prompt,
            callback_manager=callback_manager,
        )
        tool_names = [tool.name for tool in tools]
        _output_parser = output_parser or cls._get_default_output_parser()
        return cls(
            llm_chain=llm_chain,
            allowed_tools=tool_names,
            output_parser=_output_parser,
            **kwargs,
        )

    @classmethod
    def _validate_tools(cls, tools: Sequence[BaseTool]) -> None:
        validate_tools_single_input(cls.__name__, tools)
        for tool in tools:
            if tool.description is None:
                raise ValueError(
                    f"Got a tool {tool.name} without a description. For this agent, "
                    f"a description must always be provided."
                )
        super()._validate_tools(tools)


class StockMacroChain(IntentExecutor):
    """Chain that implements the MRKL system.

    Example:
        .. code-block:: python

            from langchain import OpenAI, MRKLChain
            from langchain.chains.mrkl.base import ChainConfig
            llm = OpenAI(temperature=0)
            prompt = PromptTemplate(...)
            chains = [...]
            mrkl = MRKLChain.from_chains(llm=llm, prompt=prompt)
    """
    intent_name: str = list(MACRO_ECONOMY.keys())[0]

    @classmethod
    def from_chains(
        cls, llm: BaseLanguageModel, tools: List[Tool], **kwargs: Any
    ) -> AgentExecutor:
        """User friendly way to initialize the MRKL chain.

        This is intended to be an easy way to get up and running with the
        MRKL chain.

        Args:
            llm: The LLM to use as the agent LLM.
            tools: The chains the MRKL system has access to.
            **kwargs: parameters to be passed to initialization.

        Returns:
            An initialized MRKL chain.

        """
        agent = StockMacroAgent.from_llm_and_tools(llm, tools)
        return cls(agent=agent, tools=tools, **kwargs)
        
    def _call(
        self,
        inputs: Dict[str, str],
        run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, Any]:
        """Run text through and get agent response."""
        # Construct a mapping of tool name to tool for easy lookup
        name_to_tool_map = {tool.name: tool for tool in self.tools}
        # We construct a mapping from each tool to a color, used for logging.
        color_mapping = get_color_mapping(
            [tool.name for tool in self.tools], excluded_colors=["green"]
        )
        intermediate_steps: List[Tuple[AgentAction, str]] = []
        # We now enter the agent loop (until it returns something).
        next_step_output = self._take_next_step(
            name_to_tool_map,
            color_mapping,
            inputs,
            intermediate_steps,
            run_manager=run_manager,
        )
        print("next_step_output", next_step_output)

        if isinstance(next_step_output, AgentFinish):
            return self._return(
                next_step_output, intermediate_steps, run_manager=run_manager
            )
        
        intermediate_steps.extend(next_step_output)
        if len(next_step_output) == 1:
            next_step_action = next_step_output[0]
            # See if tool should return directly
            tool_return = self._get_tool_return(next_step_action)
            if tool_return is not None:
                return self._return(tool_return, intermediate_steps)

        return {"output": "Sorry! Not found"}
