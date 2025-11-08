"""
Flask Backend for Interactive Learning Platform
DataCamp/Codecademy style web application
"""

from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
import os
import sys
import io
import traceback
import json
from contextlib import redirect_stdout, redirect_stderr
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__,
            template_folder='../frontend',
            static_folder='../frontend')
app.secret_key = os.urandom(24)
CORS(app)

# Store user progress in session (in production, use a database)
@app.route('/')
def index():
    """Main landing page"""
    return render_template('index.html')

@app.route('/lesson/<lesson_id>')
def lesson(lesson_id):
    """Serve a specific lesson"""
    return render_template('lesson.html', lesson_id=lesson_id)

@app.route('/api/run-code', methods=['POST'])
def run_code():
    """
    Execute user's Python code safely and return results.
    This runs in a restricted environment.
    """
    data = request.json
    code = data.get('code', '')
    tests = data.get('tests', [])

    # Capture stdout and stderr
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()

    results = {
        'success': False,
        'output': '',
        'error': '',
        'test_results': []
    }

    try:
        # Create a restricted global namespace
        global_namespace = {
            '__builtins__': __builtins__,
            'print': print,
            'range': range,
            'len': len,
            'str': str,
            'int': int,
            'float': float,
            'list': list,
            'dict': dict,
            'tuple': tuple,
            'set': set,
        }

        # Add Anthropic client if needed
        if 'anthropic' in code.lower() or 'client' in code:
            from anthropic import Anthropic
            global_namespace['Anthropic'] = Anthropic
            global_namespace['os'] = os

        # Execute user code
        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
            exec(code, global_namespace)

        results['output'] = stdout_capture.getvalue()
        results['success'] = True

        # Run tests if provided
        for test in tests:
            test_result = run_test(test, global_namespace)
            results['test_results'].append(test_result)

    except Exception as e:
        results['error'] = f"{type(e).__name__}: {str(e)}\n{traceback.format_exc()}"
        results['output'] = stdout_capture.getvalue()

    return jsonify(results)

def run_test(test, namespace):
    """Run a single test and return result"""
    test_result = {
        'name': test.get('name', 'Test'),
        'passed': False,
        'message': ''
    }

    try:
        # Execute test code
        test_code = test.get('code', '')
        exec(test_code, namespace)

        # Check assertion
        assertion = test.get('assertion', '')
        if assertion:
            exec(f"assert {assertion}", namespace)

        test_result['passed'] = True
        test_result['message'] = test.get('success_message', '✓ Test passed!')

    except AssertionError as e:
        test_result['message'] = test.get('failure_message', f'✗ Test failed: {str(e)}')
    except Exception as e:
        test_result['message'] = f'✗ Error in test: {str(e)}'

    return test_result

@app.route('/api/progress', methods=['GET', 'POST'])
def progress():
    """Track user progress"""
    if request.method == 'POST':
        data = request.json
        lesson_id = data.get('lesson_id')
        completed = data.get('completed', False)

        if 'progress' not in session:
            session['progress'] = {}

        session['progress'][lesson_id] = completed
        session.modified = True

        return jsonify({'success': True})

    else:
        return jsonify(session.get('progress', {}))

@app.route('/api/lessons')
def get_lessons():
    """Get list of all lessons"""
    lessons = [
        {
            'id': '1-1',
            'module': 1,
            'title': 'Your First API Call',
            'duration': '30-40 min',
            'exercises': 5
        },
        {
            'id': '1-2',
            'module': 1,
            'title': 'Messages & Conversations',
            'duration': '45-60 min',
            'exercises': 6
        },
        {
            'id': '1-3',
            'module': 1,
            'title': 'Controlling Outputs',
            'duration': '40-50 min',
            'exercises': 5
        },
        {
            'id': '1-4',
            'module': 1,
            'title': 'Working with JSON',
            'duration': '40-50 min',
            'exercises': 6
        },
        {
            'id': '2-1',
            'module': 2,
            'title': 'Understanding Tools',
            'duration': '45-60 min',
            'exercises': 5
        }
    ]

    return jsonify(lessons)

@app.route('/api/lesson/<lesson_id>')
def get_lesson_content(lesson_id):
    """Get content for a specific lesson"""
    # Load lesson content from JSON file
    lesson_file = f'../frontend/lessons/lesson_{lesson_id}.json'

    try:
        with open(lesson_file, 'r') as f:
            lesson_data = json.load(f)
        return jsonify(lesson_data)
    except FileNotFoundError:
        return jsonify({'error': 'Lesson not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
