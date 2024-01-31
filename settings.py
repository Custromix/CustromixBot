import os
from logging.config import dictConfig
from dotenv import load_dotenv

load_dotenv()
DISCORD_API_SECRET = os.getenv('DISCORD_API_TOKEN')

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters":{
        "verbose":{
            "format"
        }
    },
    "handlers":{

    },
    "loggers":{

    }
}

dictConfig(LOGGING_CONFIG)
