$(document).ready(function() {
    // Check if user is logged in
    function checkLoginStatus() {
        // This is a simple simulation - in a real app, you'd check server-side
        const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';

        if (isLoggedIn) {
            $('#loginBtn').addClass('d-none');
            $('#registerBtn').addClass('d-none');
            $('#logoutBtn').removeClass('d-none');
            $('.login-required-content').show();
            $('#loginRequired').addClass('d-none');
        } else {
            $('#loginBtn').removeClass('d-none');
            $('#registerBtn').removeClass('d-none');
            $('#logoutBtn').addClass('d-none');
            $('.login-required-content').hide();
            $('#loginRequired').removeClass('d-none');
        }
    }

    // Call on page load
    checkLoginStatus();

    // Handle logout
    $('#logoutBtn').click(function(e) {
        e.preventDefault();
        localStorage.setItem('isLoggedIn', 'false');
        checkLoginStatus();
    });

    // For demo purposes - simulate login
    $('#loginBtn').click(function(e) {
        // In a real app, this would redirect to login page
        // For demo, we'll just simulate login
        e.preventDefault();
        localStorage.setItem('isLoggedIn', 'true');
        checkLoginStatus();
    });

    // Video modal functionality
    $('.video-btn').click(function() {
        var videoSrc = $(this).data('src');
        $('#videoPlayer').attr('src', videoSrc);
        $('#videoModal').modal('show');
    });

    // When modal is closed, stop video
    $('#videoModal').on('hidden.bs.modal', function() {
        $('#videoPlayer').attr('src', '');
    });

    // Star rating functionality
    $('.rating-star').click(function() {
        const value = $(this).data('value');
        $('#rating').val(value);

        // Update stars display
        $('.rating-star').each(function(index) {
            if (index < value) {
                $(this).removeClass('far').addClass('fa');
            } else {
                $(this).removeClass('fa').addClass('far');
            }
        });
    });
});