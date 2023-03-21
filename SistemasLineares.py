from manim import *

config.max_files_cached = 1000
config.background_color = WHITE


class Cramer(Scene):
    def construct(self):
        ex2 = Matrix([["4x_{1} - x_{2} + x_{3} = 8"], 
                          ["2x_{1} + 5x_{2} + 2x_{3} = 3"],
                          ["x_{1} + 2x_{2} + 4x_{3} = 11"]],
                         left_bracket="\\{",
                         right_bracket="}"
                         )

        sistema_formal = Matrix([["a_{11}x_{1} + a_{12}x_{2} + ... + a_{1n}x_{n} = b_{1}"], 
                          ["a_{12}x_{1} + a_{22}x_{2} + ... + a_{2n}x_{n} = b_{2}"],
                          [r"\vdots"],
                          ["a_{m1}x_{1} + a_{m2}x_{2} + ... + a_{mn}x_{n} = b_{m}"]],
                         left_bracket="\\{",
                         right_bracket="}"
                         ).set_color(BLACK)
        
        sistema_formal.generate_target()
        sistema_formal.target.scale(0.7)
        sistema_formal.target.to_corner(UL)

        
        matriz_formal = MathTex(
            r"\left(\begin{array}{cc}a_{11} + a_{12} + ... + a_{1n}\\ a_{12} + a_{22} + ... + a_{2n}\\ \vdots\\ a_{m1} + a_{m2} + ... + a_{mn}\end{array}\right)",
            r"\times",
            r"\left(\begin{array}{cc}x_{1}\\ \vdots\\ x_n\end{array}\right)",
            r" = ",
            r"\left(\begin{array}{cc}b_{1}\\ \vdots\\ b_n\end{array}\right)"
        ).scale(0.8).set_color(BLACK)

        matriz_a1 = MathTex(
            r"A_{1} = "
            r"\left(\begin{array}{cc}b_{1} + a_{12} + ... + a_{1n}\\ b_{2} + a_{22} + ... + a_{2n}\\ \vdots\\ b_{n} + a_{m2} + ... + a_{mn}\end{array}\right)",
        ).scale(0.8).set_color(BLACK)

        matriz_a2 = MathTex(
            r"A_{2} = "
            r"\left(\begin{array}{cc}a_{11} + b_{1} + ... + a_{1n}\\ a_{12} + b_{2} + ... + a_{2n}\\ \vdots\\ a_{m1} + b_{n} + ... + a_{mn}\end{array}\right)",
        ).scale(0.8).set_color(BLACK)

        #Parte 1 - Monta um sistema generico
        self.play(Create(sistema_formal), run_time = 3)
        self.wait(2)
        self.play(MoveToTarget(sistema_formal))
        self.wait()

        #Parte 2 - Agrupa o sistema acima na tela 
        arr = Arrow(start = LEFT, end = RIGHT, stroke_width= 2).next_to(sistema_formal, buff = 1.5).set_color(BLACK)
        generico = Text('Ax = b', font_size= 32).next_to(arr, buff= 1.5).set_color(BLACK)
        self.play(GrowArrow(arr))
        self.wait()
        self.play(Write(generico))
        self.wait()
        matriz_formal.next_to(VGroup(sistema_formal, arr, generico), DOWN, buff= 1.5)

        #Parte 3 - Cria sistema na forma matricial
        self.play(Create(matriz_formal), run_time = 7)
        self.wait(3)

        #Parte 4 - Agrupa forma matricial acima na tela
        matriz_formal.generate_target()
        matriz_formal.target.move_to([0, 2.5, 0])
        self.play(FadeOut(VGroup(sistema_formal, arr, generico)))
        self.play(MoveToTarget(matriz_formal))
        self.wait(2)

        #Parte 5 - Explica primeiro passo do metodo
        passo_1 = Tex(r"1) Gerar n matrizes $A_{i}$, onde a coluna i é substituída por b.", font_size= 34).next_to(matriz_formal, DOWN, buff= 1.1).set_color(BLACK)
        matrizes = VGroup(matriz_a1, matriz_a2).arrange(buff= 2).next_to(passo_1, DOWN, buff= 1.1)

        self.play(Write(passo_1))
        self.wait(3)
        self.play(Create(matriz_a1), run_time= 5)
        self.wait(2)
        self.play(Create(matriz_a2), run_time= 5)
        self.wait(2)

        #Parte 6 - Explica segundo passo do metodo
        passo_2 = Tex(r"2) Calcular o valor das variáveis pelo método $x_{i} = \frac{det A_{i}}{det A}$.", font_size= 36).next_to(matriz_formal, DOWN, buff= 0.5).set_color(BLACK)
        eq = Tex(r"$x_{1}$ = ", font_size= 48).move_to([-3, -2, 0]).set_color(BLACK)
        div = Line(start= eq.get_right(), end= [4, -2, 0], buff= 0.5).set_color(BLACK)

        formal_copy = Matrix([["a_{11} + a_{12} + ... + a_{1n}"], 
                          ["a_{12} + a_{22} + ... + a_{2n}"],
                          [r"\vdots"],
                          ["a_{m1} + a_{m2} + ... + a_{mn}"]],
                         ).copy().next_to(div, UP, buff= -0.5).scale(0.5).set_color(BLACK)
        det = get_det_text(formal_copy, initial_scale_factor= 1).set_color(BLACK)
        det2 = det.copy().next_to(det, DOWN, buff= 0.5).set_color(BLACK)

        self.play(FadeOut(VGroup(passo_1, matrizes)))
        self.wait()
        self.play(Write(passo_2))
        self.wait(3)
        self.play(Write(eq))
        self.play(Create(div))
        self.play(Create(det))
        self.play(Create(formal_copy))
        self.play(Create(det2))
        self.play(Create(formal_copy.copy().next_to(formal_copy, DOWN, buff= 0.5)))
        self.wait(5)

        new_column = Matrix([["b_{1} + a_{12} + ... + a_{1n}"], 
                          ["b_{2} + a_{22} + ... + a_{2n}"],
                          [r"\vdots"],
                          ["b_{n} + a_{m2} + ... + a_{mn}"]],
                         ).copy().next_to(div, UP, buff= -0.5).scale(0.5).set_color(BLACK)
        
        aux = Rectangle(width=0.5, height= 1.5).move_to([-0.2, -0.75, 0])
        ret = SurroundingRectangle(aux).set_color(PURE_RED)
        self.play(FadeTransform(formal_copy, new_column))
        self.play(Create(ret))
        self.wait(5)

