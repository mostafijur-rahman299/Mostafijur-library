$(function(){

   $("#form").submit(function(){
       var textArea = $('#messages')
       if (textArea.val().trim() == ""){
           textArea.css({
               'box-shadow': '0 0 4px #811'
           })
           
           event.preventDefault()
       }
   })
    
    
});