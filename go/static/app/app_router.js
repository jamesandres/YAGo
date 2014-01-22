(function() {
  app.config([
    "$routeProvider", "$locationProvider", function($routeProvider, $locationProvider) {
      $locationProvider.html5Mode(true).hashPrefix("!");
      $routeProvider.when("/games", {
        templateUrl: "templates/user/gamesList.html",
        controller: "GamesListCtrl"
      });
      return $routeProvider.otherwise({
        redirectTo: "/"
      });
    }
  ]);

}).call(this);
