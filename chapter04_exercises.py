#!/usr/bin/env python3
"""Think Python (3e), Chapter 4 exercises: Functions and Interfaces.

Uses Python's built-in turtle module instead of the book's jupyturtle.
The functions forward, left, penup and pendown are imported directly, so the
code reads exactly like the book's.

Includes:
  1. Book exercises 4.11.1 - 4.11.6
  2. Comparison with the instructor's GitHub solutions
  3. Which solution is better and why
  4. How either solution could be improved
"""
import math
import turtle
from turtle import forward, left, penup, pendown


# ===========================================================================
# Helper functions from the chapter
# ===========================================================================
def jump(length):
    """Move forward length units without leaving a trail.

    Postcondition: Leaves the pen down.
    """
    penup()
    forward(length)
    pendown()


def polyline(n, length, angle):
    """Draws n line segments with the given length and angle between them.

    n: integer number of line segments
    length: length of each segment
    angle: angle between segments (in degrees)
    """
    for i in range(n):
        forward(length)
        left(angle)


def polygon(n, length):
    """Draws a regular polygon with n sides of the given length."""
    angle = 360 / n
    polyline(n, length, angle)


def arc(radius, angle):
    """Draws an arc with the given radius and angle (in degrees)."""
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(n, length, step_angle)


def circle(radius):
    """Draws a circle with the given radius."""
    arc(radius, 360)


# ===========================================================================
# Exercise 4.11.3: parallelogram
# (Written before rectangle and rhombus, because Exercise 3 asks us to
# rewrite both of them to use it.)
# ===========================================================================
def parallelogram(length1, length2, angle):
    """Draws a quadrilateral with parallel sides.

    length1: length of the first and third sides
    length2: length of the second and fourth sides
    angle: interior angle (in degrees) between the first and second sides

    The turtle turns left by 180 - angle, so the shape's interior angle
    at that corner really is angle.
    """
    for i in range(2):
        forward(length1)
        left(180 - angle)
        forward(length2)
        left(angle)


# ===========================================================================
# Exercise 4.11.1: rectangle
#
# First version (before Exercise 3):
#     def rectangle(width, height):
#         for i in range(2):
#             forward(width)
#             left(90)
#             forward(height)
#             left(90)
#
# Rewritten to use parallelogram: a rectangle is a parallelogram with
# 90-degree corners.
# ===========================================================================
def rectangle(width, height):
    """Draws a rectangle with the given width and height."""
    parallelogram(width, height, 90)


# ===========================================================================
# Exercise 4.11.2: rhombus
#
# First version (before Exercise 3):
#     def rhombus(length, angle):
#         for i in range(2):
#             forward(length)
#             left(180 - angle)
#             forward(length)
#             left(angle)
#
# Rewritten to use parallelogram: a rhombus is a parallelogram whose sides
# are all the same length.
# ===========================================================================
def rhombus(length, angle):
    """Draws a rhombus with the given side length and interior angle."""
    parallelogram(length, length, angle)


# ===========================================================================
# Exercise 4.11.4: pie shapes
# ===========================================================================
def triangle(radius, angle):
    """Draws one isosceles triangle (one slice of the pie).

    radius: length of the two equal sides
    angle: angle (in degrees) between the two equal sides, at the tip

    The tip is where the turtle starts. The turtle ends back at the tip,
    facing the same direction it started.
    """
    base = 2 * radius * math.sin(math.radians(angle / 2))
    base_angle = (180 - angle) / 2
    forward(radius)
    left(180 - base_angle)
    forward(base)
    left(180 - base_angle)
    forward(radius)
    left(180 - angle)


def draw_pie(n, radius):
    """Draws a regular polygon made of n triangular slices.

    n: number of slices (and sides)
    radius: distance from the center to each corner
    """
    angle = 360 / n
    for i in range(n):
        triangle(radius, angle)
        left(angle)


# ===========================================================================
# Exercise 4.11.5: flowers
# ===========================================================================
def petal(radius, angle):
    """Draws one petal using two arcs.

    radius: radius of the arcs
    angle: angle of each arc (in degrees); a bigger angle makes a fatter petal
    """
    for i in range(2):
        arc(radius, angle)
        left(180 - angle)


def flower(n, radius, angle):
    """Draws a flower with n petals, evenly spaced.

    n: number of petals
    radius: radius of the arcs that make each petal
    angle: angle of each arc (in degrees)
    """
    for i in range(n):
        petal(radius, angle)
        left(360 / n)


# ===========================================================================
# Exercise 4.11.6: Ask a virtual assistant
#
# Prompt: the book's prompt (the circle program using jupyturtle, followed by
#   "Write a function that draws a spiral.")
#
# Result: it figured out the module from the example and wrote a spiral that
#   draws a polyline where each segment is a little longer than the last.
#   I only had to change the import from jupyturtle to Python's turtle.
#   It didn't use any features we haven't covered yet.
# ===========================================================================
def spiral(n, length, angle, growth):
    """Draws a spiral of n segments, starting from the center.

    n: number of segments
    length: length of the first segment
    angle: turn between segments (in degrees)
    growth: how much longer each segment is than the one before
    """
    for i in range(n):
        forward(length)
        left(angle)
        length = length + growth


