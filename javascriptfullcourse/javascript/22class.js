//slice type data in array
var fdname  = [ 'hasip',' saim', 'sazid', 'arman', 'salman'];
var s = fdname.slice(2,3)
console.log(s)
console.log(fdname.slice(2,3));
console.log(fdname.slice(0,5));

//splice method in arrays
fdname.splice(0,2, "HAsip sheikh");
console.log(fdname)