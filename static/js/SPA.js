function togglePages(level, number) {
    // Hide all elements of the same level
    const elements = document.querySelectorAll(`.page-${level}`);
    elements.forEach(element => {
      element.style.display = "none";
      element.classList.remove('page-unhidden'); // Remove 'page-unhidden' class
    });

    // Show the selected element
    const element = document.getElementById(`page-${level}${number}`);
    if (element) {
      element.style.display = "block";
      element.classList.add('page-unhidden'); // Add 'page-unhidden' class
    }
  }


  document.addEventListener('DOMContentLoaded', () => {
      document.querySelectorAll('.page-xl, .page-lg, .page-sm, .page-xs, .page-ss').forEach(element => {
        element.style.display = 'none';
      });
    
      document.querySelectorAll('.page-unhidden').forEach(element => {
        element.style.display = 'block';
      });
    });
    