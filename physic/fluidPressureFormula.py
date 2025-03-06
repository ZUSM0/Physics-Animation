from manim import *

class fluidPressureFormula(Scene):
  def construct(self):
    # Criação da fórmula de pressão dos flúidos
    fluidPressureFormula = MathTex(r"P = d \cdot g \cdot h").scale(3)
    
    # Animação
    self.add(fluidPressureFormula)