from manim import *

class torriceli(Scene):
    def construct(self):
        mruvHoraria = MathTex(r"S = S_{0} + v_{0} \cdot t) + \frac{(a \cdot t²)}{2}")

        mruvBase = MathTex(r"v = v_{0} + a \cdot t")
        base2 = MathTex(r"v - v_{0} = a \cdot t")
        base3 = MathTex(r"\frac{v - v_{0}}{a} = t")
        base4 = MathTex(r"t = \frac{v - v_{0}}{a}")
        
        mruv2 = MathTex(r"S = S_{0} + v_{0} \cdot \frac{v - v_{0}}{a} + \frac{a}{2} \cdot (\frac{v - v_{0}}{a})^2")
        
        self.add(mruv2)