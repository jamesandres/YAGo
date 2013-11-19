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

        context['board'] = list()
        for x in range(19):
            context['board'].insert(x, [])
            for y in range(19):
                context['board'][x].insert(y, "%d,%d" % (x + 1, y + 1))

        print context['board']

        return context
