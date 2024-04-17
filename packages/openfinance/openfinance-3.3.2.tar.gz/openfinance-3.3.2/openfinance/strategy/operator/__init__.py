from openfinance.strategy.operator.base import OperatorManager
from openfinance.strategy.operator.mean import Mean
from openfinance.strategy.operator.acc import Acc
from openfinance.strategy.operator.latest import Latest
from openfinance.strategy.operator.yoy import Yoy
from openfinance.strategy.operator.divide_latest import DivideLatest
from openfinance.strategy.operator.moving_average import MovingAverage
from openfinance.strategy.operator.macd import MAConDiv
from openfinance.strategy.operator.rsi import RSI
from openfinance.strategy.operator.obv import OnBalanceVolume
from openfinance.strategy.operator.coefficient_variance import CoeffVar
from openfinance.strategy.operator.latest_position_index import LatestPosition
from openfinance.strategy.operator.hist import Hist

OperatorManager().register(
    [
        Mean,
        Acc,
        Latest,
        Yoy,
        DivideLatest,
        MovingAverage,
        MAConDiv,
        RSI,
        CoeffVar,
        OnBalanceVolume,
        LatestPosition,
        Hist
    ]
)