class Gauss(Scene):
    def construct(self):
        matriz_a_inicial = Matrix([["a_{11}", "a_{12}", "a_{13}", "a_{14}"],
                                ["a_{21}", "a_{22}", "a_{23}", "a_{24}"],
                                ["a_{31}", "a_{32}", "a_{33}", "a_{34}"],
                                ["a_{41}", "a_{42}", "a_{43}", "a_{44}"]],
                                left_bracket="(",
                                right_bracket=")").set_color(BLACK)
        
        mult = Tex(r"$\times$", font_size= 32).set_color(BLACK)
        
        matriz_x_inicial = Matrix([["x_{1}"],
                                ["x_{2}"],
                                ["x_{3}"],
                                ["x_{4}"]],
                                left_bracket="(",
                                right_bracket=")").set_color(BLACK)
        
        equals = Tex(r" = ", font_size= 32).set_color(BLACK)
        
        matriz_b_inicial = Matrix([["b_{1}"],
                                ["b_{2}"],
                                ["b_{3}"],
                                ["b_{4}"]],
                                left_bracket="(",
                                right_bracket=")").set_color(BLACK)
        
        forma_matricial = VGroup(matriz_a_inicial, mult, matriz_x_inicial, equals, matriz_b_inicial).arrange(buff= SMALL_BUFF).move_to([0, -2, 0]).scale(0.8)
        
        triangular_superior = Matrix([["a_{11}", "a_{12}", "a_{13}", "a_{14}"],
                                      ["0", "a_{22}", "a_{23}", "a_{24}"],
                                      ["0", "0", "a_{33}", "a_{34}"],
                                      ["0", "0", "0", "a_{44}"]],
                                      left_bracket="(",
                                      right_bracket=")").set_color(BLACK).scale(0.8)


        sistema_formal = Matrix([["a_{11}x_{1} + a_{12}x_{2} + a_{13}x_{3} + a_{14}x_{4} = b_{1}"], 
                                ["a_{21}x_{1} + a_{22}x_{2} + a_{23}x_{3} + a_{24}x_{4} = b_{2}"],
                                ["a_{31}x_{1} + a_{32}x_{2} + a_{33}x_{3} + a_{34}x_{4} = b_{3}"],
                                ["a_{41}x_{1} + a_{42}x_{2} + a_{43}x_{3} + a_{44}x_{4} = b_{4}"]],
                                left_bracket="\\{",
                                right_bracket="}"
                                ).set_color(BLACK)
        
        sistema_formal.generate_target()
        sistema_formal.target.scale(0.7)
        sistema_formal.target.to_corner(UL)

        #Parte 1 - Monta um sistema generico
        self.play(Create(sistema_formal), run_time = 3)
        self.wait(2)
        self.play(MoveToTarget(sistema_formal))
        self.wait()

        #Parte 2 - Agrupa o sistema acima na tela 
        arr = Arrow(start = LEFT, end = RIGHT, stroke_width= 4).next_to(sistema_formal, buff = 1.5).set_color(BLACK)
        generico = Text('Ax = b', font_size= 32).next_to(arr, buff= 1.5).set_color(BLACK)
        self.play(GrowArrow(arr))
        self.wait()
        self.play(Write(generico))
        self.wait()

        #Parte 3 - Cria sistema na forma matricial
        self.play(Create(forma_matricial), run_time = 5)
        self.wait(3)

        #Parte 4 - Agrupa forma matricial acima na tela
        forma_matricial.generate_target()
        forma_matricial.target.move_to([0, 2, 0])
        self.play(FadeOut(VGroup(sistema_formal, arr, generico)))
        self.play(MoveToTarget(forma_matricial))
        self.wait(2)

        #Parte 5 - Escalonamento da matriz
        pos_inicial = matriz_a_inicial.get_center()
        passo_1 = Tex(r"1) Triangularização da matriz A:", font_size= 34).next_to(forma_matricial, DOWN, buff= 1.1).set_color(BLACK)
        matriz_a_inicial.generate_target()
        matriz_a_inicial.target.move_to([0, -2.5, 0])
        triangular_superior.move_to(matriz_a_inicial.target)
        arr = Arrow(start = LEFT, end = RIGHT, max_stroke_width_to_length_ratio= 10).next_to(triangular_superior.get_rows()[0].get_left(), buff= -2).set_color(PURE_RED)
        nova_linha_1 = Tex(r"$a_{1}` = a_{1}$", font_size= 32).set_color(PURE_RED).next_to(matriz_a_inicial.target, UP, MED_SMALL_BUFF)
        nova_linha_2 = Tex(r"$a_{2}` = c \times a_{1}` + a_{2}$", font_size= 32).set_color(PURE_RED).next_to(matriz_a_inicial.target, UP, MED_SMALL_BUFF)
        nova_linha_3 = Tex(r"$a_{3}` = c \times a_{2}` + a_{3}$", font_size= 32).set_color(PURE_RED).next_to(matriz_a_inicial.target, UP, MED_SMALL_BUFF)
        nova_linha_4 = Tex(r"$a_{4}` = c \times a_{3}` + a_{4}$", font_size= 32).set_color(PURE_RED).next_to(matriz_a_inicial.target, UP, MED_SMALL_BUFF)

        self.play(MoveToTarget(matriz_a_inicial, path_arc=45 * DEGREES))
        self.wait(2)
        self.play(Write(passo_1))
        self.wait(3)
        self.play(FadeOut(passo_1))
        self.wait()
        self.play(GrowArrow(arr))
        self.wait()
        self.play(Write(nova_linha_1))
        self.wait(3)

        self.play(FadeOut(nova_linha_1))
        self.play(arr.animate.shift(DOWN/1.5))
        self.play(Write(nova_linha_2))
        self.wait()
        self.play(ReplacementTransform(matriz_a_inicial.get_rows()[1], triangular_superior.get_rows()[1]))
        self.wait(3)

        self.play(FadeOut(nova_linha_2))
        self.play(arr.animate.shift(DOWN/1.55))
        self.play(Write(nova_linha_3))
        self.wait()
        ent = matriz_a_inicial.get_entries()
        new_ent = triangular_superior.get_entries()
        self.play(ReplacementTransform(ent[8], new_ent[8]))
        self.wait(3)

        self.play(FadeOut(nova_linha_3))
        self.play(arr.animate.shift(DOWN/1.55))
        self.play(Write(nova_linha_4))
        self.wait()
        self.play(ReplacementTransform(ent[12], new_ent[12]))
        self.wait(3)

        self.play(FadeOut(nova_linha_4))
        self.play(arr.animate.shift(UP/1.55))
        self.play(Write(nova_linha_3))
        self.wait()
        self.play(ReplacementTransform(ent[9], new_ent[9]))
        self.wait(3)

        self.play(FadeOut(nova_linha_3))
        self.play(arr.animate.shift(DOWN/1.55))
        self.play(Write(nova_linha_4))
        self.wait()
        self.play(ReplacementTransform(ent[13], new_ent[13]))
        self.wait()
        self.play(ReplacementTransform(ent[14], new_ent[14]))

        #Parte 6 - Retornar a forma de sistema
        to_elim = VGroup(nova_linha_4, arr)
        matriz_a_final = VGroup(matriz_a_inicial, triangular_superior)
        matriz_a_final.generate_target()
        matriz_a_final.target.move_to(pos_inicial)

        sistema_final = Matrix([["a_{11}x_{1}", "a_{12}x_{1}+", "a_{13}x_{1}+", "a_{14}x_{1}=", "b_{1}"],
                                ["0+", "a_{22}x_{2}+", "a_{23}x_{2}+", "a_{24}x_{2}=", "b_{2}"],
                                ["0+", "0+", "a_{33}x_{3}+", "a_{34}x_{3}=", "b_{3}"],
                                ["0+", "0+", "0+", "a_{44}x_{4}=", "b_{4}"]],
                                left_bracket="\\{",
                                right_bracket="}",
                                h_buff= 1.8).set_color(BLACK)
        
        matricial_final = VGroup(matriz_a_final, mult, matriz_x_inicial, equals, matriz_b_inicial)
        passo_2 = Tex(r"2) Retrossubstituição:", font_size= 34).next_to(matricial_final, DOWN, buff= 1.1).set_color(BLACK)

        self.play(FadeOut(to_elim))
        self.wait()
        self.play(Write(passo_2))
        self.wait(3)
        self.play(FadeOut(passo_2))
        self.play(MoveToTarget(matriz_a_final, path_arc= 90 * DEGREES))
        self.wait(5)
        self.play(FadeTransform(matricial_final, sistema_final))
        self.wait(3)
        ent = sistema_final.get_entries()
        self.play(FadeOut(ent[5], ent[10], ent[11], ent[15], ent[16], ent[17]))
        self.wait(5)

