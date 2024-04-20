import json

from f_scheduler.operators.base_op import BaseOperator


class DefaultFunctionOperator(BaseOperator):
    def __init__(self, function, param, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.function = function
        self.param = param
        self.return_value = None

    def execute(self, context: dict):
        try:
            result = self.function(*self.param)
            if result is not None:
                self.return_value = result
                return result
            else:
                return True
        except Exception as e:
            print(f"Function execution failed with error: {e}")
        return False

    def __repr__(self):
        d = {'ID': self.task_id, 'Function': self.function.__name__, 'Param': self.param}
        return json.dumps(d)
