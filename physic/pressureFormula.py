from manim import *

class PressureFormula(Scene):
  def construct(self):
    pressureFormula = MathTex(r"P = \frac{F}{A}").scale(3)
    self.add(pressureFormula)