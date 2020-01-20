//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const mongoose = require("mongoose");

const app=express();

app.use(express.static("public"));
app.set('view engine','ejs');
app.use(bodyParser.urlencoded({
  extended:true

}));


mongoose.connect("mongodb://localhost:27017/userDB",{useNewUrlParser:true});

const userSchema = {
  email: String,
  password: String
};

const User = new mongoose.model("User",userSchema);

app.get("/", function(req, res){
  res.render("home");

});

app.get("/login", function(req, res){
  res.render("login");

});

app.get("/register", function(req, res){
  res.render("register");

});


app.post("/register",function(req,res){
  const newUser = new User({
    email: req.body.username,
    password:req.body.password
  });

  newUser.save(function(err){
    if (err) {
      console.log(err);
    }
    else {
      res.render("secrets");
    }
  });
});


app.listen(2000, function(){
  console.log("server started at port 2000");
});
