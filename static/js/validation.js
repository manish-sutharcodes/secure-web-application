document.addEventListener("DOMContentLoaded", function () {
    const passwordInput = document.getElementById("password");
    const errorBox = document.getElementById("password-error");

    passwordInput.addEventListener("input", function () {
        const value = passwordInput.value;

        if (value.length === 0) {
            errorBox.innerText = "Password cannot be empty";
        } 
        else if (value.length < 6) {
            errorBox.innerText = "Password must be at least 6 characters";
        } 
        else {
            errorBox.innerText = "";
        }
    });
});

function togglePassword() {
    const pwd = document.getElementById("password");

    if (pwd.type === "password") {
        pwd.type = "text";
    } else {
        pwd.type = "password";
    }
}

function toggleLoginPassword() {
    const pwd = document.getElementById("loginPassword");
    pwd.type = pwd.type === "password" ? "text" : "password";
}

function toggleRegisterPassword() {
    const pwd = document.getElementById("registerPassword");
    pwd.type = pwd.type === "password" ? "text" : "password";
}


document.addEventListener("DOMContentLoaded", () => {

    function setupToggle(passwordId, eyeId) {
        const pwd = document.getElementById(passwordId);
        const eye = document.getElementById(eyeId);

        if (!pwd || !eye) return;

        eye.addEventListener("click", () => {
            if (pwd.type === "password") {
                pwd.type = "text";
                eye.textContent = "👁";
            } else {
                pwd.type = "password";
                eye.textContent = "👁";
            }
        });
    }

    setupToggle("loginPassword", "loginEye");
    setupToggle("registerPassword", "registerEye");
});

