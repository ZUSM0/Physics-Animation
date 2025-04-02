from manim import *

class exemplos(Scene):
    def construct(self):        
        titulodados = Tex("Dados: ").scale(1.5).to_edge(UP*1.5+RIGHT*3.9)
        dado1 = MathTex(r"\Delta S = 200 km").scale(1.3).shift(ORIGIN)
        dado2 = MathTex(r"\Delta t = 4 h").scale(1.3).shift(ORIGIN)
        
        formula1 = MathTex(r"v_{m} = \frac{200}{4}").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)
        formula2 = MathTex(r"v_{m} = 50 km/h").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)
        
        # Animação do carro
        
        car = ImageMobject("imagens\carro.png")
        vector = Vector([8, 0]).shift(DOWN*2.5+LEFT*5)
        car.scale(0.7).shift(DOWN*1.9+LEFT*5)
        
        self.add(titulodados)
        
        self.play(FadeIn(car), Write(vector))
        self.play(Write(dado1.shift(DOWN*3.4)), run_time=1.75)
        self.play(dado1.animate.move_to(UP*2+RIGHT*5), Write(dado2.shift(DOWN*0.5+LEFT*5)), run_time=1.75)
        
        self.play(dado2.animate.move_to(UP*1.4+RIGHT*4.3), car.animate.move_to(DOWN*1.9), run_time=3)

        self.play(Write(formula1), run_time=2)
        self.wait(2)
        self.play(TransformMatchingShapes(formula1, formula2), run_time=2)
        self.wait(2)

        self.play(FadeOut(dado1, dado2, formula2))  
        self.wait(1)
        
        self.wait(5)

