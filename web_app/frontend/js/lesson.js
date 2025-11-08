/**
 * Lesson Page JavaScript - Interactive Code Editor & Testing
 * Handles the core interactive learning experience
 */

let editor;
let currentLesson = null;
let currentExerciseIndex = 0;
let hintsShown = 0;

// Initialize lesson when page loads
async function initializeLesson(lessonId) {
    // Initialize CodeMirror editor
    initializeEditor();

    // Load lesson content
    await loadLessonContent(lessonId);

    // Setup event listeners
    setupEventListeners();

    // Load first exercise
    loadExercise(0);
}

// Initialize CodeMirror editor
function initializeEditor() {
    const textarea = document.getElementById('code-editor');

    editor = CodeMirror.fromTextArea(textarea, {
        mode: 'python',
        theme: 'monokai',
        lineNumbers: true,
        indentUnit: 4,
        indentWithTabs: false,
        lineWrapping: true,
        autofocus: true
    });

    editor.setSize('100%', '100%');
}

// Load lesson content from server
async function loadLessonContent(lessonId) {
    try {
        const response = await fetch(`/api/lesson/${lessonId}`);
        currentLesson = await response.json();

        // Update lesson header
        document.getElementById('lesson-title').textContent = currentLesson.title;
        document.getElementById('lesson-badge').textContent = `Module ${currentLesson.module}`;

        // Update exercise counter
        updateExerciseCounter();

    } catch (error) {
        console.error('Error loading lesson:', error);
        // Fallback to demo lesson if not found
        loadDemoLesson(lessonId);
    }
}

// Load demo lesson (for testing)
function loadDemoLesson(lessonId) {
    currentLesson = {
        id: lessonId,
        module: 1,
        title: 'Your First API Call',
        exercises: [
            {
                id: 1,
                title: 'Import Anthropic Library',
                instructions: `
                    <h2>Exercise 1: Import the Anthropic Library</h2>
                    <p>Let's start by importing the Anthropic library and os module.</p>
                    <h3>Task:</h3>
                    <ol>
                        <li>Import the <code>os</code> module</li>
                        <li>Import the <code>Anthropic</code> class from <code>anthropic</code></li>
                        <li>Print "Setup complete!" to verify</li>
                    </ol>
                `,
                starterCode: `# Import the required libraries\n# TODO: Import os\n\n# TODO: Import Anthropic from anthropic\n\n# TODO: Print "Setup complete!"\n`,
                solution: `import os\nfrom anthropic import Anthropic\n\nprint("Setup complete!")`,
                explanation: `
                    <h3>Line-by-Line Explanation:</h3>
                    <pre><code>import os</code></pre>
                    <p>→ Imports Python's operating system interface. We use this to read environment variables.</p>

                    <pre><code>from anthropic import Anthropic</code></pre>
                    <p>→ Imports the Anthropic class from the anthropic library. This is the main client we use to talk to Claude.</p>

                    <pre><code>print("Setup complete!")</code></pre>
                    <p>→ Prints a message to verify everything is working.</p>
                `,
                hints: [
                    'Use <code>import os</code> to import the os module',
                    'Use <code>from anthropic import Anthropic</code> to import the Anthropic class',
                    'Use <code>print()</code> to output a message'
                ],
                tests: [
                    {
                        name: 'Imports os module',
                        assertion: '"os" in dir()',
                        success_message: '✓ os module imported correctly!',
                        failure_message: '✗ Make sure you import the os module'
                    },
                    {
                        name: 'Imports Anthropic class',
                        assertion: '"Anthropic" in dir()',
                        success_message: '✓ Anthropic class imported correctly!',
                        failure_message: '✗ Make sure you import Anthropic from anthropic'
                    }
                ]
            },
            {
                id: 2,
                title: 'Create Anthropic Client',
                instructions: `
                    <h2>Exercise 2: Create the Anthropic Client</h2>
                    <p>Now let's create a client to communicate with Claude.</p>
                    <h3>Task:</h3>
                    <ol>
                        <li>Create a variable called <code>client</code></li>
                        <li>Assign it an instance of <code>Anthropic()</code></li>
                        <li>Print the type of client to verify</li>
                    </ol>
                `,
                starterCode: `import os\nfrom anthropic import Anthropic\n\n# TODO: Create client variable\n\n# TODO: Print the type of client\n`,
                solution: `import os\nfrom anthropic import Anthropic\n\nclient = Anthropic()\nprint(type(client))`,
                explanation: `
                    <h3>Understanding the Client:</h3>
                    <pre><code>client = Anthropic()</code></pre>
                    <p>→ Creates an instance of the Anthropic class</p>
                    <p>→ This client object is your connection to Claude</p>
                    <p>→ You'll use this client to send messages and receive responses</p>
                `,
                hints: [
                    'Create a variable: <code>client = Anthropic()</code>',
                    'Use <code>type()</code> to check the type of an object',
                    'Print it with <code>print(type(client))</code>'
                ],
                tests: [
                    {
                        name: 'Client variable exists',
                        assertion: '"client" in dir()',
                        success_message: '✓ Client variable created!',
                        failure_message: '✗ Create a variable called client'
                    }
                ]
            }
        ]
    };

    updateExerciseCounter();
}

