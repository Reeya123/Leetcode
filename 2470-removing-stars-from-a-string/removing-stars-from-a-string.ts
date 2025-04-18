function removeStars(s: string): string {
    /*
    Letting TypeScript Infer
    If youre initializing right away and TypeScript can see what youre putting in, you can skip the explicit type:

    let stack = ["a", "b"]; // Inferred as string[]
    But for empty arrays, always specify:

    let stack: string[] = []; // or TS will infer as any[]
    */

    let stack: string[] = [];
    for ( let char of s){
        if (stack.length > 0 && char === "*"){
            stack.pop()
            }
        else{
            stack.push(char);
            }}
    return stack.join("");
};