from manim import *

class mruv(Scene):
    def construct(self):
        formula = MathTex(r"\frac{\Delta v}{\Delta t} = a").scale(2)
        formvelo = MathTex(r"\Delta v = v - v_{0}").scale(2).shift(DOWN*0.8)
        
        formula2 = MathTex(r"\frac{v - v_{0}}{\Delta t} = a").scale(2).shift(ORIGIN)
        formula3 = MathTex(r"\frac{v - v_{0}}{\Delta t} \cdot t = a \cdot t").scale(2)
        formula4 = MathTex(r"v - v_{0} = a \cdot t ").scale(2)
        formula5 = MathTex(r"v = v_{0} + a \cdot t ").scale(2)

        self.play(Write(formula), run_time=2)
        self.wait(3)
        self.play(Write(formvelo))
        self.play(TransformMatchingShapes(Group(formula, formvelo), formula2), run_time=2)
        self.wait(1)
        self.play(TransformMatchingShapes(formula2, formula3), run_time=2)
        self.wait(1)
        self.play(TransformMatchingShapes(formula3, formula4), run_time=2)
        self.wait(1)


        self.play(TransformMatchingShapes(formula4, formula5), run_time=2)

        self.wait(5)