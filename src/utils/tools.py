import logging


def setup_logger(log_file, level=logging.INFO, name=""):
    """ Sets up a logger """
    handler = logging.FileHandler(log_file, mode="w")
    # Another implementation:
    # handler = RotatingFileHandler(log_file,maxBytes=1024, backupCount=5)
    formatter = logging.Formatter(
    "%(asctime)s [%(levelname)-7s][%(lineno)-3d]: %(message)s",
    datefmt="%Y-%m-%d %I:%M:%S",
    )
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger