function openCard(cardId) {
  var card = document.getElementById(cardId);
  var overlay = document.querySelector('.card-overlay');
  card.style.display = 'block';
  overlay.style.display = 'block';
}

function closeCard() {
  var cards = document.querySelectorAll('.card1');
  var overlay = document.querySelector('.card-overlay');
  for (var i = 0; i < cards.length; i++) {
    cards[i].style.display = 'none';
  }
  overlay.style.display = 'none';
}


// 


  function showForm(formId) {
      // Hide all forms
      document.querySelectorAll('.form-js').forEach(form => {
          form.style.display = 'none';
      });
      // Show the selected form
      document.getElementById(formId).style.display = 'block';
  }
  function showUnhiddenForm(formId) {
      // Hide all forms
      document.querySelectorAll('.unhidden').forEach(form => {
          form.style.display = 'none';
      });
      // Show the selected form
      document.getElementById(formId).style.display = 'block';
  }



    







function openSlide(id) {
  var overlay = document.getElementById(id);
  var overlayclose = document.querySelector('.close-overlay');
  
  

  // Display the overlay with a slight delay for smoother appearance
  setTimeout(function () {
    overlay.style.transition = "transform 0.8s ease-in-out";
    overlay.style.display = "block";
    overlayclose.style.display = 'block';
    // Slide up animation with smooth transition
    overlay.style.transform = "translate(-50%, 0)";
  }, 300); // You can adjust the delay value as needed for the desired smoothness
}

function closeSlide() {
  var overlays = document.querySelectorAll('.slide-from-b');
  
  var overlayclose = document.querySelector('.close-overlay');
  
  
  overlays.forEach(function (overlay) {
    // Slide down animation with smooth transition
    overlay.style.transform = "translate(-50%, 80vh)";
  
    // Hide the overlay after animation
    setTimeout(function () {
      overlay.style.display = "none";
      overlay.style.transition = ""; // Reset transition property after hiding
    }, 800); // Adjust the delay to match the transition duration
  });
  overlayclose.style.display = 'none';
}




// shows the navbar by use of an icon
const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.querySelector('.mobile-menu');

    mobileMenuButton.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });

    // Close mobile menu when clicking outside of it
    document.addEventListener('click', (event) => {
        const isClickInsideMenu = mobileMenu.contains(event.target);
        const isClickOnButton = mobileMenuButton.contains(event.target);
        
        if (!isClickInsideMenu && !isClickOnButton) {
            mobileMenu.classList.add('hidden');
        }
    });


  // arange the items on the page in grid format
  

    const gridButton = document.getElementById('grid-btn');
    const listButton = document.getElementById('list-btn');
    const itemContainer = document.getElementById('item-container');

    gridButton.addEventListener('click', () => {
        itemContainer.classList.remove('flex');
        itemContainer.classList.add('grid');
        itemContainer.classList.remove('flex-col');
        itemContainer.classList.add('grid-cols-1', 'md:grid-cols-3');
    });

    listButton.addEventListener('click', () => {
        itemContainer.classList.remove('grid');
        itemContainer.classList.add('flex', 'flex-col');
        itemContainer.classList.remove('grid-cols-1', 'md:grid-cols-3');
    });