
function passwordConfirmation() {
    var password = document.getElementById("pass").value;
    var confirmPassword = document.getElementById("confirmpass").value;

    if (password == "") {
        alert("Error: The password field is Empty.");
    } else if (password == confirmPassword) {
        alert("Your Passwords match");
    } else {
        alert("Please make sure your passwords match.")
    }
}
// function passwordConfirmation2() {
//     var password = document.getElementById("pass").value;
//     var confirmPassword = document.getElementById("confirmpass").value;
//     if (password == confirmPassword) {
//         window.location.assign = "/frontend/templates//Services.html",true;
//         alert("Sign up successful");
//     }
// }
