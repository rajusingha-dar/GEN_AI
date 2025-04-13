import logging
import os
from pathlib import Path

# Create a logs directory if it doesn't exist
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

log_file_path = log_dir / "app.log"

# Formatter
log_format = "%(asctime)s [%(levelname)s] [%(module)s] %(message)s"
formatter = logging.Formatter(log_format)

# File handler
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(formatter)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Main logger
logger = logging.getLogger("smart_enterprise_assistant")
logger.setLevel(logging.INFO)

# Avoid duplicate handlers
if not logger.hasHandlers():
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
