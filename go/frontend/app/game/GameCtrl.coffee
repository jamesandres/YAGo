app.game.controller "GameCtrl", ["$scope", "gameService", ($scope, gameService) ->
    $scope.you = config.game['player' + config.player]
    $scope.opponent = config.game['player' + (config.player % 2 + 1)]

    $scope.title = "#{$scope.you.username} vs #{$scope.opponent.username}. You are playing #{$scope.you.color}"

    return @
]
