from openfinance.datacenter.database.quant.utils import get_data
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.source.eastmoney.util import (
    get_code_id
)
# export PYTHONPATH=$PYTHONPATH:/public/openfinance-main
# des 10个词左右
@register(name="Commodity Channel Index(CCI)", description="indicates a potential trend")
def CCI(stock_id, **kwargs):
    try:
        if not stock_id.isdigit():
            stock_id = get_code_id(stock_id)[2:]    
        n_periods = kwargs['n_periods'] if 'n_periods' in kwargs else 10
        return_info = "CCI: reading above 70 suggests strong upward momentum, while consistent values below -70 might signal a downtrend."
        return_info += "values exceeding +100 or dipping below -100 are considered extreme and might indicate an asset that's overpriced or underpriced\n"
        return_info += "The values in period of days and weeks are given below:\n"
        df = {}
        df['days'] = get_data(stock_id, freq='days', n_periods=n_periods)[['date', 'CCI']]
        df['weeks'] = get_data(stock_id, freq='weeks', n_periods=n_periods)[['date', 'CCI']]

        for freq in ['days', 'weeks']:
            return_info += f"{freq}:{df[freq]['CCI'].round(1).tolist()}, " + "\n"

        return return_info
    except:
        return f"No CCI data"  
if __name__ == "__main__":
    result = CCI('000001', n_periods=30)
    print(result)
    