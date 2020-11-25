const express = require("express");
const https = require("https");
const bodyParser = require("body-parser")

const app = express();

app.use(bodyParser.urlencoded({extended:true}));

app.get("/",function(req,res){

    res.sendFile(__dirname +"/index.html");

})

app.post("/",function(req,res){
    
    console.log(req.body.cityName)
    //console.log("Post request recieved");

    const city = req.body.cityName
    const apikey = "11afbb6bf90a9260003265292a3a86ec#"
    const unit = "metric"

    const url = "https://api.openweathermap.org/data/2.5/weather?q=" + city +"&units=" + unit + "&appid=" + apikey

    https.get(url, function(response){

        console.log(response.statusCode);

        response.on("data",function(data){
            const weatherData = JSON.parse(data)
            //console.log(weatherData);

            //getting the weather data 
            const temp = weatherData.main.temp
            const weatherDescription = weatherData.weather[0].description
            const icon = weatherData.weather[0].icon
            const iconImageUrl = "http://openweathermap.org/img/wn/"+ icon +"@2x.png"
            
            res.write("<p> the weather is currently "+ weatherDescription + "</p>")
            res.write("<h1>The temperature in " + city+ " is " + temp +" degree celcius. </h1>")
            res.write("<img src=" + iconImageUrl + ">")
            res.send()

        })
    })


})



//     res.send("server is up and running fine ")





app.listen(3000,function(){
    console.log("Server is running on port 3000")
})