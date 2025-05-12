document.addEventListener("DOMContentLoaded", function () {
  // Set default due date (one week from today)
  const dueDateInput = document.getElementById("due_date");
  if (dueDateInput && !dueDateInput.value) {
    const today = new Date();
    const nextWeek = new Date(today.getTime() + 7 * 24 * 60 * 60 * 1000);
    const formattedDate = nextWeek.toISOString().split("T")[0];
    dueDateInput.value = formattedDate;
  }
});
