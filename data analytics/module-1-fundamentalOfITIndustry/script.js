// Mobile Menu Toggle
const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');

    burger.addEventListener('click', () => {
        // Toggle Navigation
        nav.classList.toggle('nav-active');

        // Burger Animation
        burger.classList.toggle('toggle');
    });
}

// Form Submission handling (Mock)
const handleForm = () => {
    const form = document.getElementById('contact-form');
    form.addEventListener('submit', (e) => {
        e.preventDefault(); // Prevents the page from reloading
        alert('Thank you! Your message has been sent.');
        form.reset(); // Clears the form fields
    });
}

// Initialize functions
navSlide();
handleForm();