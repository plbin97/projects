# %%
from datetime import date

# %%
import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta

# %%
from ploomber import DAG
from ploomber.executors import Serial
from ploomber.tasks import PythonCallable, TaskGroup
from ploomber.products import File
from ploomber.util import ParamGrid, Interval


# %%
def get_data(product, dates):
    """
    Dummy code, in reality this would usually be a Task that pulls data
    from a database
    """
    dates_series = pd.date_range(start=dates[0],
                                 end=dates[1],
                                 closed='left',
                                 freq='D')
    values = np.random.rand(dates_series.shape[0])
    df = pd.DataFrame({'dates': dates_series, 'values': values})
    df.to_parquet(str(product))


# %%
dag = DAG()
# NOTE: this is only required for testing purpose
dag.executor = Serial(build_in_subprocess=False)

# %%
start_date = date(year=2010, month=1, day=1)
end_date = date(year=2019, month=6, day=1)
delta = relativedelta(years=1)

# %%
params_array = ParamGrid({
    'dates': Interval(start_date, end_date, delta)
}).zip()


# %%
def namer(params):
    s = str(params['dates'][0]).replace('-', '_')
    e = str(params['dates'][1]).replace('-', '_')
    return 'get_data_{}_{}'.format(s, e)


# %%
TaskGroup.from_params(task_class=PythonCallable,
                      product_class=File,
                      product_primitive='products/{{name}}.parquet',
                      task_kwargs={'source': get_data},
                      dag=dag,
                      params_array=params_array,
                      namer=namer)

# %%
dag.plot()

# %%
dag.build()
