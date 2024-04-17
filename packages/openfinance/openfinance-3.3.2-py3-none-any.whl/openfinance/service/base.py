import json
from openfinance.service.error import StatusCodeEnum

def wrapper_return(output, err = StatusCodeEnum.OK, chart = {}):
    """wrapper the result for service

    Args:
        output: Dictionary of inputs, result for str, chart for chart

    Returns:
        json string for return
    """    
    if isinstance(output, dict):
        chart = output.get("chart", {})
        output = output.get("result", "")
    return json.dumps(
    {
        "output": {
            "answer": output,
            "chart": chart
            },
        "msg": err.msg,
        "ret_code": err.code
    })