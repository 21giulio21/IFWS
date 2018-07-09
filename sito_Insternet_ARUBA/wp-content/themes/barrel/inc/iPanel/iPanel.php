<?php

    /*
     *    === Define the Path ===
    */
    defined('BARREL_IPANEL_PATH') ||
        define( 'BARREL_IPANEL_PATH' , get_template_directory() . '/iPanel/' );    

    /*
     *    === Define the Version of iPanel ===
    */
    define( 'IPANEL_VERSION' , '1.1' );    
    

    
    /*
     *    === Define the Classes Path ===
    */
    if ( defined('BARREL_IPANEL_PATH') ) {
        define( 'IPANEL_CLASSES_PATH' , BARREL_IPANEL_PATH . 'classes/' );
    } else {
        define( 'IPANEL_CLASSES_PATH' , get_template_directory() . '/iPanel/classes/' );
    }
    
    function barrel_iPanelLoad(){
        require_once IPANEL_CLASSES_PATH . 'ipanel.class.php';
		if( file_exists(BARREL_IPANEL_PATH . 'options.php') )
			require_once BARREL_IPANEL_PATH . 'options.php';
    }
    
    if ( defined('BARREL_IPANEL_PLUGIN_USAGE') ) {
        if ( BARREL_IPANEL_PLUGIN_USAGE === true ) {
            add_action('plugins_loaded', 'barrel_iPanelLoad');
        } else {
            add_action('init', 'barrel_iPanelLoad');
        }
    } else {
        add_action('init', 'barrel_iPanelLoad');
    }