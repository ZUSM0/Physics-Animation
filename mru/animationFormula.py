from manim import *

class formula(Scene):
  def construct(self):
    formula = MathTex(r"v = \frac{\Delta x}{\Delta t} ")
    
    formula2 = MathTex(r"v = \frac{S - S_{0}}{t - t_{0}}")
    formula3 = MathTex(r"v \cdot t = S - S_{0}")
    formula4 = MathTex(r"S = S_{0} + v \cdot t")
    