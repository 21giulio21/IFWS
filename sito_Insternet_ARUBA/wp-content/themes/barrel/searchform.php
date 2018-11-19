<?php
/**
 * The template for displaying search forms in Barrel
 *
 * @package Barrel
 */
?>
	<form method="get" id="searchform" class="searchform" action="<?php echo esc_url( home_url( '/' ) ); ?>">
		<input type="search" class="field" name="s" value="<?php echo esc_attr( get_search_query() ); ?>" id="s" placeholder="<?php echo esc_html__('Type keyword(s) here', 'barrel' ); ?>" />
		<input type="submit" class="submit btn" id="searchsubmit" value="<?php echo esc_html__( 'Search', 'barrel' ); ?>" />
	</form>
