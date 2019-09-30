$(function(){

   $("#form").submit(function(event){
       var name = $("#name").val();
       var password = $("#password").val();
       var message = $("#message").val();
       var isChecked = $("#checkbox").is(":checked");
    
       nameValidation(name, event)
       passwordValidation(password, event)
       messageValidation(message, event)
       checkValidation(isChecked, event)
   });
    
   // name validation 
   
    function nameValidation(name, event){
        if(!isValidateName(name)){
            $("#name-feedback").text("Please enter at least five character.")
            event.preventDefault()
        }else{
         $("#name-feedback").text("")
        }
    }
   

   
   function isValidateName(name){
       return name.length >= 5
   }

   // password validation 
   function passwordValidation(password, event){
        if(!isValidatePassword(password)){
            $("#password-feedback").text("The password at least 6 charecter and contains a number.")
            event.preventDefault()
        }else{
        $("#password-feedback").text("")
        }
    }


    function isValidatePassword(password){
        return password.length >= 6 && /.*[0-9].*/.test(password)
    }

    // message validation 
    function messageValidation(message, event){
        if(!isValidateMessage(message)){
            $("#message-feedback").text("Please enter a message")
            event.preventDefault()
        }else{
         $("#message-feedback").text("")
        }
    }
 
 
    function isValidateMessage(message){
        return message.trim() != ""
    }

    // checkbox validation 
    function checkValidation(isChecked, event){
        if(!isChecked){
            $("#checkbox-feedback").text("Please agree with this.")
            event.preventDefault()
        }else{
         $("#checkbox-feedback").text("")
        }
    }
    
});