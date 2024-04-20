# f-scheduler 
Simplify Lightweight Function Scheduler with Python 3

f(unction)-scheduler is a Python package designed to Simplify Lightweight Function Scheduling. It is built with Python 3.

## Inspiration

The inspiration for this project came from studying the code of Apache Airflow operators. 

The functionality and design patterns observed in the Airflow operators have greatly influenced the development of f-scheduler.

## Installation

You can install f-scheduler using pip:

```bash
pip install f-scheduler
```

## Usage

```python
# import f_scheduler package
from f_scheduler import ConditionOperator, DefaultFunctionOperator, IterFunctionOperator, DAG, Converter

# create a DAG
dag = DAG()

# add tasks to the DAG
dag.add_task(DefaultFunctionOperator(function=print, param=(['hello']), task_id='hello_task'))
dag.add_task(DefaultFunctionOperator(function=print, param=(['bye']), task_id='bye_task'))
dag.add_task(ConditionOperator(10 > 1, task_id='condition_task'))
dag.add_task(IterFunctionOperator(function=print, param=(['What your name?']), iterations=5, task_id='iter_task'))

# set the dependency between tasks :  hello_task >> condition_task >> iter_task >> bye_task
task_order = ['hello_task', 'condition_task', 'iter_task', 'bye_task']

# set the dependency between tasks
# using the converter
converter = Converter(dag)
converter.convert_list_to_dag(task_order).run('hello_task')
# or dag.set_downstream('hello_task', 'condition_task')
# dag.set_downstream('condition_task', 'iter_task')

# if you want to get the return value of the task, you can use this method
print(dag.get_return_value('iter_task'))

# print all tasks
print(dag.get_all_tasks())

# clear all tasks
dag.clear()
```

## License

f-scheduler is licensed under the Apache License.

## Project Links

- [Homepage](https://github.com/minwook-shin/f-scheduler)
- [Bug Tracker](https://github.com/minwook-shin/f-scheduler/issues)