class ALU(Scene):
    def construct(self):
        a = Rectangle(width=2, height=2).set_color(BLACK)
        eqals = Tex(r"=", font_size= 38).set_color(BLACK)
        l = Polygon([0, 2, 0], [0, 0, 0], [2, 0, 0]).set_color(BLACK)
        dot = Dot(radius= 0.075).set_color(BLACK)
        u = Polygon([-2, 2, 0], [0, 2, 0], [0, 0, 0]).set_color(BLACK)

        alu = VGroup(a, eqals, l, dot, u).arrange(buff= 0.5)
        label_a = Text("A", font_size= 32).set_color(BLACK).next_to(a, DOWN)
        label_l = Text("L", font_size= 32).set_color(BLACK).next_to(l, DOWN)
        label_u = Text("U", font_size= 32).set_color(BLACK).next_to(u, DOWN)
        
        matriz_a_inicial = Matrix([["a_{11}", "a_{12}", "a_{13}", "a_{14}"],
                                ["a_{21}", "a_{22}", "a_{23}", "a_{24}"],
                                ["a_{31}", "a_{32}", "a_{33}", "a_{34}"],
                                ["a_{41}", "a_{42}", "a_{43}", "a_{44}"]],
                                left_bracket="(",
                                right_bracket=")").set_color(BLACK)
        
        mult = Tex(r"$\times$", font_size= 32).set_color(BLACK)
        
        matriz_x_inicial = Matrix([["x_{1}"],
                                ["x_{2}"],
                                ["x_{3}"],
                                ["x_{4}"]],
                                left_bracket="(",
                                right_bracket=")").set_color(BLACK)
        
        equals = Tex(r" = ", font_size= 32).set_color(BLACK)
        
        matriz_b_inicial = Matrix([["b_{1}"],
                                ["b_{2}"],
                                ["b_{3}"],
                                ["b_{4}"]],
                                left_bracket="(",
                                right_bracket=")").set_color(BLACK)
        
        forma_matricial = VGroup(matriz_a_inicial, mult, matriz_x_inicial, equals, matriz_b_inicial).arrange(buff= SMALL_BUFF).move_to([0, -2, 0]).scale(0.8)
        
        triangular_superior = Matrix([["u_{11}", "u_{12}", "u_{13}", "u_{14}"],
                                      ["0", "u_{22}", "u_{23}", "u_{24}"],
                                      ["0", "0", "u_{33}", "u_{34}"],
                                      ["0", "0", "0", "u_{44}"]],
                                      left_bracket="(",
                                      right_bracket=")").set_color(BLACK).scale(0.8)


        sistema_formal = Matrix([["a_{11}x_{1} + a_{12}x_{2} + a_{13}x_{3} + a_{14}x_{4} = b_{1}"], 
                                ["a_{21}x_{1} + a_{22}x_{2} + a_{23}x_{3} + a_{24}x_{4} = b_{2}"],
                                ["a_{31}x_{1} + a_{32}x_{2} + a_{33}x_{3} + a_{34}x_{4} = b_{3}"],
                                ["a_{41}x_{1} + a_{42}x_{2} + a_{43}x_{3} + a_{44}x_{4} = b_{4}"]],
                                left_bracket="\\{",
                                right_bracket="}"
                                ).set_color(BLACK)
        
        sistema_formal.generate_target()
        sistema_formal.target.scale(0.7)
        sistema_formal.target.to_corner(UL)

        #Parte 1 - Monta um sistema generico
        self.play(Create(sistema_formal), run_time = 3)
        self.wait(2)
        self.play(MoveToTarget(sistema_formal))
        self.wait()

        #Parte 2 - Agrupa o sistema acima na tela 
        arr = Arrow(start = LEFT, end = RIGHT, stroke_width= 4).next_to(sistema_formal, buff = 1.5).set_color(BLACK)
        generico = Text('Ax = b', font_size= 32).next_to(arr, buff= 1.5).set_color(BLACK)
        self.play(GrowArrow(arr))
        self.wait()
        self.play(Write(generico))
        self.wait()

        #Parte 3 - Cria sistema na forma matricial
        self.play(Create(forma_matricial))
        self.wait(3)

        #Parte 4 - Agrupa forma matricial acima na tela
        forma_matricial.generate_target()
        forma_matricial.target.move_to([0, 2, 0])
        self.play(FadeOut(VGroup(generico, arr, sistema_formal), shift= UP),
                  MoveToTarget(forma_matricial))
        self.wait(2)

        #Parte 5 - Montar matriz U

        triangular_inferior = Matrix([["1", "0", "0", "0"],
                                      ["c_{1}", "1", "0", "0"],
                                      ["c_{2}", "c_{4}", "1", "0"],
                                      ["c_{3}", "c_{5}", "c_{6}", "1"]],
                                      left_bracket="(",
                                      right_bracket=")").set_color(BLACK).scale(0.8).move_to([0, 2.5, 0])
        k = triangular_inferior.get_entries()

        self.play(FadeOut(mult, matriz_x_inicial, equals, matriz_b_inicial, shift= RIGHT),
                  matriz_a_inicial.animate.shift(RIGHT * 1.5))
        self.wait()
        u_inicial = matriz_a_inicial.copy()
        u_inicial.generate_target()
        u_inicial.target.move_to([0, -2, 0])
        self.play(MoveToTarget(u_inicial),
                FadeOut(matriz_a_inicial))
        self.wait()

        passo_1 = Tex(r"1) Criação da matriz U a partir de A:", font_size= 34).next_to(u_inicial, UP, buff= 1.1).set_color(BLACK)
        triangular_superior.move_to(u_inicial.target)
        arr = Arrow(start = LEFT, end = RIGHT, max_stroke_width_to_length_ratio= 10).next_to(triangular_superior.get_rows()[0].get_left(), buff= -2).set_color(PURE_RED)
        nova_linha_1 = Tex(r"$u_{1} = a_{1}$", font_size= 32).set_color(PURE_RED).next_to(u_inicial.target, UP, MED_SMALL_BUFF)
        nova_linha_2 = Tex(r"$u_{2} = c \times u_{1} + a_{2}$", font_size= 32).set_color(PURE_RED).next_to(u_inicial.target, UP, MED_SMALL_BUFF)
        nova_linha_3 = Tex(r"$u_{3} = c \times u_{2} + a_{3}$", font_size= 32).set_color(PURE_RED).next_to(u_inicial.target, UP, MED_SMALL_BUFF)
        nova_linha_4 = Tex(r"$u_{4} = c \times u_{3} + a_{4}$", font_size= 32).set_color(PURE_RED).next_to(u_inicial.target, UP, MED_SMALL_BUFF)
        ent = u_inicial.get_entries()
        new_ent = triangular_superior.get_entries()

        self.play(Write(passo_1))
        self.wait(3)
        self.play(FadeOut(passo_1))
        self.wait()
        self.play(GrowArrow(arr))
        self.wait()
        self.play(Write(nova_linha_1))
        self.play(ReplacementTransform(u_inicial.get_rows()[0], triangular_superior.get_rows()[0]))
        self.wait()

        self.play(FadeOut(nova_linha_1))
        self.play(arr.animate.shift(DOWN/1.5))
        self.play(Write(nova_linha_2))
        self.wait()
        self.play(ReplacementTransform(u_inicial.get_rows()[1], triangular_superior.get_rows()[1]))
        self.wait()

        arr_2 = Arrow(start= UP, end= DOWN).move_to([-0.3, 0.6, 0]).set_color(BLACK)
        constant = Tex(r"$c_{1}$", font_size= 32).set_color(BLACK).next_to(arr_2, DOWN, buff= 0.2)
        constant.generate_target()
        constant.target.move_to(k[4])
        self.wait()
        self.play(GrowArrow(arr_2))
        self.wait()
        self.play(MoveToTarget(constant, path_arc= 30 * DEGREES))

        self.play(FadeOut(nova_linha_2, arr_2))
        self.play(arr.animate.shift(DOWN/1.55))
        self.play(Write(nova_linha_3))
        self.wait()
        self.play(ReplacementTransform(ent[8], new_ent[8]),
                  ReplacementTransform(ent[10], new_ent[10]),
                  ReplacementTransform(ent[11], new_ent[11]))
        
        arr_2 = Arrow(start= UP, end= DOWN).move_to([-0.3, 0.6, 0]).set_color(BLACK)
        constant_2 = Tex(r"$c_{2}$", font_size= 32).set_color(BLACK).next_to(arr_2, DOWN, buff= 0.2)
        constant_2.generate_target()
        constant_2.target.move_to(k[8])
        self.wait()
        self.play(GrowArrow(arr_2))
        self.wait()
        self.play(MoveToTarget(constant_2, path_arc= 30 * DEGREES))

        self.play(FadeOut(nova_linha_3, arr_2))
        self.play(arr.animate.shift(DOWN/1.55))
        self.play(Write(nova_linha_4))
        self.wait()
        self.play(ReplacementTransform(ent[12], new_ent[12]),
                  ReplacementTransform(ent[15], new_ent[15]))
        
        arr_2 = Arrow(start= UP, end= DOWN).move_to([-0.3, 0.6, 0]).set_color(BLACK)
        constant_3 = Tex(r"$c_{3}$", font_size= 32).set_color(BLACK).next_to(arr_2, DOWN, buff= 0.2)
        constant_3.generate_target()
        constant_3.target.move_to(k[12])
        self.wait()
        self.play(GrowArrow(arr_2))
        self.wait()
        self.play(MoveToTarget(constant_3, path_arc= 30 * DEGREES))

        self.play(FadeOut(nova_linha_4, arr_2))
        self.play(arr.animate.shift(UP/1.55))
        self.play(Write(nova_linha_3))
        self.wait()
        self.play(ReplacementTransform(ent[9], new_ent[9]))

        arr_2 = Arrow(start= UP, end= DOWN).move_to([-0.3, 0.6, 0]).set_color(BLACK)
        constant_4 = Tex(r"$c_{4}$", font_size= 32).set_color(BLACK).next_to(arr_2, DOWN, buff= 0.2)
        constant_4.generate_target()
        constant_4.target.move_to(k[9])
        self.wait()
        self.play(GrowArrow(arr_2))
        self.wait()
        self.play(MoveToTarget(constant_4, path_arc= 30 * DEGREES))

        self.play(FadeOut(nova_linha_3, arr_2))
        self.play(arr.animate.shift(DOWN/1.55))
        self.play(Write(nova_linha_4))
        self.wait()
        self.play(ReplacementTransform(ent[13], new_ent[13]))
        self.play(ReplacementTransform(ent[14], new_ent[14]))

        arr_2 = Arrow(start= UP, end= DOWN).move_to([-0.3, 0.6, 0]).set_color(BLACK)
        constant_5 = Tex(r"$c_{5}$", font_size= 32).set_color(BLACK).next_to(arr_2, DOWN, buff= 0.2)
        constant_6 = Tex(r"$c_{6}$", font_size= 32).set_color(BLACK).next_to(arr_2, DOWN, buff= 0.2)
        constant_5.generate_target()
        constant_6.generate_target()
        constant_5.target.move_to(k[13])
        constant_6.target.move_to(k[14])
        self.wait()
        self.play(GrowArrow(arr_2))
        self.wait()
        self.play(MoveToTarget(constant_5, path_arc= 30 * DEGREES))
        self.play(MoveToTarget(constant_6, path_arc= 30 * DEGREES))
        self.play(FadeOut(nova_linha_4, arr, arr_2))
        self.wait(3)


        self.play(FadeIn(k[0], k[5], k[10], k[15]))
        self.wait()
        self.play(FadeIn(k[1], k[2], k[3], k[6], k[7], k[11]))
        self.play(Create(triangular_inferior.get_brackets()))
        self.wait()

        u = Text("U = ", font_size= 38).next_to(u_inicial, LEFT).set_color(BLACK)
        l = Text("L = ", font_size= 38).next_to(triangular_inferior, LEFT).set_color(BLACK)
        self.play(Write(u))
        self.play(Write(l))
        self.wait(2)

        self.play(FadeOut(u, l))
        matriz_u = VGroup(u_inicial, triangular_superior)
        matriz_u.generate_target()
        matriz_u.target.next_to(triangular_inferior, RIGHT, buff= SMALL_BUFF)
        self.play(MoveToTarget(matriz_u, path_arc= 90 * DEGREES))
        self.wait()
        matriz_a_inicial.next_to(triangular_inferior, LEFT, buff= 0.5)
        eqals.next_to(matriz_a_inicial, RIGHT, buff= SMALL_BUFF)
        self.play(FadeIn(matriz_a_inicial, eqals, shift= RIGHT))
        self.wait(5)


        #Parte 6 - Resolver sistema Ly=b
        alu_text = Text("A = LU", font_size= 42).set_color(BLACK).to_corner(UL)
        ly  = Text("2) Resolver o sistema Ly = b", font_size= 32).set_color(BLACK).move_to([0, 2, 0])
        alu = VGroup(matriz_a_inicial, eqals, triangular_inferior, matriz_u, constant, constant_2, constant_3, constant_4, constant_5, constant_6)
        matriz_y = Matrix([["y_{1}"],
                            ["y_{2}"],
                            ["y_{3}"],
                            ["y_{4}"]],
                            left_bracket="(",
                            right_bracket=")").set_color(BLACK).scale(0.8)

        self.wait()
        self.play(FadeOut(alu, shift= UP))
        self.wait()
        self.play(Write(ly))
        self.wait(3)

        triangular_inferior0 = Matrix([["1", "0", "0", "0"],
                                      ["c_{1}", "1", "0", "0"],
                                      ["c_{2}", "c_{4}", "1", "0"],
                                      ["c_{3}", "c_{5}", "c_{6}", "1"]],
                                      left_bracket="(",
                                      right_bracket=")").set_color(BLACK).scale(0.8)
        lyb = VGroup(triangular_inferior0, matriz_y, equals, matriz_b_inicial).arrange().next_to(ly, DOWN, buff= 2)
        sistema_lyb = Matrix([["1y_{1} + 0y_{2} + 0y_{3} + 0y_{4} = b_{1}"], 
                                ["c_{1}y_{1} + 1y_{2} + 0y_{3} + 0y_{4} = b_{2}"],
                                ["c_{2}y_{1} + c_{4}y_{2} + 1y_{3} + 0y_{4} = b_{3}"],
                                ["c_{3}y_{1} + c_{5}y_{2} + c_{6}y_{3} + 1y_{4} = b_{4}"]],
                                left_bracket="\\{",
                                right_bracket="}"
                                ).set_color(BLACK).move_to(lyb)
        self.play(Create(lyb))
        self.wait(3)
        self.play(FadeTransform(lyb, sistema_lyb))
        self.wait(5)
        matriz_y.next_to(ly, DOWN, buff= 2)
        self.play(FadeTransform(sistema_lyb, matriz_y))

        #Parte 7 - Resolver sistema Ux = b
        ux  = Text("3) Resolver o sistema Ux = y", font_size= 32).set_color(BLACK).move_to([0, 2, 0])

        sistema_uxy = Matrix([["u_{11}x_{1} + u_{12}x_{2} + u_{13}x_{3} + u_{14}x_{4} = y_{1}"], 
                                ["0x_{1} + u_{22}x_{2} + u_{23}x_{3} + u_{24}x_{4} = y_{2}"],
                                ["0x_{1} + 0x_{2} + u_{33}x_{3} + u_{34}x_{4} = y_{3}"],
                                ["0x_{1} + 0x_{2} + 0x_{3} + u_{44}x_{4} = y_{4}"]],
                                left_bracket="\\{",
                                right_bracket="}"
                                ).set_color(BLACK).move_to(lyb)


        self.play(FadeOut(ly))
        self.play(Write(ux))
        self.wait(3)
        self.play(matriz_y.animate.shift(RIGHT*3.5))
        eq = Text("=", font_size= 48).next_to(matriz_y, LEFT).set_color(BLACK)
        x = matriz_x_inicial.copy().next_to(eq, LEFT)
        u = triangular_superior.copy().next_to(x, LEFT)
        self.play(Create(u),
                  Create(x),
                  Create(eq))
        self.wait(5)
        self.play(FadeTransform(VGroup(matriz_y, eq, x, u), sistema_uxy))
        self.wait(5)

