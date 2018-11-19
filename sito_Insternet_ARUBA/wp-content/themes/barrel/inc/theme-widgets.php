<?php
/**
 * Theme Widgets and sidebars
 */

$barrel_theme_options = barrel_get_theme_options();

/**
 * Theme sidebars
 */
if (!function_exists('barrel_widgets_init')) :
function barrel_widgets_init() {

    $barrel_theme_options = barrel_get_theme_options();
    
    register_sidebar(
      array(
        'name' => esc_html__( 'Blog sidebar', 'barrel' ),
        'id' => 'main-sidebar',
        'description' => esc_html__( 'Widgets in this area will be shown in the left or right site column for blog related pages.', 'barrel' )
      )
    );
    register_sidebar(
      array(
        'name' => esc_html__( 'Page sidebar', 'barrel' ),
        'id' => 'page-sidebar',
        'description' => esc_html__( 'Widgets in this area will be shown in the left or right site column for pages.', 'barrel' )
      )
    );
    register_sidebar(
      array(
        'name' => esc_html__( 'Portfolio sidebar', 'barrel' ),
        'id' => 'portfolio-sidebar',
        'description' => esc_html__( 'Widgets in this area will be shown in the left or right site column for portfolio items pages.', 'barrel' )
      )
    );
    register_sidebar(
      array(
        'name' => esc_html__( 'WooCommerce sidebar', 'barrel' ),
        'id' => 'woocommerce-sidebar',
        'description' => esc_html__( 'Widgets in this area will be shown in the left or right site column for woocommerce pages.', 'barrel' )
      )
    );
    register_sidebar(
      array(
        'name' => esc_html__( 'Offcanvas Right sidebar', 'barrel' ),
        'id' => 'offcanvas-sidebar',
        'description' => esc_html__( 'Widgets in this area will be shown in the right floating offcanvas menu sidebar that can be opened by toggle button in header. You can enable this sidebar in theme control panel.', 'barrel' )
      )
    );

    register_sidebar(
      array(
        'name' => esc_html__( 'Bottom sidebar (4 column)', 'barrel' ),
        'id' => 'bottom-sidebar',
        'description' => esc_html__( 'Widgets in this area will be shown below site content in 4 column.', 'barrel' )
      )
    );

    register_sidebar(
      array(
        'name' => esc_html__( 'Footer sidebar (1-5 columns)', 'barrel' ),
        'id' => 'footer-sidebar',
        'description' => esc_html__( 'Widgets in this area will be shown in site footer in 4 column below Bottom sidebar.', 'barrel' )
      )
    );

    register_sidebar(
      array(
        'name' => esc_html__( 'Header Left Sidebar', 'barrel' ),
        'id' => 'header-left-sidebar',
        'description' => esc_html__( 'Widgets in this area will be shown in the left header below menu if you use Left side header.', 'barrel' )
      )
    );
    
    // Mega Menu sidebars
    if(isset($barrel_theme_options['megamenu_sidebars_count']) && ($barrel_theme_options['megamenu_sidebars_count'] > 0)) {
        for ($i = 1; $i <= $barrel_theme_options['megamenu_sidebars_count']; $i++) {
            register_sidebar(
              array(
                'name' => esc_html__( 'MegaMenu sidebar #', 'barrel' ).$i,
                'id' => 'megamenu_sidebar_'.$i,
                'description' => esc_html__( 'You can use this sidebar to display widgets inside megamenu items in menus.', 'barrel' )
              )
            );
        }
    }

    // Custom widgets
    register_widget('Barrel_Widget_Recent_Posts');
    register_widget('Barrel_Widget_Social_Icons');
}
endif;
add_action( 'widgets_init', 'barrel_widgets_init' );

/**
 * Recent_Posts widget class
 */
class Barrel_Widget_Recent_Posts extends WP_Widget {

    public function __construct() {
        $widget_ops = array('classname' => 'widget_barrel_recent_entries', 'description' => esc_html__( "Your site&#8217;s most recent Posts with thumbnails.", 'barrel') );
        parent::__construct('barrel-recent-posts', esc_html__('Barrel Recent Posts', 'barrel'), $widget_ops);
        $this->alt_option_name = 'widget_barrel_recent_entries';
    }

