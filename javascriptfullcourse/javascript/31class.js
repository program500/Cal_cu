//scope in js

//1.block scope
//2.Function scope
//3.Global scope 

var fdname = "Hasip"; //Global scope 
console.log(fdname)


function v(){
    var name = "Nice";
    console.log(fdname); 
     
}

v();


// block scope 
{
    let tumi = "Tomar nam ki";
    console.log(tumi)
}
