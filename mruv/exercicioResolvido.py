from manim import *

class resolvido(Scene):
    def construct(self):
        enunciado = Text("É dada a seguinte função horária da velocidade escalar de uma partícula em movimento uniformemente variado:").shift(UP*3).scale_to_fit_width(config.frame_width*0.98)
        formulaPrincipal = MathTex(r"v = 15 + 20 \cdot t ").scale(1.5).shift(1.5*UP)

        alternativa1 = Text("a) A velocidade escalar inicial e a aceleração escalar da partícula.").shift(ORIGIN).scale_to_fit_width(config.frame_width*0.7)
    
        alternativa2 = Text("b) A velocidade esclar no instante 4 s.").shift(DOWN*0.7).scale_to_fit_width(config.frame_width*0.7)
        alternativa3 = Text("c) O instante em que a velocidade esclar vale 225 m/s").shift(DOWN*1.4).scale_to_fit_width(config.frame_width*0.7)

        formula = MathTex(r"v = v_{0} + a \cdot t ").scale(2)

        self.add(enunciado)
        self.add(formulaPrincipal)
        self.add(alternativa1)
        self.add(alternativa2)
        self.add(alternativa3)