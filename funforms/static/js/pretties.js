jQuery(function ($) {
  var selectors = {
    formValidateName: "[form-validate-name] input",
  };

  $(selectors.formValidateName).on('keydown', function (evt) {
    var $this = $(this);

    if (evt.which == 13) {
      evt.preventDefault();
      return;
    }
  });

});