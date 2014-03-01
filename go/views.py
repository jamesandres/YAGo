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

    def _error(self, message, status=200):
        data = {
            'errors': {
                'message': message
            }
        }
        return HttpResponse(
            simplejson.dumps(data),
            mimetype='application/json',
            status=status)

    def post(self, request, *args, **kwargs):
        game_id = kwargs.get('pk', '')

        try:
            game = Game.objects.get(pk=game_id)
        except Game.DoesNotExist:
            return self._error("Cannot make play in game '%s'" % game_id, 400)

        if request.user == game.player1:
            player = 1
        elif request.user == game.player2:
            player = 2
        else:
            return self._error("Access denied", 403)

        x = str(request.POST.get('x', ''))
        y = str(request.POST.get('y', ''))

        play = Play(game=game, loc=x + ',' + y, player=player)

        try:
            # NOTE: calculate_sequence will throw a ValidationError if a player
            #       tries to play out of turn
            play.calculate_sequence()
            play.full_clean()
        except ValidationError as e:
            return self._error(". ".join(e.messages), 400)

        play.save()
        return HttpResponse(
            model_to_json(play),
            mimetype='application/json')
