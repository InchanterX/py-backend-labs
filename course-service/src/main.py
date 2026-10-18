import logging
import logging.config

import yaml

from src.core.config import get_settings
from src.web.app import create_app
from src.web.lifespans import lifespan_app
from src.web.routers import ROUTERS

logger = logging.getLogger(__name__)

if __name__ == "src.main":
    with open("log-config.yaml", encoding="UTF-8") as file:
        log_config = yaml.safe_load(file)
    logging.config.dictConfig(log_config)
    settings = get_settings()
    app = create_app(settings, ROUTERS, lifespan=lifespan_app)
    logger.debug(f"Created app={app} with settings={settings}")
