from manim import *

class raposaCoelho(Scene):
    def construct(self):
        enunciado = MarkupText("Uma raposa encontra-se a 100 m de um coelho, perseguindo-0. Sabendo que as velocidades da raposa e do coelho valem, respectivamente, 72 km/h e 54 km/h, responda: Quanto tempo dura essa bem-sucedida perseguição?").shift(UP*3).scale_to_fit_width(config["frame_width"]*0.75).scale(1.3)

        self.add(enunciado) # Tem que ser Write

        raposa = ImageMobject("imagens\Raposa.png")
        raposa.scale(1.1).shift(DOWN*2+LEFT*5)

        coelho = ImageMobject("imagens\coelho.jpg")
        coelho.scale(0.43).shift(DOWN*2.2+ RIGHT*2.7)
        
        self.play(FadeIn(raposa), run_time=1.75)
        self.play(FadeIn(coelho), run_time=1.85)

        vector1 = Vector([2, 0])
        vector2 = Vector([1.5, 0])

        vector1.next_to(raposa, RIGHT).shift(DOWN*0.3)
        veloRaposa = MathTex(r"72 Km/h").scale(1).next_to(vector1, UP).shift(DOWN*0.125)

        vector2.next_to(coelho, RIGHT).shift(DOWN*0.3)
        veloCoelho = MathTex(r"54 Km/h").scale(1).next_to(vector2, UP).shift(RIGHT*0.3).shift(DOWN*0.1)

        self.play(FadeIn(vector1), run_time=1.75) 
        self.play(Write(veloRaposa), run_time=1.75)  

        self.play(FadeIn(vector2), run_time=1.75) 
        self.play(Write(veloCoelho), run_time=1.75) 

        distancia = Line().put_start_and_end_on(LEFT*5, RIGHT*2.7).shift(DOWN*3.1)
        valordistancia = MathTex(r"100 m").next_to(distancia, DOWN)

        self.play(Write(distancia), run_time=1.75) 
        self.play(Write(valordistancia), run_time=1.75)

        # Parte da formula

        formulaRaposa = MathTex(r"S_{r} = 0 + 72 \cdot t").scale(1.15).shift(LEFT*4.5 + DOWN*0.2)

        formulaCoelho = MathTex(r"S_{c} = 100 + 54 \cdot t").scale(1.15).shift(RIGHT*3.2 + DOWN*0.2)

        self.play(Write(formulaRaposa), run_time=2.75)
        self.play(Write(formulaCoelho), run_time=2.75)

        veloRaposa2 = MathTex(r"\frac{72}{3.6}").scale(1).next_to(vector1, UP).shift(DOWN*0.125)
        veloCoelho2 = MathTex(r"\frac{54}{3.6}").scale(1).next_to(vector2, UP).shift(RIGHT*0.3).shift(DOWN*0.1)
        veloRaposa3 = MathTex(r"20 m/s").scale(1).next_to(vector1, UP).shift(DOWN*0.125)
        veloCoelho3 = MathTex(r"15 m/s").scale(1).next_to(vector2, UP).shift(RIGHT*0.3).shift(DOWN*0.1)

        self.play(TransformMatchingShapes(veloRaposa, veloRaposa2), run_time=2.5)
        self.play(TransformMatchingShapes(veloRaposa2, veloRaposa3), run_time=2.5)

        self.play(TransformMatchingShapes(veloCoelho, veloCoelho2), run_time=2.5)
        self.play(TransformMatchingShapes(veloCoelho2, veloCoelho3), run_time=2.5)

        formulaRaposa2 = MathTex(r"S_{r} = 0 + 20 \cdot t").scale(1.15).shift(LEFT*4.5 + DOWN*0.2)

        formulaCoelho2 = MathTex(r"S_{c} = 100 + 15 \cdot t").scale(1.15).shift(RIGHT*3.2 + DOWN*0.2)

        self.play(TransformMatchingTex(formulaRaposa, formulaRaposa2), run_time=2.5)
        self.play(TransformMatchingTex(formulaCoelho, formulaCoelho2), run_time=2.5) 

        igualar = MathTex(r"S_{r} = S_{c}").scale(1.15).shift(UP*1.5+LEFT*0.7)
        formularc = MathTex(r"20 \cdot t = 100 + 15 \cdot t").scale(1.15).shift(UP*1.5+LEFT*0.7)

        self.play(Write(igualar), run_time=2)
        self.wait(1.75)

        self.play(TransformMatchingShapes(Group(formulaRaposa2, igualar, formulaCoelho2),formularc), run_time=2.5)

        formularc1 = MathTex(r"20 \cdot t - 15 \cdot t = 100").scale(1.15).next_to(formularc, DOWN)
        formularc2 = MathTex(r"5 \cdot t = 100").scale(1.15).next_to(formularc, DOWN)

        self.play(Write(formularc1), run_time=2.5)
        self.play(TransformMatchingShapes(formularc1, formularc2), run_time=2.5)

        formularc3 = MathTex(r"t = \frac{100}{5}").scale(1.15).next_to(formularc1, DOWN)
        resultado = MathTex(r"t = 20 segundos").scale(1.15).next_to(formularc1, DOWN)
        
        self.play(Write(formularc3), run_time=2.5)
        self.play(TransformMatchingShapes(formularc3, resultado), run_time=2.5)

        self.wait(2)