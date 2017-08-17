/* google auth when btn pushed */
$("#BTN_GOOGLE_LOGIN").click(function(){
    /* replace google auth with provider variable */
    var provider = new firebase.auth.GoogleAuthProvider();

    /* process login with provider auth */
    firebase.auth().signInWithPopup(provider).then(function(result) {
        // code to process when successful login
        $('#AUTH_STATE').text(result.user.displayName + "님 로그인 하셨습니다.");
        }).catch(function(error) {
            // code to process when login fail
            alert(error.message)
            });
    });
/* facebook auth when btn pushed */
$("#BTN_FACEBOOK_LOGIN").click(function(){
    /* replace google auth with provider variable */
    var provider = new firebase.auth.FacebookAuthProvider();

    firebase.auth().signInWithPopup(provider).then(function(result) {
      // This gives you a Facebook Access Token. You can use it to access the Facebook API.
      var token = result.credential.accessToken;
      // The signed-in user info.
      var user = result.user;
      // ...
    }).catch(function(error) {
      // Handle Errors here.
      var errorCode = error.code;
      var errorMessage = error.message;
      // The email of the user's account used.
      var email = error.email;
      // The firebase.auth.AuthCredential type that was used.
      var credential = error.credential;
      // ...
    });
    });

/* detect changes in auth state */
firebase.auth().onAuthStateChanged(function(user) {
    if (user) {
        $('#AUTH_STATE').hide();
        $('#BTN_FACEBOOK_LOGIN').hide();
        $('#BTN_GOOGLE_LOGIN').hide();
        $('#BTN_LOGOUT').show();
        // show user info
        $('#USER_NAME').text(user.displayName);
        $('#USER_MAIL').text(user.email);
        $('#USER_UID').text(user.uid);
        $('#USER_PHOTO').attr('src', user.photoURL);
        $('#USER_INFO').show();
    } else {
        $('#AUTH_STATE').show();
        $('#AUTH_STATE').text("로그인");
        $('#BTN_FACEBOOK_LOGIN').show();
        $('#BTN_GOOGLE_LOGIN').show();
        $('#BTN_LOGOUT').hide();
        // Hide user info
        $('#USER_INFO').hide();
    }
});

/* cancel auth when logout btn pushed */
$('#BTN_LOGOUT').click(function() {
    firebase.auth().signOut().then(function() {
        alert("로그아웃 되었습니다.");
    }, function(error) {
        alert(error.message);
    })
});