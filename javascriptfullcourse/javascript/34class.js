//Inner function in jacascript 
function বাইরেরফাংশন(x) {
    function ইনারফাংশন(y) {
        return y + 1;
    }
    return ইনারফাংশন(x);
}

const ফলাফল = বাইরেরফাংশন(5);
console.log(ফলাফল);  // আউটপুট: 6


function main(x){
    function inop(y){

    }
    return y + 1 
    
}