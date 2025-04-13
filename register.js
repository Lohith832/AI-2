// static/js/register.js

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const password1 = document.getElementById("password1");
    const password2 = document.getElementById("password2");
    const errorMsg = document.getElementById("errorMsg");

    form.addEventListener("submit", function (e) {
        if (password1.value !== password2.value) {
            e.preventDefault();
            errorMsg.textContent = "Passwords do not match.";
        } else {
            errorMsg.textContent = "";
        }
    });
});