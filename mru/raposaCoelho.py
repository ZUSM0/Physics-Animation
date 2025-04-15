from manim import *

class raposaCoelho(Scene):
    def construct(self):
        enunciado = MarkupText("Uma raposa encontra-se a 100 m de um coelho, perseguindo-0. Sabendo que as velocidades da raposa e do coelho valem, respectivamente, 72 km/h e 54 km/h, responda: Quanto tempo dura essa bem-sucedida perseguição?").shift(UP*3).scale_to_fit_width(config["frame_width"]*0.75).scale(1.3)

        self.add(enunciado) # Tem que ser Write


        raposa = ImageMobject("imagens\carro.png")
        raposa.scale(0.7).shift(DOWN*2+LEFT*5)

        coelho = ImageMobject("imagens\pessoa.jpg")
        coelho.scale(0.5).shift(DOWN*2+ RIGHT*2.7)
        self.add(raposa, coelho)


        vector1 = Vector([2, 0])
        vector2 = Vector([1.5, 0])

        vector1.next_to(raposa, RIGHT)
        veloRaposa = MathTex(r"72 Km/h").scale(1).next_to(vector1, UP)

        vector2.next_to(coelho, RIGHT)
        veloCoelho = MathTex(r"54 Km/h").scale(1).next_to(vector2, UP).shift(RIGHT*0.3)

        self.add(vector1) # Tem que ser Fadein
        self.add(veloRaposa) # tem que ser Write 

        self.add(vector2) # tem que ser Fadein
        self.add(veloCoelho) # tem que ser Write