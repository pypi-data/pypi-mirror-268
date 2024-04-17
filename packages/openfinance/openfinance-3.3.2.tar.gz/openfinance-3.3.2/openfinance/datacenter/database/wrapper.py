from typing import Dict, Any, Union, List

def wrapper(result: Union[Dict[str, Any], List[Any], str], show_all=True):
    """Wrapper result to unify style and assemble result
       Args:
            result: output from func
            show_all: whether all func outputs show charts
       Return:
            dict or str
    """
    if isinstance(result, str):
        return {
            "result": result
        }
    elif isinstance(result, list):
        if show_all:
            ret = []
            for d in result:
                if isinstance(d, dict):
                    ret.append(d)
                elif isinstance(d, str):
                    ret.append({
                        "result": d
                    })
                elif isinstance(d, list):
                    for inner in d:
                        ret.append(inner)
            return ret
        else:
            ret = ""
            chart = []          
            for d in result:
                if isinstance(d, dict):
                    ret += d['result'] + "\n```\n"
                    if "chart" in d:
                        chart.append(d["chart"])
                elif isinstance(d, str):
                    ret += d + "\n"
            if len(chart):
                return {
                    "result": ret,
                    "chart": chart[0]
                }
            else:
                return {
                    "result": ret
                }
    else:
        return result