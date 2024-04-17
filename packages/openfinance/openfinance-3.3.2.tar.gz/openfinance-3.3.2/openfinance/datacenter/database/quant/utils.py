import requests
import pandas as pd
import json
import numpy as np

key = '8140ad230f687daede75a08855e8ae5ff40c3ba8'
url = 'http://139.159.205.40:8808/'

def get_data(stock_id, freq, n_periods):
    """
    args:
        stock_id: 股票代码, e.g. 000001
        freq: 数据频率，目前支持日、周频
        n_periods: 

    """

    json_map = {'stock_id': stock_id, 'days':n_periods, 'key':key,'scale':freq}
    r = requests.post(url + 'quant/historyfactor', json=json_map)
    if r.status_code == 200:
        if r.json()['code'] == 200:
            data = json.loads(r.json()['data'])
            # 日期
            df = pd.DataFrame.from_records([data['date']]).T
            df.columns= ['date']
            # 因子解析
            df['factor_value_pair'] = data['factor_value_pair']
            df['factor_value_pair'] = df.factor_value_pair.apply(lambda x: x.split(';'))
            factor_cols = [c.split(':')[0] for c in df.factor_value_pair.iloc[0]]
            df['factor_value_pair'] = df.factor_value_pair.apply(lambda x: [i.split(':')[1] for i in x])
            factor_value_pair = pd.DataFrame(df['factor_value_pair'].to_list(), columns=factor_cols)

            df = pd.merge(df.reset_index(drop=True), factor_value_pair, left_index=True, right_index=True)
            df = df[df.columns.drop('factor_value_pair')]

            # 去除因子值全为空的列
            df = df.replace('None', np.nan)
            for col in factor_cols:
                df[col] = df[col].astype(float)
            df = df.dropna(axis=1, how='all')
            return df

    print(r.json()['message'])
    return pd.DataFrame([])




if __name__ == "__main__":
    df = get_data(stock_id='000001', freq='days', n_periods=10)
    print(df)
    
    df = get_data('000001', 'weeks', 10)
    print(df)