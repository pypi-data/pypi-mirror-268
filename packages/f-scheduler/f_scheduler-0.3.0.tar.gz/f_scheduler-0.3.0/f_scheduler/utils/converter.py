class Converter:
    def __init__(self, dag):
        self.dag = dag

    def convert_list_to_dag(self, list_of_tasks):
        for i in range(len(list_of_tasks) - 1):
            self.dag.set_downstream(list_of_tasks[i], list_of_tasks[i + 1])
        return self.dag
