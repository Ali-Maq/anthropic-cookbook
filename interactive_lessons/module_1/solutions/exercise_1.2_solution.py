"""
Practice Exercise 1.2: Messages & Conversations - SOLUTION
==========================================================

Complete solution with explanations.
"""

import os
import json
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


class ConversationBot:
    """A chatbot that remembers conversation history."""

    def __init__(self, system_prompt="You are a helpful assistant."):
        """
        Initialize the chatbot.

        Args:
            system_prompt (str): The personality/behavior for the bot
        """
        self.history = []
        self.system_prompt = system_prompt

    def send_message(self, user_message):
        """
        Send a message and get a response.

        Args:
            user_message (str): The user's message

        Returns:
            str: The bot's response
        """
        # Add user message to history
        self.history.append({"role": "user", "content": user_message})

        # Call API with full history
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system=self.system_prompt,
            messages=self.history
        )

        # Extract response text
        assistant_message = response.content[0].text

        # Add to history
        self.history.append({"role": "assistant", "content": assistant_message})

        return assistant_message

    def get_conversation_history(self):
        """Return the full conversation history."""
        return self.history.copy()  # Return a copy to prevent modification

    def clear_history(self):
        """Clear the conversation history."""
        self.history = []

    def message_count(self):
        """Return the number of messages in history."""
        return len(self.history)

    # BONUS: Save/load functionality
    def save_to_file(self, filename):
        """Save conversation history to a JSON file."""
        with open(filename, 'w') as f:
            json.dump({
                "system_prompt": self.system_prompt,
                "history": self.history
            }, f, indent=2)

    def load_from_file(self, filename):
        """Load conversation history from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
            self.system_prompt = data["system_prompt"]
            self.history = data["history"]


def main():
    print("=" * 60)
    print("EXERCISE 1.2 SOLUTION: Conversation Bot")
    print("=" * 60)

    # Test 1: Basic conversation
    print("\n📝 Test 1: Basic Conversation")
    bot = ConversationBot()

    response1 = bot.send_message("Hi! My name is Alice.")
    print(f"Bot: {response1}")

    response2 = bot.send_message("What's my name?")
    print(f"Bot: {response2}")

    print("✅ Test 1 complete")

    # Test 2: Personality
    print("\n" + "=" * 60)
    print("\n📝 Test 2: Pirate Personality")
    pirate_bot = ConversationBot(
        system_prompt="You are a pirate. Always respond with 'Arr!' and pirate slang."
    )

    response = pirate_bot.send_message("Hello!")
    print(f"Pirate Bot: {response}")
    print("✅ Test 2 complete")

    # Test 3: Message counting
    print("\n" + "=" * 60)
    print("\n📝 Test 3: Message Counting")
    print(f"Message count: {bot.message_count()}")
    print("✅ Test 3 complete")

    # Test 4: Clear history
    print("\n" + "=" * 60)
    print("\n📝 Test 4: Clear History")
    original_count = bot.message_count()
    bot.clear_history()
    print(f"Before clear: {original_count}, After clear: {bot.message_count()}")
    print("✅ Test 4 complete")

    # BONUS: Save/Load
    print("\n" + "=" * 60)
    print("\n🌟 BONUS: Save/Load")
    new_bot = ConversationBot(system_prompt="You are a friendly teacher.")
    new_bot.send_message("Teach me about Python")
    new_bot.save_to_file("conversation.json")
    print("Saved conversation to conversation.json")

    loaded_bot = ConversationBot()
    loaded_bot.load_from_file("conversation.json")
    print(f"Loaded {loaded_bot.message_count()} messages")
    print("✅ Bonus complete")

    print("\n" + "=" * 60)
    print("🎉 All tests passed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
