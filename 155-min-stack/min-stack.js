
class MinStack {
    constructor() {
        this.stack = [];     // Main stack
        this.minStack = [];  // Stack to track minimum values
    }

    push(val) {
        this.stack.push(val);
        if (this.minStack.length === 0 || val <= this.minStack[this.minStack.length - 1]) {
            this.minStack.push(val);
        }
    }

    pop() {
        if (this.stack.length > 0) {
            const popped = this.stack.pop();
            if (popped === this.minStack[this.minStack.length - 1]) {
                this.minStack.pop();
            }
        }
    }

    top() {
        if (this.stack.length > 0) {
            return this.stack[this.stack.length - 1];
        }
        return null;
    }

    getMin() {
        if (this.minStack.length > 0) {
            return this.minStack[this.minStack.length - 1];
        }
        return null;
    }
}


/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */