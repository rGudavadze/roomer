import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from uuid import UUID

from django.conf import settings
from google.cloud import tasks_v2

from apps.utils.logger import logger

PROJECT_ID = "roomer-app-375320"
PROJECT_LOCATION = "europe-west3"
PROJECT_TASK = "roomer-tasks"


class CloudTaskClient:
    """
    Cloud Task Client
    """

    def __init__(self):
        if (env := os.environ.get("DJANGO_SETTINGS_MODULE")) and env in [
            "roomer.settings.dev-local",
            "roomer.settings.test",
        ]:
            base_dir = Path(__file__).resolve().parent.parent.parent
            try:
                path = os.path.join(base_dir, "roomer-app-375320-c6460f617396.json")
                self.client = tasks_v2.CloudTasksClient.from_service_account_file(path)

            except Exception as e:  # noqa
                logger.error("Something went wrong.")
                self.client = tasks_v2.CloudTasksClient()
        else:
            self.client = tasks_v2.CloudTasksClient()

        self.parent = self.client.queue_path(PROJECT_ID, PROJECT_LOCATION, PROJECT_TASK)

    @staticmethod
    def generate_booking_finish_task(booking_id, seconds):
        task = {
            "http_request": {
                "http_method": "POST",
                "url": settings.ENVS.get("ROOMER_FUNCTION_URL"),
            },
        }

        schedule_time = datetime.utcnow() + timedelta(seconds=seconds)
        formatted_schedule_time = schedule_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        task["schedule_time"] = formatted_schedule_time

        body = {"message": str(booking_id)}
        payload = json.dumps(body)

        converted_payload = payload.encode()

        task["http_request"]["body"] = converted_payload

        return task

    def create_task(self, booking_id: UUID, timer):
        task = self.generate_booking_finish_task(booking_id, timer.seconds)
        response = self.client.create_task(request={"parent": self.parent, "task": task})
        return response
