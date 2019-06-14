function add (a) {
	return function (b) {
		return function (c){
			a + b + c
		}
	}
}

let addTwoNumsTo5 = add(5)
let addNumTo15 = addTwoNumsTo5(10)

console.log(addNumTo15(20))
