document.addEventListener("DOMContentLoaded", () => {
  const sidebar = document.querySelector(".sidebar");
  const sidebarHoverArea = document.querySelector(".sidebar-hover-area");
  const sidebarOverlay = document.querySelector(".sidebar-overlay");
  const sidebarClose = document.querySelector(".sidebar-close");
  const sidebarToggle = document.querySelector(".sidebar-toggle");
  const mobileBreakpoint = 650;

  function checkMobile() {
    return window.innerWidth <= mobileBreakpoint;
  }

  // Toggle sidebar on hover (mobile only)
  sidebarHoverArea.addEventListener("mouseenter", () => {
    if (checkMobile()) {
      openSidebar();
    }
  });

  // Toggle sidebar with button
  sidebarToggle.addEventListener("click", toggleSidebar);

  // Close sidebar with close button
  sidebarClose.addEventListener("click", closeSidebar);

  // Close sidebar when clicking outside
  sidebarOverlay.addEventListener("click", closeSidebar);

  function toggleSidebar() {
    if (sidebar.classList.contains("active")) {
      closeSidebar();
    } else {
      openSidebar();
    }
  }

  function openSidebar() {
    if (!checkMobile()) return;
    sidebar.classList.add("active");
    sidebarOverlay.classList.add("active");
  }

  function closeSidebar() {
    sidebar.classList.remove("active");
    sidebarOverlay.classList.remove("active");
  }

  // Handle window resize
  window.addEventListener("resize", () => {
    if (!checkMobile()) {
      closeSidebar();
    }
  });
});
