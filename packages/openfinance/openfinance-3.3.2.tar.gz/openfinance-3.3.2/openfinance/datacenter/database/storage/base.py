import datetime
from typing import Any, Callable, Dict, Optional, Tuple, List, Union
from openfinance.datacenter.database.storage import stock_func

class DataUpdater:
    '''
        class used for update database
    '''
    func: List[Callable] = []
   
    def load_func(
        self, 
        func: Union[List[Callable], Callable]
    ) -> None:
        if isinstance(func, List):
            self.func += func
        else:
            self.func.append(func)

    def daily_update(
        self
    ) -> None:
        '''
            default function should update latest data
        '''
        for func in self.func:
            print(func.__name__)
            func()
    
    def init_update(
        self
    ) -> None:
        '''
            default function should update latest data
        '''
        for func in self.func:
            print(func.__name__)
            func(init=True)

if __name__ == "__main__":
    updater = DataUpdater()
    updater.load_func(
        stock_func
    )
    updater.daily_update()