    public function widget($args, $instance) {
        $cache = array();
        if ( ! $this->is_preview() ) {
            $cache = wp_cache_get( 'widget_barrel_recent_posts', 'widget' );
        }

        if ( ! is_array( $cache ) ) {
            $cache = array();
        }

        if ( ! isset( $args['widget_id'] ) ) {
            $args['widget_id'] = $this->id;
        }

        if ( isset( $cache[ $args['widget_id'] ] ) ) {
            echo wp_kses_post($cache[ $args['widget_id'] ]);
            return;
        }

        ob_start();

        $title = ( ! empty( $instance['title'] ) ) ? $instance['title'] : '';

        /** This filter is documented in wp-includes/default-widgets.php */
        $title = apply_filters( 'widget_title', $title, $instance, $this->id_base );

        $number = ( ! empty( $instance['number'] ) ) ? absint( $instance['number'] ) : 5;
        if ( ! $number )
            $number = 5;
        $show_date = isset( $instance['show_date'] ) ? $instance['show_date'] : false;
        $show_thumb = isset( $instance['show_thumb'] ) ? $instance['show_thumb'] : false;

        /**
         * Filter the arguments for the Recent Posts widget.
         *
         * @since 3.4.0
         *
         * @see WP_Query::get_posts()
         *
         * @param array $args An array of arguments used to retrieve the recent posts.
         */
        $r = new WP_Query( apply_filters( 'widget_barrel_posts_args', array(
            'posts_per_page'      => $number,
            'no_found_rows'       => true,
            'post_status'         => 'publish',
            'ignore_sticky_posts' => true
        ) ) );

        if ($r->have_posts()) :
?>
        <?php echo wp_kses_post($args['before_widget']); ?>
        <?php if ( $title ) {
            echo wp_kses_post($args['before_title'] . $title . $args['after_title']);
        } ?>
        <ul>
        <?php $i=0; ?>
        <?php while ( $r->have_posts() ) : $r->the_post(); ?>
        <?php $image_bg = ''; ?>
            <li class="clearfix">
            <?php if (( $show_thumb ) && has_post_thumbnail( get_the_ID() )) : ?>
            <div class="widget-post-thumb-wrapper">
            <a href="<?php the_permalink(); ?>">
            <?php the_post_thumbnail('barrel-blog-thumb-widget'); ?>
            </a>
            </div>
            <?php endif; ?>
            <div class="widget-post-details-wrapper">
                <div class="post-title"><a href="<?php the_permalink(); ?>"><?php get_the_title() ? the_title() : the_ID(); ?></a></div>
                <?php if ( $show_date ) : ?>
                    <div class="post-date"><?php echo get_the_date(); ?></div>
                <?php endif; ?>
            </div>
            </li>
            <?php $i++; ?>
        <?php endwhile; ?>
        </ul>
        <?php echo wp_kses_post($args['after_widget']); ?>
<?php
        // Reset the global $the_post as this query will have stomped on it
        wp_reset_postdata();

        endif;

        if ( ! $this->is_preview() ) {
            $cache[ $args['widget_id'] ] = ob_get_flush();
            wp_cache_set( 'widget_barrel_recent_posts', $cache, 'widget' );
        } else {
            ob_end_flush();
        }
    }

    public function update( $new_instance, $old_instance ) {
        $instance = $old_instance;
        $instance['title'] = strip_tags($new_instance['title']);
        $instance['number'] = (int) $new_instance['number'];
        $instance['show_date'] = isset( $new_instance['show_date'] ) ? (bool) $new_instance['show_date'] : false;
        $instance['show_thumb'] = isset( $new_instance['show_thumb'] ) ? (bool) $new_instance['show_thumb'] : false;

        $alloptions = wp_cache_get( 'alloptions', 'options' );
        if ( isset($alloptions['widget_barrel_recent_entries']) )
            delete_option('widget_barrel_recent_entries');

        return $instance;
    }

