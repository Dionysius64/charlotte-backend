import yaml
import logging

logger = logging.getLogger("chat_app")

def load_config(path="config.yaml"):
    """
    Load config from YAML file
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        logger.info(f"Config loaded from {path}")
        return config
    except FileNotFoundError:
        logger.warning(f"{path} not found. Using defaults.")
        return {"conversation_title": "Conversation"}