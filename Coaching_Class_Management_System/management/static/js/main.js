// main.js

// Toggle password visibility on both Login and Register pages
function togglePassword() {
    const inputs = document.querySelectorAll('input[type="password"]');
    inputs.forEach(input => {
        input.type = input.type === "password" ? "text" : "password";
    });
}
