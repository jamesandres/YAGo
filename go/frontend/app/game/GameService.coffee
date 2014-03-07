app.game.provider "gameService", ->
    @pusher = null
    @channel = null

    @ensurePusherConnection = =>
        if not @pusher
            @pusher = new Pusher config.pusher.key
        if not @channel
            @channel = @pusher.subscribe("yago.game." + config.game.id);
        window.test = @

    @$get = ["$http", ($http) =>
        bindPusherEvent:  (event_name, callback) =>
            @channel.bind event_name, callback

        play: (x, y) =>
            return $http.post '/g/' + config.game.id + '/play',
                "x": x
                "y": y
                # Sending the pusher socket ID helps the server avoid echoing
                # this client's pushes back again
                "socket_id": @pusher.connection.socket_id
    ]

    @
