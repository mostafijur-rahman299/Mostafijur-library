let lime = {
    
	type : 'Mexican lime',
    
	color: 'green',
    
	getInformation: function(){
       
		 return this.type + this.color
	}

}

lime.getInformation()


***Using anonymous function***

let lime = new function() {
    this.type = 'Mexican lime';
    this.color = 'green';
    this.getInformation = function() {
        return 'This ' + this.type + ' is ' + this.color + '.';
    };
}