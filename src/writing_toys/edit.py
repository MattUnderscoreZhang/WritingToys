from dataclasses import asdict

from writing_toys.critic import Criticism
from writing_toys.interface import get_interface


def edit(
    writing: str,
    criticism: Criticism,
) -> str:
    interface = get_interface()
    interface.set_system_message(
"""
Given the writing sample and critical feedback, edit the piece.
Match the length and formatting of the original.
Do not output a critique.
"""
    )
    response = interface.say(
f"""
{writing}

{asdict(criticism)}
"""
    )
    return response
