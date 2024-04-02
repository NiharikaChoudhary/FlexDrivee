var sQuery = '<?php echo $sQuery; ?>';
jQuery(document).ready(function () {
  jQuery(window).scroll(function () {
    var scrollTop = jQuery(this).scrollTop();
    var button1Offset = jQuery('#collapse-one').offset().top;
    var button2Offset = jQuery('#collapse-two').offset().top;
    var button3Offset = jQuery('#collapse-three').offset().top;
    var button4Offset = jQuery('#collapse-four').offset().top;
    var button5Offset = jQuery('#collapse-five').offset().top;

    // Reset all button highlights
    jQuery('.myDIV div').removeClass('active');

    // Highlight the buttons based on the scroll position
    if (scrollTop >= button1Offset && scrollTop < button2Offset-200) {
      jQuery('#headingOne').addClass('active');
    } else if (scrollTop >= button2Offset-600 && scrollTop < button3Offset-300) {
      jQuery('#heading2').addClass('active');
    } 
    
  });
});
var a = document.querySelectorAll(".myDIV button");
        for (var i = 0, length = a.length; i < length; i++) {
            a[i].onclick = function () {
                var b = document.querySelector(".myDIV div.active");
                if (b) b.classList.remove("active");
                this.parentNode.classList.add('active');
            };
        } 
