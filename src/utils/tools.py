import logging
from logging import Logger

def setup_logger(log_file: str, level: str = logging.INFO, name: str = "") -> Logger:
    """ Sets up a new logger.
    
    Args:
        log_file: Name of the log file.
        level: Logging level to use.
        name: Logger name

    Returns:
        logger: Logger object
    """
    handler = logging.FileHandler(log_file, mode="w")
    formatter = logging.Formatter(
    "%(asctime)s [%(levelname)-7s][%(lineno)-3d]: %(message)s",
    datefmt="%Y-%m-%d %I:%M:%S",
    )
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger