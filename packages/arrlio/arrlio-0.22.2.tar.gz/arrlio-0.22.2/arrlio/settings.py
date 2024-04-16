import os

ENV_PREFIX = os.environ.get("ARRLIO_ENV_PREFIX", "ARRLIO_")

BACKEND = "arrlio.backends.local"

TASK_QUEUE = "arrlio.tasks"
TASK_MIN_PRIORITY = 1
TASK_MAX_PRIORITY = 10
TASK_PRIORITY = 1
TASK_TIMEOUT = 300
TASK_TTL = 300
TASK_ACK_LATE = False
TASK_RESULT_TTL = 300
TASK_RESULT_RETURN = True
TASK_EVENTS = False

EVENT_TTL = 300

TASK_QUEUES = [TASK_QUEUE]

EXECUTOR = "arrlio.executor"

LOG_LEVEL = "ERROR"
LOG_SANITIZE = True
