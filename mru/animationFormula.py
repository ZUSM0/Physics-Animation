from manim import *

class formula(Scene):
  def construct(self):
    formula = MathTex(r"v = \frac{\Delta s}{\Delta t}")
    formula2 = MathTex(r"\Delta s = v \cdot t")
    formula3 = MathTex(r"S - S_{0} = v \cdot t")
    formula4 = MathTex(r"S = S_{0} + v \cdot t")

    self.play(Write(formula), run_time=2)
    self.wait(1)
    self.play(TransformMatchingShapes(formula, formula2), run_time=2)
    self.wait(2)
    self.play(TransformMatchingShapes(formula2, formula3), run_time=2)
    self.wait(2)
    self.play(TransformMatchingShapes(formula3, formula4), run_time=2)
    self.wait(4)
    