/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function(s) {
    
    let stack = [];
    for ( let char of s){
        if (stack.length > 0 && char === "*"){
            stack.pop()
            }
        else{
            stack.push(char);
            }}
    return stack.join("");


};