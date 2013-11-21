from django.views.generic import View, ListView, DetailView
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.utils import simplejson

from go.models import Kifu, Play
from go.utils.json_serializer import model_to_json


class ListGamesView(ListView):

    template_name = 'list-games.html'
    model = Kifu


class GameView(DetailView):

    template_name = 'game.html'
    model = Kifu

    def get_context_data(self, **kwargs):
        context = super(GameView, self).get_context_data(**kwargs)

        kifu = context['kifu']
        context['game'] = {
            'id': kifu.id,
            'date': kifu.date,
            'player1': str(kifu.player1),
            'player2': str(kifu.player2),
            'board_size': kifu.board_size,
        }

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
        kifu_id = kwargs.get('kifu_id', '')
        kifu = Kifu.objects.filter(pk=kifu_id)

        if not kifu:
            return self._error("Cannot make play in game '%s'" % kifu_id)

        play = Play(
            kifu=kifu[0],
            loc=request.POST.get('x', '') + ',' + request.POST.get('y', ''))

        play.calculate_sequence_and_player()

        print "play.full_clean(): ", play.full_clean()

        try:
            play.full_clean()
        except ValidationError:
            return self._error(
                "You cannot make move '%s' in game '%s'" % (play.loc, play.kifu))

        play.save()
        return HttpResponse(
            model_to_json(play),
            mimetype='application/json')
