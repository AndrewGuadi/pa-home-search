document.addEventListener('DOMContentLoaded', function() {
    // Example "Get Started" button action for the homepage
    const ctaButton = document.querySelector('.cta-button');
    if (ctaButton) {
      ctaButton.addEventListener('click', () => {
        alert('Redirecting to our Property Search page...');
        // Uncomment to actually redirect:
        // window.location.href = '/property-search.html';
      });
    }
  });
  