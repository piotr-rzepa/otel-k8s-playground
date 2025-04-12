from locust import HttpUser, task
import random


class DiceServerUser(HttpUser):
    host = "http://localhost/flask"

    @task
    def hello_world(self):
        player = random.choice(["X", None, "Y", "Z"])
        if player is None:
            self.client.get("/rolldice")
        else:
            self.client.get(f"/rolldice?player={player}")
