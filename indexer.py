class Task:
    task_name = 'task_name'

    def get_task_name(self):
        return self.task_name

    def run_task(self, data):
        raise NotImplementedError()


class Pipeline:
    steps = []

    # single raw data provider
    def raw_data_provider(self):
        raise NotImplementedError()

    def initiate(self, *tasks):
        self.steps = [*tasks]

    def processed_data_handler(self):
        raise NotImplementedError()

    def run(self):
        raw_data = self.raw_data_provider()
        processed_data = raw_data
        for step in self.steps:
            raw_data = processed_data
            processed_data = step(processed_data)
        self.processed_data_handler(processed_data)
