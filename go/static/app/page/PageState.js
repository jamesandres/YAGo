(function() {
  app.page.factory("PageState", function() {
    var headTitle, status, title;
    status = "loading";
    headTitle = "YAGo";
    title = "YAGo";
    return {
      status: function(newStatus) {
        if (newStatus) {
          status = newStatus;
        }
        return status;
      },
      headTitle: function(newHeadTitle, appendSiteName) {
        if (newHeadTitle) {
          appendSiteName = (!angular.isUndefined(appendSiteName) ? appendSiteName : true);
          headTitle = newHeadTitle;
          if (appendSiteName) {
            headTitle += " | YAGo";
          }
        }
        return headTitle;
      },
      title: function(newTitle) {
        if (newTitle) {
          title = newTitle;
        }
        return title;
      }
    };
  });

}).call(this);
