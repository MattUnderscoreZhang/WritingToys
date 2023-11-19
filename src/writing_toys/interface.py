from dotenv import load_dotenv
import os
from typing import cast

from gpt_interface import GptInterface


def get_interface(
    json_mode: bool = False,
) -> GptInterface:
    load_dotenv()
    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPEN_API_KEY")),
        model="gpt-4",
        json_mode=json_mode,
    )
    return interface
