<?php
session_start();
/*
Questa pagina prende come input: Email , USERNAME e PREZZO e fa la richiesta di pagamento
Nella variabile $_SESSION["MESI"] contiene una variabile contenente il numero di mesi per cui voglio pagare l'offerta



if( !isset($_SESSION["EMAIL"]) || !isset($_SESSION["USERNAME"]) || !isset($_SESSION["PREZZO"]|| !isset($_SESSION["MESI"])   )
{
  $return = '{ "success":"failed", "reason":"POST data not vali" }';
  echo $return;
  return;
}
*/
$prezzo = "302.00"; //$_SESSION["PREZZO"];
$mesi = 1;
echo '
<div id="paypal-button"></div>
<script src="https://www.paypalobjects.com/api/checkout.js"></script>

';

?>



<script>
paypal.Button.render({
  // Configure environment
  // Configure environment
  env: 'production',
    client: {
      production: 'AbuzFtw77DFKtZMPkCjduWWwd67dGIA3EBQ4VroO7IeAz__0THosuQo51Ta4wIQ8O4VVEnjRI2q2Ol7S' //Enter your live client ID here
    },
  client: {
    sandbox: 'AdXdacvd6FSl1q3wJf8MHg8yqQv0smaHXIbDYh3f0e4Iy2ULhhup4lVf5ejs15qIk0nkMAbHNdCVlpNb',
    production: 'AbuzFtw77DFKtZMPkCjduWWwd67dGIA3EBQ4VroO7IeAz__0THosuQo51Ta4wIQ8O4VVEnjRI2q2Ol7S'
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
        total: <?php echo "'{$prezzo}'"?>,
        currency: 'EUR',
        details: {
          subtotal: <?php echo "'{$prezzo}'"?>,
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
            price: <?php echo "'{$prezzo}'"?>,
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
</script>
