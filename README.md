Tools to help generate writing ideas.

# Setup

These tools require an OpenAI API key (https://platform.openai.com/docs/api-reference/authentication).

I recommend creating a .env file and adding it to your .gitignore file. The file would contain the following:

```
OPENAI_API_KEY=sk-exampleKey
```

# Examples

Try out the following:

```bash
python examples/characters.py
python examples/settings.py
python examples/characters.py --emotion_random
python examples/characters.py --prompt "A gigantic sentient tapeworm living in the belly of a whale"
python examples/settings.py --emotion_random
python examples/settings.py --prompt "A galactic maze"
```

See the examples/ folder for more.
