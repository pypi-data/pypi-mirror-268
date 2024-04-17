from openfinance.datacenter.database.quant.utils import get_data
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.source.eastmoney.util import (
    get_code_id
)
# export PYTHONPATH=$PYTHONPATH:/public/openfinance-main
# des 10个词左右
@register(name="VPT", description="indicate whether volume is increasing or decreasing with price")
def VPT(stock_id, **kwargs):
    try:
        if not stock_id.isdigit():
            stock_id = get_code_id(stock_id)[2:]    
        n_periods = kwargs['n_periods'] if 'n_periods' in kwargs else 10
        return_info = "VPT:A rising VPT values indicates volume is aligning with an upward price trend. It suggests long position force is dominant. "
        return_info += "Falling VPT signals volume aligning with downward price move. It suggests short selling force is dominant."
        return_info += "Flat VPT means volume is rising or falling without a definitive price trend. It suggests a balance status for long and short position\n"
        return_info += "The values in period of days and weeks are given below:\n"
        df = {}
        df['days'] = get_data(stock_id, freq='days', n_periods=n_periods)[['date', 'VPT']]
        df['weeks'] = get_data(stock_id, freq='weeks', n_periods=n_periods)[['date', 'VPT']]

        for freq in ['days', 'weeks']:
            return_info += f"{freq}:{df[freq]['VPT'].round(1).tolist()}, " + "\n"

        return return_info
    except:
        return f"No VPT data"  
if __name__ == "__main__":
    result = VPT('000001', n_periods=30)
    print(result)
    