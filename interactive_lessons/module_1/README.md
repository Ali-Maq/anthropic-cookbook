# 🟢 Module 1: Foundations

Welcome to Module 1! This is where your journey with the Anthropic Python SDK begins.

## 📚 Overview

**Time to Complete**: 2-3 hours
**Difficulty**: Beginner
**Prerequisites**: Basic Python knowledge

In this module, you'll learn the fundamental building blocks of working with Claude's API. By the end, you'll be able to build simple conversational AI applications!

---

## 🎯 Learning Objectives

After completing this module, you will be able to:

- ✅ Make API calls to Claude using the Python SDK
- ✅ Understand API request and response structures
- ✅ Build multi-turn conversations with memory
- ✅ Use system prompts to control Claude's behavior
- ✅ Manage conversation history efficiently
- ✅ Control output parameters like temperature and max_tokens
- ✅ Extract and work with structured data

---

## 📖 Lessons

### Lesson 1.1: Your First API Call
**Time**: 30-40 minutes

**What you'll learn**:
- Setting up the Anthropic client
- Making your first API call
- Understanding the response structure
- Extracting answers from Claude
- Token usage and costs

**Files**:
- 📓 Notebook: `lesson_1.1.ipynb`
- ✍️ Practice: `practice/exercise_1.1.py`
- ✅ Solution: `solutions/exercise_1.1_solution.py`

---

### Lesson 1.2: Messages & Conversations
**Time**: 45-60 minutes

**What you'll learn**:
- Multi-turn conversations
- Managing conversation history
- User vs Assistant roles
- System prompts and personality
- Building a conversation manager

**Files**:
- 📓 Notebook: `lesson_1.2.ipynb`
- ✍️ Practice: `practice/exercise_1.2.py`
- ✅ Solution: `solutions/exercise_1.2_solution.py`

---

### Lesson 1.3: Controlling Outputs
**Time**: 40-50 minutes

**What you'll learn**:
- Temperature and randomness
- Max tokens explained
- Stop sequences
- Getting consistent results
- JSON mode basics

**Files**:
- 📓 Notebook: `lesson_1.3.ipynb`
- ✍️ Practice: `practice/exercise_1.3.py`
- ✅ Solution: `solutions/exercise_1.3_solution.py`

---

### Lesson 1.4: Working with JSON
**Time**: 40-50 minutes

**What you'll learn**:
- Enabling JSON mode
- Extracting structured data
- Data validation
- Error handling
- Real-world use cases

**Files**:
- 📓 Notebook: `lesson_1.4.ipynb`
- ✍️ Practice: `practice/exercise_1.4.py`
- ✅ Solution: `solutions/exercise_1.4_solution.py`

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install anthropic python-dotenv jupyter
```

### 2. Set Up Your API Key

Create a `.env` file in the root directory:

```bash
ANTHROPIC_API_KEY=your_api_key_here
```

Get your API key from: https://console.anthropic.com

### 3. Start with Lesson 1.1

```bash
jupyter notebook lesson_1.1.ipynb
```

---

## 📝 How to Use These Lessons

Each lesson follows this structure:

### 1. 📚 Read the Concepts
Start by reading the explanations. Concepts are broken down into simple language with analogies and examples.

### 2. 🔍 Study the Code
Every code cell has **LINE-BY-LINE EXPLANATIONS** that explain what each line does and why.

Example:
```python
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# LINE-BY-LINE EXPLANATION:
# ---------------------------
# client = Creates a variable called 'client'
# Anthropic(...) = Creates an instance of the Anthropic class
# api_key=... = Passes your API key for authentication
# os.environ.get(...) = Safely gets your API key from environment variables
```

### 3. 🧪 Run the Code
Execute each cell and observe the outputs. **Experiment** by changing values!

### 4. ✍️ Complete Practice Exercises
After each lesson, complete the corresponding practice file in the `practice/` folder.

### 5. ✅ Check Solutions
Compare your work with the solutions in the `solutions/` folder.

### 6. 🤔 Reflect
Answer the reflection questions at the end of each lesson to solidify your understanding.

---

## 💡 Learning Tips

### Do's ✅
- **Type the code yourself** - Don't copy/paste! Muscle memory helps learning
- **Experiment** - Change parameters and see what happens
- **Read error messages** - They're teaching tools!
- **Take breaks** - Learning is better in focused sessions
- **Ask questions** - Use the reflection prompts to think deeply

### Don'ts ❌
- Don't rush through - take time to understand
- Don't skip the practice exercises
- Don't just read - actually run the code!
- Don't be afraid to make mistakes

---

## 🎯 Module Project: Simple Q&A Chatbot

After completing all lessons, build this capstone project:

**Project**: Create a command-line chatbot that:
1. Has a configurable personality (system prompt)
2. Maintains conversation history
3. Tracks and displays token usage
4. Can save/load conversations to/from files
5. Has error handling for network issues

**Starter code**: `module_project/chatbot_starter.py`
**Solution**: `module_project/chatbot_solution.py`

---

## 📊 Self-Assessment

After completing this module, you should be able to answer:

- [ ] What is an API and why use it?
- [ ] How do you authenticate with the Anthropic API?
- [ ] What's the difference between input and output tokens?
- [ ] Why must you send conversation history with each API call?
- [ ] What is a system prompt and when should you use one?
- [ ] How do you extract text from Claude's response?
- [ ] What's the purpose of `max_tokens`?
- [ ] How do you handle API errors gracefully?

---

## 🔗 Additional Resources

### Official Documentation
- [Anthropic API Docs](https://docs.anthropic.com)
- [Python SDK Reference](https://github.com/anthropics/anthropic-sdk-python)
- [API Reference](https://docs.anthropic.com/en/api)

### Helpful Links
- [Pricing Information](https://www.anthropic.com/pricing)
- [Rate Limits](https://docs.anthropic.com/en/api/rate-limits)
- [Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/best-practices)

### Community
- [Discord Community](https://discord.gg/anthropic)
- [GitHub Discussions](https://github.com/anthropics/anthropic-sdk-python/discussions)

---

## ❓ Troubleshooting

### "API key not found" error
- Make sure you created a `.env` file
- Check that it contains `ANTHROPIC_API_KEY=your_key`
- Verify you called `load_dotenv()` in your code

### "Module not found" error
- Run `pip install anthropic python-dotenv`
- Make sure you're in the correct Python environment

### Rate limit errors
- You're making too many requests too quickly
- Add delays between requests with `time.sleep(1)`
- Check your rate limits at console.anthropic.com

### Timeout errors
- Your internet connection might be slow
- Try increasing the timeout in the client
- Check Anthropic's status page

---

## ✅ Module Complete Checklist

Before moving to Module 2, make sure you've:

- [ ] Completed all 4 lessons
- [ ] Finished all practice exercises
- [ ] Reviewed the solutions
- [ ] Built the module project
- [ ] Can answer all self-assessment questions
- [ ] Understand how to make API calls confidently

---

## 🎓 Next Steps

Once you've completed Module 1, you're ready for:

**🟢 Module 2: Tool Use Basics** - Learn how to give Claude the ability to use functions and external tools!

---

## 💬 Feedback

Found an issue or have suggestions? Open an issue in the GitHub repo or join our Discord community!

---

**Happy Learning! 🚀**

Remember: Everyone starts somewhere. Take your time, practice regularly, and don't hesitate to review concepts multiple times. You've got this!