// Load a specific exercise
function loadExercise(index) {
    if (!currentLesson || index < 0 || index >= currentLesson.exercises.length) {
        return;
    }

    currentExerciseIndex = index;
    const exercise = currentLesson.exercises[index];

    // Update instructions
    document.getElementById('exercise-instructions').innerHTML = exercise.instructions;

    // Update explanation
    document.getElementById('explanation-content').innerHTML = exercise.explanation || '<p>Complete the exercise to see the explanation.</p>';

    // Reset hints
    hintsShown = 0;
    document.getElementById('hints-list').innerHTML = '';

    // Load starter code
    editor.setValue(exercise.starterCode || '');

    // Update counter
    updateExerciseCounter();

    // Update navigation buttons
    updateNavButtons();

    // Clear output and tests
    clearOutput();
    hideTestResults();

    // Update progress bar
    updateLessonProgress();
}

// Update exercise counter
function updateExerciseCounter() {
    const counter = document.getElementById('exercise-counter');
    if (counter && currentLesson) {
        counter.textContent = `Exercise ${currentExerciseIndex + 1} of ${currentLesson.exercises.length}`;
    }
}

// Update navigation buttons
function updateNavButtons() {
    const prevBtn = document.getElementById('prev-exercise');
    const nextBtn = document.getElementById('next-exercise');

    if (prevBtn) {
        prevBtn.disabled = currentExerciseIndex === 0;
    }

    if (nextBtn && currentLesson) {
        nextBtn.disabled = currentExerciseIndex >= currentLesson.exercises.length - 1;
    }
}

// Setup event listeners
function setupEventListeners() {
    // Navigation buttons
    document.getElementById('prev-exercise')?.addEventListener('click', previousExercise);
    document.getElementById('next-exercise')?.addEventListener('click', nextExercise);

    // Run and submit buttons
    document.getElementById('run-code')?.addEventListener('click', runCode);
    document.getElementById('submit-code')?.addEventListener('click', submitCode);

    // Reset button
    document.getElementById('reset-code')?.addEventListener('click', resetCode);

    // Clear output button
    document.getElementById('clear-output')?.addEventListener('click', clearOutput);

    // Tab switching
    document.querySelectorAll('.tab').forEach(tab => {
        tab.addEventListener('click', () => switchTab(tab.dataset.tab));
    });
}

// Switch tabs
function switchTab(tabName) {
    // Update tab buttons
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelector(`[data-tab="${tabName}"]`)?.classList.add('active');

    // Update tab content
    document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
    document.getElementById(`tab-${tabName}`)?.classList.add('active');
}

// Run code (without tests)
async function runCode() {
    const code = editor.getValue();

    try {
        const response = await fetch('/api/run-code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ code: code })
        });

        const result = await response.json();

        if (result.success) {
            displayOutput(result.output || 'Code executed successfully!', 'output');
        } else {
            displayOutput(result.error, 'error');
        }

    } catch (error) {
        displayOutput(`Network error: ${error.message}`, 'error');
    }
}

// Submit code (runs tests)
async function submitCode() {
    const code = editor.getValue();
    const exercise = currentLesson.exercises[currentExerciseIndex];

    try {
        const response = await fetch('/api/run-code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                code: code,
                tests: exercise.tests || []
            })
        });

        const result = await response.json();

        // Display output
        if (result.output) {
            displayOutput(result.output, 'output');
        }

        if (result.error) {
            displayOutput(result.error, 'error');
            return;
        }

        // Display test results
        displayTestResults(result.test_results);

        // Check if all tests passed
        const allPassed = result.test_results.every(t => t.passed);

        if (allPassed) {
            showSuccessModal();
            markExerciseComplete();
        }

    } catch (error) {
        displayOutput(`Network error: ${error.message}`, 'error');
    }
}

