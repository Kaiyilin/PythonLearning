import logging
import logging.config
"""
Set the logging configuration to logging.conf
This is the file config method and for dict config 
you can check the documentations
"""
# allows you to change somthing without modify long code
logging.config.fileConfig('logging.conf')

logger = logging.getLogger("simpleLogger")
logger.debug("This is the debug message")
