<?php
/**
 * @package Barrel
 */

$barrel_theme_options = barrel_get_theme_options();

$post_classes = get_post_class();

$current_post_class = $post_classes[4];

// This post formats will display content before title
$post_classes_content_top = array('format-audio', 'format-video', 'format-gallery', 'format-status', 'format-link');

$category_html = '';

// Blog posts style
if(isset($barrel_theme_options['blog_post_elements_style'])) {
  $post_class_add = 'blog-post-style-'.$barrel_theme_options['blog_post_elements_style'];
} else {
  $post_class_add = 'blog-post-style-square';
}
?>

<div class="content-block blog-post clearfix <?php echo esc_attr($post_class_add); ?>">
	<article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
		
				
				<div class="post-content-wrapper">
					<?php 
					if(in_array($current_post_class , $post_classes_content_top)) {
						
						echo '<div class="entry-content">';
						the_content( esc_html__( 'Continue reading', 'barrel' ) );
						echo '</div>';
						
					} else {

						$category_html = '<div class="post-categories">'.( get_the_category_list( ', ', 0, $post->ID )).'</div>';

						if ( has_post_thumbnail() ):
					
						?>
						<div class="blog-post-thumb text-center">
							<a href="<?php the_permalink(); ?>" rel="bookmark">
							<?php the_post_thumbnail('barrel-blog-thumb'); ?>
							</a>
							<?php echo wp_kses_post($category_html); ?>
						</div>
						<?php
						endif;
					}

					$post_comments = get_comments_number($post->ID);

					?>
					<div class="post-content">
						<?php if(!has_post_thumbnail()) {
							echo wp_kses_post($category_html);
						}
						?>
						<div class="post-info">
						<span><a href="<?php the_permalink(); ?>" rel="bookmark"><?php the_time(get_option( 'date_format' ));  ?></a></span><span class="post-comments-count"><i class="fa fa-comment"></i><?php echo esc_html($post_comments); ?></span><?php edit_post_link( esc_html__( 'Edit', 'barrel' ), ' <span class="edit-link">', '</span>' ); ?>
						</div>
						<h2 class="entry-title post-header-title"><a href="<?php the_permalink(); ?>" rel="bookmark"><?php the_title(); ?></a></h2>
						
						<?php if(!in_array($current_post_class , $post_classes_content_top)): ?>
						<!-- .entry-content -->
						<div class="entry-content">
							<?php 
							
							the_content();
							
							wp_link_pages( array(
								'before' => '<div class="page-links">' . esc_html__( 'Pages:', 'barrel' ),
								'after'  => '</div>',
							) );
							?>
						</div><!-- // .entry-content -->
						<?php endif;?>
					
							
					</div>
		
				</div>
			
		
	</article>
</div>