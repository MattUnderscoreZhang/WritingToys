from dotenv import load_dotenv
import os
from typing import cast

from gpt_interface import GptInterface


def get_openai_api_key() -> str:
    load_dotenv()
    return cast(str, os.getenv("OPEN_API_KEY"))


def get_interface(
    json_mode: bool = False,
) -> GptInterface:
    interface = GptInterface(
        openai_api_key=get_openai_api_key(),
        model="gpt-4",
        json_mode=json_mode,
    )
    return interface
