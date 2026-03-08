from .client import StandClient
from .updates import *

import logging
import os
import datetime

LOG_DIR = "astandy_logs"
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

for file in os.listdir(LOG_DIR):
    if file.endswith(".log"):
        try:
            os.rename(f"{LOG_DIR}/{file}", f"{LOG_DIR}/{file}.old")
        except FileNotFoundError:
            pass

old_logs = sorted(
    [f for f in os.listdir(LOG_DIR) if f.endswith(".log.old")],
    key=lambda x: os.path.getmtime(f'{LOG_DIR}/{x}'),
    reverse=True
)

for file in old_logs[5:]:
    try:
        os.remove(f'{LOG_DIR}/{file}')
    except FileNotFoundError:
        pass

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(f"astandy_logs/client-{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
    ]
)

__all__ = [
    "StandClient"
]