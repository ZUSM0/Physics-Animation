from manim import *

class torriceli(Scene):
    def construct(self):      
        trapezio = MathTex(r"A = \frac{(B + b) \cdot h}{2}").scale(1.75)

        self.add(trapezio)