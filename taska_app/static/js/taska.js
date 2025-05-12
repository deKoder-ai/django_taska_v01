document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM fully loaded and parsed");
  console.log("taska.js loaded");

  const sidebar = document.querySelector(".sidebar");
  // Set the scroll behavior to smooth
  sidebar.style.scrollBehavior = "smooth";

  // -好运-0☢0-----0☢0☠☠0☢0-----0☢0☠☠0☢0-----0☢0☠☠0☢0-----0☢0-好运-
  // __new project form

  newProject.addEventListener("click", function () {
    console.log("New project button clicked");

    // Show New Project Form
    // const template = document.getElementById('newProjectTemplate').cloneNode(true);
    const container = document.getElementById("newProjectContainer");
    container.style.display = "block";

    // Scroll back to top
    sidebar.scrollTop = 0;
  });

  // -好运-0☢0-----0☢0☠☠0☢0-----0☢0☠☠0☢0-----0☢0☠☠0☢0-----0☢0-好运-
  // __sidebar project buttons
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
