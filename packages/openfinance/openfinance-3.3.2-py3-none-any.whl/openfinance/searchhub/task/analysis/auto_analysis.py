import asyncio
import json
import time

from typing import Dict
from openfinance.config import Config

from openfinance.searchhub.task.analysis.analysis_task import AnalysisTask

class AntoAnalysis(AnalysisTask):
    name = "autoAnalysis"

if __name__ == '__main__':
    task = AntoAnalysis()
    while True:
        #result = asyncio.run(task.agent.acall("为什么最近大盘持续下跌"))
        #result = asyncio.run(task.agent.acall("比亚迪的股票值得买入吗", company="比亚迪"))
        result = asyncio.run(task.agent.acall("比较比亚迪和贵州茅台的财务数据，谁值得投资", company=["比亚迪","贵州茅台"]))
        print(result)
        if "finish" in result:
            break
        time.sleep(2)