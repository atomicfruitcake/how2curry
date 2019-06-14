function add (a, b) {
	return a + b
}

function multiply (a, b) {
	return a * b
}

let double = multiply(2)
let add7 = add(7)

let doubleThenAdd7 = add7(multiply())

function doubleThenAdd7 (a) {
	return add7(multiply(a))
}

console.log(doubleThenAdd7(4)) // logs 15

function add7ThenDouble (a) {
	return multiply(add7(a))
}

console.log(add7ThenDouble(5)) // logs 22
