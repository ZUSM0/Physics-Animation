from manim import *

class resolvido(Scene):
    def construct(self):
        enunciado = MarkupText("É dada a seguinte função horária da velocidade escalar de uma partícula em movimento uniformemente variado:").shift(UP*3).scale_to_fit_width(config["frame_width"]*0.75).scale(1.3)
        
        formulaPrincipal = MathTex(r"v = 15 + 20 \cdot t ").scale(1.5).shift(1.5*UP)

        alternativa1 = MarkupText("Determine:\na) A velocidade escalar inicial e a aceleração escalar da partícula.").shift(ORIGIN).scale_to_fit_width(config["frame_width"]*0.95)
    
        alternativa2 = MarkupText("b) A velocidade esclar no instante 4 s.").shift(DOWN*0.8+LEFT*2.6).scale_to_fit_width(config["frame_width"]*0.59)
        
        alternativa3 = MarkupText("c) O instante em que a velocidade esclar vale 225 m/s").shift(DOWN*1.4+LEFT*0.6).scale_to_fit_width(config["frame_width"]*0.87)

        formula = MathTex(r"v = v_{0} + a \cdot t ").scale(2)

        self.add(enunciado)
        self.add(formulaPrincipal)
        self.add(alternativa1)
        self.add(alternativa2)
        self.add(alternativa3)