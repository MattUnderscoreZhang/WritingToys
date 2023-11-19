from dotenv import load_dotenv
import json
import os
from typing import Literal, cast

from gpt_interface import GptInterface


PartOfSpeech = Literal["noun", "verb", "adjective", "adverb"]


def generate_random_words(
    n_words: int,
    part_of_speech: PartOfSpeech | None = None,
    unusualness: float | None = None,
) -> list[str]:
    load_dotenv()
    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPEN_API_KEY")),
        model="gpt-3.5-turbo",
        json_mode=True,
    )
    interface.set_system_message(
        "Return random words in a JSON list, like [\"word_1\", \"word_2\", ...]"
    )
    prompt = f"Generate {n_words} random words."
    if part_of_speech:
        prompt += f"\nThe words should all be {part_of_speech}s."
    if unusualness:
        prompt += f"\nOn a scale from 0-1, generate words with an unusualness value of {unusualness}."
    response = interface.say(prompt)
    words = json.loads(response)
    return words
