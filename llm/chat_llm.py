import json
import logging
from openai import AzureOpenAI

from prompts.system_prompt import build_system_prompt

logger = logging.getLogger("chat_app")


class ChatLLM:

    def __init__(self, config: dict):

        self.name = config["llm"]["name"]

        azure = config["azure_openai"]

        self.client = AzureOpenAI(
            api_key=azure["api_key"],
            api_version=azure["api_version"],
            azure_endpoint=azure["endpoint"],
        )

        self.deployment = azure["deployment"]

        self.system_prompt = build_system_prompt(self.name)

        logger.info(f"LLM initialized with name: {self.name}")


    def generate_reply(self, history: list[dict]) -> dict:
        logger.info(f"LLM generating reply with {len(history)} messages")
        try:

            conversation = ""

            for msg in history:
                conversation += (
                    f"{msg['author']}: {msg['message']} "
                    f"(emotion={msg['emotion']})\n"
                )

            full_input = f"{self.system_prompt}\n\n{conversation}"

            response = self.client.responses.create(
                model=self.deployment,
                input=full_input,
            )

            content = response.output_text
            logger.info(f"LLM raw response: {content}")
            parsed = json.loads(content.strip())

            return {
                "author": self.name,
                "message": parsed.get("message", ""),
                "emotion": int(parsed.get("emotion", 0)),
            }

        except Exception as e:
            logger.error(f"LLM error: {e}")

            return {
                "author": self.name,
                "message": "Error generating response.",
                "emotion": 0,
            }