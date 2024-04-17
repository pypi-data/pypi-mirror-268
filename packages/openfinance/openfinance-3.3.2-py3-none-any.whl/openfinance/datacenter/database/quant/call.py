import requests
import numpy as np
import json

token = '8140ad230f687daede75a08855e8ae5ff40c3ba8'
url = 'http://114.132.71.128:5001/'


def get_factor_process(
    factor=None,
    quant_data=None,
    ext: str = ""
):
    json_map = {
        'factor': factor,
        'quant_data': quant_data,
        'ext': ext,
        'token': token
    }
    r = requests.post(url + 'quant/calc', json=json_map)
    if r.status_code == 200:
        jsondata = json.loads(r.text)
        if jsondata['status'] == 0:
            data = jsondata['result']
            return [0 if np.isnan(x) else round(x, 2) for x in data]
