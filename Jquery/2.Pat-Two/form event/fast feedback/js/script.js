$(function(){
    var form = $('#form')
    fastFeedbackFrom(form)

    form.submit(function(event){
       var name = $("#name").val();
       var password = $("#password").val();
       var message = $("#message").val();
       var isChecked = $("#checkbox").is(":checked");
    
       nameValidation(name, event)
       passwordValidation(password, event)
       messageValidation(message, event)
       checkValidation(isChecked, event)
   });
    

   function fastFeedbackFrom(formElement){
       var nameInput = formElement.find("#name")
       var passwordInput = formElement.find("#password")
       var messageInput = formElement.find("#message")
       var checkboxInput = formElement.find("#checkbox")

       nameInput.blur(function(event){
        var name = $(this).val()
        nameValidation(name, event)
        if(!isValidateName(name)){
            $(this).css({'box-shadow': '0 0 4px #811', 'border': '1px solid #666'})
        }else{
            $(this).css({'box-shadow': '0 0 4px #181', 'border': '1px solid #060'})
        }
       })

       passwordInput.blur(function(event){
        var password = $(this).val()
        passwordValidation(password, event)
        if(!isValidatePassword(password)){
            $(this).css({'box-shadow': '0 0 4px #811', 'border': '1px solid #666'})
        }else{
            $(this).css({'box-shadow': '0 0 4px #181', 'border': '1px solid #060'})
        }
       })

       messageInput.blur(function(event){
        var message = $(this).val()
        messageValidation(message, event)
        if(!isValidateMessage(message)){
            $(this).css({'box-shadow': '0 0 4px #811', 'border': '1px solid #666'})
        }else{
            $(this).css({'box-shadow': '0 0 4px #181', 'border': '1px solid #060'})
        }
       })

       checkboxInput.blur(function(event){
        var isChecked = $(this).is(":checked")
        checkValidation(isChecked, event)
        if(!isChecked){
            $(this).add("label[for='cb']").css({'box-shadow': '0 0 4px #811', 'border': '1px solid #666'})
        }else{
            $(this).add("label[for='cb']").css({'box-shadow': '0 0 4px #181', 'border': '1px solid #060'})
        }
       })
       
   }


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