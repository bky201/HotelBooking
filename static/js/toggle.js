document.addEventListener("DOMContentLoaded", function() {
    var toggleButtons = document.querySelectorAll(".toggleButton");
    toggleButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var content = button.closest(".content");
            content.querySelector(".truncated").classList.toggle("hidden");
            content.querySelector(".full").classList.toggle("hidden");
        });
    });
});