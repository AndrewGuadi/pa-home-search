document.addEventListener('DOMContentLoaded', function() {
    // Toggle the mobile navigation menu (applies to every page with .hamburger & .nav-menu)
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    // Only add event listener if these elements exist on the current page
    if (hamburger && navMenu) {
      hamburger.addEventListener('click', () => {
        navMenu.classList.toggle('active');
      });
    }
  });
  