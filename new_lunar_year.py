import sys
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from asciimatics.effects import Print, Stars, Cycle
from asciimatics.renderers import StaticRenderer, FigletText
from asciimatics.scene import Scene

YEAR = 2023
RABBIT = r""" 
               ((`\
            ___ \\ '--._
         .'`   `'    o  )
        /    \   '. __.'
       _|    /_  \ \_\_
      {_\______\-'\__\_\
"""
CAT = r"""
    /\_/\           ___
   = o_o =_______    \ \ 
    __^      __(  \.__) )
(@)<_____>__(_____)____/
"""


def demo(screen):
    effects = [
        Stars(screen, screen.width),
        Print(screen,
              StaticRenderer(images=[CAT, CAT]),
              x=screen.width - 25,
              y=screen.height - 5),
        Print(screen,
              StaticRenderer(images=[RABBIT, RABBIT]),
              x=0 - 5,
              y=screen.height - 7),
        Cycle(screen,
              FigletText('HAPPY', font='small'),
              screen.height // 2 - 5),
        Cycle(screen,
              FigletText(f'NEW LUNAR YEAR {YEAR}', font='small'),
              screen.height // 2)
    ]
    screen.play(
        [Scene(effects=effects)],
        stop_on_resize=True
    )


while True:
    try:
        Screen.wrapper(demo)
        sys.exit(0)
    except ResizeScreenError as e:
        pass
