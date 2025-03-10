$(document).ready(function() {
    // Form validation
    $('#registerForm').on('submit', function(event) {
        event.preventDefault();
        event.stopPropagation();

        const password = $('#password').val();
        const confirmPassword = $('#confirmPassword').val();

        // Check if passwords match
        if (password !== confirmPassword) {
            $('#confirmPassword')[0].setCustomValidity('Passwords do not match');
        } else {
            $('#confirmPassword')[0].setCustomValidity('');
        }

        if (this.checkValidity()) {
            // Simulate registration - in a real app, this would make an API call
            localStorage.setItem('isLoggedIn', 'true');
            window.location.href = 'index.html';
        }

        $(this).addClass('was-validated');
    });

    // Clear custom validity when confirm password changes
    $('#confirmPassword').on('input', function() {
        this.setCustomValidity('');
    });
});