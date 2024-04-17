from openfinance.agentflow.prompt.base import PromptTemplate

def build_from_name(
    role: str,
    background: str = ""
):
    role_prompt_template = ""
    if not background:
        role_prompt_template += """
        You are {role}, you must answer question in {role}'s tone and think based on {role}'s mind
        """
    else:
        role_prompt_template += """
        You are {role}, you must answer question in {role}'s tone and think based on {role}'s mind
        Background: {background}
        """
    return role_prompt_template