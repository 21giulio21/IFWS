(function($) {

	$( '#lostpasswordform' ).submit( function( event ) {

		var text = $( '#somfrp_user_info' ).val();

		if ( ! text ) {
			//TODO: CONTROLLARE CHE LA MAIL È NEL DATABASE
			sompassFieldInvalid( $( '#lostpasswordform #somfrp_user_info' ) )
			event.preventDefault();
			return false;
		}

	});


	$( '#resetpasswordform' ).submit( function( event ) {

		var new_pass = $( '#som_new_user_pass' ).val();
		var new_pass2 = $( '#som_new_user_pass_again' ).val();

		if ( new_pass && new_pass2 ) {
			sompass_posting_reset();
		}

	});

	function sompassFieldInvalid( element ) {
		//TODO: QUI DEVO CONTROLLARE SE LA MAIL é PRESENTE NEL MIO DATABASE, SE È PRESENTE ALLORA DEVO MANDARE LA MAIL, ALtrimenti
		//devo DIRE CHE LA MAIL È SCONOSCIUTA
	}

	function sompass_posting_reset() {
		$( '#resetpasswordform #reset-pass-submit' ).attr( 'disabled', true );
	}

	function sompass_posting() {
		$( '#lostpasswordform #reset-pass-submit' ).attr( 'disabled', true );
	}

	$( '#lostpasswordform #somfrp_user_info' ).on('input', function() {
		//
	});

})( jQuery );
