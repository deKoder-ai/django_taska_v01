// document.addEventListener("DOMContentLoaded", function () {
//   const sidebar = document.getElementById("sidebar");
//   const mainContainer = document.getElementById("content");

//   function updateLayout() {
//     if (window.innerWidth >= 1000) {
//       // Desktop view
//       sidebar.style.transform = "translateX(0)";
//       mainContainer.style.marginLeft = "200px";
//     } else {
//       // Mobile/tablet view
//       sidebar.style.transform = "translateX(-180px)";
//       mainContainer.style.marginLeft = "0";
//     }
//   }

//   // Initialize layout
//   updateLayout();

//   // Update on resize
//   window.addEventListener("resize", updateLayout);

//   // Handle hover for mobile view
//   sidebar.addEventListener("mouseenter", function () {
//     if (window.innerWidth < 1000) {
//       sidebar.style.transform = "translateX(0)";
//     }
//   });

//   sidebar.addEventListener("mouseleave", function () {
//     if (window.innerWidth < 1000) {
//       sidebar.style.transform = "translateX(-180px)";
//     }
//   });
// });
