from manim import *

class PressureFormula(Scene):
  def construct(self):
    # Criação da fórmula de pressão
    pressureFormula = MathTex(r"P = \frac{F}{A}").scale(3)

    # Animação
    self.add(pressureFormula)