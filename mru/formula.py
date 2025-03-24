from manim import *

class mru(Scene):
    def construct(self):
        formula = MathTex(r"v_{m} = \frac{\Delta x}{\Delta t} ").scale(3)

        self.add(formula)