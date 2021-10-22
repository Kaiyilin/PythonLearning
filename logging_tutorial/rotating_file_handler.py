import logging
from logging import handlers
from logging.handlers import (
    RotatingFileHandler, 
    TimedRotatingFileHandler
)

"""you are doing a large prt
with lots of logging info, and you want to 
trace the most recent one. the rotating file handler 
helps you keep the file small
"""

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# in 2000 bytes, it will automatically chang to another log file 
# with 2 backupCount i.e. only preserve the most recent 3
handler = RotatingFileHandler(
    filename="big_pjt.log", 
    maxBytes=200, 
    backupCount=2
    )

logger.addHandler(handler)

for f in range(800):
    logger.info(f"{f}")

"""TimedRotatingFileHandler
"""
t_logger = logging.getLogger(__name__)
t_logger.setLevel(logging.INFO)

# The log file will be created after 5s
t_handler = TimedRotatingFileHandler(
    filename="big_pjt_time.log", 
    when="s",
    interval=5,
    backupCount=2
    )

t_logger.addHandler(t_handler)

for f in range(8000):
    t_logger.info(f"{f}")