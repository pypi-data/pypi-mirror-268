class BaseOperator:
    def __init__(self, task_id: str):
        self.task_id = task_id
        self.next_task = None

    def execute(self, context: dict):
        raise NotImplementedError()

    def next(self, task):
        self.next_task = task
        return self

    def run(self):
        result = self.execute({})
        if result and self.next_task:
            self.next_task.run()
        else:
            return False
