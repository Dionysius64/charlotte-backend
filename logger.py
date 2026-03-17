import logging

def setup_logger():
    logger = logging.getLogger("chat_app")
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger