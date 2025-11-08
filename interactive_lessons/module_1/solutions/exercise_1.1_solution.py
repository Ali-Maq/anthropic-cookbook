"""
Practice Exercise 1.1: Your First API Call - SOLUTION
======================================================

This is the complete solution to Exercise 1.1.
Use this to check your work or if you get stuck!
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

# SOLUTION 1: Create the Anthropic client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


def ask_question(question):
    """
    Send a question to Claude and return the answer.

    Args:
        question (str): The question to ask

    Returns:
        str: Claude's answer
    """
    # SOLUTION 2: Make an API call to Claude
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": question}
        ]
    )

    # SOLUTION 3: Extract the text from the response
    answer = response.content[0].text

    return answer


# BONUS: Version with error handling
def ask_question_safe(question):
    """
    Send a question to Claude with error handling.

    Args:
        question (str): The question to ask

    Returns:
        str: Claude's answer or error message
    """
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": question}
            ]
        )
        return response.content[0].text

    except Exception as e:
        return f"Error occurred: {str(e)}"


def main():
    """Main function to test the implementation."""

    print("=" * 60)
    print("EXERCISE 1.1 SOLUTION: Your First API Call")
    print("=" * 60)

    # Test 1: Simple question
    print("\n📝 Test 1: Simple Question")
    question1 = "What is the capital of Japan?"
    answer1 = ask_question(question1)
    print(f"Q: {question1}")
    print(f"A: {answer1}")
    print("✅ Test 1 complete!")

    # Test 2: Explaining a concept
    print("\n" + "=" * 60)
    print("\n📝 Test 2: Concept Explanation")
    question2 = "Explain what an API is in one sentence."
    answer2 = ask_question(question2)
    print(f"Q: {question2}")
    print(f"A: {answer2}")
    print("✅ Test 2 complete!")

    # Test 3: Custom question
    print("\n" + "=" * 60)
    print("\n📝 Test 3: Custom Question")
    question3 = "What are three fun facts about space?"
    answer3 = ask_question(question3)
    print(f"Q: {question3}")
    print(f"A: {answer3}")
    print("✅ Test 3 complete!")

    # Bonus: Test error handling
    print("\n" + "=" * 60)
    print("\n🌟 BONUS: Testing Error Handling")
    safe_answer = ask_question_safe("Tell me a joke!")
    print(f"Safe Answer: {safe_answer}")
    print("✅ Bonus complete!")

    print("\n" + "=" * 60)
    print("🎉 All tests passed! Great work!")
    print("=" * 60)


if __name__ == "__main__":
    main()
