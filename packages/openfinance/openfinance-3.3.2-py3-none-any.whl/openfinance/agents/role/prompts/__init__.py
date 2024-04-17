from openfinance.agents.role.prompts.catherine_wood import Catherine_Wood_PROMPT
from openfinance.agents.role.prompts.ray_dalio import Ray_Dalio_PROMPT
from openfinance.agents.role.prompts.warren_buffett import Warren_Buffett_PROMPT
from openfinance.agents.role.prompts.elon_musk import ELON_MUSK_PROMPT
from openfinance.agents.role.prompts.valuation_investor import valuation_PROMPT
from openfinance.agents.role.prompts.quant_investor import quant_PROMPT
from openfinance.agents.role.prompts.growth_investor import growth_PROMPT

roles_prompts = {
    "Catherine Wood": Catherine_Wood_PROMPT,
    "Ray Dalio": Ray_Dalio_PROMPT,
    "Elon Musk": ELON_MUSK_PROMPT,
    "Warren Buffett": Warren_Buffett_PROMPT,
    "Value Investor": valuation_PROMPT,
    "Growth Investor": growth_PROMPT,    
    "Quant Investor": quant_PROMPT
}