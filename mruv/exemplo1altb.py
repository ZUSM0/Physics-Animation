from manim import *

class altb(Scene):
    def construct(self):
        formulaPrincipal = MathTex(r"v = 15 + 20 \cdot t ").scale(1.75).shift(ORIGIN)

        formula1 = MathTex(r"v = 15 + 20 \cdot 4").scale(1.75).shift(ORIGIN)
        formula2 = MathTex(r"v = 15 + 80").scale(1.75).shift(ORIGIN)
        formula3 = MathTex(r"v = 95 m/s ").scale(1.75).shift(ORIGIN)

        self.play(Write(formulaPrincipal))
        self.wait(1)
        self.play(TransformMatchingShapes(formulaPrincipal, formula1), run_time=2)
        self.wait(1)
        self.play(TransformMatchingShapes(formula1, formula2), run_time=2)
        self.wait(1)
        self.play(TransformMatchingShapes(formula2, formula3), run_time=2)

        self.wait(3)

        self.remove(formula3)
        self.wait(1)

        formulac1 = MathTex(r"225 = 15 + 20 \cdot t ").scale(1.75).shift(ORIGIN)
        formulac2 = MathTex(r"225 - 15 = 20 \cdot t ").scale(1.75).shift(ORIGIN)
        formulac3 = MathTex(r"210 = 20 \cdot t ").scale(1.75).shift(ORIGIN)
        formulac3 = MathTex(r"\frac{210}{20} = t ").scale(1.75).shift(ORIGIN)
        formulac4 = MathTex(r"10.5 = t ").scale(1.75).shift(ORIGIN)
        formulac5 = MathTex(r"t = 10.5 s ").scale(1.75).shift(ORIGIN)

        self.play(Write(formulaPrincipal), run_time=2)
        self.wait(1)
        self.play(TransformMatchingShapes(formulaPrincipal, formulac1), run_time=2)
        self.wait(1)
        self.play(TransformMatchingShapes(formulac1, formulac2), run_time=2)
        self.wait(1)
        self.play(TransformMatchingShapes(formulac2, formulac3), run_time=2)
        self.wait(1)
        self.play(TransformMatchingShapes(formulac3, formulac4), run_time=2)
        self.wait(1)
        self.play(TransformMatchingShapes(formulac4, formulac5), run_time=2)

        self.wait(5)