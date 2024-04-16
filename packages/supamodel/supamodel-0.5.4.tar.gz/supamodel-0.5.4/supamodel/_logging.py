import logging

import devtools
from loguru import logger
from rich import print
from rich.logging import RichHandler

httpx_logger = logging.getLogger("httpx")
httpx_logger.disabled = True

# logger.configure(
#     handlers=[
#         {
#             "sink": RichHandler(rich_tracebacks=True),
#             "level": "DEBUG",
#             "format": "{time} - {level} - {message}",
#         }
#     ]
# )

# logger.debug("This is a debug message")
# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")
# logger.critical("This is a critical message")


__all__ = ["logger", "devtools", "print"]
