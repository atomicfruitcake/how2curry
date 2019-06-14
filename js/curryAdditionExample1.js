function add (a) {
    return function (b) {
        return a + b;
    }
}

let add5 = add(5)

console.log(add5(3)) // prints out 8
