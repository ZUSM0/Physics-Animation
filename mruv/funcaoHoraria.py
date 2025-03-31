from manim import *

class funcaoHoraria(Scene):
    def construct(self):
        velocidade = MathTex(r"v = ").scale(1.75).shift(UP*1)
        vm = MathTex(r"V_{m} = \frac{(v_{0} + v)}{2").scale(1.75).shift(DOWN*1)

        formula = MathTex(r"V_{m} = \frac{(v_{0} + v_{0} + a \cdot t)}{2}").scale(1.75)

        formula2 = MathTex(r"V_{m} = \frac{(2v_{0} + a \cdot t)}{2}").scale(1.75)

        position = MathTex(r"ΔS = v_{m} \cdot t").scale(1.75)
        
        formula3 = MathTex(r"ΔS = \frac{(2v_{0} + a \cdot t)}{2} \cdot t").scale(1.75)
        
        formula4 = MathTex(r"ΔS = \frac{(2v_{0} \cdot t)}{2} + \frac{(a * t²)}{2}")

        formula5 = MathTex(r"ΔS = v_{0} \cdot t) + \frac{(a * t²)}{2}")

        formula6 = MathTex(r"S - S_{0} = v_{0} \cdot t) + \frac{(a * t²)}{2}")

        formula7 = MathTex(r"S = S_{0} + v_{0} \cdot t) + \frac{(a * t²)}{2}")

        self.play(Write(velocidade))
        self.play(Write(vm))

        self.play(TransformMatchingShapes(Group(velocidade, vm), formula))
