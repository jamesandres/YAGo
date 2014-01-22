app.page.factory "PageState", ->
  status = "loading"
  headTitle = "YAGo"
  title = "YAGo"

  status: (newStatus) ->
    status = newStatus  if newStatus
    status

  headTitle: (newHeadTitle, appendSiteName) ->
    if newHeadTitle
      appendSiteName = (if not angular.isUndefined(appendSiteName) then appendSiteName else true)
      headTitle = newHeadTitle
      headTitle += " | YAGo"  if appendSiteName
    headTitle

  title: (newTitle) ->
    title = newTitle  if newTitle
    title
