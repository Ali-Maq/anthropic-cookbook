/**
 * Main App JavaScript - Homepage Functionality
 * Handles lesson loading, progress tracking, and navigation
 */

// Load lessons and populate the module cards
async function loadLessons() {
    try {
        const response = await fetch('/api/lessons');
        const lessons = await response.json();

        // Group lessons by module
        const module1Lessons = lessons.filter(l => l.module === 1);
        const module2Lessons = lessons.filter(l => l.module === 2);

        // Populate module 1
        const module1Container = document.getElementById('module-1-lessons');
        module1Lessons.forEach(lesson => {
            module1Container.appendChild(createLessonElement(lesson));
        });

        // Populate module 2
        const module2Container = document.getElementById('module-2-lessons');
        module2Lessons.forEach(lesson => {
            module2Container.appendChild(createLessonElement(lesson));
        });

        // Load and update progress
        await loadProgress();

    } catch (error) {
        console.error('Error loading lessons:', error);
    }
}

// Create a lesson list item element
function createLessonElement(lesson) {
    const div = document.createElement('div');
    div.className = 'lesson-item';
    div.onclick = () => goToLesson(lesson.id);

    div.innerHTML = `
        <div class="lesson-info">
            <h4>${lesson.title}</h4>
            <p class="lesson-meta">${lesson.duration} · ${lesson.exercises} exercises</p>
        </div>
        <div class="lesson-status" id="status-${lesson.id}">○</div>
    `;

    return div;
}

// Navigate to a lesson
function goToLesson(lessonId) {
    window.location.href = `/lesson/${lessonId}`;
}

// Load user progress from the server
async function loadProgress() {
    try {
        const response = await fetch('/api/progress');
        const progress = await response.json();

        // Update lesson status icons
        Object.keys(progress).forEach(lessonId => {
            if (progress[lessonId]) {
                const statusElement = document.getElementById(`status-${lessonId}`);
                if (statusElement) {
                    statusElement.textContent = '✓';
                    statusElement.parentElement.classList.add('completed');
                }
            }
        });

        // Calculate module progress
        updateModuleProgress(1, progress);
        updateModuleProgress(2, progress);

        // Update progress dashboard
        updateProgressDashboard(progress);

    } catch (error) {
        console.error('Error loading progress:', error);
    }
}

// Update module progress bar
function updateModuleProgress(moduleNum, progress) {
    const moduleLessons = Array.from(document.querySelectorAll(`#module-${moduleNum}-lessons .lesson-item`));
    const total = moduleLessons.length;

    if (total === 0) return;

    const completed = moduleLessons.filter(item => item.classList.contains('completed')).length;
    const percentage = (completed / total) * 100;

    const progressFill = document.getElementById(`progress-module-${moduleNum}`);
    const progressText = document.getElementById(`progress-text-${moduleNum}`);

    if (progressFill) {
        progressFill.style.width = `${percentage}%`;
    }

    if (progressText) {
        progressText.textContent = `${Math.round(percentage)}% Complete`;
    }
}

// Update progress dashboard
function updateProgressDashboard(progress) {
    const completedCount = Object.values(progress).filter(Boolean).length;

    const lessonsCompletedEl = document.getElementById('lessons-completed');
    const timeSpentEl = document.getElementById('time-spent');
    const exercisesPassedEl = document.getElementById('exercises-passed');

    if (lessonsCompletedEl) {
        lessonsCompletedEl.textContent = completedCount;
    }

    // Estimate time spent (rough calculation)
    const avgTimePerLesson = 0.75; // hours
    const timeSpent = (completedCount * avgTimePerLesson).toFixed(1);

    if (timeSpentEl) {
        timeSpentEl.textContent = `${timeSpent}h`;
    }

    // Estimate exercises passed (rough calculation)
    const avgExercisesPerLesson = 5;
    const exercisesPassed = completedCount * avgExercisesPerLesson;

    if (exercisesPassedEl) {
        exercisesPassedEl.textContent = exercisesPassed;
    }
}

// Save progress to server
async function saveProgress(lessonId, completed) {
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
