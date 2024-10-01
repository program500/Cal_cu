// object in javascript 
var your_name = "Your name";
var village = "Your village";
var village = "Mother's name ";
var myinfo = {yourName: "Hasip", village: "Tutapara", phonenumber: 0123398348}
console.log(myinfo)
console.log(myinfo.phonenumber)
console.log(myinfo.yourName)
var ne = myinfo['village']
console.log(ne)


//object templete constractor paramitars
function Myfo(YourName, village, phonebo){
    this.YourName = YourName;
    this.village = village;
    this.phonebo = phonebo;
    this.sho = function(){
        console.log(this.YourName);
        console.log(this.village);
        console.log(this.phonebo);
    }

}
var newobj = new Myfo("Hasip", "Tutapara", 2048094)
console.log(newobj)

console.log(newobj)
newobj.sho();