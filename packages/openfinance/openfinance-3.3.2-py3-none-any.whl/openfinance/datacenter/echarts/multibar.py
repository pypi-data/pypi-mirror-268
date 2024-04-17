from typing import Dict, Any, Union, List
from openfinance.datacenter.echarts.base import ChartManager

def multibar(inputs: Union[Dict[str, Any], List[Any]], 
        labels: Dict[str, str]) -> Dict[str, Any]:
    """ translate dataformat to echart format for bar
        :param inputs: Data from database（x, y）
        :param labels: Identify labels of Data (title)
        :return option: echart format
    """
    data = {}
    if isinstance(inputs, List):
        xlabel = labels['x']
        ylabel = labels['y']
        data[xlabel] = []
        for y in ylabel:
            data[y] = []

        for i in inputs:
            for k in data.keys():
                data[k].append(i[k]) 
    source = [
        [d[0]] + d[1] for d in data.items()
    ]
    option = {
        "legend": {},
        "tooltip": {},
        "dataset": {
            "source": source
        },
        "xAxis": { "type": 'category' },
        "yAxis": {},
        "series": [{ "type": 'bar' }, { "type": 'bar' }, { "type": 'bar' }]
    }

    return option