// Sign up form validation
// Sign up form validation



// Login form validation
document.getElementById("login-form").addEventListener("submit", function(event) {
    var usernameEmail = document.getElementById("username-email").value;
    var password = document.getElementById("password").value;

    var usernameEmailError = document.getElementById("username-email-error");
    var passwordError = document.getElementById("password-error");
    var loginError = document.getElementById("login-error");

    usernameEmailError.textContent = "";
    passwordError.textContent = "";
    loginError.textContent = "";

    if (usernameEmail === "" || password === "") {
        event.preventDefault();
        if (usernameEmail === "") {
            usernameEmailError.textContent = "Please enter your username or email!";
        }
        if (password === "") {
            passwordError.textContent = "Please enter your password!";
        }
        return false;
    } else {
        // Display error message for invalid username/email or password
        loginError.textContent = "Invalid username/email or password!";
    }
});

// Function to validate the email address
function isEmailValid(email) {
    var pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(email);
}

  
// Password validation
document.getElementById("signup-form").addEventListener("submit", function(event) {
    var password = document.getElementById("password").value;
    var passwordError = document.getElementById("password-error");

    passwordError.textContent = "";

    if (!isPasswordValid(password)) {
        event.preventDefault();
        document.getElementById("password-error").innerHTML = "Password should contain at least 8 characters, one uppercase letter, one digit, and one special character!";
        return false;
    }
});

// Function to validate the password
function isPasswordValid(password) {
    var pattern = /^(?=.*\d)(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$/;
    return pattern.test(password);
}
