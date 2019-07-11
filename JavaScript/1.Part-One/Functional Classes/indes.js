function Fruit(type){
	this.type = type;
	this.color = 'unKnown';
	this.getInformation = function(){
		return 'This ' + this.type + ' is ' + this.color
	}
}


let obj = Fruit('apple')

obj.type
obj.color
obj.getInformation();