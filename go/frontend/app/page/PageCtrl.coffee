app.page.controller "PageCtrl", ["$scope", "PageState", ($scope, PageState) ->
    console.log "PAGE CONTROLLER"

    $scope.PageState = PageState

    return @
]
