from openfinance.datacenter.database.quant.utils import get_data
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.source.eastmoney.util import (
    get_code_id
)
# export PYTHONPATH=$PYTHONPATH:/public/openfinance-main
# des 10个词左右
@register(name="BBIC", description="Get volatility and consolidation of stock")
def BBIC(stock_id, **kwargs):
    try:
        if not stock_id.isdigit():
            stock_id = get_code_id(stock_id)[2:]    
        n_periods = kwargs['n_periods'] if 'n_periods' in kwargs else 10
        return_info = "Low BBIC readings below 0.1 indicate low volatility and consolidation. High BBIC readings above 0.3 indicate increased volatility and a stronger trend.\n"
        df = {}
        df['days'] = get_data(stock_id, freq='days', n_periods=n_periods)[['date', 'BBIC']]
        df['weeks'] = get_data(stock_id, freq='weeks', n_periods=n_periods)[['date', 'BBIC']]

        for freq in ['days', 'weeks']:
            return_info += f"{freq}:{df[freq]['BBIC'].round(1).tolist()}, "

        return return_info
    except:
        return f"No BBIC data"        



if __name__ == "__main__":
    result = BBIC('000001', n_periods=30)
    print(result)
    