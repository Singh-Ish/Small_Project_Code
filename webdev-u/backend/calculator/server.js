const express = require('express');
const bodyparser = require("body-parser");

const app = express();
const port = 3000;

app.use(bodyparser.urlencoded({extended: true}))

//app.get('/', (req, res) => res.sendFile(__dirname + "./index.html") );
app.get("/", function(req, res){
  console.log(" running the root html");
  res.sendFile(__dirname + "/index.html") ;

});

app.post("/",function(req,res){
  console.log("entering the post function");
  console.log(req.body);

  var num1 = Number(req.body.num1);
  var num2 = Number(req.body.num2);

  var result = num1 + num2;
  res.send(" The result of the calculation is " + result);
});
/*
app.post("/", function(req,res){
  console.log("inside post function");
  console.log(req.body);
  res.send(" thank you fo posting that!");

});
*/

app.get("/contact", function(req, res){
  res.send("Contact me at: ishdeepsingh@sce.carleton.ca");
});


app.get("/about", function(req, res){
  res.send("about the web development");
});



app.listen(port, () => console.log(`Example app listening on port ${port}!`));
