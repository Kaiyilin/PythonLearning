import logging


"""
Specify multiple handlers for different logging level
"""
logger = logging.getLogger(__name__)

# create handler 
stream_h = logging.StreamHandler()
file_h = logging.FileHandler(filename="error.log")

# level and format

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("warning!")
logger.error("error")