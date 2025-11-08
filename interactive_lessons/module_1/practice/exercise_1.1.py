"""
Practice Exercise 1.1: Your First API Call
===========================================

INSTRUCTIONS:
Complete the TODOs below to practice making API calls to Claude.
Run this file with: python exercise_1.1.py

Make sure you have:
1. Created a .env file with your ANTHROPIC_API_KEY
2. Installed required packages: pip install anthropic python-dotenv
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

# TODO 1: Create the Anthropic client
# HINT: client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
client = None  # Replace None with your code


def ask_question(question):
    """
    Send a question to Claude and return the answer.

    Args:
        question (str): The question to ask

    Returns:
        str: Claude's answer
    """
    # TODO 2: Make an API call to Claude
    # HINT: Use client.messages.create() with:
    #       - model: "claude-3-5-sonnet-20241022"
    #       - max_tokens: 1024
    #       - messages: A list with one user message

    response = None  # Replace with your API call

    # TODO 3: Extract the text from the response
    # HINT: response.content[0].text

    answer = None  # Replace with your code

    return answer


def main():
    """Main function to test your implementation."""

    print("=" * 60)
    print("EXERCISE 1.1: Your First API Call")
    print("=" * 60)

    # Test 1: Simple question
    print("\n📝 Test 1: Simple Question")
    question1 = "What is the capital of Japan?"
    try:
        answer1 = ask_question(question1)
        print(f"Q: {question1}")
        print(f"A: {answer1}")
        print("✅ Test 1 passed!")
    except Exception as e:
        print(f"❌ Test 1 failed: {e}")

    # Test 2: Explaining a concept
    print("\n" + "=" * 60)
    print("\n📝 Test 2: Concept Explanation")
    question2 = "Explain what an API is in one sentence."
    try:
        answer2 = ask_question(question2)
        print(f"Q: {question2}")
        print(f"A: {answer2}")
        print("✅ Test 2 passed!")
    except Exception as e:
        print(f"❌ Test 2 failed: {e}")

    # Test 3: Your own question!
    print("\n" + "=" * 60)
    print("\n📝 Test 3: Your Custom Question")

    # TODO 4: Ask your own question!
    your_question = "Replace this with your own question"

    try:
        your_answer = ask_question(your_question)
        print(f"Q: {your_question}")
        print(f"A: {your_answer}")
        print("✅ Test 3 passed!")
    except Exception as e:
        print(f"❌ Test 3 failed: {e}")

    print("\n" + "=" * 60)
    print("🎉 Exercise complete! Check your answers above.")
    print("=" * 60)


# BONUS CHALLENGE: Add error handling to ask_question()
# Wrap the API call in a try/except block to handle errors gracefully

if __name__ == "__main__":
    main()
