app.game.factory "gameService", ["$http", ($http) ->
    play: (x, y) ->
        return $http.post '/g/' + config.game.id + '/play',
            "x": x
            "y": y
]
