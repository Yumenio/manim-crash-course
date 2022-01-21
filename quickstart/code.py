from manim import *

class CreateCircle(Scene):
  def construct(self):
    circle = Circle()
    circle.set_fill(RED, opacity = 0.5)
    self.play(Create(circle))

class SquareToCircle(Scene):
  def construct(self):
    circle = Circle()
    circle.set_fill(RED, opacity = 0.7)

    square = Square()
    square.rotate(PI/4)
    
    self.play(Create(square))
    self.play(Transform(square,circle))
    self.play(FadeOut(square))


class SquareNextToCircle(Scene):
  def construct(self):
    circle = Circle()
    circle.set_fill(RED, opacity=0.7)

    square = Square()
    square.rotate(PI/4)
    
    square.next_to(circle, RIGHT, buff=-0.5)
    self.play(Create(square), Create(circle))