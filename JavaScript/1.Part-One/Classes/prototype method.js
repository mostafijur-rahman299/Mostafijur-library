class Account{
	constructor(firstName, lastName){
		this.firstname = firstName
		this.lastname = lastName
	}
	get_fullName(){
		return this.firstname + this.lastname
	}
}

var obj = new Account('sajib ','mahmud')
obj.get_fullName()