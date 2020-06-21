const express = require("express"); // importing express package 
const app = express(); // creating the express variable 

const bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({extended:true}))

app.listen(3000,function(){
    console.log("server started on port 3000");
}); // listening to any http request running on a port on your local machine 

// adding a call back function to the port


// addressing the GET request on the main page 
app.get("/", function(request,response){

    
    response.sendFile( __dirname + "/templates/index.html")
});

// addressing the post method on the main page 
app.post("/",function(req,res){

    var  email  = req.body.uemail;
    var password = req.body.password;

   
    res.send(" Thank you for submiting th details."+ "\n \n"+" The Name is " + email + "\n \n The Password is " + password )

    
    //res.send("Thank you ")
});

// other pages routes 
app.get("/contact",function(request,response){
    response.send(" hello from contact page ")
});