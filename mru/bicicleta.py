from manim import *

class bicicleta(Scene):
  def construct(self):
    #Parte do ciclista 
    
    dadoBic1 = MathTex(r"\Delta S = 2 km").scale(1.3).shift(ORIGIN)
    dadoBic2 = MathTex(r"\Delta t = 5 min").scale(1.3).shift(ORIGIN+DOWN*1)   
    
    dadoBic12 = MathTex(r"\Delta S = 2000 m").scale(1.3).shift(ORIGIN)
    dadoBic22 = MathTex(r"\Delta t = 300 s").scale(1.3).shift(ORIGIN+DOWN*1)  

    self.play(Write(dadoBic1), run_time=2)
    self.play(Write(dadoBic2), run_time=2)
    self.wait(3)
    self.play(TransformMatchingShapes(dadoBic1, dadoBic12), run_time=2)
    self.play(TransformMatchingShapes(dadoBic2, dadoBic22), run_time=2)

    formulabic1 = MathTex(r"v_{m} = \frac{2000}{300}").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)
    formulabic2 = MathTex(r"v_{m} = 6.67 m/s").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)

    self.play(dadoBic12.animate.move_to(UP*2+RIGHT*5), run_time=2)
    self.play(dadoBic22.animate.move_to(UP*1.4+RIGHT*4.6), run_time=2)

    self.wait(2)
    self.play(Write(formulabic1), run_time=3)
    self.wait(2)
    self.play(TransformMatchingShapes(formulabic1, formulabic2), run_time=2)
    self.wait(3)
    
    self.play(FadeOut(dadoBic12, dadoBic22, formulabic2))
    self.wait(1)