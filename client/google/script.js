function onSignIn(googleUser) {
    let profile = googleUser.getBasicProfile();
    let userName = profile.getName();
    let userEmail = profile.getEmail();
    let userImage = profile.getImageUrl();

    document.getElementById("user-image").src = userImage;
    document.getElementById("user-name").textContent = "Name: " + userName;
    document.getElementById("user-email").textContent = "Email: " + userEmail;

    document.getElementById("user-info").style.display = "block";
}

function signInWithGoogle() {
    gapi.auth2.getAuthInstance().signIn().then(onSignIn);
}
