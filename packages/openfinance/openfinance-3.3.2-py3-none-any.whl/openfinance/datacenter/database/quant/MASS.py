from openfinance.datacenter.database.quant.utils import get_data
from openfinance.datacenter.knowledge.decorator import register
from openfinance.datacenter.database.source.eastmoney.util import (
    get_code_id
)
# export PYTHONPATH=$PYTHONPATH:/public/openfinance-main
# des 10个词左右
@register(name="MASS", description="identify trend reversals")
def MASS(stock_id, **kwargs):
    try:
        if not stock_id.isdigit():
            stock_id = get_code_id(stock_id)[2:]    
        n_periods = kwargs['n_periods'] if 'n_periods' in kwargs else 10
        return_info = "A large high-low range signals indecision and potential reversal\n"
        df = {}
        df['days'] = get_data(stock_id, freq='days', n_periods=n_periods)[['date', 'MASS']]
        df['weeks'] = get_data(stock_id, freq='weeks', n_periods=n_periods)[['date', 'MASS']]

        for freq in ['days', 'weeks']:
            return_info += f"{freq}:{df[freq]['MASS'].round(1).tolist()}, "

        return return_info
    except:
        return f"No MASS data"  



if __name__ == "__main__":
    result = MASS('000001', n_periods=30)
    print(result)
    