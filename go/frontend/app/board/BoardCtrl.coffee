app.board.controller "BoardCtrl", ["$scope", ($scope) ->
  return @
]

# // jQuery(function ($) {
# //     var i, x, y,
# //         classes,
# //         star,
# //         play, loc,
# //         $el = $('<div class="game-play-area"></div>'),
# //         $board = $('<div class="go-board"></div>'),
# //         $board_inner = $('<div class="inner"></div>'),
# //         $interaction_layer = $('<div class="interaction-layer"></div>');

# //     $board.append($board_inner);
# //     $el.append($board);
# //     $el.append($interaction_layer);
# //     $('body').append($el);

# //     // Build the board, the visible part
# //     for (x = 1; x <= game.board_size - 1; x++) {
# //         for (y = 1; y <= game.board_size - 1; y++) {
# //             classes = ['cell', 'cell-' + x + '-' + y + ''];

# //             star = '';

# //             if ((x - 4) % 6 == 0 && (y - 4) % 6 == 0) {
# //                 star = '<div class="star"></div>';
# //             }

# //             $board_inner.append([
# //                 '<div class="', classes.join(' ') ,'">',
# //                     star,
# //                     '<span class="label">', x, ',', y, '</span>',
# //                 '</div>'].join('')
# //             );
# //         }
# //     }

# //     // Build the board, the visible part
# //     for (x = 1; x <= game.board_size; x++) {
# //         for (y = 1; y <= game.board_size; y++) {
# //             classes = ['btn', 'btn-' + x + '-' + y + '']
# //             $interaction_layer.append([
# //                 '<div class="', classes.join(' ') ,'" ',
# //                      'data-x="', x, '" data-y="', y, '">',
# //                 '</div>'
# //             ].join(''));
# //         }
# //     }

# //     // Lay out the previous plays
# //     for (i = 0; i < game.plays.length; i++) {
# //         play = game.plays[i];
# //         loc = play.loc.split(',');

# //         color = (play.player - 1) % 2 === 0 ? 'black' : 'white';

# //         $('.btn-' + loc[0] + '-' + loc[1])
# //             .append('<div class="stone stone-' + color + '"></div>')
# //             .addClass('btn-disabled');
# //     };

# //     // Yucky rough click handling
# //     $interaction_layer.find('.btn:not(.btn-disabled)').click(function () {
# //         var $btn = $(this);

# //         $.ajax({
# //             method: 'POST',
# //             url: '/' + game.id + '/play',
# //             data: {
# //                 x: $btn.data('x'),
# //                 y: $btn.data('y')
# //             },
# //             success: function (data) {
# //                 color = (data.player - 1) % 2 === 0 ? 'black' : 'white';
# //                 $btn
# //                     .append('<div class="stone stone-' + color + '"></div>')
# //                     .addClass('btn-disabled');
# //             },
# //         });
# //     });
# // });