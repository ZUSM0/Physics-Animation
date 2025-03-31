from manim import *

class torriceli(Scene):
    def construct(self):
        formula = MathTex(r"v_{m} = \frac{\Delta s}{\Delta t} ").scale(3)

        vm = MathTex(r"V_{m} = \rfrac{(V_{0} + v)}{2}").scale(2)

        self.add(vm)        