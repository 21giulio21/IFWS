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


  // Codice che viener chiamato quando premo il pulsante piu o il pulsante meno
  jQuery('#plus-button').on('click', function(){
    var valore = parseInt(jQuery('#tempo').text())
    valore = valore + 1;

    jQuery('#tempo').html(valore);
    ScrivoSulloSpanMonths();
  });

// quando premo il pulsante conferma il mio ordine deve aprirsi la pagina per confermare l'ordine
  jQuery('#myBtn').on('click', function(){
    window.open('http://google.com');
  });

// per il bottone meno, fa descescere il valore sul pupop
  jQuery('#minus-button').on('click', function(){

    var valore = parseInt(jQuery('#tempo').text())
    if(valore != 0)
    {
      valore = valore - 1;

      jQuery('#tempo').html(valore);
      ScrivoSulloSpanMonths();

    }
  });

// funzione che permette di capire se scrivere months o month in base ai valori
  function ScrivoSulloSpanMonths()
  {
    var valore = parseInt(jQuery('#tempo').text())
    if(valore == 0) jQuery('#months').html(" Months");
    else if(valore == 1) jQuery('#months').html(" Month");
    else jQuery('#months').html(" Months");
  }




   ///// Menu per pagare
   jQuery('#button-rinnova').on('click', function(){
   if(jQuery('#popup-pay').css('display') == "none"){
    jQuery('#popup-pay')
      .css("display", "flex")
      .hide()
      .fadeIn();
   } else {

   }
   });



   ///Fine per pagare
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


function reguirePayment(price)
{
  price = "'".concat(price).concat("'");
  console.log(price);

paypal.Button.render({
  // Configure environment
  // Configure environment
  env: "production",
    client: {
      production: "AbuzFtw77DFKtZMPkCjduWWwd67dGIA3EBQ4VroO7IeAz__0THosuQo51Ta4wIQ8O4VVEnjRI2q2Ol7S"
    },
  client: {
    sandbox: "AdXdacvd6FSl1q3wJf8MHg8yqQv0smaHXIbDYh3f0e4Iy2ULhhup4lVf5ejs15qIk0nkMAbHNdCVlpNb",
    production: "AbuzFtw77DFKtZMPkCjduWWwd67dGIA3EBQ4VroO7IeAz__0THosuQo51Ta4wIQ8O4VVEnjRI2q2Ol7S"
  },
  // Customize button (optional)
  locale: 'en_US',
  style: {
    size: 'small',
    color: 'gold',
    shape: 'pill',
  },
  // Set up a payment
  payment: function (data, actions) {
  return actions.payment.create({
    transactions: [{
      amount: {
        total: '30.00',
        currency: 'EUR',
        details: {
          subtotal: '30.00',
          tax: '0.00',
          shipping: '0.00',
          handling_fee: '0.00',
          shipping_discount: '0.00',
          insurance: '0.00'
        }

      },
      description: 'The payment transaction description.',
      custom: '90048630024435',
      //invoice_number: '12345', Insert a unique invoice number
      payment_options: {
        allowed_payment_method: 'INSTANT_FUNDING_SOURCE'
      },
      soft_descriptor: 'ECHI5786786',
      item_list: {
        items: [
          {
            name: 'Instatrack Services ',
            description: '',
            quantity: '1',
            price: '30.00',
            tax: '0.00',
            sku: '1',
            currency: 'EUR'
          }
        ]
      }
    }],
    note_to_payer: 'Contact us for any questions on your order.'
  });
},
  // Execute the payment
  onAuthorize: function (data, actions) {
    return actions.payment.execute()
      .then(function () {
        // Show a confirmation message to the buyer
        window.alert('Thank you for your purchase!');
      });
  }
}, '#paypal-button');

}

function handleToggle(currentElement) {
  const trifolo = jQuery(currentElement).text().replace(/^\s+|\s+$/g,'');
  if(trifolo == "Disattiva"){
    jQuery(currentElement).text("Attiva");
    if(jQuery(currentElement).attr('action') == "toggle-bot")
      jQuery("i", jQuery(currentElement).parent().parent()).removeClass("fa-check").addClass("fa-times");
  } else if(trifolo == "Attiva"){
    jQuery(currentElement).text("Disattiva");
    if(jQuery(currentElement).attr('action') == "toggle-bot")
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
