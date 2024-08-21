document.addEventListener('DOMContentLoaded', function() {
    navbarIsOpen = false;
    const navbarToggle = document.querySelector('#navbar-toggle');
    const navbar = document.querySelector('#navbar');

    navbarToggle.addEventListener('click', function() {
        if (!navbarIsOpen) {
        navbar.setAttribute('class', 'w-full md:block md:w-auto')
        navbarIsOpen = true;
        } else {
            navbar.setAttribute('class', 'hidden w-full md:block md:w-auto')
            navbarIsOpen = false;
        }
    });
});
