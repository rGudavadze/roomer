import json
from datetime import datetime, timedelta
from uuid import UUID

from google.cloud import tasks_v2


class CloudTaskClient:
    def __init__(self):
        # path = "/home/roma/Desktop/roomer/roomer-app-375320-c6460f617396.json"
        # self.client = tasks_v2.CloudTasksClient.from_service_account_file(path)
        self.client = tasks_v2.CloudTasksClient()
        self.parent = self.client.queue_path("roomer-app-375320", "europe-west3", "roomer-tasks")

    @staticmethod
    def generate_task(roomer_id, seconds):
        task = {
            "http_request": {
                "http_method": "POST",
                "url": "https://europe-west3-roomer-app-375320.cloudfunctions.net/roomer-function",
            },
        }

        schedule_time = datetime.utcnow() + timedelta(seconds=seconds)
        formatted_schedule_time = schedule_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        task["schedule_time"] = formatted_schedule_time

        body = {"message": str(roomer_id)}
        payload = json.dumps(body)

        converted_payload = payload.encode()

        task["http_request"]["body"] = converted_payload

        return task

    def create_task(self, booking_id: UUID, timer):
        task = self.generate_task(booking_id, timer.seconds)
        response = self.client.create_task(request={"parent": self.parent, "task": task})
        return response
