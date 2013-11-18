from django.views.generic import TemplateView

from go.models import Kifu, Play


class GameView(TemplateView):

    template_name = 'game.html'
    model = Kifu

    def get_context_data(self, **kwargs):
        context = super(GameView, self).get_context_data(**kwargs)

        # TODO: Add the game content here.