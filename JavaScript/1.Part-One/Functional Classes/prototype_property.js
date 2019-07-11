function Fruit(type){
	this.type = type;
	this.color = 'UnKnown';
}
Fruit.prototype.getInformation = function(){
	return 'This ' + this.type + ' is ' + this.color
}

let obj = Fruit('apple')
obj.getInformation()
