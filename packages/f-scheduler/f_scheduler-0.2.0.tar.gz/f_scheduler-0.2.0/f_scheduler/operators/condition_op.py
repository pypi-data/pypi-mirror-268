from f_scheduler.operators.base_op import BaseOperator


class ConditionOperator(BaseOperator):
    def __init__(self, condition: bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.condition = condition

    def execute(self, context: dict) -> bool:
        return self.condition
