from django.views.generic import View, ListView, DetailView
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.utils import simplejson

from go.models import Game, Play
from go.utils.json_serializer import model_to_json


class ListGamesView(ListView):

    template_name = 'list-games.html'
    model = Game


class GameView(DetailView):

    template_name = 'game.html'
    model = Game

    def get_context_data(self, **kwargs):
        context = super(GameView, self).get_context_data(**kwargs)

        game = context['game']
        context['game_data'] = {
            'id': game.id,
            'date': game.date,
            'player1': game.player1.to_dict(),
            'player2': game.player2.to_dict(),
            'board_size': game.board_size,
            'plays': game.plays(),
        }
        context['player'] = self.request.user.to_dict()

        return context


class APIPlayView(View):
    http_method_names = ['post']

    def _error(self, message):
        errors = {
            'message': message
        }
        return HttpResponse(
            simplejson.dumps(errors), mimetype='application/json')

    def post(self, request, *args, **kwargs):
        game_id = kwargs.get('pk', '')
        game = Game.objects.filter(pk=game_id)

        if not game:
            return self._error("Cannot make play in game '%s'" % game_id)

        play = Play(
            game=game[0],
            loc=request.POST.get('x', '') + ',' + request.POST.get('y', ''))

        play.calculate_sequence_and_player()

        print "play.full_clean(): ", play.full_clean()

        try:
            play.full_clean()
        except ValidationError:
            return self._error(
                "You cannot make move '%s' in game '%s'" % (play.loc, play.game))

        play.save()
        return HttpResponse(
            model_to_json(play),
            mimetype='application/json')
