
import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S',level=logging.DEBUG, filename='logs.txt')

logger = logging.getLogger('muks')

#another_logger = logging.getLogger('muks.coremodules')  # gets a child logger called 'database' of 'my_app'

logger.debug("This is a debug log")
logger.info("This is an info log")
logger.critical("This is critical")
logger.error("An error occurred")

"""
Add logging to your projects moving forward! It’s great when you can trace what was happening in your system as it happened with extensive logs (although, it does mean the code will be longer since you need to include logging statements everywhere).
"""