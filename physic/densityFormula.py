from manim import *

class densityFormula(Scene):
  def construct(self):
    densityFormula = MathTex(r"d = \frac{m}{V}").scale(3)
    
    self.add(densityFormula)