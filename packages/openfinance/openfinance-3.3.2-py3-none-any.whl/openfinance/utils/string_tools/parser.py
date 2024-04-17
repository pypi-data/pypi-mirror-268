from __future__ import print_function
import json

# function to unwarp nested jsonformat data
def dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, (dict, list, tuple)):
                for d in dict_generator(value, pre + [key]):
                    yield d
            else:
                yield pre + [key, value]
    elif isinstance(indict, (list, tuple)):
        for index, value in enumerate(indict):
            for d in dict_generator(value, pre):
                yield d
    else:
        yield pre + [indict]

def parse_from_md(filename):
    stack = []
    level = -1
    with open(filename, "r") as infile:
        for l in infile:
            data = l.rstrip("").strip("\n").split("-")
            if len(data) == 1:
                continue
            new_level = int(len(data[0])/3)
            factor = data[1].strip()
            if new_level > level:
                stack.append(factor)
            elif new_level == level:
                stack[-1] = factor
            else:
                stack = stack[:new_level]
                stack.append(factor)
            level = new_level
            print(stack)


if __name__ == "__main__":
    parse_from_md('openfinance/datacenter/knowledge/schema.md')