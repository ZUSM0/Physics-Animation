from manim import *

class pessoa(Scene):
  def construct(self):
    # Parte da pessoa
    titulodados = Tex("Dados: ").scale(1.5).to_edge(UP*1.5+RIGHT*3.9)
    dadoPes1 = MathTex(r"\Delta S = 10 m").scale(1.3).shift(ORIGIN+UP*1.5)
    dadoPes2 = MathTex(r"\Delta t = 4 s").scale(1.3).shift(ORIGIN+UP*0.7)

    person = ImageMobject("imagens\pessoa.jpg")
    vector = Vector([8, 0]).shift(DOWN*2.5+LEFT*5)
    person.scale(0.5).shift(DOWN*1.5+LEFT*5)
        
    self.add(titulodados)
        
    self.play(FadeIn(person), Write(vector), run_time=1.5)
    self.wait(1.5)

    self.play( Write(dadoPes1.shift(DOWN*5), run_time=1.75), person.animate.move_to(DOWN*1.5), run_time=2)
    self.play(Write(dadoPes2.shift(DOWN*0.5+LEFT*5)), run_time=1.75)

    self.play(dadoPes1.animate.move_to(UP*2+RIGHT*4.7), dadoPes2.animate.move_to(UP*1.4+RIGHT*4.3), run_time=2)
    self.wait(0.4)

    formulaPes1 = MathTex(r"v_{m} = \frac{10}{4}").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)
    formulaPes2 = MathTex(r"v_{m} = 2.5 m/s").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)

    self.play(Write(formulaPes1), run_time=2)
    self.wait(1.75)
    self.play(TransformMatchingShapes(formulaPes1, formulaPes2), run_time=2)
    self.wait(2)

    formulaPes3 = MathTex(r"v_{m} = 2.5 \cdot 3.6").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)
    formulaPes4 = MathTex(r"v_{m} = 9 km/h").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)

    self.play(TransformMatchingShapes(formulaPes2, formulaPes3), run_time=2)
    self.wait(2)
    self.play(TransformMatchingShapes(formulaPes3, formulaPes4), run_time=2)
    self.wait(2)

    formulaPes5 = MathTex(r"v_{m} = \frac{9}{3.6}").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)
    formulaPes6 = MathTex(r"v_{m} = 2.5 m/s").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)

    self.play(TransformMatchingShapes(formulaPes4, formulaPes5), run_time=2)
    self.wait(2)
    self.play(TransformMatchingShapes(formulaPes5, formulaPes6), run_time=2)
    
    self.wait(4)