// Display output in console
function displayOutput(text, type = 'output') {
    const console = document.getElementById('output-console');
    const className = type === 'error' ? 'console-error' : 'console-output';

    const outputDiv = document.createElement('div');
    outputDiv.className = className;
    outputDiv.textContent = text;

    console.appendChild(outputDiv);
    console.scrollTop = console.scrollHeight;
}

// Clear output console
function clearOutput() {
    document.getElementById('output-console').innerHTML = '';
}

// Display test results
function displayTestResults(testResults) {
    const testList = document.getElementById('test-list');
    const testSection = document.getElementById('test-results');

    testList.innerHTML = '';

    testResults.forEach(test => {
        const testDiv = document.createElement('div');
        testDiv.className = `test-item ${test.passed ? 'passed' : 'failed'}`;

        testDiv.innerHTML = `
            <div class="test-icon">${test.passed ? '✓' : '✗'}</div>
            <div>
                <div class="test-name">${test.name}</div>
                <div class="test-message">${test.message}</div>
            </div>
        `;

        testList.appendChild(testDiv);
    });

    testSection.style.display = 'block';
}

// Hide test results
function hideTestResults() {
    document.getElementById('test-results').style.display = 'none';
}

// Reset code to starter
function resetCode() {
    const exercise = currentLesson.exercises[currentExerciseIndex];
    if (exercise) {
        editor.setValue(exercise.starterCode || '');
        clearOutput();
        hideTestResults();
    }
}

// Show success modal
function showSuccessModal() {
    const modal = document.getElementById('success-modal');
    modal.classList.add('show');
}

// Close modal
function closeModal() {
    const modal = document.getElementById('success-modal');
    modal.classList.remove('show');
}

// Navigate to next exercise
function nextExercise() {
    if (currentExerciseIndex < currentLesson.exercises.length - 1) {
        loadExercise(currentExerciseIndex + 1);
    }
}

// Navigate to previous exercise
function previousExercise() {
    if (currentExerciseIndex > 0) {
        loadExercise(currentExerciseIndex - 1);
    }
}

// Mark exercise as complete
function markExerciseComplete() {
    updateLessonProgress();

    // If all exercises complete, mark lesson as complete
    const allComplete = currentLesson.exercises.length > 0 &&
                       currentExerciseIndex === currentLesson.exercises.length - 1;

    if (allComplete) {
        saveLessonProgress(currentLesson.id, true);
    }
}

// Update lesson progress bar
function updateLessonProgress() {
    const completed = currentExerciseIndex + 1;
    const total = currentLesson.exercises.length;
    const percentage = (completed / total) * 100;

    const progressBar = document.getElementById('lesson-progress');
    if (progressBar) {
        progressBar.style.width = `${percentage}%`;
    }

    const progressText = document.getElementById('exercises-completed-text');
    if (progressText) {
        progressText.textContent = `${completed} of ${total} exercises completed`;
    }
}

// Save lesson progress
async function saveLessonProgress(lessonId, completed) {
    try {
        await fetch('/api/progress', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                lesson_id: lessonId,
                completed: completed
            })
        });
    } catch (error) {
        console.error('Error saving progress:', error);
    }
}

// Show next hint
function showNextHint() {
    const exercise = currentLesson.exercises[currentExerciseIndex];
    if (!exercise.hints || hintsShown >= exercise.hints.length) {
        return;
    }

    const hintsList = document.getElementById('hints-list');
    const hintDiv = document.createElement('div');
    hintDiv.className = 'hint-item';
    hintDiv.style.cssText = 'padding: 1rem; margin-top: 1rem; background: #f0f9ff; border-left: 4px solid #3b82f6; border-radius: 4px;';
    hintDiv.innerHTML = `<strong>Hint ${hintsShown + 1}:</strong> ${exercise.hints[hintsShown]}`;

    hintsList.appendChild(hintDiv);
    hintsShown++;

    // Hide button if no more hints
    if (hintsShown >= exercise.hints.length) {
        document.querySelector('.hint-btn').style.display = 'none';
    }
}
