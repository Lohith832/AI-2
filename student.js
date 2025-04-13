// static/js/student.js

document.addEventListener("DOMContentLoaded", function () {
    const examBtn = document.getElementById("startExamBtn");

    examBtn.addEventListener("click", function () {
        window.location.href = "/exam/"; // Adjust URL to match Django exam view
    });
});