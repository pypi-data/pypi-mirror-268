from pydantic import BaseModel
from typing import  Callable, Any, Dict, List, Union, Tuple
from openfinance.searchhub.task.base import Task

from openfinance.searchhub.task.analysis.analysis_task import AnalysisTask
from openfinance.searchhub.task.analysis.fixed_analysis_task import FixedAnalysisTask
from openfinance.searchhub.task.search.search_task import SearchTask
from openfinance.searchhub.task.compare.compare_task import CompareTask
from openfinance.searchhub.task.role.role_task import RoleTask
from openfinance.searchhub.task.search_sql.search_sql_task import SearchSqlTask
from openfinance.searchhub.task.percept.percept_task import PerceptTask
from openfinance.searchhub.task.percept.online_percept_task import OnlinePerceptTask

candidate_tasks = [
    AnalysisTask,
    SearchTask,
    CompareTask,
    RoleTask,
    SearchSqlTask,
    PerceptTask,
    FixedAnalysisTask,
    OnlinePerceptTask
]

class TaskManager():
    tasks: Dict[str, Task] = {}
    def __init__(
        self,
        config
    ):
        self.config = config
        tasks = self.config.get('task')
        for task in candidate_tasks:
            if task.name in tasks:
                self.tasks[task.name] = task()
    
    def get_tasks(
        self
    ) -> List[str]:
        '''
            default is for non task chat
        '''
        return list(self.tasks.keys()) + ["default"]

    def get_task_by_name(
        self,
        name: str
    ) -> Task:
        return self.tasks.get(name, None)

    def extract_task(
        self,
        query: str
    ) -> Dict[str, str]:
        """
        Extract task name and fix query for input
        """
        for t in self.tasks.keys():
            if query.startswith("@" + t):
                return {
                    "task": t,
                    "query": query[len(t)+1:]
                }
        return {"query": query}
