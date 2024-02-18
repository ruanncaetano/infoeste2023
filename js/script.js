document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggleMenu");
    const sidebar = document.querySelector(".sidebar");
    const btn = document.querySelector(".btn");
    const menuLinks = document.querySelectorAll("#menuLink");

    toggleButton.addEventListener("click", function () {
        toggleSidebar();
    });

    menuLinks.forEach(function (link) {
        link.addEventListener("click", function () {
            toggleSidebar();
        });
    });

    function toggleSidebar() {
        sidebar.classList.toggle("aberta");
        btn.classList.toggle("expandir");
    }
});