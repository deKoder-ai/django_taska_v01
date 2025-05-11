document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM fully loaded and parsed");
  console.log("taska.js loaded");

  const sidebar = document.querySelector(".sidebar");
  // Set the scroll behavior to smooth
  sidebar.style.scrollBehavior = "smooth";

  const newProject = document.getElementById("newProject");
  newProject.addEventListener("click", function () {
    console.log("New project button clicked");

    // Scroll back to top
    sidebar.scrollTop = 0;
  });

  document.querySelectorAll(".sb-btn").forEach((button) => {
    button.addEventListener("click", function () {
      const projectId = this.id.replace("project-", "");
      // Now you have the unique identifier (ID or slug) of the clicked project
      console.log("Project clicked:", projectId);

      // Scroll back to top
      sidebar.scrollTop = 0;
    });
  });
});
