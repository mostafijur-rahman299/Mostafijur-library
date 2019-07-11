class Point{
	constructor(x, y){
		this.x = x;
		this.y = y;
	}
	static distance(a, b){
		const dx = a.x - b.x;
		const dy = a.y - b.y;
	}
}

const obj = new Point(5, 5)
const obj2 = new Point(10, 10)

// The correct way to call static method
Point.distance(obj, obj2)

// Attempt to call a static method on an instance of the class
try{
     console.log(obj.distance(obj1,obj2))
}catch(exception){
	console.log(exception.name + ': ' + exception.message)
}