class Cramer_ex2(Scene):
    def construct(self):
        sistema = Matrix([["4x_{1} - x_{2} + x_{3} = 8"], 
                          ["2x_{1} + 5x_{2} + 2x_{3} = 3"],
                          ["x_{1} + 2x_{2} + 4x_{3} = 11"]],
                         left_bracket="\\{",
                         right_bracket="}"
                         ).set_color(BLACK).move_to([0, 0, 0])
        
        matriz_a = Matrix([["4", "-1", "1"],
                            ["2", "5", "2"],
                            ["1", "2", "4"]],
                            left_bracket="(",
                            right_bracket=")").set_color(BLACK).scale(0.8).move_to([-2, 2, 0])
        
        matriz_ai = Matrix([["4", "-1", "8"],
                            ["2", "5", "3"],
                            ["1", "2", "11"]],
                            left_bracket="(",
                            right_bracket=")").set_color(BLACK).scale(0.8).move_to([-2, -2, 0])
        
        det_a = get_det_text(matriz_a, determinant= 69, initial_scale_factor= 1).set_color(BLACK)
        det_ai = get_det_text(matriz_ai, determinant= 207, initial_scale_factor= 1).set_color(BLACK)
        result = MathTex(r"x_{3} = \frac{207}{69} = 3", font_size= 48).set_color(BLACK).move_to([3, 0, 0])
        self.play(FadeIn(MathTex(r"A = ", font_size= 48).set_color(BLACK).next_to(det_a, LEFT)))
        self.play(FadeIn(MathTex(r"A_{3} = ", font_size= 48).set_color(BLACK).next_to(det_ai, LEFT)))
        self.play(FadeIn(matriz_a))
        self.wait()
        self.play(FadeIn(det_a))
        self.wait()
        self.play(FadeIn(matriz_ai))
        self.wait()
        self.play(FadeIn(det_ai))
        self.wait(2)
        self.play(Write(result))
        self.wait(3)

