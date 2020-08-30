from faker import Faker


class Task:
    task_name = 'task_name'

    def get_task_name(self):
        return self.task_name

    def run_task(self, data):
        raise NotImplementedError()


class Pipeline:
    # single raw data provider
    def raw_data_provider(self):
        # TODO: return generator
        raise NotImplementedError()

    def initiate(self, *tasks):
        self.steps = [*tasks]

    def processed_data_handler(self, processed_data):
        raise NotImplementedError()

    def run(self):
        # TODO: Add threading
        continue_pipeline = True
        while continue_pipeline:
            raw_data = self.raw_data_provider()
            if raw_data is None:
                continue_pipeline = False
                continue
            processed_data = raw_data
            for step in self.steps:
                raw_data = processed_data
                processed_data = step.run_task(processed_data)
            self.processed_data_handler(processed_data)


class FakeDataPipeline(Pipeline):
    number_of_data = 0

    def __init__(self, data_limit_count, **kwargs):
        super().__init__(*kwargs)
        self.data_limit_count = data_limit_count
        self.fake = Faker()

    def raw_data_provider(self):
        if self.number_of_data >= self.data_limit_count:
            return None
        self.number_of_data += 1
        return {
            'text': self.fake.paragraph()
        }

    def processed_data_handler(self, processed_data):
        print(processed_data)


class TextLengthCalculatorTask(Task):
    task_name = 'text_length_calculator_task'

    def run_task(self, data):
        data['length'] = len(data['text'])
        return data


text_length_calculator_task = TextLengthCalculatorTask()
f = FakeDataPipeline(100)
f.initiate(text_length_calculator_task)
f.run()