# ===========================================================================
# PART 2: COMPARISON WITH THE INSTRUCTOR'S SOLUTIONS
# ===========================================================================
#
# Exercise 1 (rectangle): The instructor loops over (b, h) and calls
#   polyline(1, s, 90) to draw each side. That works, but calling polyline
#   to draw ONE line is a roundabout way to write forward(s) and left(90).
#   The names b and h are also less clear than width and height.
#
# Exercise 2 (rhombus): Same pattern. It works, but the docstring calls
#   the angle "the first interior angle", while the turtle actually turns
#   LEFT by that angle. So the corner it labels 60 degrees is really
#   120 degrees. The finished shape still has two 60-degree corners and two
#   120-degree corners, so it looks right, but the description is off.
#   (There's also a typo: "bie".)
#
# Exercise 3 (parallelogram): Good. rectangle and rhombus are both
#   rewritten to call parallelogram, which is exactly what the book asks.
#   The same interior-angle naming issue as Exercise 2 applies. My version
#   turns left(180 - angle), so angle really is the interior angle.
#   Exercise 4 contains a second copy of parallelogram that uses
#   features[0] and features[1] instead of unpacking (side, angle). That's
#   harder to read than the Exercise 3 version.
#
# Exercise 4 (pie shapes): The math is correct and the shapes come out
#   right. But isosceles_triangle takes the BASE angle, so draw_pie has to
#   work out base_angle = 90 - 180 / n and then turn by 180 - 2 * base_angle,
#   which equals 360 / n anyway. The variable called center_angle is not
#   actually the center angle: the real center angle is 180 - center_angle.
#   My triangle takes the angle at the tip, so draw_pie just uses
#   360 / n directly, with no extra conversion. There's also an unused import
#   (from math import degrees).
#
# Exercise 5 (flowers): Matches the book's approach and mine. petal
#   computes return_angle and then never uses it. The file is also named
#   "Excercise05.py" (misspelled). flower's optional petal_angle is a nice
#   extra.
#
# Exercise 6 (virtual assistant spiral): The instructor didn't include it.
#
# Every file: The instructor copies polyline, polygon and jump into every
#   file, even where they aren't used (jump is never called). Every function
#   also depends on a global variable named my_turtle that's created at the
#   bottom of the file. A function that quietly relies on a global is harder
#   to reuse. I imported forward and left directly from turtle, so my code
#   matches the book.
#
#
# ===========================================================================
# PART 3: WHICH SOLUTION IS BETTER, AND WHY?
# ===========================================================================
#
# Both sets of solutions draw the right shapes. The instructor's Exercise 3
# is a great example of generalization: one parallelogram function replaces
# separate rectangle and rhombus code. I think my versions are a bit better
# for this chapter, because their INTERFACES are easier to use:
#   - parallelogram's angle really is the shape's interior angle.
#   - triangle takes the angle at the tip, so draw_pie can just divide 360
#     by n. The caller doesn't have to convert angles first.
#   - Everything is in one file, with no duplicated or unused functions.
# This is the main idea of the chapter: a good interface hides the details
# and makes the function easy to call correctly.
#
#
# ===========================================================================
# PART 4: CAN EITHER SOLUTION BE IMPROVED, AND HOW?
# ===========================================================================
#
# Instructor's solutions:
#   - Use forward/left instead of polyline(1, ...) for single sides.
#   - Name parameters for what they mean (width/height instead of b/h) and
#     make the docstrings match what the code actually does with the angle.
#   - Let triangle take the tip angle so draw_pie doesn't need extra math,
#     and rename center_angle.
#   - Remove unused code (jump, return_angle, the degrees import), and put
#     the shared functions in one place instead of copying them into
#     every file.
#
# My solutions:
#   - The functions draw from wherever the turtle happens to be, so drawing
#     several shapes means moving the turtle by hand first (see move_to
#     below). A version that takes x and y parameters would be easier to use.
#   - polyline, arc and circle could take the number of segments as a
#     parameter instead of always using 30.
#   - spiral only grows by a fixed amount each step. A true Archimedean
#     spiral is based on the angle, which would need features from later
#     chapters.


# ===========================================================================
# Drawing all the exercises
# ===========================================================================
def move_to(x, y):
    """Moves the turtle to (x, y) without drawing and points it east."""
    penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    pendown()


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    turtle.speed(0)
    turtle.hideturtle()

    # Exercises 1-3: rectangle, rhombus, parallelogram
    move_to(-350, 250)
    rectangle(80, 40)
    move_to(-200, 250)
    rhombus(50, 60)
    move_to(-80, 250)
    parallelogram(100, 60, 60)

    # Exercise 6: spiral
    move_to(250, 280)
    spiral(60, 1, 20, 0.4)

    # Exercise 4: pies with 5, 6, 7 and 8 slices
    move_to(-280, 50)
    draw_pie(5, 70)
    move_to(-100, 50)
    draw_pie(6, 70)
    move_to(80, 50)
    draw_pie(7, 70)
    move_to(260, 50)
    draw_pie(8, 70)

    # Exercise 5: three flowers
    move_to(-250, -250)
    flower(7, 60, 60)
    move_to(0, -250)
    flower(10, 40, 80)
    move_to(250, -250)
    flower(20, 140, 20)

    turtle.exitonclick()
