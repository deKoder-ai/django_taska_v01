document.addEventListener("DOMContentLoaded", function () {
  const loadingElement = document.getElementById("loading");
  const errorElement = document.getElementById("error-message");

  // Hide loading spinner when page fully loads
  loadingElement.style.display = "none";

  // Handle any inline errors passed from backend
  if (window.initialError) {
    showError(window.initialError);
  }

  // Future-proofing for AJAX implementation
  function showError(message) {
    errorElement.textContent = message;
    errorElement.style.display = "block";
  }

  function hideError() {
    errorElement.style.display = "none";
  }

  // Export functions for potential future AJAX use
  window.projectLoader = {
    showError,
    hideError,
  };
});
