
var MODAL_FLAG = 0;

function create_modal(info, target){
    let modal_id = "modal_" + MODAL_FLAG.toString();
    MODAL_FLAG += 1;
    let this_modal_html = `
<div class="modal fade" id="`+modal_id+`" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog modal-full" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">`+info.name+`</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">×</span>
                </button>
            </div>
            <div class="modal-body p-4" style="word-wrap: break-word;">
                <div style="max-height: 300px;text-align: center;">
                    <img src="`+info.img+`"/>
                </div>
                <div class="row">
                    <div class="col-sm-6 col-lg-6"> Release Year:</div>
                    <div class="col-sm-6 col-lg-6"> `+info.year+` </div>
                </div>
                <div class="row">
                    <div class="col-sm-6 col-lg-6"> Genres:</div>
                    <div class="col-sm-6 col-lg-6"> `+info.genres+` </div>
                </div>
                <div class="row">
                    <div class="col-sm-6 col-lg-6"> Director:</div>
                    <div class="col-sm-6 col-lg-6"> `+info.director+` </div>
                </div>
                <div class="row">
                    <div class="col-sm-6 col-lg-6"> Actors/Actress:</div>
                    <div class="col-sm-6 col-lg-6"> `+info.actors+` </div>
                </div>
                <div class="row">
                    <div class="col-sm-6 col-lg-6"> Company:</div>
                    <div class="col-sm-6 col-lg-6"> `+info.company+` </div>
                </div>
                <hr/>
                <p>`+info.description+`</p>
            </div>
        </div>
    </div>
</div>
`;

    $('#'+target+"_modals").append(this_modal_html);
    return modal_id;
}

