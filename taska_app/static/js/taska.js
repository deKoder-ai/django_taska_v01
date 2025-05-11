document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM fully loaded and parsed");
  console.log("Taska.js loaded");

  document.querySelectorAll(".sb-btn").forEach((button) => {
    button.addEventListener("click", function () {
      const projectId = this.id.replace("project-", "");
      // Now you have the unique identifier (ID or slug) of the clicked project
      console.log("Project clicked:", projectId);
    });
  });
});
