import json

from f_scheduler.operators.base_op import BaseOperator


class ConditionOperator(BaseOperator):
    def __init__(self, condition: bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.condition = condition

    def execute(self, context: dict) -> bool:
        return self.condition

    def __repr__(self):
        d = {'ID': self.task_id, 'Condition': self.condition}
        return json.dumps(d)
