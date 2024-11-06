document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.login-form');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    // const submitButton = document.querySelector('.login-btn');

   
    function showError(input, message) {
        const formControl = input.parentElement;
        const errorElement = formControl.querySelector('.error-message') || document.createElement('div');
        errorElement.className = 'error-message';
        errorElement.style.color = 'red';
        errorElement.style.fontSize = '14px';
        errorElement.style.marginTop = '5px';
        errorElement.textContent = message;
        if (!formControl.querySelector('.error-message')) {
            formControl.appendChild(errorElement);
        }
        input.style.borderColor = 'red';
    }

    function showSuccess(input) {
        const formControl = input.parentElement;
        const errorElement = formControl.querySelector('.error-message');
        if (errorElement) {
            formControl.removeChild(errorElement);
        }
        input.style.borderColor = '#4CAF50';
    }

    function validatePassword(input) {
        if (input.value.trim() === '') {
            showError(input, 'Password is required');
            return false;
        }
        if (input.value.length < 6) {
            showError(input, 'Password must be at least 6 characters');
            return false;
        }
        showSuccess(input);
        return true;
    }

    function validateUsername(input) {
        const value = input.value.trim();
        if (value === '') {
            showError(input, 'Username is required');
            return false;
        }
        // Username pattern: 3-30 characters, can contain letters, numbers, dots and underscores
        const usernamePattern = /^[a-zA-Z0-9_\.]{3,30}$/;
        
        if (usernamePattern.test(value)) {
            showSuccess(input);
            return true;
        }
        
        showError(input, 'Username must be 3-30 characters and can contain letters, numbers, dots and underscores');
        return false;
    }

    // Real-time validation
    usernameInput.addEventListener('blur', function() {
        validateUsername(this);
    });

    passwordInput.addEventListener('blur', function() {
        validatePassword(this);
    });

    // Form submission
    form.addEventListener('submit', function(e) {
        e.preventDefault();

        let isValid = true;
        isValid = validateUsername(usernameInput) && isValid;
        isValid = validatePassword(passwordInput) && isValid;

        if (isValid) {
            form.submit(); 
        }
    });
});
