// Initialize AOS (Animate on Scroll)
document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS animation library
    AOS.init({
        duration: 1000,
        once: true,
        easing: 'ease',
        offset: 100
    });

    // Preloader
    const preloader = document.querySelector('.preloader');
    window.addEventListener('load', function() {
        preloader.classList.add('hidden');
    });

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.style.padding = '10px 0';
            navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.padding = '15px 0';
            navbar.style.boxShadow = 'none';
        }
    });

    // Smooth scrolling for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70,
                    behavior: 'smooth'
                });
                
                // Update active nav link
                document.querySelectorAll('.nav-link').forEach(navLink => {
                    navLink.classList.remove('active');
                });
                this.classList.add('active');
            }
        });
    });

    // Active nav link on scroll
    const sections = document.querySelectorAll('section');
    window.addEventListener('scroll', function() {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            
            if (pageYOffset >= (sectionTop - 100)) {
                current = section.getAttribute('id');
            }
        });
        
        document.querySelectorAll('.nav-link').forEach(navLink => {
            navLink.classList.remove('active');
            if (navLink.getAttribute('href') === `#${current}`) {
                navLink.classList.add('active');
            }
        });
    });

    // Back to top button
    const backToTopButton = document.querySelector('.back-to-top');
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopButton.classList.add('show');
        } else {
            backToTopButton.classList.remove('show');
        }
    });
    
    backToTopButton.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Add preloader to the DOM
    if (!document.querySelector('.preloader')) {
        const preloaderDiv = document.createElement('div');
        preloaderDiv.className = 'preloader';
        preloaderDiv.innerHTML = '<div class="loader"></div>';
        document.body.appendChild(preloaderDiv);
    }

    // Add back to top button to the DOM
    if (!document.querySelector('.back-to-top')) {
        const backToTopDiv = document.createElement('div');
        backToTopDiv.className = 'back-to-top';
        backToTopDiv.innerHTML = '<i class="fas fa-arrow-up"></i>';
        document.body.appendChild(backToTopDiv);
    }

    // Typing effect for hero subtitle
    const heroSubtitle = document.querySelector('.hero-subtitle');
    if (heroSubtitle) {
        const text = heroSubtitle.textContent;
        heroSubtitle.innerHTML = '';
        heroSubtitle.classList.add('typed-text');
        
        let charIndex = 0;
        function typeWriter() {
            if (charIndex < text.length) {
                heroSubtitle.innerHTML += text.charAt(charIndex);
                charIndex++;
                setTimeout(typeWriter, 100);
            } else {
                heroSubtitle.classList.remove('typed-text');
            }
        }
        
        setTimeout(typeWriter, 500);
    }

    // Add animation delay to project cards for staggered effect
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach((card, index) => {
        card.setAttribute('data-aos-delay', 100 * (index % 3));
    });

    // Form validation
    const contactForm = document.querySelector('.contact-form form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            let isValid = true;
            const nameInput = contactForm.querySelector('input[name="name"]');
            const emailInput = contactForm.querySelector('input[name="email"]');
            const subjectInput = contactForm.querySelector('input[name="subject"]');
            const messageInput = contactForm.querySelector('textarea[name="message"]');
            
            // Simple validation
            if (nameInput && !nameInput.value.trim()) {
                nameInput.classList.add('is-invalid');
                isValid = false;
            } else if (nameInput) {
                nameInput.classList.remove('is-invalid');
            }
            
            if (emailInput && (!emailInput.value.trim() || !validateEmail(emailInput.value))) {
                emailInput.classList.add('is-invalid');
                isValid = false;
            } else if (emailInput) {
                emailInput.classList.remove('is-invalid');
            }
            
            if (subjectInput && !subjectInput.value.trim()) {
                subjectInput.classList.add('is-invalid');
                isValid = false;
            } else if (subjectInput) {
                subjectInput.classList.remove('is-invalid');
            }
            
            if (messageInput && !messageInput.value.trim()) {
                messageInput.classList.add('is-invalid');
                isValid = false;
            } else if (messageInput) {
                messageInput.classList.remove('is-invalid');
            }
            
            if (!isValid) {
                event.preventDefault();
            }
        });
    }
    
    // Email validation function
    function validateEmail(email) {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }
});