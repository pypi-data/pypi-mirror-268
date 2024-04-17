import uuid

import loguru
import sys


def config_logger():
    appName = "seSql"
    logLevel = "INFO"
    request_id = str(uuid.uuid4())
    apiKey = "------------"

    config = {
        "handlers": [
            {"sink": sys.stdout, "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | {extra[app]} | <blue>{extra[request_id]}</blue> | <green>{extra[key]}</green> | <level>{level: <8}</level> | <cyan><level>{message}</level></cyan>", "level": logLevel},
            # {"sink": sys.stdout, "format": "<blue>{extra[app]}</blue> | <level>{level: <8}</level> | <cyan><level>{message}</level></cyan>", "level": logLevel},
        ],
        "extra": {"app": appName, "request_id": request_id, "key": apiKey}
    }
    loguru.logger.remove()
    loguru.logger.configure(**config)
    return loguru.logger


logger = config_logger()
