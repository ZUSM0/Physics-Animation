from manim import *

class exemplos(Scene):
    def construct(self):
        titulodados = Tex("Dados: ").scale(1.5).to_edge(UP*1.5+RIGHT*4.3)
        dado1 =    MathTex(r"\Delta S = 200 km").scale(1.3).to_edge(UP*3+RIGHT*0.7)
        dado2 = MathTex(r"\Delta t = 4 h").scale(1.3).to_edge(UP*4.5+RIGHT*3.45)
       
        dados = VGroup(titulodados, dado1, dado2)

        formula = MathTex(r"v_{m} = \frac{\Delta x}{\Delta t} ").scale(1.6).shift(UP*1+LEFT*1)

        self.add(titulodados)
        self.add(dado1)
        self.add(dado2)

        self.add(formula)

