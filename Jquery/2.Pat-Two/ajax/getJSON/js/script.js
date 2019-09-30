
$(function(){
    // $.getJson()
    var filckrApi = "https://www.flickr.com/services/feeds/photos_public.gne?jsoncallback=?"
    $.getJSON(filckrApi, {
        tags: "islam",
        tagmode: "any",
        format: "json"
    }).done(function(data){
        // success
        console.log(data)
        $.each(data.items, function(index, item){
            console.log(item.media.m)
        })
    }).fail(function(){
        alert("Ajax call fail.")
    })
})

