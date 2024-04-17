from typing import Dict, Any, Union, List
from openfinance.datacenter.echarts.base import ChartManager

def stack_line(inputs: Union[Dict[str, Any], List[Any]], 
        labels: Dict[str, str]) -> Dict[str, Any]:
    """ translate dataformat to echart format for bar
        :param inputs: Data from database（x, y）
        :param labels: Identify labels of Data (title)
        :return option: echart format
    """

    legend = labels["y"]
    if isinstance(legend, str):
        legend = [legend]
    if isinstance(inputs, List):
        x = []
        y = {}  
        xlabel = labels['x']
        for i in inputs:
            x.append(i[xlabel])
            for j in legend:
                if j not in y:
                    y[j] = []
                y[j].append(i[j])
        series = [
            {
                "name": x,
                "type": 'line',
                #"stack": 'Total',
                "data": y[x]
            } for x in legend
        ]
    elif isinstance(inputs, Dict):
        x = inputs[labels['x']]
        series = [
            {
                "name": x,
                "type": 'line',
                "ignoreYaxisNan": True,                
                #"stack": 'Total',
                "data": inputs[x]                
            } for x in legend
        ]
    option = {
        "title": {
            "text": labels["title"],
            "top": 0,
            "left": "center"
        },
        "tooltip": {
            "trigger": 'axis'
        },
        "legend": {
            "data": legend,
            "top": 30
        },
        "grid": {
            "top": 60,
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": x
        },
        "yAxis": {
            "type": 'value'
        },
        "series": series
    }
    return option