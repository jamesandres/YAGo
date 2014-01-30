app = angular.module 'yago', [
        'ngRoute',
        'yago.page',
        'yago.game',
    ]

app.page = angular.module 'yago.page', []
app.game = angular.module 'yago.game', []

window.app = app
