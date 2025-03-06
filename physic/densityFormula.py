from manim import *

class densityFormula(Scene):
  def construct(self):
    # Criação da fórmula de densidade
    densityFormula = MathTex(r"d = \frac{m}{V}").scale(3)
    
    # Animação
    self.add(densityFormula)