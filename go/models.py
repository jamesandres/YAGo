# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


PLAYER_CHOICES = (
    (1, 'Player 1'),
    (2, 'Player 2'),
)

BOARD_LOCATIONS = []

for x in range(19):
    for y in range(19):
        loc = "%d,%d" % (x, y)
        BOARD_LOCATIONS.append([loc, loc])


def xstr(s):
    if not s:
        return ''
    else:
        return str(s)


class Play(models.Model):
    """
    A single play in a game as defined by sequence, player and play location.
    """

    seq = models.PositiveSmallIntegerField()
    player = models.PositiveSmallIntegerField(choices=PLAYER_CHOICES)
    loc = models.CharField(choices=BOARD_LOCATIONS, max_length="7")

    def __str__(self):
        return ' '.join([
            xstr(self.seq),
            xstr(self.player),
        ])

admin.site.register(Play)


class Kifu(models.Model):
    """
    Kifu (棋譜) is the Japanese term for a game record for a game of Go or
    shogi. Kifu is traditionally used to record games on a grid diagram,
    marking the plays on the points by numbers.
    """

    date = models.DateTimeField()

    player1 = models.ForeignKey(User, related_name='kifu_player1')
    player2 = models.ForeignKey(User, related_name='kifu_player2')

    plays = models.ForeignKey(Play)

    def __str__(self):
        return ' '.join([
            xstr(self.date),
            xstr(self.player1),
            xstr(self.player2),
        ])

admin.site.register(Kifu)
