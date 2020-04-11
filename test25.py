from  locust import HttpLocust,TaskSet,task
class UserTask(TaskSet):
    @task
    def tc_index(self):
        self.client.get("/")

class UserOne(HttpLocust):
    task_set = UserTask
    weight = 1
    min_wait = 1000
    max_wait = 3000
    stop_timeout = 5
    host = "https://www.baidu.com"

class UserTwo(HttpLocust):
    weight = 2
    task_set = UserTask
    host = "https://www.baidu.com"
