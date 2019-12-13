

const express = require("express");
const bodyparser = require("body-parser");
const request = require("request");


const app = express();

const port = 3000;
app.listen(port, () => console.log(`the server is listening on port ${port}!`));


app.use(bodyparser.urlencoded({extended: true}))

app.get("/", function(req, res){
  res.sendFile(__dirname + "/index.html");

});


app.post("/", function(req, res){
//  console.log(req.body.Crypto);
  //res.send("inside the post function");

  var crypto = req.body.crypto;
  var fiat = req.body.fiat;

  var baseUrl = "https://apiv2.bitcoinaverage.com/indices/global/ticker/";

  var finalUrl = baseUrl + crypto + fiat;

  request(finalUrl, function (error, response, body) {
  //console.log('error:', error); // Print the error if one occurred
  //console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
  //console.log('body:', body); // Print the HTML for the Google homepage.

  var data = JSON.parse(body);
  var price = data.last;
  var currentDate = data.display_timestamp;

  res.write("<p> The current date is " + currentDate +"</p>");

  res.write("<h1> The current price of "+ crypto +" is " + price + " " + fiat+ "</h1>");

  res.send();

});


});
