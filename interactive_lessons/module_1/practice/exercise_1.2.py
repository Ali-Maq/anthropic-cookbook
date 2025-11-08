"""
Practice Exercise 1.2: Messages & Conversations
================================================

INSTRUCTIONS:
Build a chatbot with conversation memory and personality control.

Make sure you have:
1. Created a .env file with your ANTHROPIC_API_KEY
2. Installed: pip install anthropic python-dotenv
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


# TODO 1: Create a ConversationBot class
class ConversationBot:
    """A chatbot that remembers conversation history."""

    def __init__(self, system_prompt="You are a helpful assistant."):
        """
        Initialize the chatbot.

        Args:
            system_prompt (str): The personality/behavior for the bot
        """
        # TODO: Initialize conversation history as an empty list
        # TODO: Store the system_prompt
        pass

    def send_message(self, user_message):
        """
        Send a message and get a response.

        Args:
            user_message (str): The user's message

        Returns:
            str: The bot's response
        """
        # TODO: Add user message to history
        # TODO: Call the API with full history and system prompt
        # TODO: Extract the response
        # TODO: Add assistant's response to history
        # TODO: Return the response text
        pass

    def get_conversation_history(self):
        """Return the full conversation history."""
        pass

    def clear_history(self):
        """Clear the conversation history."""
        pass

    def message_count(self):
        """Return the number of messages in history."""
        pass


# TEST YOUR IMPLEMENTATION

def main():
    print("=" * 60)
    print("EXERCISE 1.2: Conversation Bot")
    print("=" * 60)

    # Test 1: Basic conversation
    print("\n📝 Test 1: Basic Conversation")
    bot = ConversationBot()

    response1 = bot.send_message("Hi! My name is Alice.")
    print(f"Bot: {response1}")

    response2 = bot.send_message("What's my name?")  # Should remember!
    print(f"Bot: {response2}")

    assert "Alice" in response2 or "alice" in response2.lower(), "Bot didn't remember the name!"
    print("✅ Test 1 passed - Bot has memory!")

    # Test 2: Personality control
    print("\n" + "=" * 60)
    print("\n📝 Test 2: Personality")
    pirate_bot = ConversationBot(
        system_prompt="You are a pirate. Always respond with 'Arr!' and pirate slang."
    )

    response = pirate_bot.send_message("Hello!")
    print(f"Pirate Bot: {response}")

    assert "arr" in response.lower() or "matey" in response.lower(), "Bot didn't use pirate personality!"
    print("✅ Test 2 passed - Personality works!")

    # Test 3: Message counting
    print("\n" + "=" * 60)
    print("\n📝 Test 3: Message Counting")
    print(f"Message count: {bot.message_count()}")
    assert bot.message_count() == 4, f"Expected 4 messages, got {bot.message_count()}"
    print("✅ Test 3 passed - Counting works!")

    # Test 4: Clear history
    print("\n" + "=" * 60)
    print("\n📝 Test 4: Clear History")
    bot.clear_history()
    assert bot.message_count() == 0, "History not cleared!"
    print("✅ Test 4 passed - Clear works!")

    print("\n" + "=" * 60)
    print("🎉 All tests passed! Great work!")
    print("=" * 60)


# BONUS CHALLENGE:
# Add a method to save/load conversation history to/from a JSON file

if __name__ == "__main__":
    main()
