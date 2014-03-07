app.config ["gameServiceProvider", (gameServiceProvider) ->
    gameServiceProvider.ensurePusherConnection()
]
