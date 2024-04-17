from openfinance.datacenter.echarts.base import ChartManager
from openfinance.datacenter.echarts.bar import bar
from openfinance.datacenter.echarts.tree import tree
from openfinance.datacenter.echarts.pie import pie
from openfinance.datacenter.echarts.multibar import multibar
from openfinance.datacenter.echarts.stacked_line import stack_line

ChartManager().register(
    "bar", bar
)

ChartManager().register(
    "line", stack_line
)

ChartManager().register(
    "pie", pie
)

ChartManager().register(
    "multibar", multibar
)

ChartManager().register(
    "tree", tree
)