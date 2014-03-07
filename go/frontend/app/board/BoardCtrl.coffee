app.board.controller "BoardCtrl", ["$scope", "gameService", ($scope, gameService) ->
    $scope.cells = []
    $scope.buttons = []

    $scope.btn_click = (btn) ->
        p = gameService.play btn.x, btn.y
        p.success (data) ->
            # color = (data.player - 1) % 2 === 0 ? 'black' : 'white';
            # $btn
            #     .append('<div class="stone stone-' + color + '"></div>')
            #     .addClass('btn-disabled');
            console.log "SUCCESS: ", data

    gameService.bindPusherEvent "play", (data) ->
        console.log "DATA", data

    board_iterator = (x_dim, y_dim, fn) ->
        for x in [x_dim[0]..x_dim[1]]
            for y in [y_dim[0]..y_dim[1]]
                fn(x, y, x + ',' + y)

    bs = config.game.board_size
    plays_map = {}

    # Lay out the previous plays
    for play in config.game.plays
        loc = play.loc.split(',')
        plays_map[loc] = play

    # Build the list of cells
    dim = [1, bs - 1]
    board_iterator dim, dim, (x, y, loc) ->
        $scope.cells.push
            class: 'cell-' + x + '-' + y + ''
            has_star: ((x - 4) % 6 == 0) and ((y - 4) % 6 == 0)
            label: loc

    # Build the list of buttons to interact with playable points
    dim = [1, bs]
    board_iterator dim, dim, (x, y, loc) ->
        play = plays_map[loc]

        if play?
            stone_class = if (play.player % 2) + 1 == 1 then 'stone-white' else 'stone-black';
        else
            stone_class = false

        $scope.buttons.push
            class: 'btn-' + x + '-' + y + ''
            x: x
            y: y
            stone_class: stone_class

    return @
]
