from openfinance.datacenter.database.quant.utils import get_data
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.source.eastmoney.util import (
    get_code_id
)
# export PYTHONPATH=$PYTHONPATH:/public/openfinance-main
# des 10个词左右
@register(name="Buy Ratio", description="identify potential buy signals and confirm bullish trends")
def BR(stock_id, **kwargs):
    try:
        if not stock_id.isdigit():
            stock_id = get_code_id(stock_id)[2:]    
        n_periods = kwargs['n_periods'] if 'n_periods' in kwargs else 10
        return_info = "BR:A reading above 300 indicates that the asset maybe over-bought in the market, while a reading below 40 indicates that the asset maybe under estimate and could be in a turn-over stage\n"
        return_info += "The values in period of days and weeks are given below:\n"
        df = {}
        df['days'] = get_data(stock_id, freq='days', n_periods=n_periods)[['date', 'BR']]
        df['weeks'] = get_data(stock_id, freq='weeks', n_periods=n_periods)[['date', 'BR']]

        for freq in ['days', 'weeks']:
            return_info += f"{freq}:{df[freq]['BR'].round(1).tolist()}, " + "\n"

        return return_info
    except:
        return f"No BR data"  
if __name__ == "__main__":
    result = BR('000001', n_periods=30)
    print(result)