document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    // Perform login validation here
    document.getElementById('login-container').style.display = 'none';
    document.getElementById('main-container').style.display = 'block';
});