class Gauss_ex2(Scene):
    def construct(self):
        matriz_a = Matrix([["4", "-1", "1"],
                            ["2", "5", "2"],
                            ["1", "2", "4"]],
                            left_bracket="(",
                            right_bracket=")").set_color(BLACK)
        matriz_a_meio = Matrix([["4", "-1", "1"],
                                ["0", "11/2", "3/2"],
                                ["0", "9/4", "15/4"]],
                                left_bracket="(",
                                right_bracket=")").set_color(BLACK).move_to(matriz_a)
        matriz_a_final = Matrix([["4", "-1", "1"],
                                ["0", "11/2", "3/2"],
                                ["0", "0", "69/22"]],
                                left_bracket="(",
                                right_bracket=")").set_color(BLACK).move_to(matriz_a)
        
        a = Text("A = ", font_size= 48).next_to(matriz_a, LEFT).set_color(BLACK)
        self.wait()
        self.play(FadeIn(a))
        self.play(FadeIn(matriz_a))
        self.wait()
        arr = Arrow(start = LEFT, end = RIGHT, max_stroke_width_to_length_ratio= 10).next_to(matriz_a.get_rows()[0].get_left(), buff= -2).set_color(BLACK)
        self.play(FadeOut(a))
        self.play(GrowArrow(arr))
        eq1 = Tex(r"$a_{1}` = a_{1}$", font_size= 32).set_color(BLACK).next_to(matriz_a, UP, MED_SMALL_BUFF)
        eq_2 = Tex(r"$a_{2}` = \frac{-1}{2} \times a_{1}` + a_{2}$", font_size= 32).set_color(BLACK).next_to(matriz_a, UP, MED_SMALL_BUFF)
        eq_3 = Tex(r"$a_{3}` = \frac{-1}{4} \times a_{1}` + a_{3}$", font_size= 32).set_color(BLACK).next_to(matriz_a, UP, MED_SMALL_BUFF)
        eq_4 = Tex(r"$a_{3}` = \frac{-9}{22} \times a_{2}` + a_{3}$", font_size= 32).set_color(BLACK).next_to(matriz_a, UP, MED_SMALL_BUFF)

        self.play(FadeIn(eq1))
        self.wait()
        self.play(FadeOut(eq1))
        self.play(arr.animate.shift(DOWN/1.5))
        self.play(Write(eq_2))
        self.wait()
        self.play(ReplacementTransform(matriz_a.get_rows()[1], matriz_a_meio.get_rows()[1]))
        self.wait(3)

        self.play(FadeOut(eq_2))
        self.play(arr.animate.shift(DOWN))
        self.play(Write(eq_3))
        self.wait()
        self.play(ReplacementTransform(matriz_a.get_rows()[2], matriz_a_meio.get_rows()[2]))
        self.wait(3)

        self.play(FadeOut(eq_3))
        self.wait()
        self.play(FadeIn(eq_4))
        self.play(ReplacementTransform(matriz_a_meio.get_rows()[2], matriz_a_final.get_rows()[2]))
        self.wait()
        self.play(FadeOut(eq_4, arr))
        self.wait(5)
