// =========================================
// PHO 101 - INTERACTIVE FUNCTIONALITY
// =========================================

// GALLERY FUNCTIONALITY
let currentSlideIndex = 0;
const slides = document.querySelectorAll('.gallery-slide');
const totalSlides = slides.length;

function changeSlide(direction) {
  currentSlideIndex += direction;
  
  if (currentSlideIndex >= totalSlides) {
    currentSlideIndex = 0;
  } else if (currentSlideIndex < 0) {
    currentSlideIndex = totalSlides - 1;
  }
  
  updateGallery();
}

function currentSlide(index) {
  currentSlideIndex = index;
  updateGallery();
}

function updateGallery() {
  // Update slide position
  const gallerySlides = document.getElementById('gallerySlides');
  if (gallerySlides) {
    gallerySlides.style.transform = `translateX(-${currentSlideIndex * 100}%)`;
  }
  
  // Update dots
  const dots = document.querySelectorAll('.gallery-dot');
  dots.forEach((dot, index) => {
    dot.classList.remove('active');
    if (index === currentSlideIndex) {
      dot.classList.add('active');
    }
  });
}

// AUTO-ADVANCE GALLERY EVERY 6 SECONDS
function autoAdvanceGallery() {
  const galleryContainer = document.querySelector('.gallery-container');
  if (galleryContainer) {
    setInterval(() => {
      changeSlide(1);
    }, 6000);
  }
}

// NAVIGATION ACTIVE STATE
function updateNavigation() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}

// SMOOTH SCROLL FOR ANCHOR LINKS
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth'
      });
    }
  });
});

// PAGE TRANSITIONS
window.addEventListener('load', () => {
  autoAdvanceGallery();
  updateNavigation();
  
  // Fade in animation on page load
  const pages = document.querySelectorAll('.page');
  pages.forEach(page => {
    if (page.classList.contains('active')) {
      page.style.animation = 'fadeIn 0.6s ease-in';
    }
  });
});

// KEYBOARD NAVIGATION FOR GALLERY
document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowLeft') changeSlide(-1);
  if (e.key === 'ArrowRight') changeSlide(1);
});

// TOUCH SUPPORT FOR MOBILE GALLERY
let touchStartX = 0;
let touchEndX = 0;

function handleGestureSwipe() {
  if (touchEndX < touchStartX - 50) {
    changeSlide(1); // Swipe left, go to next slide
  }
  if (touchEndX > touchStartX + 50) {
    changeSlide(-1); // Swipe right, go to previous slide
  }
}

const galleryContainer = document.querySelector('.gallery-container');
if (galleryContainer) {
  galleryContainer.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, false);

  galleryContainer.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleGestureSwipe();
  }, false);
}

// BUTTON HOVER SOUND (Optional - uncomment if you want click feedback)
// const buttons = document.querySelectorAll('.btn, .gallery-arrow, .social-icon');
// buttons.forEach(btn => {
//   btn.addEventListener('mouseover', () => {
//     // Optional: Add sound or haptic feedback here
//   });
// });

// SCROLL ANIMATION TRIGGER
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.animation = 'fadeIn 0.6s ease-in forwards';
    }
  });
}, observerOptions);

// Observe menu items and sections
document.querySelectorAll('.menu-item, .about-image-box').forEach(el => {
  observer.observe(el);
});

console.log('Pho 101 Website - Interactive Features Loaded Successfully');
