from manim import *

class exemplos(Scene):
    def construct(self):        
        titulodados = Tex("Dados: ").scale(1.5).to_edge(UP*1.5+RIGHT*3.9)
        dado1 = MathTex(r"\Delta S = 200 km").scale(1.3).shift(ORIGIN)
        dado2 = MathTex(r"\Delta t = 4 h").scale(1.3).shift(ORIGIN)
        
        formula1 = MathTex(r"v_{m} = \frac{200}{4}").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)
        formula2 = MathTex(r"v_{m} = 50 km/h").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)

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
        self.wait(2)

        self.play(FadeOut(dado1, dado2, formula2))  
        self.wait(1)
        
        # Parte do ciclista 
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

        # Parte da pessoa
        dadoPes1 = MathTex(r"\Delta S = 10 m").scale(1.3).shift(ORIGIN+UP*1.5)
        dadoPes2 = MathTex(r"\Delta t = 4 s").scale(1.3).shift(ORIGIN+UP*0.7)
        
        self.play(Write(dadoPes1), run_time=2)
        self.play(Write(dadoPes2), run_time=2)
        
        self.play(dadoPes1.animate.move_to(UP*2+RIGHT*4.7), run_time=2)
        self.play(dadoPes2.animate.move_to(UP*1.4+RIGHT*4.3), run_time=2)
        self.wait(2)
        
        formulaPes1 = MathTex(r"v_{m} = \frac{10}{4}").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)
        formulaPes2 = MathTex(r"v_{m} = 2.5 m/s").scale(1.6).shift(ORIGIN+UP*1+LEFT*1.5)
        
        self.play(Write(formulaPes1), run_time=2)
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
        
        
        
        self.wait(5)

