class Account{
	constructor(firstName, lastName){
		this.firstname = firstName
		this.lastname = lastName
	}
}

var obj = new Account('sajib ','mahmud')

Accont.prototype.get_fullName = function(){
	return this.firstname + this.lastname
}

obj.get_fullName()
