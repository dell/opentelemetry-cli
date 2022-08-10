import sys
import time
from datetime import datetime


PY36 = sys.version_info[0:2] == (3, 6)


def time_ns():
    if PY36:  # pragma: no cover
        now = datetime.now()
        return int(now.timestamp() * 1e9)
    else:
        return time.time_ns()
