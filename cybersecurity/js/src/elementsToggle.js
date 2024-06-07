document.getElementById("signup_pass").addEventListener("click", elementsToggle);
document.getElementById("signup_submit").addEventListener("click", elementsToggle);


function elementsToggle() {
    let signup = document.getElementById("signup");
    let warning = document.getElementById("warning");

    signup.classList.remove("visible");
    signup.classList.add("hidden");

    warning.classList.remove("hidden");
    warning.classList.add("visible");
}
