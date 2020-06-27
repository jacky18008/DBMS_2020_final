$(document).on("keydown", "form", function(event) { 
    return event.key != "Enter";
});
$("#inputQuery").keydown(function(event) { 
    if(event.key == "Enter"){
        $("#btnQuery").click();
        console.log("search: "+$("#inputQuery").val());
    }
});
$("#btnQuery").click(function(){
    $.ajax({
        type:       'POST',
        data:       { query: $("#inputQuery").val() },
        url:        'http://localhost:8888/search',
        //crossDomain: true,
        success:    function(response){
                        var res = JSON.parse(response);
                        console.log(res);
                        $('#search_results').html("");
                        $('#search_results_modals').html("");
                        res = res.results;
                        show_slider_blocks(res, "search_results");
                    }
    });
})
