const express = require("express");
const bodyparser = require("body-parser"); // to grab the data from HTML
const request = require("requests");

const app = express();

const port = 3000;
app.listen(port, () => console.log(`the server is listening on port ${port}!`));

app.use(bodyparser.urlencoded({extended: true}));

app.use(express.static("public")); // refering to static files for the web


app.get("/" ,function(req, res){

  res.sendFile(__dirname + "/signup.html");




});

app.post("/", function(req,res){
  console.log("in post function");

  var firstName = req.body.fName;
  var lastName = req.body.lName;
  var email = req.body.email;

  console.log( firstName + " " + lastName + " " + email);

});

app.get("/success", function(req, res){

  res.sendFile(__dirname + "/success.html");
});


app.get("/failure", function(req, res){

  res.sendFile(__dirname + "/failure.html");
});
