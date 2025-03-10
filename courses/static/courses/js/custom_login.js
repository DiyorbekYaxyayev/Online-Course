$(document).ready(function() {
    // Form validation
    $('#loginForm').on('submit', function(event) {
        event.preventDefault();
        event.stopPropagation();

        if (this.checkValidity()) {
            // Simulate login - in a real app, this would make an API call
            localStorage.setItem('isLoggedIn', 'true');
            window.location.href = 'index.html';
        }

        $(this).addClass('was-validated');
    });
});