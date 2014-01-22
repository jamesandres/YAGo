(function() {
  var app;

  app = angular.module('yago', ['ngRoute', 'yago.page']);

  app.page = angular.module('yago.page', []);

  window.app = app;

}).call(this);
