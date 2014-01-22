app.config ["$routeProvider", "$locationProvider", ($routeProvider, $locationProvider) ->

  # See: http://docs.angularjs.org/guide/dev_guide.services.$location
  $locationProvider.html5Mode(true).hashPrefix "!"

  $routeProvider.when "/games",
    templateUrl: "templates/user/gamesList.html"
    controller: "GamesListCtrl"

  $routeProvider.otherwise redirectTo: "/"
]