"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Kyle Brown.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(600,600)
    circle1_centre = rg.Point(200,200)
    circle2_centre = rg.Point(400,300)
    circle1 = rg.Circle(circle1_centre,100)
    circle2 = rg.Circle(circle2_centre,50)
    circle2.fill_color = 'red'
    circle1.attach_to(window)
    circle2.attach_to(window)

    window.render()

    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


    window = rg.RoseWindow(800,700)

    circle_centre_x = 300
    circle_centre_y = 150
    circle_Centre = rg.Point(circle_centre_x,circle_centre_y)
    circle_thickness = 5
    circlefill = 'blue'

    circle1 = rg.Circle(circle_Centre,150)
    circle1.fill_color = circlefill
    circle1.outline_thickness = circle_thickness

    corner1_x = 500
    corner1_y = 100
    corner2_x = 600
    corner2_y = 500
    corner1 = rg.Point(corner1_x,corner1_y)
    corner2 = rg.Point(corner2_x,corner2_y)
    rectthic = 20
    rectfill = 'none'

    rectangle = rg.Rectangle(corner1,corner2)
    rectangle.outline_thickness = rectthic


    circle1.attach_to(window)
    rectangle.attach_to(window)

    print('Circle outline thickness =',circle_thickness)
    print('Circle fill =',circlefill)
    print('Circle centre =',circle_Centre)
    print('Circle centre x =', circle_centre_x)
    print('Circle centre y =', circle_centre_y)
    print('Rectangle outline thickness =', rectthic)
    print('Rectangle fill colour =',rectfill)
    print('Rectangle 1st corner =',corner1)
    print('Rectangle 2nd corner =',corner2)

    window.render()
    window.close_on_mouse_click()


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # ------------------------------------------------------------------


    window = rg.RoseWindow(500,500)

    L1start = rg.Point(100,100)
    L1end = rg.Point(400,400)
    L2start = rg.Point(500,0)
    L2end = rg.Point(400,100)

    L1 = rg.Line(L1start,L1end)
    L2 = rg.Line(L2start,L2end)
    L2.thickness = 20
    L2mid = L2.get_midpoint()


    L1.attach_to(window)
    L2.attach_to(window)

    print('L2 midpoint =',L2mid)
    print('L2 midpoint x coordinate =',L2mid.x)
    print('L2 midpoint y coordinate =',L2mid.y)

    window.render()
    window.close_on_mouse_click()



# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
