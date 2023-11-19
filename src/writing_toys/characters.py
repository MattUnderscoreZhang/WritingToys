from writing_toys.interface import get_interface
from writing_toys.random_words import generate_random_words


def generate_character() -> str:
    words = (
        generate_random_words(2, part_of_speech="verb") +
        generate_random_words(2, part_of_speech="adjective") +
        generate_random_words(2, part_of_speech="noun")
    )

    interface = get_interface()
    interface.set_system_message(
        """
        Write as though you were describing a character in a worldbuilding document.
        Don't describe the setting that the character exists in.
        You may use the words in the prompt, but don't parrot them back in the same order.
        If need be, you may choose to not use all the words if some don't make sense in context.
        Write only a single paragraph, and include only the interesting details.
        """
    )
    response = interface.say(
        f"""
        Describe a character that can be described by the following words: {words}.
        """
    )
    # TODO: generate a random location on earth to use as starting inspiration
    # TODO: generate a random time to use as starting inspiration
    return response
