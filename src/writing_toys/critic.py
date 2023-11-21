from dataclasses import dataclass
import json

from writing_toys.interface import get_interface


@dataclass
class Criticism:
    originality: int
    self_consistency: int
    grammatical_errors: str
    criticism: str


def criticize_writing(writing: str) -> Criticism:
    interface = get_interface(json_mode=True)
    interface.set_system_message(
"""
Review the given writing sample and provide the following feedback in JSON form:

{
    "originality": 1-5,
    "self_consistency": 1-5,
    "grammatical_errors": grammar and tense errors,
    "criticism": critique writing
}
"""
    )
    response = interface.say(writing)
    return Criticism(**json.loads(response))
