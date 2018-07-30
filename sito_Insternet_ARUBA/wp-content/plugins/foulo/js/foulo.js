const plugin_home = "https://www.instatrack.eu/wp-content/plugins/foulo/";

jQuery(window).on('load', function(){

  jQuery('.account-list button').on('click', function(){

    var currentElement = jQuery(this);
    var address = plugin_home + "action-handler.php";
    var newValue = jQuery(currentElement).text().trim() == "Disattiva" ? 0 : 1;

    console.log(jQuery(currentElement).text().trim());
    console.log(newValue);

    var data = {
      action: jQuery(this).attr('action')
    }

    switch (jQuery(this).attr('action')) {

      case "toggle-bot":
      console.log("Update script attivo");
      console.log(newValue)
        data.parameters = {
          username: jQuery(this).attr('instagram-account'),
          script_active: newValue
        }
        break

      case "toggle-comments":
        data.parameters = {
          username: jQuery(this).attr('instagram-account'),
          commenta: newValue
        }
        break

      case "toggle-likes":
        data.parameters = {
          username: jQuery(this).attr('instagram-account'),
          like: newValue
        }
        break

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

  //Quando premo il pulsante rinnova apro un pupop con la descrizione fino a quando è attivo e la possibilità di rinnovo
  jQuery('#button-rinnova').on('click', function(){
    console.log("Press rinnova button");
    if(jQuery('#new-account-box').css('display') == "none"){
      jQuery('#new-account-box')
        .css("display", "flex")
        .hide()
        .fadeIn();
    } else {

    }
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

  //Faccio in modo che il pulsante per agiungere un account funzioni
  jQuery('#new-account').on('click', function(){
    var address = plugin_home + "action-handler.php";

    var curl_request2 = {
      action: "ADD_INSTAGRAM_ACCOUNT"
    }
    curl_request2.parameters = {
      USERNAME: jQuery('#popup-username').val(),
      PASSWORD_INSTAGRAM: jQuery('#popup-password').val(),
    }

    //Da qui faccio la richiesta con i valori appena costruiti
    ajaxRequest(address, curl_request2)
      .done(function(msg){
        console.log("ajaxRequest done: " + msg);
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
  } else if(jQuery(currentElement).text() == "Attiva"){
    jQuery(currentElement).text("Disattiva");
    console.log(jQuery("i", jQuery(currentElement).parent().parent()));
    jQuery("i", jQuery(currentElement).parent().parent()).removeClass("fa-times").addClass("fa-check");
  }
}


function ajaxRequest(address, parameters){
  console.log(address);
  console.log(parameters);
  return jQuery.ajax({
    method: "POST",
    url: address,
    data: parameters
  })
}
