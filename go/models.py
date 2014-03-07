# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.forms import ValidationError


PLAYER_CHOICES = (
    (1, 'Player 1'),
    (2, 'Player 2'),
)

BOARD_LOCATIONS = []

for x in range(19):
    for y in range(19):
        loc = "%d,%d" % (x + 1, y + 1)
        BOARD_LOCATIONS.append([loc, loc])


def xstr(s):
    if not s:
        return ''
    else:
        return str(s)


class Game(models.Model):
    """
    Kifu (棋譜) is the Japanese term for a game record for a game of Go or
    shogi. Kifu is traditionally used to record games on a grid diagram,
    marking the plays on the points by numbers.
    """

    date = models.DateTimeField()

    player1 = models.ForeignKey(User, related_name='game_player1')
    player2 = models.ForeignKey(User, related_name='game_player2')

    board_size = models.PositiveSmallIntegerField(default=19)

    def plays(self):
        plays = []

        data = Play.objects.filter(game=self).order_by('seq')
        for datum in data:
            plays.append({
                'player': datum.player,
                'loc': datum.loc,
            })

        return plays

    def to_dict(self):
        return {
            'date': str(self.date),
            'player1': self.player1,
            'player2': self.player2,
            'board_size': int(self.board_size),
        }

    def __str__(self):
        return "%s: %s vs. %s" % (
            self.date.strftime('%d, %B %Y'),
            xstr(self.player1),
            xstr(self.player2)
        )

admin.site.register(Game)


class Play(models.Model):
    """
    A single play in a game as defined by sequence, player and play location.
    """

    game = models.ForeignKey(Game)

    seq = models.PositiveSmallIntegerField()
    player = models.PositiveSmallIntegerField(choices=PLAYER_CHOICES)
    loc = models.CharField(choices=BOARD_LOCATIONS, max_length="7")

    class Meta:
        unique_together = (('game', 'seq'),)

    def validate_unique(self, exclude=None):
        others = Play.objects.filter(
            game=self.game, loc=self.loc).exclude(pk=self.pk)

        if others.count() > 0:
            raise ValidationError("There is a stone at this location.")

    def clean(self):
        is_first = not Play.objects.filter(game=self.game).exists()

        if is_first and self.player != 1:
            raise ValidationError("Black must play the first move.")

        return self.player

    def calculate_sequence(self):
        try:
            last_play = Play.objects.filter(game=self.game).latest('seq')
        except Play.DoesNotExist:
            last_play = None

        if not last_play:
            self.seq = 0
        else:
            if last_play.player == self.player:
                raise ValidationError("You cannot play twice in a row")

            self.seq = last_play.seq + 1

    def to_dict(self):
        return {
            'id': self.id,
            # 'game': self.game,
            'seq': int(self.seq),
            'player': self.player,
            'loc': self.loc,
        }

    def __str__(self):
        return "Play #%d in %s at %s by player #%d " % (
            self.seq,
            self.game,
            self.loc,
            self.player)

admin.site.register(Play)


def User_to_dict(self):
    return {
        'id': self.id,
        'username': self.username,
    }

User.to_dict = User_to_dict
