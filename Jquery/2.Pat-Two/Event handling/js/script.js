$(function(){

    // **********click 
    // $('#btn-click').click(function(event) {
    //     console.log(event)
    //     alert("Button was clicked!")
    // });
    // $('.red-box').click(function(){
    //     $(this).css({
    //         'background-color': 'purple',
    //     });
    // });

    // ***********hover
    // $('#btn-hover').hover(function(){
    //     alert('Button was hoverd!')
    // });
    
    // var blueBox = $('.blue-box')
    // blueBox.hover(function(){
    //     $(this).stop().fadeTo(500, 0.7)
    // }, function(){
    //     $(this).stop().fadeTo(500, 1)
    // })

    // **************mouseenter and mouseleave
    // var greenBox = $('.green-box')
    // greenBox.mouseenter(function() {
    //     $(this).stop().fadeTo(500, 0.7)
    // });

    // greenBox.mouseleave(function() {
    //     $(this).stop().fadeTo(500, 1)
    // });

    // *************on("click", function(){...})
    // $('html').on('click keydown', function(){
    //     console.log('Mouse was clicked or key was pressed')
    // });
    // var images = [
    //     "images/laptop-mobile_small.jpg",
    //     "images/laptop-on-table_small.jpg",
    //     "images/people-office-group-team_small.jpg"
    // ]
    // i = 0
    // $('.gallery').find('img').on('click', function(){
    //     i = (i+1) % images.length
    //     $(this).fadeOut(function(){
    //         $(this).attr("src", images[i]).fadeIn();
    //     });
    // });

    // ***********delegated
    // $('p').click(function(){
    //     $(this).slideUp()
    // })
    // $('#content').append("<p>This paragraph is added dinamically.</p>")

    // $('#content').on('click', 'p', function(){
    //     $(this).slideUp();
    // })
    // $('#content').append("<p>This paragraph is added dinamically.</p>")

    // $('body').on('mouseenter', 'li', function(){
    //     $(this).css('color', '#B3B6B7')
    // })

    // **************passing aditional data
    // $('#btn-click').click({
    //     name : "Sajib Mahmud",
    //     domain : "depnox.com"
    // },function(event){
    //     greetUser(event.data)
    // })

    // function greetUser(userdata){
    //     username = userdata.name || "Anonymous"
    //     domain = userdata.domain || "example.com"

    //     alert("Welcome back " + username + " form " + domain)
    // }

    // **************image gallery
    // var galleryImageItems = $('.gallery').find('img')
    // galleryImageItems.css('width', '33%').css('opacity', '0.7')
    
    // galleryImageItems.mouseenter(function(){
    //     $(this).stop().fadeTo(500, 1)
    // });
    // galleryImageItems.mouseleave(function(){
    //     $(this).stop().fadeTo(500, 0.7)
    // })

    // ******************keydown and keyup
    // $('html').keydown(function(event){
    //     alert(event.which)
    // })
    $('html').keydown(function(event){
        if (event.which == 39){
            $('.blue-box').animate({
                'marginLeft': '+=20px'
            }, 50)
        }
    })

});