// Project cache to avoid repeated API calls
const projectCache = {};

document.addEventListener("DOMContentLoaded", function () {
  if (window.PROJECT_ID) {
    loadProject(window.PROJECT_ID);
    return;
  }

  // Then check URL path
  const path = window.location.pathname;
  const projectIdMatch = path.match(/\/projects\/(\d+)\/?/);

  if (projectIdMatch) {
    loadProject(projectIdMatch[1]);
  }

  // Add click handlers to all project buttons
  document.querySelectorAll(".sb-btn").forEach((button) => {
    button.addEventListener("click", function () {
      const projectId = this.id.split("-")[1];
      loadProject(projectId);
      history.pushState({}, "", `/projects/${projectId}/`);
    });
  });

  // Handle back/forward navigation
  window.addEventListener("popstate", function () {
    const path = window.location.pathname;
    const projectIdMatch = path.match(/\/projects\/(\d+)\/?/);
    if (projectIdMatch) {
      loadProject(projectIdMatch[1]);
    }
  });
});

async function loadProject(projectId) {
  try {
    showLoading(true);
    hideError();

    if (projectCache[projectId]) {
      updateUI(projectCache[projectId]);
      return;
    }

    const response = await fetch(`/api/projects/${projectId}/`);

    if (response.status === 403) {
      window.location.href = "/accounts/login/";
      return;
    }

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    projectCache[projectId] = data;
    updateUI(data);
  } catch (error) {
    showError(error.message);
  } finally {
    showLoading(false);
  }
}

function updateUI(projectData) {
  const titleElement = document.getElementById("project-title");
  const dueDateElement = document.getElementById("project-due-date");
  const taskList = document.getElementById("task-list");

  // Null check all elements
  if (!titleElement || !dueDateElement || !taskList) {
    console.error("Required elements not found in DOM");
    return;
  }

  titleElement.textContent = projectData.title || "Untitled Project";

  if (projectData.due_date) {
    dueDateElement.textContent = new Date(
      projectData.due_date
    ).toLocaleDateString();
  } else {
    dueDateElement.textContent = "No due date";
  }

  taskList.innerHTML = "";

  if (!projectData.tasks || projectData.tasks.length === 0) {
    taskList.innerHTML = '<li class="no-tasks">No tasks available</li>';
    return;
  }

  projectData.tasks.forEach((task) => {
    const li = document.createElement("li");
    li.textContent = task.title || "Untitled Task";
    taskList.appendChild(li);
  });
}

function showLoading(show) {
  document.getElementById("loading").style.display = show ? "flex" : "none";
}

function showError(message) {
  const errorDiv = document.getElementById("error-message");
  errorDiv.innerHTML = `
    ${message}
    <button class="dismiss-error" aria-label="Dismiss error">&times;</button>
  `;
  errorDiv.style.display = "block";

  // Add dismiss handler
  errorDiv.querySelector(".dismiss-error").addEventListener("click", hideError);
}

function hideError() {
  document.getElementById("error-message").style.display = "none";
}
