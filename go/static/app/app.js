(function() {
  var app;

  app = angular.module('yago', ['ngRoute', 'yago.page', 'yago.game']);

  app.page = angular.module('yago.page', []);

  app.games_list = angular.module('yago.games_list', []);

  app.game = angular.module('yago.game', []);

  app.board = angular.module('yago.board', []);

  window.app = app;

  app.config([
    "$routeProvider", "$locationProvider", function($routeProvider, $locationProvider) {
      $locationProvider.html5Mode(true);
      $routeProvider.when("/", {
        templateUrl: "http://localhost:8000/static/app/games_list/games_list.html",
        controller: "GamesListCtrl"
      });
      $routeProvider.when("/g/:id", {
        templateUrl: "http://localhost:8000/static/app/game/game.html",
        controller: "GameCtrl"
      });
      $routeProvider.when("/fake", {
        templateUrl: "http://localhost:8000/static/app/game/game.html",
        controller: "GameCtrl"
      });
      return $routeProvider.otherwise({
        redirectTo: "/"
      });
    }
  ]);

  app.run([
    "$location", function($location) {
      return $location.path('/');
    }
  ]);

}).call(this);
