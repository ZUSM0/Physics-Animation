from manim import *

class deducaoVelocidadeMedia(Scene):
    def construct(self):
        position = MathTex(r"\Delta S = \frac{(v_{0} + v_{f}) \cdot \Delta t}{2}").scale(1.75).shift(UP*1)
        
        vm2 = MathTex(r"V_{m} \cdot \Delta t = \Delta S").scale(1.75)                 
        vm2.shift(DOWN*1)

        formula = MathTex(r"V_{m} \cdot \Delta t = \frac{(v_{0} + v_{f}) * \Delta t}{2")
        formula2 = MathTex(r"V_{m} = \frac{(v_{0} + v_{f})}{2")

        self.play(Write(position))
        self.play(Write(vm2))

        self.play(TransformMatchingShapes(Group(position, vm2), formula))
        self.play(TransformMatchingShapes(formula, formula2))

        self.wait(3)