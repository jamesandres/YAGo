app.board.directive "yagoBoard", ->
    restrict: "E"
    scope: {}
    templateUrl: '/static/app/board/board.html'

app.board.directive "yagoCell", ->
    restrict: "E"
    scope: {}
    template: '<div class="cell"></div>'