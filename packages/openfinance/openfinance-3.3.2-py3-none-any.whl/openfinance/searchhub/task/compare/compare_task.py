from openfinance.searchhub.task.analysis.analysis_task import AnalysisTask
class CompareTask(AnalysisTask):
    name = "compare"

if __name__ == '__main__':
    #print(analysis_with_role("Should we buy it or sell it now"))
    task = CompareTask()
    result = task.aexecute("which one is better", company = ["傲农生物", "隆基绿能"])
    print(result)
