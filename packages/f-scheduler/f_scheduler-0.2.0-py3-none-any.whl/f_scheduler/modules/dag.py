class DAG:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.task_id] = task

    def set_downstream(self, task_id, next_task_id):
        task = self.tasks[task_id]
        next_task = self.tasks[next_task_id]
        task.next(next_task)

    def run(self, start_task_id):
        start_task = self.tasks[start_task_id]
        start_task.run()

    def clear(self):
        self.tasks.clear()

    def get_return_value(self, task_id):
        return self.tasks[task_id].return_value

    def get_all_tasks(self):
        return self.tasks

    def update_task(self, task_id, new_param):
        task = self.tasks[task_id]
        if task:
            task.param = new_param
        else:
            print(f"No task found with id: {task_id}")
