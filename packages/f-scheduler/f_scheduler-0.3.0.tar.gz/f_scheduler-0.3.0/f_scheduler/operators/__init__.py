from f_scheduler.operators.condition_op import ConditionOperator
from f_scheduler.operators.function_op import DefaultFunctionOperator
from f_scheduler.operators.iter_function_op import IterFunctionOperator


operators = {
    'ConditionOperator': ConditionOperator,
    'FunctionOperator': DefaultFunctionOperator,
    'IterFunctionOperator': IterFunctionOperator
}
