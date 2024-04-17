from typing import Dict, Any, Union, List
from openfinance.datacenter.echarts.base import ChartManager


def pie(inputs: Union[Dict[str, Any], List[Any]], 
        labels: Dict[str, str]) -> Dict[str, Any]:
    """ translate dataformat to echart format for bar
        :param inputs: Data from database（x, y）
        :param labels: Identify labels of Data (title)
        :return option: echart format
    """
    series = []
    if isinstance(inputs, List):
        xlabel = labels['x']
        ylabel = labels['y']
        series = [
            {
                "value": i[ylabel], "name": i[xlabel] 
            }   
            for i in inputs
        ]
    option = {
        "title": {
          "text": labels["title"],
          "left": "center"
        },
        "tooltip": {
            "trigger": 'item'
        },
        "legend": {
            "orient": 'vertical',
            "left": 'left'
        },
        "series": [
            {
            "name": 'Access From',
            "type": 'pie',
            "radius": '50%',
            "data": series,
            "emphasis": {
                "itemStyle": {
                "shadowBlur": 10,
                "shadowOffsetX": 0,
                "shadowColor": 'rgba(0, 0, 0, 0.5)'
                }
            }
            } 
        ]
    }
    return option