from typing import Dict, Any, Union, List
from openfinance.datacenter.echarts.base import ChartManager


def bar(inputs: Union[Dict[str, Any], List[Any]], 
        labels: Dict[str, str]) -> Dict[str, Any]:
    """ translate dataformat to echart format for bar
        :param inputs: Data from database（x, y）
        :param labels: Identify labels of Data (title)
        :return option: echart format
    """
    x = []
    y = []
    if isinstance(inputs, List):
        xlabel = labels['x']
        ylabel = labels['y']
        for i in inputs:
            x.append(i[xlabel])
            y.append(i[ylabel])
    option = {
        "title": {
          "text": labels["title"],
          "left": "center"
        },
        "xAxis": {
            "type": 'category',
            "name": labels['x'],
            "data":  x
        },
        "yAxis": {
            "type": 'value',
            "name": labels['y']
        },
        "series": [
            {
                "data": y,
                "type": 'bar',
                "showBackground": True,
                "backgroundStyle": {
                    "color": 'rgba(180, 180, 180, 0.2)'
                }
            }
        ]
    }
    return option