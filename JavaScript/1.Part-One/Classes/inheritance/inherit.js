class Math{
	constructor(x, y){
		this.x = x ;
		this.y = y;
	}
	add(){
		return this.x + this.y
	}
}
class Math2 extends Math{
	sub(){
		return this.x - this.y
	}
}
class Math3 extends Math2{
	mul(){
		return this.x - this.y
	}
	advance(a){
		return super/this.add() + a
	}
}

var obj = new Math3(10, 5)
obj.sub()

obj.add()

