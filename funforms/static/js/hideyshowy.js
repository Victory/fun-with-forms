jQuery(function ($) {
  $("#id_check_this").click(function (evt) {
    var $this = $(this);
    if ($this.is(':checked')) {
      $("#showIfIsChecked").show();
    } else {
      $("#showIfIsChecked").hide();
    }
    
  });
}(jQuery));