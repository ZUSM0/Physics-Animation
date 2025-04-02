from manim import *

class bicicleta(Scene):
  def construct(self):
    #Parte do ciclista 
    titulodados = Tex("Dados: ").scale(1.5).to_edge(UP*1.5+RIGHT*3.9)
    dadoBic1 = MathTex(r"\Delta S = 2 km").scale(1.3).shift(DOWN*3.1+LEFT*0.6)
    dadoBic2 = MathTex(r"\Delta t = 5 min").scale(1.3).shift(ORIGIN+LEFT*0.6) 
    
    bike = ImageMobject("imagens\image.png")
    vector = Vector([8, 0]).shift(DOWN*2.5+LEFT*5)
    bike.scale(0.35).shift(DOWN*1.5+LEFT*5)
        
    self.add(titulodados)  
    
    self.play(FadeIn(bike), Write(vector), run_time=1.5)
    self.wait(1.5)
    
    dadoBic12 = MathTex(r"\Delta S = 2000 m").scale(1.3).shift(DOWN*3.1+LEFT*0.6)
    dadoBic22 = MathTex(r"\Delta t = 300 s").scale(1.3).shift(ORIGIN+LEFT*0.6)  

    self.play(Write(dadoBic1), run_time=2)
    self.play(Write(dadoBic2), run_time=2)
    self.wait(3)
    
    self.play(bike.animate.move_to(DOWN*1.5), TransformMatchingShapes(dadoBic1, dadoBic12), run_time=2)
    self.wait(1)
    self.play(TransformMatchingShapes(dadoBic2, dadoBic22), run_time=2)
    
    self.wait(2)

    self.play(dadoBic12.animate.move_to(UP*2+RIGHT*5), dadoBic22.animate.move_to(UP*1.4+RIGHT*4.6), run_time=2)
    
    formulabic1 = MathTex(r"v_{m} = \frac{2000}{300}").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)
    formulabic2 = MathTex(r"v_{m} = 6.67 m/s").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)

    self.wait(2)
    self.play(Write(formulabic1), run_time=2.75)
    self.wait(2)
    self.play(TransformMatchingShapes(formulabic1, formulabic2), run_time=2)
    self.wait(3)
    
    self.play(FadeOut(dadoBic12, dadoBic22, formulabic2))
    self.wait(1)