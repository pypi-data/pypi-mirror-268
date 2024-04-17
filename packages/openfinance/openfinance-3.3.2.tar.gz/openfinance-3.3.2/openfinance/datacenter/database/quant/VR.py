from openfinance.datacenter.database.quant.utils import get_data
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.source.eastmoney.util import (
    get_code_id
)
# export PYTHONPATH=$PYTHONPATH:/public/openfinance-main
# des 10个词左右
@register(name="Volume Ratio (VR)", description="analyze the relationship between the volume of buying and selling")
def VR(stock_id, **kwargs):
    try:
        if not stock_id.isdigit():
            stock_id = get_code_id(stock_id)[2:]    
        n_periods = kwargs['n_periods'] if 'n_periods' in kwargs else 10
        return_info = "VR: VR value ranges from 0 to infinity, with values above 1 indicating a bullish trend and values below 1 indicating a bearish trend."
        return_info = "A value of 1 suggests that buyers and sellers are evenly matched\n"
        return_info += "The values in period of days and weeks are given below:\n"
        df = {}
        df['days'] = get_data(stock_id, freq='days', n_periods=n_periods)[['date', 'VR']]
        df['weeks'] = get_data(stock_id, freq='weeks', n_periods=n_periods)[['date', 'VR']]

        for freq in ['days', 'weeks']:
            return_info += f"{freq}:{df[freq]['VR'].round(1).tolist()}, " + "\n"

        return return_info
    except:
        return f"No VR data"  
if __name__ == "__main__":
    result = VR('000001', n_periods=30)
    print(result)
    