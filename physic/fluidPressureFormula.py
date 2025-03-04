from manim import *

class fluidPressureFormula(Scene):
  def construct(self):
    fluidPressureFormula = MathTex(r"P = d \cdot g \cdot h").scale(3)
    self.add(fluidPressureFormula)