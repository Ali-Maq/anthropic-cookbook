# 🎓 Interactive Anthropic SDK Learning Platform

## 🌟 **A DataCamp/Codecademy-Style Web Application**

This is a fully interactive web platform for learning the Anthropic Python SDK with:
- ✅ **Interactive code editor** (CodeMirror)
- ✅ **Automatic test runner** with instant feedback
- ✅ **Progress tracking** across modules and lessons
- ✅ **Line-by-line explanations**
- ✅ **Hints system** for guided learning
- ✅ **Beautiful DataCamp-inspired UI**

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd web_app
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Create a `.env` file in the `web_app` directory:

```bash
ANTHROPIC_API_KEY=your_api_key_here
```

### 3. Run the Server

```bash
python backend/app.py
```

### 4. Open Your Browser

Navigate to: **http://localhost:5000**

🎉 **You're ready to learn!**

---

## 📁 Project Structure

```
web_app/
│
├── backend/
│   └── app.py                  # Flask server with code execution
│
├── frontend/
│   ├── index.html              # Homepage with modules
│   ├── lesson.html             # Interactive lesson page
│   │
│   ├── css/
│   │   └── style.css           # DataCamp-inspired styling
│   │
│   ├── js/
│   │   ├── app.js              # Homepage logic
│   │   └── lesson.js           # Lesson interactivity
│   │
│   └── lessons/
│       └── lesson_*.json       # Lesson content (to be added)
│
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## ✨ Features

### 🖥️ Interactive Code Editor
- Syntax highlighting with CodeMirror
- Python mode with auto-indentation
- Monokai theme for comfortable coding
- Run code directly in the browser

### ✅ Automatic Testing
- Write code and get instant feedback
- Unit tests run automatically
- Clear pass/fail indicators
- Helpful error messages

### 📊 Progress Tracking
- Track completion across all modules
- Visual progress bars
- Session-based progress (upgradeable to database)
- Celebrate milestones

### 🎯 Learning Features
- **Instructions Tab**: Clear, step-by-step tasks
- **Explanation Tab**: Line-by-line code breakdown
- **Hints Tab**: Progressive hints when you're stuck
- **Starter Code**: Pre-filled templates to guide you
- **Reset Button**: Start over anytime

### 🎨 Beautiful UI
- DataCamp-inspired design
- Responsive layout (works on mobile!)
- Dark theme for code editing
- Smooth animations and transitions

---

## 🏗️ How It Works

### Architecture

```
┌─────────────┐
│   Browser   │
│  (Frontend) │
└──────┬──────┘
       │ HTTP Requests
       │
┌──────▼──────┐
│    Flask    │
│  (Backend)  │
└──────┬──────┘
       │
       ├─► Execute Python Code (sandboxed)
       ├─► Run Tests
       ├─► Track Progress
       └─► Serve Lessons
```

### Code Execution Flow

1. **User writes code** in CodeMirror editor
2. **Clicks "Run Code"** or "Submit Answer"
3. **Frontend sends code** to Flask backend via POST /api/run-code
4. **Backend executes code** in restricted namespace
5. **Runs tests** if provided
6. **Returns results** (output, errors, test results)
7. **Frontend displays** results with color-coded feedback

---

## 🎓 Available Lessons

### Module 1: Foundations
1. **Lesson 1.1**: Your First API Call
2. **Lesson 1.2**: Messages & Conversations
3. **Lesson 1.3**: Controlling Outputs
4. **Lesson 1.4**: Working with JSON

### Module 2: Tool Use
1. **Lesson 2.1**: Understanding Tools

### Coming Soon
- Module 3: Vision & Multimodal
- Module 4: RAG Systems
- Module 5: Agent Patterns

---

## 🔧 API Endpoints

### `GET /`
Returns the homepage with module overview

### `GET /lesson/<lesson_id>`
Returns the interactive lesson page

### `POST /api/run-code`
Execute Python code and run tests

**Request Body**:
```json
{
  "code": "print('Hello, World!')",
  "tests": [
    {
      "name": "Test name",
      "assertion": "some_variable == expected_value",
      "success_message": "✓ Test passed!",
      "failure_message": "✗ Test failed"
    }
  ]
}
```

**Response**:
```json
{
  "success": true,
  "output": "Hello, World!\n",
  "error": "",
  "test_results": [
    {
      "name": "Test name",
      "passed": true,
      "message": "✓ Test passed!"
    }
  ]
}
```

### `GET /api/lessons`
Get list of all lessons

### `GET /api/lesson/<lesson_id>`
Get content for a specific lesson

### `GET /api/progress`
Get user's progress

### `POST /api/progress`
Save user's progress

---

## 🔒 Security Notes

**Current Implementation**:
- Code execution uses a restricted global namespace
- Limited built-in functions available
- Session-based progress (not persistent across browser sessions)

**For Production**:
- Use Docker containers for code execution
- Implement user authentication
- Use a database for progress tracking
- Add rate limiting
- Implement proper sandboxing (e.g., PyPy sandbox, Docker)

---

## 🎨 Customization

### Adding New Lessons

Create a JSON file in `frontend/lessons/`:

```json
{
  "id": "1-1",
  "module": 1,
  "title": "Your First API Call",
  "exercises": [
    {
      "id": 1,
      "title": "Exercise Title",
      "instructions": "<h2>Task</h2><p>Instructions here</p>",
      "starterCode": "# Your starter code\n",
      "solution": "# Complete solution",
      "explanation": "<h3>Explanation</h3><p>Details...</p>",
      "hints": ["Hint 1", "Hint 2"],
      "tests": [
        {
          "name": "Test description",
          "assertion": "variable_name == expected_value",
          "success_message": "✓ Passed!",
          "failure_message": "✗ Failed"
        }
      ]
    }
  ]
}
```

### Customizing Styles

Edit `frontend/css/style.css` and modify the CSS variables:

```css
:root {
    --primary-color: #3b82f6;    /* Change to your brand color */
    --secondary-color: #10b981;  /* Success color */
    --dark-bg: #1e293b;          /* Dark theme background */
}
```

---

## 🚧 Development

### Running in Development Mode

```bash
# Enable Flask debug mode
export FLASK_DEBUG=1
python backend/app.py
```

### Testing Code Execution

```bash
curl -X POST http://localhost:5000/api/run-code \
  -H "Content-Type: application/json" \
  -d '{"code": "print(\"Hello, World!\")"}'
```

---

## 📊 Tech Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: Vanilla JavaScript (no framework needed!)
- **Code Editor**: CodeMirror
- **Styling**: Custom CSS (DataCamp-inspired)
- **Code Execution**: Python exec() with restricted namespace

---

## 🎯 Roadmap

- [ ] Add user authentication
- [ ] Database for persistent progress
- [ ] More lesson content (Modules 3-8)
- [ ] Video explanations
- [ ] Community features (share solutions)
- [ ] Achievements and badges
- [ ] Dark mode toggle
- [ ] Code playback/recording
- [ ] Mobile app

---

## 🤝 Contributing

Want to add lessons or improve the platform? Here's how:

1. Fork the repository
2. Create your feature branch
3. Add lesson content or features
4. Test thoroughly
5. Submit a pull request

---

## 📝 License

This educational platform is built for learning purposes.

---

## 🎉 Start Learning!

```bash
python backend/app.py
```

Then open **http://localhost:5000** in your browser and start your interactive learning journey!

**Happy Coding!** 🚀
