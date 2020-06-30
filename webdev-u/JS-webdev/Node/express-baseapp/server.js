const express = require("express"); // importing express package 
const app = express(); // creating the express variable 

const bodyPaeser = require("body-parser");

app.listen(3000,function(){
    console.log("server started on port 3000");
}); // listening to any http request running on a port on your local machine 

// adding a call back function to the port


// addressing the GET request on the main page 
app.get("/", function(request,response){

    
    response.sendFile( __dirname + "/templates/index.html")
});



// other pages routes 
app.get("/contact",function(request,response){
    response.send(" hello from contact page ")
});