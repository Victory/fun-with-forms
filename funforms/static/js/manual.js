jQuery(function ($) {
  var bindRemove = function () {
    $elms = $(".author button");
    $elms.click(function (evt) {
      console.log('click');
      $(this).parents(".author").remove();
      $elms = $(".author button");
      if ($elms.length == 2) {
        $("button", $(".author")[0]).remove();
        return;
      }
    });
  };
  bindRemove();
  $("#add_author").click(function (evt) {
    var $proto = $($("#author_prototype").html());
    var $div = $("<div>");
    $div.append($proto);
    $("#authors").append($div);
    bindRemove();
  });
});