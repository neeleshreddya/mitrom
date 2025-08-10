<?php get_header(); ?>

<!-- Slider Section -->
<section id="slider" class="slider section dark-background">
  <div class="container" data-aos="fade-up" data-aos-delay="100">
    <?php echo do_shortcode('[recent_post_slider category="job" limit="5" design="design-1"]'); ?>
  </div>
</section>

<!-- Random Job Posts Section -->
<?php echo do_shortcode('[random_job_posts]'); ?>

<!-- Trending Section -->
<div class="container" data-aos="fade-up" data-aos-delay="100">
  <div class="trending">
    <h3>Trending</h3>
    <?php
    if (function_exists('wpp_get_mostpopular')) {
        $args = array(
            'limit' => 5,
            'range' => 'all',
            'thumbnail_width' => 50,
            'thumbnail_height' => 50,
            'post_html' => '<li>{thumb} <a href="{url}">{text_title}</a></li>',
        );
        echo '<ul class="trending-post">';
        wpp_get_mostpopular($args);
        echo '</ul>';
    }
    ?>
  </div>
</div>

<?php get_footer(); ?>
