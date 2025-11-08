# 🟢 Module 2: Tool Use Basics

## 📚 Overview

**Time to Complete**: 3-4 hours
**Difficulty**: Beginner to Intermediate
**Prerequisites**: Module 1 complete

This module teaches you how to give Claude superpowers by connecting it to external tools and functions!

---

## 🎯 Learning Objectives

After completing this module, you will be able to:

- ✅ Understand what tools are and why they're powerful
- ✅ Define custom tools for Claude to use
- ✅ Implement the tool use loop
- ✅ Build agents that use tools autonomously
- ✅ Work with multiple tools simultaneously
- ✅ Use Pydantic for type-safe tool definitions
- ✅ Handle errors and edge cases

---

## 📖 Lessons

### Lesson 2.1: Understanding Tools ✅
**Time**: 45-60 minutes

Learn the fundamentals of tool use:
- What tools are and why they matter
- Defining your first tool (calculator)
- The tool use request-execute-respond loop
- Building reusable tool handlers

**Files**:
- 📓 `lesson_2.1.ipynb`
- ✍️ `practice/exercise_2.1.py`
- ✅ `solutions/exercise_2.1_solution.py`

---

### Lesson 2.2: Building Your First Agent
**Time**: 45-60 minutes

Create an autonomous agent:
- What makes something an "agent"
- Multi-turn tool use
- Building a customer service agent
- Agent decision-making patterns

---

### Lesson 2.3: Multiple Tools & Parallel Execution
**Time**: 45-60 minutes

Advanced tool patterns:
- Giving Claude access to many tools
- How Claude chooses which tool to use
- Parallel tool execution
- Tool chaining and workflows

---

### Lesson 2.4: Type-Safe Tools with Pydantic
**Time**: 45-60 minutes

Professional tool development:
- Using Pydantic models for validation
- Automatic schema generation
- Type hints and IDE support
- Production-ready tool patterns

---

## 🚀 Getting Started

Make sure you completed Module 1 first! Then:

```bash
cd interactive_lessons/module_2
jupyter notebook lesson_2.1.ipynb
```

---

## 🎯 Module Project: Multi-Tool Assistant

Build a complete AI assistant that can:
1. Answer questions (using web search tool)
2. Do calculations (calculator tool)
3. Set reminders (reminder tool)
4. Check weather (weather API tool)
5. Send emails (email tool - simulated)

**Project files**: `module_project/`

---

## 💡 What You'll Build

### Lesson 2.1
- ✅ Calculator tool
- ✅ Weather tool (simulated)
- ✅ Tool use handler function

### Lesson 2.2
- ✅ Customer service agent
- ✅ Multi-turn conversations with tools
- ✅ Context-aware tool usage

### Lesson 2.3
- ✅ Multi-tool system
- ✅ Parallel execution
- ✅ Tool selection logic

### Lesson 2.4
- ✅ Pydantic-based tools
- ✅ Validated inputs
- ✅ Professional code patterns

---

## ✅ Completion Checklist

- [ ] Completed all 4 lessons
- [ ] Finished all practice exercises
- [ ] Built the module project
- [ ] Can explain what tools are
- [ ] Can define and implement custom tools
- [ ] Can build a multi-tool agent
- [ ] Understand tool selection and execution

---

## 🎓 Next Steps

Once complete, move to **Module 3: Vision & Multimodal** to learn how to work with images and documents!
