(function() {
  app.page.controller("PageCtrl", [
    "$scope", "PageState", function($scope, PageState) {
      $scope.PageState = PageState;
      return this;
    }
  ]);

}).call(this);
