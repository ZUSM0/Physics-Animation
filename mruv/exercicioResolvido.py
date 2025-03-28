from manim import *

class resolvido(Scene):
    def construct(self):
        enunciado = Tex("É dada a seguinte função horária da velocidade escalar de uma partícula em movimento uniformemente variado:")
        formulaPrincipal = MathTex(r"v = 15 + 20 \cdot t ").scale(2)

        alternativas = ("Determine:\na) A velocidade escalar inicial e a aceleração escalar da partícula.\nb) A velocidade esclar no instante 4 s.\nc) O instante em que a velocidade esclar vale 225 m/s")

        formula = MathTex(r"v = v_{0} + a \cdot t ").scale(2)