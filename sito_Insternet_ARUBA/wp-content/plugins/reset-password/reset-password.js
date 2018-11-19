
jQuery(window).on('load', function(){

  // implemento il codice per il robot
  var script = document.createElement('script');
  script.src = 'https://www.google.com/recaptcha/api.js';
  script.type = 'text/javascript';
  document.getElementsByTagName('head')[0].appendChild(script);


} );
