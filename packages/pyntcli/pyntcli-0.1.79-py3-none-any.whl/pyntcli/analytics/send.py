import requests
import time
import platform

from pyntcli import __version__
from pyntcli.transport import pynt_requests
import pyntcli.log.log as log


PYNT_DEFAULT_USER_ID = "d9e3b82b-2900-43bf-8c8f-7ffe2f0cda36"
MIXPANEL_TOKEN = "05c26edb86084bbbb803eed6818cd8aa"
MIXPANEL_URL = "https://api-eu.mixpanel.com/track?ip=1"

logger = log.get_logger()


def stop():
    if not AnalyticsSender._instance:
        return
    AnalyticsSender.instance().done()


def emit(event, properties=None):
    AnalyticsSender.instance().emit(event, properties)


def deferred_emit(event, properties=None):
    AnalyticsSender.instance().deferred_emit(event, properties)


def set_user_id(user_id):
    AnalyticsSender.instance().set_user_id(user_id)


CLI_START = "cli_start"
LOGIN_START = "cli_login_start"
LOGIN_DONE = "cli_login_done"
CICD = "CI/CD"
ERROR = "error"
DOCKER_PLATFORM = "platform"


class AnalyticsSender():
    _instance = None

    def __init__(self, user_id=PYNT_DEFAULT_USER_ID) -> None:
        self.user_id = user_id
        self.version = __version__
        self.events = []

    @staticmethod
    def instance():
        if not AnalyticsSender._instance:
            AnalyticsSender._instance = AnalyticsSender()

        return AnalyticsSender._instance

    def base_event(self, event_type):
        return {
            "event": event_type,
            "properties":  {
                "time": time.time(),
                "distinct_id": self.user_id,
                "$os": platform.platform(),
                "cli_version": self.version,
                "token": MIXPANEL_TOKEN
            }
        }

    def emit(self, event, properties):
        base_event = self.base_event(event)

        if properties:
            for k, v in properties.items():
                base_event["properties"][k] = v

        if self.user_id != PYNT_DEFAULT_USER_ID:
            try:
                pynt_requests.post(MIXPANEL_URL, json=[base_event])
            except Exception:
                logger.info(f"mixpanel unavailable, sending to logz: {base_event}")
        else:
            self.events.append(base_event)

    def deferred_emit(self, event, properties):
        base_event = self.base_event(event)

        if properties:
            for k, v in properties.items():
                base_event["properties"][k] = v

        self.events.append(base_event)

    def set_user_id(self, user_id):
        self.user_id = user_id
        for i, _ in enumerate(self.events):
            self.events[i]["properties"]["distinct_id"] = user_id
        self.done()

    def done(self):
        if self.events:
            try:
                pynt_requests.post(MIXPANEL_URL, json=self.events)
            except Exception:
                logger.info(f"mixpanel unavailable, sending to logz: {self.events}")
            self.events = []
