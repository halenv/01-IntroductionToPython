"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Noelle Hale.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

felix = rg.SimpleTurtle('turtle')
felix.speed = 20
felix.pen = rg.Pen('orange',10)
einstein = rg.SimpleTurtle()
einstein.speed = 30
einstein.pen = rg.Pen('midnight blue', 5)

sizef = 150
radius = 30

for k in range (10):
    felix.draw_regular_polygon(10-k,sizef)

    felix.pen_up()
    felix.right(45)
    felix.backward(15)
    felix.pen_down()

    sizef = sizef - 10
    felix.speed = 20 + 2*k

for j in range (14):

    einstein.begin_fill()
    einstein.draw_circle(radius)

    einstein.pen_up()
    einstein.forward(radius/2)
    einstein.pen_down()

    radius= radius + 10

window.close_on_mouse_click()
