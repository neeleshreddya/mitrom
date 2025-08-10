<?php
// Shortcode for 6 random 'job' category posts with thumbnails and dates
function random_job_posts_shortcode() {
    $args = array(
        'category_name' => 'job',
        'posts_per_page' => 6,
        'orderby' => 'rand',
    );
    $query = new WP_Query($args);
    $output = '<section id="random-job-posts" class="random-job-posts section"><div class="container">';
    if ($query->have_posts()) {
        while ($query->have_posts()) {
            $query->the_post();
            $output .= '<div class="random-post-item">';
            if (has_post_thumbnail()) {
                $output .= '<a href="' . get_permalink() . '">' . get_the_post_thumbnail(get_the_ID(), 'thumbnail') . '</a>';
            }
            $output .= '<a href="' . get_permalink() . '">' . get_the_title() . '</a>';
            $output .= '<div class="post-date">' . get_the_date() . '</div>';
            $output .= '</div>';
        }
    } else {
        $output .= 'No posts found.';
    }
    wp_reset_postdata();
    $output .= '</div></section>';
    return $output;
}
add_shortcode('random_job_posts', 'random_job_posts_shortcode');

// Enqueue theme CSS and JS assets
function mitrom_theme_scripts() {
    // CSS files
    wp_enqueue_style('bootstrap-css', get_template_directory_uri() . '/assets/css/bootstrap.min.css', array(), '5.3.3');
    wp_enqueue_style('swiper-css', get_template_directory_uri() . '/assets/css/swiper-bundle.min.css', array(), '8.0.0');
    wp_enqueue_style('main-style', get_template_directory_uri() . '/assets/css/main.css', array(), '1.0');

    // JS files in footer
    wp_enqueue_script('bootstrap-js', get_template_directory_uri() . '/assets/js/bootstrap.bundle.min.js', array('jquery'), '5.3.3', true);
    wp_enqueue_script('swiper-js', get_template_directory_uri() . '/assets/js/swiper-bundle.min.js', array(), '8.0.0', true);
    wp_enqueue_script('main-js', get_template_directory_uri() . '/assets/js/main.js', array('jquery'), '1.0', true);
}
add_action('wp_enqueue_scripts', 'mitrom_theme_scripts');
?>
