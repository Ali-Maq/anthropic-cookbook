# 🚀 Quick Start Guide - Interactive Learning System

Welcome to the **Interactive Anthropic Cookbook Learning System**! This guide will get you started in 5 minutes.

---

## ⚡ 5-Minute Setup

### Step 1: Install Required Packages

```bash
pip install anthropic python-dotenv jupyter pandas
```

### Step 2: Get Your API Key

1. Go to https://console.anthropic.com
2. Sign up or log in
3. Navigate to API Keys
4. Create a new key
5. Copy it (you'll only see it once!)

### Step 3: Create Your `.env` File

In the root of the `anthropic-cookbook` directory, create a file called `.env`:

```bash
# .env file
ANTHROPIC_API_KEY=your_actual_api_key_here
```

**Important**: Never commit this file to git! It's in `.gitignore` already.

### Step 4: Start Learning!

```bash
cd interactive_lessons/module_1
jupyter notebook lesson_1.1.ipynb
```

---

## 🗺️ Your Learning Journey

### Complete Beginner? Start Here!

Follow this path:

1. **Read**: [`INTERACTIVE_LEARNING_HUB.md`](../INTERACTIVE_LEARNING_HUB.md) - Overview of everything
2. **Start**: Module 1, Lesson 1.1 - Your first API call
3. **Practice**: Complete exercises after each lesson
4. **Build**: Module 1 project - Simple chatbot

**Time Investment**: 2-3 hours for Module 1

### Quick Learner? Fast Track!

If you have programming experience:

1. Start with Module 1, Lesson 1.1 (basics)
2. Skip to Module 2 if you grasp concepts quickly
3. Focus on practice exercises
4. Build the module projects

**Time Investment**: 1-2 hours for Module 1

### Specific Goal? Choose Your Path!

**Goal: Build a Chatbot**
- Module 1 (all lessons) → Module 2 (Lessons 2.1-2.3)

**Goal: Process Documents**
- Module 1 (Lessons 1.1, 1.4) → Module 3 (all lessons)

**Goal: Build RAG System**
- Module 1 (Lessons 1.1-1.2) → Module 4 (all lessons)

**Goal: Build AI Agents**
- Module 1 (all) → Module 2 (all) → Module 5 (all)

---

## 📁 Directory Structure

```
interactive_lessons/
│
├── INTERACTIVE_LEARNING_HUB.md    # Main curriculum overview
├── QUICKSTART.md                  # This file!
│
├── module_1/                      # Foundations
│   ├── README.md                  # Module overview
│   ├── lesson_1.1.ipynb          # Lesson notebooks
│   ├── lesson_1.2.ipynb
│   ├── practice/                  # Practice exercises
│   │   ├── exercise_1.1.py
│   │   └── ...
│   └── solutions/                 # Exercise solutions
│       ├── exercise_1.1_solution.py
│       └── ...
│
├── module_2/                      # Tool Use (coming soon)
├── module_3/                      # Vision & Multimodal (coming soon)
└── ...                            # More modules
```

---

## 🎯 What You'll Learn

### Module 1: Foundations (Available Now!)
✅ Making API calls
✅ Multi-turn conversations
✅ System prompts
✅ Working with JSON

### Coming Soon:
- Module 2: Tool Use Basics
- Module 3: Vision & Multimodal
- Module 4: RAG Systems
- Module 5: Agent Patterns
- Module 6: Advanced Topics
- Module 7: Skills & Automation
- Module 8: Enterprise & Production

---

## 💻 How Lessons Work

Each lesson includes:

### 📓 Interactive Jupyter Notebooks
- Concept explanations in plain English
- **Line-by-line code explanations**
- Runnable examples
- Experiments to try

### ✍️ Practice Exercises
- Hands-on coding challenges
- Real-world scenarios
- Progressive difficulty

### ✅ Solutions
- Complete solutions with explanations
- Best practices highlighted
- Alternative approaches shown

### 🎯 Projects
- End-of-module capstone projects
- Apply everything you learned
- Build portfolio pieces

---

## 🔍 Example: Your First 10 Minutes

Let's see what a lesson looks like:

```python
# In lesson_1.1.ipynb, you'll see:

# Import libraries
import os
from anthropic import Anthropic

# LINE-BY-LINE EXPLANATION:
# ---------------------------
# import os
#   'os' is Python's operating system interface
#   We use it to read environment variables (like your API key)
#
# from anthropic import Anthropic
#   Import the main Anthropic class
#   This is what talks to Claude!

# Create a client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Make your first API call
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

# Get the answer
answer = response.content[0].text
print(answer)
```

See? Every line is explained! No mystery code.

---

## 🎓 Learning Modes

### 🐢 Thorough Mode (Recommended for Beginners)
- Read all explanations
- Run every code cell
- Complete all exercises
- Answer reflection questions
- Build module projects

**Time**: 3-4 hours per module

### 🐇 Fast Track Mode
- Skim concepts you know
- Focus on code examples
- Do practice exercises only
- Skip reflection questions
- Build projects if time permits

**Time**: 1-2 hours per module

### 🎯 Project-Based Mode
- Jump straight to module projects
- Reference lessons when stuck
- Learn by building
- Google/AI assist when needed

**Time**: 30-60 minutes per module

---

## ❓ FAQ

### Q: Do I need to know Python?
**A**: Basic Python knowledge helps, but we explain everything line-by-line. If you know variables, functions, and lists, you're good!

### Q: How much does this cost?
**A**: The learning materials are free! You'll pay only for API usage:
- Module 1: ~$0.10-0.50 in API costs
- Practice responsibly and costs stay minimal

### Q: Can I use a different model than Sonnet?
**A**: Yes! Try:
- `claude-3-haiku-20240307` (faster, cheaper)
- `claude-3-opus-20240229` (smarter, more expensive)

### Q: I'm getting errors. Help!
**A**: Check:
1. Is your API key in the `.env` file?
2. Did you run `load_dotenv()`?
3. Did you install all packages?
4. See the Troubleshooting section in each module README

### Q: How long does the full curriculum take?
**A**:
- Complete beginner: 40-50 hours
- Some experience: 20-30 hours
- Experienced developer: 10-15 hours

### Q: Can I skip lessons?
**A**: Yes! But we recommend doing Module 1 completely since it's foundational.

---

## 🌟 Success Tips

1. **Code Along**: Type code yourself, don't copy/paste
2. **Experiment**: Change values, break things, learn!
3. **Practice Daily**: 30 minutes/day > 3 hours on weekend
4. **Build Projects**: Apply knowledge to real problems
5. **Join Community**: Share progress, ask questions
6. **Review Often**: Revisit earlier lessons

---

## 🐛 Troubleshooting

### Common Issues:

**"ModuleNotFoundError: No module named 'anthropic'"**
```bash
pip install anthropic
```

**"API key not found"**
- Check `.env` file exists
- Verify it contains `ANTHROPIC_API_KEY=your_key`
- Make sure you ran `load_dotenv()`

**"Rate limit exceeded"**
- You're making requests too fast
- Add `time.sleep(1)` between requests
- Check your rate limits at console.anthropic.com

**Jupyter not starting**
```bash
pip install jupyter
jupyter notebook
```

---

## 📚 Additional Resources

### Official Docs
- [Anthropic Documentation](https://docs.anthropic.com)
- [API Reference](https://docs.anthropic.com/en/api)
- [Python SDK](https://github.com/anthropics/anthropic-sdk-python)

### Community
- [Discord](https://discord.gg/anthropic)
- [GitHub Discussions](https://github.com/anthropics/anthropic-sdk-python/discussions)

### Original Cookbook
- Browse the main cookbook for production examples
- All original tutorials are still available
- Use as reference for advanced topics

---

## ✅ Ready to Start?

You have everything you need! Here's your first step:

```bash
cd interactive_lessons/module_1
jupyter notebook lesson_1.1.ipynb
```

**Or** if you prefer reading first:
1. Open [`INTERACTIVE_LEARNING_HUB.md`](../INTERACTIVE_LEARNING_HUB.md)
2. Read the curriculum overview
3. Choose your learning path
4. Start Module 1!

---

## 💬 Feedback & Support

- **Found a bug?** Open an issue on GitHub
- **Have a suggestion?** Join our Discord
- **Love it?** Star the repo and share with friends!

---

**Happy Learning! 🚀**

Remember: Every expert was once a beginner. Take your time, practice regularly, and enjoy the journey!
