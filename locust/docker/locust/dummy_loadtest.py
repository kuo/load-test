from locust import Locust, HttpLocust, TaskSet, task

class DummyTaskSet(TaskSet):

    @task(1)
    def find(self):
        self.client.get("/")


class DummyLoadTester(HttpLocust):
    host = "https://stage4-iio.gashpoint.com"
    task_set = DummyTaskSet
    min_wait = 5000
    max_wait = 15000
