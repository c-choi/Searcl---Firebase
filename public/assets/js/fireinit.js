// Initialize Firebase
var config = {
        apiKey: "AIzaSyAkaWESNGQro0lAO9WX2o3rFoJHZ4toHhk",
        authDomain: "searcl-ce85f.firebaseapp.com",
        databaseURL: "https://searcl-ce85f.firebaseio.com",
        projectId: "searcl-ce85f",
        storageBucket: "searcl-ce85f.appspot.com",
        messagingSenderId: "792236016004"
};
firebase.initializeApp(config);
// Get a reference to the database service
var database = firebase.database();