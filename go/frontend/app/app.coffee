app = angular.module 'yago', [
        'yago.page',
        'yago.games_list',
        'yago.game',
        'yago.board',
    ]

app.page = angular.module 'yago.page', []
app.games_list = angular.module 'yago.games_list', []
app.game = angular.module 'yago.game', []
app.board = angular.module 'yago.board', []

window.app = app
