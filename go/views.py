from django.views.generic import ListView, DetailView

from go.models import Kifu, Play


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
            'date': kifu.date,
            'player1': str(kifu.player1),
            'player2': str(kifu.player2),
            'board_size': kifu.board_size,
        }

        return context
