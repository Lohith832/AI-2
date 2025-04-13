// static/js/about_us.js

document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".team-card");

    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.transition = "opacity 0.6s ease, transform 0.6s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, index * 200); // delay animation
    });
});