    public function form( $instance ) {
        $title     = isset( $instance['title'] ) ? esc_attr( $instance['title'] ) : '';
        $number    = isset( $instance['number'] ) ? absint( $instance['number'] ) : 5;
        $show_date = isset( $instance['show_date'] ) ? (bool) $instance['show_date'] : false;
        $show_thumb = isset( $instance['show_thumb'] ) ? (bool) $instance['show_thumb'] : false;
?>
        <p><label for="<?php echo esc_attr($this->get_field_id( 'title' )); ?>"><?php esc_html_e( 'Title:', 'barrel' ); ?></label>
        <input class="widefat" id="<?php echo esc_attr($this->get_field_id( 'title' )); ?>" name="<?php echo esc_attr($this->get_field_name( 'title' )); ?>" type="text" value="<?php echo esc_attr($title); ?>" /></p>

        <p><label for="<?php echo esc_attr($this->get_field_id( 'number' )); ?>"><?php esc_html_e( 'Number of posts to show:', 'barrel' ); ?></label>
        <input id="<?php echo esc_attr($this->get_field_id( 'number' )); ?>" name="<?php echo esc_attr($this->get_field_name( 'number' )); ?>" type="text" value="<?php echo esc_attr($number); ?>" size="3" /></p>

        <p><input class="checkbox" type="checkbox" <?php checked( $show_date ); ?> id="<?php echo esc_attr($this->get_field_id( 'show_date' )); ?>" name="<?php echo esc_attr($this->get_field_name( 'show_date' )); ?>" />
        <label for="<?php echo esc_attr($this->get_field_id( 'show_date' )); ?>"><?php esc_html_e( 'Display post date?', 'barrel' ); ?></label></p>

        <p><input class="checkbox" type="checkbox" <?php checked( $show_thumb ); ?> id="<?php echo esc_attr($this->get_field_id( 'show_thumb' )); ?>" name="<?php echo esc_attr($this->get_field_name( 'show_thumb' )); ?>" />
        <label for="<?php echo esc_attr($this->get_field_id( 'show_thumb' )); ?>"><?php esc_html_e( 'Display post featured image?', 'barrel' ); ?></label></p>
<?php
    }
}


/**
 * Barrel buttons widget class
 *
 */
class Barrel_Widget_Social_Icons extends WP_Widget {

    public function __construct() {
        $widget_ops = array('classname' => 'widget_barrel_social_icons', 'description' => esc_html__( 'Show social follow icons set in theme admin panel.', 'barrel' ) );
        parent::__construct('barrel-social-icons', esc_html__('Barrel Social Icons', 'barrel'), $widget_ops);
        $this->alt_option_name = 'widget_barrel_social_icons';
    }

    public function widget( $args, $instance ) {
        $barrel_theme_options = barrel_get_theme_options();

        $cache = array();

        if ( ! $this->is_preview() ) {
            $cache = wp_cache_get('widget_barrel_social_icons', 'widget');
        }
        if ( ! is_array( $cache ) ) {
            $cache = array();
        }

        if ( ! isset( $args['widget_id'] ) )
            $args['widget_id'] = $this->id;

        if ( isset( $cache[ $args['widget_id'] ] ) ) {
            echo wp_kses_post($cache[ $args['widget_id'] ]);
            return;
        }

        $output = '';

        $title = ( ! empty( $instance['title'] ) ) ? $instance['title'] : esc_html__( 'Subscribe and follow', 'barrel' );

        /** This filter is documented in wp-includes/default-widgets.php */
        $title = apply_filters( 'widget_title', $title, $instance, $this->id_base );

        $output .= $args['before_widget'];
        if ( $title ) {
            $output .= $args['before_title'] . $title . $args['after_title'];
        }

        $output .= '<div class="textwidget">';

        $output_end = '</div>';
        $output_end .= $args['after_widget'];

        echo wp_kses_post($output); // This variable contains WordPress widget code and can't be escaped with WordPress functions 

        barrel_social_icons_show();

        echo wp_kses_post($output_end);

        if ( ! $this->is_preview() ) {
            $cache[ $args['widget_id'] ] = $output;
            wp_cache_set( 'widget_barrel_social_icons', $cache, 'widget' );
        }
    }

    public function update( $new_instance, $old_instance ) {
        $instance = $old_instance;
        $instance['title'] = strip_tags($new_instance['title']);

        $alloptions = wp_cache_get( 'alloptions', 'options' );
        if ( isset($alloptions['barrel_social_icons']) )
            delete_option('barrel_social_icons');

        return $instance;
    }

    public function form( $instance ) {
        $title  = isset( $instance['title'] ) ? esc_attr( $instance['title'] ) : '';
?>
        <p><label for="<?php echo esc_attr($this->get_field_id( 'title' )); ?>"><?php esc_html_e( 'Title:', 'barrel' ); ?></label>
        <input class="widefat" id="<?php echo esc_attr($this->get_field_id( 'title' )); ?>" name="<?php echo esc_attr($this->get_field_name( 'title' )); ?>" type="text" value="<?php echo esc_attr($title); ?>" /></p>
<?php
    }
}
?>