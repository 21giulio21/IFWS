const plugin_home = "https://www.instatrack.eu/wp-content/plugins/dashboard/";




jQuery(window).on('load', function(){

  functionRequireJS();

  jQuery('.account-list button').on('click', function(){
      switch (jQuery(this).attr('action'))
      {

      case "toggle-bot":
      var currentElement = jQuery(this);
      var address = plugin_home + "action-handler.php";
      var newValue = jQuery(currentElement).text().trim() == "Deactivate" ? 0 : 1;

      console.log(jQuery(currentElement).text().trim());
      console.log(newValue);

      var data = {
        action: jQuery(this).attr('action')
      }
        data.parameters = {
          username: jQuery(this).attr('instagram-account'),
          script_active: newValue
        }
        break

      case "toggle-comments":
      var currentElement = jQuery(this);
      var address = plugin_home + "action-handler.php";
      var newValue = jQuery(currentElement).text().trim() == "Deactivate" ? 0 : 1;

      console.log(jQuery(currentElement).text().trim());
      console.log(newValue);

      var data = {
        action: jQuery(this).attr('action')
      }
          data.parameters = {
          username: jQuery(this).attr('instagram-account'),
          commenta: newValue
        }
        break

      case "toggle-likes":
      var currentElement = jQuery(this);
      var address = plugin_home + "action-handler.php";
      var newValue = jQuery(currentElement).text().trim() == "Deactivate" ? 0 : 1;

      console.log(jQuery(currentElement).text().trim());
      console.log(newValue);

      var data = {
        action: jQuery(this).attr('action')
      }
        data.parameters = {
          username: jQuery(this).attr('instagram-account'),
          like: newValue
        }
      case "toggle-bot-pay":
        //Devo far aprire il menu dove posso pagare
        if(jQuery('#popup-pay').css('display') == "none"){

          loadButtonPaypal(0,0);


         jQuery('#popup-pay')
           .css("display", "flex")
           .hide()
           .fadeIn();
        } else {

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
    var quanti_mesi = parseInt(jQuery('#tempo').text())
    quanti_mesi = quanti_mesi + 1;

    jQuery('#tempo').html(quanti_mesi);
    ScrivoSulloSpanMonths();



    changeEuroToPay(quanti_mesi);

  });
  //Quando modifico la select del prezzo deve modificare il prezzo finale.
  jQuery('select').on('change', function() {
    var quanti_mesi = parseInt(jQuery('#tempo').text())
    changeEuroToPay(quanti_mesi);


  });


// per il bottone meno, fa descescere il quanti_mesi sul pupop
  jQuery('#minus-button').on('click', function(){

    var quanti_mesi = parseInt(jQuery('#tempo').text())
    if(quanti_mesi != 0)
    {
      quanti_mesi = quanti_mesi - 1;

      jQuery('#tempo').html(quanti_mesi);
      ScrivoSulloSpanMonths();

      changeEuroToPay(quanti_mesi);

    }
    changeEuroToPay("0");

  });

//Permette di modificare il pagamento.
function changeEuroToPay(quanti_mesi)
{
  jQuery('#paypal-button > div').remove()
  var prezzo = 0;
  //specifico quanto devo pagare. quanti_mesi (= mesi) * piano tariffario.
  var pianoScelto = parseInt(jQuery('#box-plane').val());
  if(pianoScelto == 1)
  {
    prezzo = quanti_mesi * 19.99;

  }else if(pianoScelto == 2)
  {
    prezzo = quanti_mesi * 35.99;

  }else{

    prezzo = quanti_mesi * 69.99;
  }
  console.log("piano scelto: " + pianoScelto);

  loadButtonPaypal(prezzo.toString(),quanti_mesi);

}



// funzione che permette di capire se scrivere months o month in base ai valori
  function ScrivoSulloSpanMonths()
  {
    var quanti_mesi = parseInt(jQuery('#tempo').text())
    if(quanti_mesi == 0) jQuery('#months').html(" Months");
    else if(quanti_mesi == 1) jQuery('#months').html(" Month");
    else jQuery('#months').html(" Months");
  }
  function updateTEMPO_FINE_ISCRIZIONEOnDatabase(quanti_mesi)
  {
    //Ottengo lo username specificato:
    var username_selected = jQuery("#box-username").val();

    // Ottengo il numero di seondi per cui vale l'abbonamento.
    var secondi_in_cui_vale_abbonamento = 2678400 * quanti_mesi

    //Calcolo i secondi per la fine dell'abbonamento
    var tempo_fine_abbonamento = Math.floor(new Date() / 1000) + secondi_in_cui_vale_abbonamento ;

    //Aggiorno il campo TEMPO_FINE_ISCRIZIONE nel database per lo username specificato
    var curl_request2 = {
      action: "RENEW-SUBSCRIPTION"
    }
    curl_request2.parameters = {
      USERNAME: username_selected,
      TEMPO_FINE_ISCRIZIONE: tempo_fine_abbonamento ,
    }

    var address = plugin_home + "action-handler.php"
    ajaxRequest(address, curl_request2)
      .done(function(msg){
        console.log("ajaxRequest done: " + msg);


      })
      .fail(function(xhr, status, error) {
        console.log("Error: status " + status + " message: " + error);
      });


  }

  function loadButtonPaypal( price,quanti_mesi)
  {

    updateTEMPO_FINE_ISCRIZIONEOnDatabase(quanti_mesi);
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
            total:  String(price),
            currency: 'EUR',
            details: {
              subtotal:  String(price),
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
                price: String(price),
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
            //se sono qui dentro allora devo

            // Show a confirmation message to the buyer
            window.alert('Thank you for your purchase!');
          });
      }
    }, '#paypal-button');

  }




   ///// Menu per pagare
   jQuery('#button-rinnova').on('click', function(){
     if(jQuery('#popup-pay').css('display') == "none"){

      loadButtonPaypal(0,0);


      jQuery('#popup-pay').css("display", "flex").hide().fadeIn();
   } else {

   }
   });



   ///Fine per pagare
     jQuery('#toggle-account-box').on('click', function(){
       console.log("Apro la view per inserire un utente");
       // per primo devo far si che il loader non funzioni.
       jQuery('#box-loader').css("display", "none");


    if(jQuery('#new-account-box').css('display') == "none"){

      jQuery('#new-account-box')
        .css("display", "flex")
        .hide()
        .fadeIn()

      if(jQuery(window).scrollTop() != 0) {
        jQuery('body').css('position', 'relative');
      }

      jQuery('html').addClass('prevent-scrolling');
      //jQuery('html').toggleClass('prevent-scrolling');
    } else {

    }
  });

  jQuery('#clouse-button').on('click', function(){
    jQuery('#popup-pay').hide('slow');
    jQuery('html').removeClass('prevent-scrolling');
    location.reload();
  });

  jQuery('#new-account-box i').on('click', function(){
    jQuery('#new-account-box').hide('slow');
    jQuery('html').removeClass('prevent-scrolling');
  });

  //Faccio in modo che il pulsante per agiungere un account funzioni
  jQuery('#new-account').on('click', function(){
    // faccio partire il loader
    jQuery('#box-loader').css('display',"")
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

        // Stop del loading
        jQuery('#box-loader').css("display", "none");
        if(msg.includes("reason"))
        {
          jQuery('#errore-paragrafo').html("Username already in use");
        }else {
          location.reload();
        }
      })
      .fail(function(xhr, status, error) {
        // Stop del loading
        jQuery('#box-loader').css("display", "none");
        console.log("Error: status " + status + " message: " + error);
      });

  });

} );

function functionRequireJS()
{
  var script = document.createElement('script');
  script.src = 'https://www.google.com/recaptcha/api.js';
  script.type = 'text/javascript';
  document.getElementsByTagName('head')[0].appendChild(script);

}


function handleToggle(currentElement) {
  const trifolo = jQuery(currentElement).text().replace(/^\s+|\s+$/g,'');
  if(trifolo == "Deactivate"){
    jQuery(currentElement).text("Activate");
    if(jQuery(currentElement).attr('action') == "toggle-bot")
      jQuery("i", jQuery(currentElement).parent().parent()).removeClass("fa-check").addClass("fa-times");
  } else if(trifolo == "Activate"){
    jQuery(currentElement).text("Deactivate");
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
