# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

import types


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


class Kifu(models.Model):
    """
    Kifu (棋譜) is the Japanese term for a game record for a game of Go or
    shogi. Kifu is traditionally used to record games on a grid diagram,
    marking the plays on the points by numbers.
    """

    date = models.DateTimeField()

    player1 = models.ForeignKey(User, related_name='kifu_player1')
    player2 = models.ForeignKey(User, related_name='kifu_player2')

    board_size = models.PositiveSmallIntegerField(default=19)

    def plays(self):
        plays = []

        data = Play.objects.filter(kifu=self).order_by('seq')
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

admin.site.register(Kifu)


class Play(models.Model):
    """
    A single play in a game as defined by sequence, player and play location.
    """

    kifu = models.ForeignKey(Kifu)

    seq = models.PositiveSmallIntegerField()
    player = models.PositiveSmallIntegerField(choices=PLAYER_CHOICES)
    loc = models.CharField(choices=BOARD_LOCATIONS, max_length="7")

    def calculate_sequence_and_player(self):
        # TODO: Handle finished game.
        if not isinstance(self.kifu, Kifu):
            return False

        try:
            last_play = Play.objects.filter(kifu=self.kifu).latest('seq')
        except Play.DoesNotExist:
            last_play = None

        if not last_play:
            self.seq = 0
            self.player = 1
        else:
            self.seq = last_play.seq + 1
            self.player = ((last_play.player + 1) % 2) + 1

        return True

    def to_dict(self):
        return {
            'id': self.id,
            # 'kifu': self.kifu,
            'seq': int(self.seq),
            'player': self.player,
            'loc': self.loc,
        }

    def __str__(self):
        return ' '.join([
            xstr(self.kifu),
            xstr(self.seq),
            xstr(self.player),
            xstr(self.loc),
        ])

admin.site.register(Play)


def User_to_dict(self):
    return {
        'id': self.id,
        'username': self.username,
    }

User.to_dict = User_to_dict
