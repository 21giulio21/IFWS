const plugin_home = "https://www.instatrack.eu/wp-content/plugins/foulo/";

jQuery(window).on('load', function(){

  jQuery('.account-list button').on('click', function(){

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

  jQuery('#toggle-account-box').on('click', function(){
    if(jQuery('#new-account-box').css('display') == "none"){
      jQuery('#new-account-box')
        .css("display", "flex")
        .hide()
        .fadeIn();
    } else {

    }
  });

  jQuery('#new-account-box i').on('click', function(){
    jQuery('#new-account-box').hide('slow');
  });

} );


function handleToggle(currentElement) {
  if(jQuery(currentElement).text() == "Disattiva"){
    jQuery(currentElement).text("Attiva");
    jQuery("i", jQuery(currentElement).parent().parent()).removeClass("fa-check").addClass("fa-times");
  } else if(jQuery(currentElement).text() == "Attiva"){
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
