function searchMatrix(matrix: number[][], target: number): boolean {
    const rows:number =  matrix.length;
    const cols: number = matrix[0].length;
    
    let left: number  = 0;
    let right: number = rows* cols - 1;
    
    while (left <= right){
        let midindex: number = Math.floor((left + right) / 2);
        let row: number = Math.floor(midindex / cols);
        let col: number = Math.floor(midindex % cols);
        
        const midvalue:number = matrix[row][col];
        
        if (midvalue === target){
            return true;
        }
        
        if (midvalue < target){
            left = midindex + 1;
        }
        
        else{
            right = midindex - 1;
        }
    
        
    }
    return false;   
};