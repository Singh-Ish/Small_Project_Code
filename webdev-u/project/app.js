
const express = require("express");
const bodyparser = require("body-parser"); // to grab the data from HTML
const request = require("requests");

const app = express();

const port = 3000;

app.listen(port, () => console.log(`the server is listening on port ${port}!`));

app.use(bodyparser.urlencoded({extended: true}));
app.use(express.static("public")); // refering to static files for the web


app.get("/" ,function(req, res){

  console.log("hello from the main response ");
//  res.send("hello");

var today = new Date();

if(today.getDay() === 6 || today.getDay() === 0){
  res.write("<h1> yay it's the weekend</h1>");
}
else {
  res.sendFile(__dirname + "/index.html");
}

res.send();
});
