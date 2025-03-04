from manim import *

class fluidPressureFormulaAnimation(Scene):
  def construct(self):
    # Fómula de pressão mecânica
    pressureFormula = MathTex(r"P = \frac{F_{p}}{A}").scale(1.75)
    
    # Fórmula da forca Peso
    forceFormula1 = MathTex(r"F_{p} = m \cdot g").scale(1.75)
    forceFormula2 = MathTex(r"F_{p} = d \cdot V \cdot g").scale(1.75)
    forceFormula3 = MathTex(r"F_{p} = d \cdot A \cdot h \cdot g").scale(1.75)
    
    # Fórmula da densidade
    densityFormula1 = MathTex(r"d = \frac{m}{V}").scale(1.75)
    densityFormula2 = MathTex(r"m = d \cdot V").scale(1.75)
    
    # Fómula de volume
    volumeFormula = MathTex(r"V = A \cdot h").scale(2)
    
    # Fórmula da pressão dos fluidos 
    fluidPressureFomula1 = MathTex(r"P = \frac{d \cdot A \cdot h \cdot g}{A}").scale(2)
    
    fluidPressureFomula = MathTex(r"P = d \cdot g \cdot h").scale(2)
    
    # Animação
    self.play(Write(pressureFormula), run_time=2)
    self.play(pressureFormula.animate.move_to(2.75*UP + 5.3*LEFT), run_time=2)
    
    self.play(Write(forceFormula1), run_time=2)
    self.wait(1.75)
    self.play(forceFormula1.animate.move_to(2.75*UP), run_time=2)
    
    self.play(Write(densityFormula1), run_time=3)
    self.wait(1.75)
    self.play(TransformMatchingShapes(densityFormula1, densityFormula2), run_time=2)
    self.wait(1.75)
    
    self.play(TransformMatchingShapes(Group(densityFormula2, forceFormula1), forceFormula2), run_time=2)
    self.wait(1.75)
    self.play(forceFormula2.animate.move_to(2.75*UP), run_time=2)
    
    self.play(Write(volumeFormula), run_time=2)
    self.wait(1.75)
    self.play(TransformMatchingShapes(Group(volumeFormula, forceFormula2), forceFormula3), run_time=2)
    self.wait(1.75)
    
    self.play(forceFormula3.animate.move_to(2.75*UP), run_time=2)
    self.play(pressureFormula.animate.move_to(ORIGIN), run_time=2)
    self.wait(1.75)
    
    self.play(TransformMatchingShapes(Group(pressureFormula, forceFormula3), fluidPressureFomula1), run_time=2)
    self.wait(2)
    self.play(TransformMatchingShapes(fluidPressureFomula1, fluidPressureFomula), run_time=2)
    
    self.wait(4)
    