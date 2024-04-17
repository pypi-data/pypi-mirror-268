from typing import Dict, Any, Union, List
from openfinance.datacenter.echarts.base import ChartManager


def tree(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """ translate dataformat to echart format for tree
        :param inputs: Data from database（x, y）
        :param labels: Identify labels of Data (title)
        :return option: echart format
    """
    datajson = {
        "name": "思考路径",
        "children": []
    }
    for k, v in inputs.items():
        innerjson = []
        for m in v:
            innerjson.append({
                "name": m
            })
        datajson["children"].append({
            "name": k,
            "children": innerjson
        })
    option = {
        "tooltip": {
            "trigger": "item",
            "triggerOn": "mousemove" 
        },
        "series": [
            {
            "type": "tree",
            "data": [datajson],
            "top": "1%",
            "left": "7%",
            "bottom": "1%",
            "right": "20%",
            "symbolSize": 7,
            "label": {
                "position": "left",
                "verticalAlign": "middle",
                "align": "right",
                "fontSize": 9
            },
            "leaves": {
                "label": {
                "position": "right",
                "verticalAlign": "middle",
                "align": "left"
                }
            },
            "emphasis": {
                "focus": "descendant"
            },
            "expandAndCollapse": True,
            "animationDuration": 550,
            "animationDurationUpdate": 750
            }
        ]
    }
    return option