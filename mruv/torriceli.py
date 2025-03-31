from manim import *

class torriceli(Scene):
    def construct(self):
        mruvHoraria = MathTex(r"S = S_{0} + v_{0} \cdot t) + \frac{(a * t²)}{2}")

        mruvBase = MathTex(r"v = v_{0} + a \cdot t")
        base2 = MathTex(r"v - v_{0} = a \cdot t")
        base3 = MathTex(r"\frac{v - v_{0}}{a} = t")