(function() {
  app.config([
    "$routeProvider", "$locationProvider", function($routeProvider, $locationProvider) {
      $locationProvider.html5Mode(true).hashPrefix("!");
      $routeProvider.when("/", {
        templateUrl: "static/app/game_list/game_list.html",
        controller: "GamesListCtrl"
      });
      $routeProvider.when("/g/:id", {
        templateUrl: "static/app/game/game.html",
        controller: "GameCtrl"
      });
      return $routeProvider.otherwise({
        redirectTo: "/"
      });
    }
  ]);

}).call(this);
