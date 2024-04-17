import asyncio
from openfinance.config import Config
from openfinance.agents.role.manager import RoleManager
config = Config()

if __name__ == '__main__':
    role_manager = RoleManager(config=config)
    buffett = role_manager.get_role("buffett")  
    print(asyncio.run(
        buffett.acall(
            "--- Season 2022年第3季度 2022年第4季度 2023年第1季度 YoY of Total GDP 3.0 3.0 4.5 YoY of Primary Industry Production 4.2 4.1 3.7 YoY of Secondary Industry Production 3.9 3.8 3.3 YoY of Tertiary Industry Production 2.3 2.3 5.4 --- Month 2023年03月份 2023年04月份 2023年05月份 YoY of Base Currency 12.7 12.4 11.6 YoY of Circulating Currency 11.0 10.7 9.6 --- Month 2023年03月份 2023年04月份 2023年05月份 Sequential of CPI 0.7 0.1 0.2 --- Month 2023年03月份 2023年04月份 2023年05月份 PPI 97.5 96.4 95.4 YoY of PPI -2.5 -3.6 -4.6 --- based on data, which kind of stock should people buy, show more cleary your think path numercialy"
            )))