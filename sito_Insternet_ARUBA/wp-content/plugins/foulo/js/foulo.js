const plugin_home = "https://www.instatrack.eu/wp-content/plugins/foulo/";

jQuery(window).on('load', function(){
  console.log('Mantovani caricato');

  jQuery('button').on('click', function(){

    var currentElement = jQuery(this);
    var address = plugin_home + "action-handler.php";
    var newValue = jQuery(currentElement).text().trim() == "Disattiva" ? 0 : 1;

    console.log(jQuery(currentElement).text().trim());
    console.log(newValue);

    var data = {
      action: jQuery(this).attr('action'),
      parameters: {
        username: jQuery(this).attr('instagram-account'),
        script_active: newValue
      }
    }

    ajaxRequest(address, data)
      .done(function(msg){
        console.log("ajaxRequest done: " + msg);
        handleToggle(currentElement);
      })
      .fail(function(xhr, status, error) {
        console.log("Error: status " + status + " message: " + error);
      });


  });

} );


function handleToggle(currentElement) {
  if(jQuery(currentElement).text() == "Disattiva"){
    jQuery(currentElement).text("Attiva");
    jQuery("i", jQuery(currentElement).parent().parent()).removeClass("fa-check").addClass("fa-times");
  } else {
    jQuery(currentElement).text("Disattiva");
    console.log(jQuery("i", jQuery(currentElement).parent().parent()));
    jQuery("i", jQuery(currentElement).parent().parent()).removeClass("fa-times").addClass("fa-check");
  }
}


function ajaxRequest(address, parameters){
  return jQuery.ajax({
    method: "POST",
    url: address,
    data: parameters
  })
}
