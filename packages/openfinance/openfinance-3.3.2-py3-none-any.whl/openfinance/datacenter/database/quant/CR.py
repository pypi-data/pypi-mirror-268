from openfinance.datacenter.database.quant.utils import get_data
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.source.eastmoney.util import (
    get_code_id
)
# export PYTHONPATH=$PYTHONPATH:/public/openfinance-main
# des 10个词左右
@register(name="Intermediate Willingness Index(CR)", description="reflect the market's willingness to buy and sell")
def CR(stock_id, **kwargs):
    try:
        if not stock_id.isdigit():
            stock_id = get_code_id(stock_id)[2:]    
        n_periods = kwargs['n_periods'] if 'n_periods' in kwargs else 10
        return_info = "CR Values:if values always above 1 means the market is in a strong market; if values often runs below 1, the market is in a weak market.\n"
        return_info += "If readings falls below 0.4, the chance of the stock price forming a bottom is quite high.\n"
        return_info += "When CR is higher than 3-4, the stock price can easily reverse downward."
        return_info += "The values in period of days and weeks are given below:\n"
        df = {}
        df['days'] = get_data(stock_id, freq='days', n_periods=n_periods)[['date', 'CR']]
        df['weeks'] = get_data(stock_id, freq='weeks', n_periods=n_periods)[['date', 'CR']]

        for freq in ['days', 'weeks']:
            return_info += f"{freq}:{df[freq]['CR'].round(1).tolist()}, " + "\n"

        return return_info
    except:
        return f"No CR data"  
if __name__ == "__main__":
    result = CR('000001', n_periods=30)
    print(result)
    