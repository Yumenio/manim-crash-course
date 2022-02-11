from manim import *

class Test(Scene):
  def construct(self):
    circle = Circle()
    ax = Axes(x_range=[0,8,1], y_range=[0,8,1], tips=True)
    graph = ax.plot(lambda x: x**2, x_range=[0.01,4], use_smoothing=True)

    # self.add(circle)
    self.play(circle.animate.shift(RIGHT))
    self.play(circle.animate.shift(RIGHT))
    self.play(graph.animate.shift(RIGHT))
    # self.play(circle)