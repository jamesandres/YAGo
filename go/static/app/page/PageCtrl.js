(function() {
  app.page.controller("PageCtrl", [
    "$scope", "PageState", function($scope, PageState) {
      console.log("PAGE CONTROLLER");
      $scope.PageState = PageState;
      return this;
    }
  ]);

}).call(this);
