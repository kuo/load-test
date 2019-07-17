from locust import Locust, HttpLocust, TaskSet, task

class DummyTaskSet(TaskSet):

    @task(1)
    def find(self):
        header = {'content-type': 'application/json'}
        payload = {
            "access_token": "FEF16453FBF28DE0F4CD4597E04E3189F0B769A74A4E0201B6",
            "nonce_str": "abc123",
            "sign": "DCD972098347772E52FD70187A43FC88"
        }

        self.client.post("/findAll", json=payload, headers=header)


class DummyLoadTester(HttpLocust):
    host = "https://stage4-iioapi.gashpoint.com/public/api/position"
    task_set = DummyTaskSet
    min_wait = 5000
    max_wait = 15000
