import logging

def setup_logger():
    logger = logging.getLogger("chat_app")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    ch = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger