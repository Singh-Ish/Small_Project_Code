const express = require("express")

const app = express()

app.get("/",function(req,res){

res.send("server is up and running fine ")

})





app.listen(3000,function(){
    console.log("Server is running on port 3000")
})