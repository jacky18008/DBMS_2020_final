

function show_slider_blocks(data, target){
  data.forEach(function(element){
    let this_modal_id = create_modal(element, target);
    let desc = element.description;
    if(desc.length > 150){
      desc = desc.substring(0,150) + '...';
    }
    $("#"+target).append(`
    <div class="col-xs-12 col-md-2 related-article">
      <div class="col-xs-12 no-padding">
        <div class="post-img">
          <a href="#"><img src="`+element.img+`" alt=""></a>
        </div>
        <div class="post-title">
          <a id="`+this_modal_id+`_activator" href="#`+this_modal_id+`" role="button" data-toggle="modal">`+element.name+`</a>
        </div>
        <div class="post-description">`+desc+`</div>
      </div>
    </div>
    `);
    if(HASH != 'null'){
      $("#"+this_modal_id+"_activator").click(function(e){
        $.post("clicked", {hash: HASH, id: element.id})
      });
    }
  });
}




        


