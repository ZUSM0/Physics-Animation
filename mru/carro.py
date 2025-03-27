from manim import *

class exemplos(Scene):
    def construct(self):        
        titulodados = Tex("Dados: ").scale(1.5).to_edge(UP*1.5+RIGHT*3.9)
        dado1 = MathTex(r"\Delta S = 200 km").scale(1.3).shift(ORIGIN)
        dado2 = MathTex(r"\Delta t = 4 h").scale(1.3).shift(ORIGIN)
        
        formula1 = MathTex(r"v_{m} = \frac{200}{4}").scale(1.6)
        formula2 = MathTex(r"v_{m} = 50 km/h").scale(1.6)

        # Colocar carro no inicio da animação!
        self.play(Write(titulodados))
        self.play(Write(dado1), run_time=1.75)
        self.play(dado1.animate.move_to(UP*2+RIGHT*5), run_time=2)
        self.play(Write(dado2),run_time=1)
        self.play(dado2.animate.move_to(UP*1.4+RIGHT*4.3), run_time=2)

        self.wait(2)
        self.play(Write(formula1), run_time=2)
        self.wait(2)
        self.play(TransformMatchingShapes(formula1, formula2), run_time=2)
        self.wait(3)

        # Ver como remover dado1, dado2, formula2  
        
        # Parte do ciclista 
        dadoBic1 =    MathTex(r"\Delta S = 2 km").scale(1.3).shift(ORIGIN)
        dadoBic2 = MathTex(r"\Delta t = 5 min").scale(1.3).shift(ORIGIN+DOWN*0.5)   
        
        dadoBic12 = MathTex(r"\Delta S = 2000 m").scale(1.3)
        dadoBic22 = MathTex(r"\Delta t = 300 s").scale(1.3).shift(ORIGIN+DOWN*0.5)  

        self.play(Write(dadoBic1))
        self.play(Write(dadoBic2))
        self.play(TransformMatchingShapes(dadoBic1, dadoBic12))
        self.play(TransformMatchingShapes(dadoBic2, dadoBic22))

        formulabic1 = MathTex(r"v_{m} = \frac{2000}{300}").scale(1.6)
        formulabic2 = MathTex(r"v_{m} = 6.67 m/hs").scale(1.6)

        self.play(dadoBic12.animate.move_to(UP*2+RIGHT*5), run_time=2)
        self.play(dadoBic22.animate.move_to(UP*1.4+RIGHT*4.3), run_time=2)

        self.wait(2)
        self.play(Write(formulabic1), run_time=2)
        self.wait(2)
        self.play(TransformMatchingShapes(formulabic1, formulabic2), run_time=2)
        self.wait(3)

        # Parte da pessoa
        dadoPes1 =    MathTex(r"\Delta S = 10 m").scale(1.3).to_edge(UP*3+RIGHT*0.7)
        dadoPes2 = MathTex(r"\Delta t = 4 s").scale(1.3).to_edge(UP*4.5+RIGHT*3.45)
       
        formulaPes1 = MathTex(r"v_{m} = \frac{10}{4}")
        formulaPes2 = MathTex(r"v_{m} = 2.5 m/s")

        formulaPes3 = MathTex(r"v_{m} = 2.5 \cdot 3.6")
        formulaPes4 = MathTex(r"v_{m} = 9 km/h")

        formulaPes5 = MathTex(r"v_{m} = \frac{9}{3.6}")
        formulaPes6 = MathTex(r"v_{m} = 2.5 m/s")

