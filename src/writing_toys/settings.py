from ai_emotion.simple_emotion import PlutchikEmotion
from dataclasses import asdict

from writing_toys.interface import get_interface
from writing_toys.random_words import generate_random_words


def generate_setting(
    starting_prompt: str | None = None,
    emotion: PlutchikEmotion | None = None,
) -> str:
    words = (
        generate_random_words(3, part_of_speech="noun") +
        generate_random_words(3, part_of_speech="adjective")
    )

    interface = get_interface()
    interface.set_system_message(
"""
Write as though you were describing a location in a worldbuilding document.
Do not describe any specific characters in the setting.
You may use the words in the prompt, but don't parrot them back in the same order.
If need be, you may choose to not use all the words if some don't make sense in context.
Write only a single paragraph, and include only the interesting details.
Do not use overly flowery language, and aim to write simply.
"""
    )
    prompt = (
f"""
Describe a setting that can be described by the following words: {words}.
"""
    )
    if starting_prompt:
        prompt += (
f"""
Make the setting fit with this general prompt: {starting_prompt}.
"""
        )
    if emotion:
        prompt += (
f"""
Make the setting evoke the following emotion as closely as possible, where each value ranges from 0-1: {asdict(emotion)}.
Do not use any of these words in the response itself unless necessary.
"""
        )
    response = interface.say(prompt)
    # TODO: generate a random location on earth to use as starting inspiration
    # TODO: generate a random time to use as starting inspiration
    return response
