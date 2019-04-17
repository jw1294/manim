#########################################################################################
###
### IMPORTS
###
#########################################################################################


from big_ol_pile_of_manim_imports import *


#########################################################################################
###
### UTILITIES
###
#########################################################################################


class Struct():
    pass


def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False


#########################################################################################
###
### SECTION 1.1
###
#########################################################################################


class Title(Scene):

    def initialise(self):
        self.line1=TextMobject("An Introduction to Machine Learning Methods")
        self.line2=TextMobject("and their Application to Quantum Mechanical Problems")
        self.line3=TextMobject("Jack Wetherell")
        self.line3.set_color(GREY)
        self.line1.move_to(2*UP)
        self.line2.next_to(self.line1, DOWN)
        self.line3.next_to(self.line2, 4*DOWN)


    def animation1(self):
        self.add(self.line1, self.line2, self.line3)


    def construct(self):

        # initialise
        print('initialising...')
        self.initialise()

        # animation 1
        print('animation 1...')
        self.animation1()
        self.wait(3)


#########################################################################################
###
### SECTION 1.2
###
#########################################################################################


class Quiz(Scene):

    def initialise(self):
        self.image1 = ImageMobject("p1")
        self.image2 = ImageMobject("p2")
        self.image3 = ImageMobject("p3")
        self.image1.move_to(5*LEFT)
        self.image2.next_to(self.image1, 6.5*RIGHT)
        self.image3.next_to(self.image2, 6.5*RIGHT)

        self.cross1_1 = Line(self.image1.get_corner(DOWN+LEFT) + 0.5*DOWN + 0.5*LEFT, self.image1.get_corner(UP+RIGHT) + 0.5*UP + 0.5*RIGHT, color=RED, stroke_width=10.0)
        self.cross1_2 = Line(self.image1.get_corner(UP+LEFT) + 0.5*UP + 0.5*LEFT, self.image1.get_corner(DOWN+RIGHT) + 0.5*DOWN + 0.5*RIGHT, color=RED, stroke_width=10.0)
        self.cross2_1 = Line(self.image2.get_corner(DOWN+LEFT) + 0.5*DOWN + 0.5*LEFT, self.image2.get_corner(UP+RIGHT) + 0.5*UP + 0.5*RIGHT, color=RED, stroke_width=10.0)
        self.cross2_2 = Line(self.image2.get_corner(UP+LEFT) + 0.5*UP + 0.5*LEFT, self.image2.get_corner(DOWN+RIGHT) + 0.5*DOWN + 0.5*RIGHT, color=RED, stroke_width=10.0)
        self.cross3_1 = Line(self.image3.get_corner(DOWN+LEFT) + 0.5*DOWN + 0.5*LEFT, self.image3.get_corner(UP+RIGHT) + 0.5*UP + 0.5*RIGHT, color=RED, stroke_width=10.0)
        self.cross3_2 = Line(self.image3.get_corner(UP+LEFT) + 0.5*UP + 0.5*LEFT, self.image3.get_corner(DOWN+RIGHT) + 0.5*DOWN + 0.5*RIGHT, color=RED, stroke_width=10.0)

        self.line1 = TextMobject("Generative Adversarial Networks")
        self.line1.set_color(RED)
        self.line1.next_to(self.image2, 4*DOWN)


    def animation1(self):
        self.play(FadeIn(self.image1))
        self.wait(1)
        self.play(FadeIn(self.image2))
        self.wait(1)
        self.play(FadeIn(self.image3))


    def animation2(self):
        self.play(ShowCreation(self.cross1_1), ShowCreation(self.cross2_1), ShowCreation(self.cross3_1))
        self.play(ShowCreation(self.cross1_2), ShowCreation(self.cross2_2), ShowCreation(self.cross3_2))


    def animation3(self):
        self.play(Write(self.line1))


    def construct(self):

        # initialise
        print('initialising...')
        self.initialise()

        # animation 1
        print('animation 1...')
        self.animation1()
        self.wait(3)

        # animation 2
        print('animation 2...')
        self.animation2()
        self.wait(3)

        # animation 3
        print('animation 3...')
        self.animation3()
        self.wait(3)


#########################################################################################
###
### SECTION 1.3
###
#########################################################################################


class Overview(Scene):

    def initialise(self):
        self.line1 = TextMobject("Regression")
        self.line2 = TextMobject("Neural Networks")
        self.line3 = TextMobject("Evolutionary Algorithms")
        self.line4 = TextMobject("Applications")
        self.line1.move_to(4*LEFT + 3*UP)
        self.line2.move_to(4*LEFT + 0*UP)
        self.line3.move_to(4*LEFT + 3*DOWN)
        self.line4.move_to(4*RIGHT + 0*UP)

        self.box = Rectangle(height=1, width=3)
        self.box.surround(self.line1)

        self.arrow_1 = Arrow(1*LEFT + 3*UP, 2.7*RIGHT+0.3*UP)
        self.arrow_2 = Arrow(1*LEFT + 0*UP, 2.7*RIGHT)
        self.arrow_3 = Arrow(1*LEFT + 3*DOWN, 2.7*RIGHT+0.3*DOWN)


    def animation1(self):
        self.play(Write(self.line1))


    def animation2(self):
        self.play(Write(self.line2))


    def animation3(self):
        self.play(Write(self.line3))


    def animation4(self):
        self.play(Write(self.line4), ShowCreation(self.arrow_1), ShowCreation(self.arrow_2), ShowCreation(self.arrow_3))


    def animation5(self):
        self.play(ShowCreation(self.box))


    def construct(self):

        # initialise
        print('initialising...')
        self.initialise()

        # animation 1
        print('animation 1...')
        self.animation1()
        self.wait(3)

        # animation 2
        print('animation 2...')
        self.animation2()
        self.wait(3)

        # animation 3
        print('animation 3...')
        self.animation3()
        self.wait(3)

        # animation 4
        print('animation 4...')
        self.animation4()
        self.wait(3)

        # animation 4
        print('animation 5...')
        self.animation5()
        self.wait(3)


#########################################################################################
###
### SECTION 2.1
###
#########################################################################################


class DefinitionRegression(GraphScene):

    def initialise(self, seed=1):
        self.g1 = Struct()
        self.g1.graph_origin = ORIGIN + 3*LEFT + 3*DOWN
        self.g1.axes_color = WHITE
        self.g1.function_color = YELLOW
        self.g1.x_min = 0
        self.g1.x_max = 10
        self.g1.y_min = 0
        self.g1.y_max = 10
        self.g1.x_axis_label = "$x$"
        self.g1.y_axis_label = "$y$"
        self.g1.x_labeled_nums = list(np.linspace(0, 10, 11, dtype='int'))
        self.g1.y_labeled_nums = list(np.linspace(0, 10, 11, dtype='int'))
        self.g1.center_point = 0
        self.g1.x_axis_width = 7
        self.g1.y_axis_height = 6


    def focus_graph(self, g, animate=False):
        self.__dict__.update(g.__dict__)
        self.setup_axes(animate=animate)


    def draw_graph(self, g, animate=True):
        self.focus_graph(g, animate=animate)


    def create_data(self, g):
        self.focus_graph(g)
        x = np.linspace(1,10,10)
        N = 2.0
        self.m_real = 0.8
        self.c_real = 1.0
        y = self.m_real*x + self.c_real + N*np.random.random(len(x))*2 - N
        x = list(x)
        y = list(y)
        data = []
        for i in range(len(x)):
            p = Dot(color=RED)
            p.move_to(self.gp_to_rp([x[i],y[i],0], g))
            data.append(p)
        self.data = VGroup(*data)


    def gp_to_rp(self, gp, g):
        rp = [0,0,0]
        rp[0] = (gp[0]*g.x_axis_width)/(g.x_max - g.x_min) + g.graph_origin[0]
        rp[1] = (gp[1]*g.y_axis_height)/(g.y_max - g.y_min) + g.graph_origin[1]
        return rp


    def play_text(self):
        self.text1 = TextMobject("Regression: Modelling the relationship between")
        self.text2 = TextMobject("quantities given data")
        self.text2.next_to(self.text1, DOWN)
        self.play(Write(self.text1))
        self.play(Write(self.text2))


    def play_remove_text(self):
        self.play(FadeOut(self.text1), FadeOut(self.text2))


    def play_data(self):
        self.play(FadeIn(self.data))


    def play_predict(self):
        v = 5.5
        self.arrow1 = Arrow(self.gp_to_rp([v,0,0],self.g1) + DOWN, self.gp_to_rp([v,0,0],self.g1), color=GREEN)
        self.arrow2 = Arrow(self.gp_to_rp([0,v,0],self.g1) + LEFT, self.gp_to_rp([0,v,0],self.g1), color=GREEN)
        self.line1 = Line(self.gp_to_rp([v,0,0],self.g1), self.gp_to_rp([v,v,0],self.g1), stroke_width=2.0, color=GREEN)
        self.line2 = Line(self.gp_to_rp([v,v,0],self.g1), self.gp_to_rp([0,v,0],self.g1), stroke_width=2.0, color=GREEN)
        self.qm = TextMobject("?", color=GREEN)
        self.qm.next_to(self.arrow2, LEFT)
        self.play(ShowCreation(self.arrow1))
        self.play(ShowCreation(self.line1))
        self.play(ShowCreation(self.line2))
        self.play(FadeIn(self.arrow2), FadeIn(self.qm))


    def construct(self):

        # initialise
        print('initialising...')
        np.random.seed(2)
        self.initialise()

        # draw text
        print('drawing text...')
        self.play_text()
        self.wait(3)

        # remove text
        print('remove text...')
        self.play_remove_text()
        self.wait(3)

        # draw axis
        print('drawing axis...')
        self.draw_graph(self.g1)

        # creating data
        print('creating data...')
        self.create_data(self.g1)

        # show data
        print('showing data...')
        self.play_data()
        self.wait(3)

        # show predict
        print('showing predict...')
        self.play_predict()

        # wait
        self.wait(3)


#########################################################################################
###
### SECTION 2.2
###
#########################################################################################


class LinearRegressionIntro(GraphScene):

    def initialise(self, seed=1):
        self.g1 = Struct()
        self.g1.graph_origin = ORIGIN + 6*LEFT + 2*DOWN
        self.g1.axes_color = WHITE
        self.g1.function_color = YELLOW
        self.g1.x_min = 0
        self.g1.x_max = 10
        self.g1.y_min = 0
        self.g1.y_max = 10
        self.g1.x_axis_label = "$x$"
        self.g1.y_axis_label = "$y$"
        self.g1.x_labeled_nums = list(np.linspace(0, 10, 11, dtype='int'))
        self.g1.y_labeled_nums = list(np.linspace(0, 10, 11, dtype='int'))
        self.g1.center_point = 0
        self.g1.x_axis_width = 5
        self.g1.y_axis_height = 5

        self.g2 = Struct()
        self.g2.graph_origin = ORIGIN + 1.5*RIGHT + 2*DOWN
        self.g2.axes_color = BLUE
        self.g2.function_color = BLUE
        self.g2.x_min = 0
        self.g2.x_max = 3
        self.g2.y_min = 0
        self.g2.y_max = 3
        self.g2.x_axis_label = "$m$"
        self.g2.y_axis_label = "$c$"
        self.g2.x_labeled_nums = list(np.linspace(0, 3, 4, dtype='int'))
        self.g2.y_labeled_nums = list(np.linspace(0, 3, 4, dtype='int'))
        self.g2.center_point = 0
        self.g2.x_axis_width = 5
        self.g2.y_axis_height = 5

        self.m_real = 0.8
        self.c_real = 1.0

        self.m = [1.0, 0.5, 0.1, 0.5, 1.0, 0.5]
        self.c = [1.0, 0.5, 1.5, 1.5, 0.1, 2.5]
        self.functions = [lambda x: self.m[0]*x +self. c[0],
            lambda x: self.m[1]*x + self.c[1],
            lambda x: self.m[2]*x + self.c[2],
            lambda x: self.m[3]*x + self.c[3],
            lambda x: self.m[4]*x + self.c[4],
            lambda x: self.m[5]*x + self.c[5]]


    def focus_graph(self, g, animate=False):
        self.__dict__.update(g.__dict__)
        self.setup_axes(animate=animate)


    def draw_graph(self, g, animate=True):
        self.focus_graph(g, animate=animate)


    def create_functions(self, g):
        self.focus_graph(g)
        self.function_lines = []
        for f in self.functions:
            self.function_lines.append(self.get_graph(f, self.function_color))


    def create_data(self, g):
        self.focus_graph(g)
        x = np.linspace(1,10,10)
        N = 2.0
        y = self.m_real*x + self.c_real + N*np.random.random(len(x))*2 - N
        x = list(x)
        y = list(y)
        data = []
        for i in range(len(x)):
            p = Dot(color=RED)
            p.move_to(self.gp_to_rp([x[i],y[i],0], g))
            data.append(p)
        self.data = VGroup(*data)


    def create_point(self, g):
        self.focus_graph(g)
        self.point = Dot(color=BLUE)
        self.point.move_to(self.gp_to_rp([self.m[0],self.c[0],0], g))


    def create_text(self):
        self.text1 = TextMobject('Linear Regression')
        self.text1.move_to(3*RIGHT + 3*UP)

        self.text2 = TexMobject(r"y = ", r"m", r"x + ", r"c")
        self.text2.set_color_by_tex_to_color_map({"m": BLUE,"c": BLUE})
        self.text2.next_to(self.text1, 3*DOWN)

        self.arrow1 = Arrow(ORIGIN, DOWN, color=WHITE)
        self.arrow2 = Arrow(ORIGIN, DOWN, color=WHITE)
        self.arrow1.next_to(self.text2, DOWN)
        self.arrow2.next_to(self.arrow1, 4*RIGHT)

        self.text3 = TextMobject('Configuration Space', color=BLUE)
        self.text3.move_to(3*RIGHT + 0*DOWN)


    def gp_to_rp(self, gp, g):
        rp = [0,0,0]
        rp[0] = (gp[0]*g.x_axis_width)/(g.x_max - g.x_min) + g.graph_origin[0]
        rp[1] = (gp[1]*g.y_axis_height)/(g.y_max - g.y_min) + g.graph_origin[1]
        return rp


    def play_data(self):
        self.play(FadeIn(self.data))


    def play_text1(self):
        self.play(Write(self.text1))
        self.wait(3)
        self.play(Write(self.text2))


    def play_text2(self):
        self.play(ShowCreation(self.arrow1), ShowCreation(self.arrow2), Write(self.text3))


    def play_remove_text(self):
        self.play(FadeOut(self.text1), FadeOut(self.text3), FadeOut(self.arrow1), FadeOut(self.arrow2), ApplyMethod(self.text2.move_to, 3*DOWN))


    def play_guess(self):
        self.focus_graph(self.g1)
        line = self.function_lines[0]
        self.placeholder = VectorizedPoint(self.input_to_graph_point(self.center_point, self.function_lines[0]))
        self.play(Transform(self.placeholder, line, run_time=2))


    def play_guess_point(self):
        self.play(ShowCreation(self.point, run_time=2))


    def play_random_search(self):
        self.focus_graph(self.g1)
        for i, line in enumerate(self.function_lines):
            if i == 0:
                pass
            else:
                self.play(Transform(self.placeholder, line, run_time=2), ApplyMethod(self.point.move_to,self.gp_to_rp([self.m[i],self.c[i],0],self.g2), run_time=2))
            self.wait(1)


    def construct(self):

        # initialise
        print('initialising...')
        np.random.seed(2)
        self.initialise()

        # draw left axis
        print('drawing left axis...')
        self.draw_graph(self.g1)

        # initialise data and functions
        print('creating data...')
        self.create_data(self.g1)
        self.create_functions(self.g1)

        # show data
        print('showing data...')
        self.play_data()

        # draw text
        print('showing text...')
        self.create_text()
        self.play_text1()
        self.play_guess()
        self.wait()
        self.play_text2()
        self.wait(3)
        self.play_remove_text()

        # draw right axis
        print('drawing right axis...')
        self.draw_graph(self.g2)

        # initialise functions and point
        print('creating point...')
        self.create_point(self.g2)
        self.play_guess_point()
        self.wait(3)

        # play search animation
        print('playing search animation...')
        self.play_random_search()

        # wait at the end of each slide
        self.wait(3)


class LinearRegressionGradientDecent(GraphScene):

    def initialise(self, seed=1):
        self.g1 = Struct()
        self.g1.graph_origin = ORIGIN + 3.5*RIGHT + 2*DOWN
        self.g1.axes_color = WHITE
        self.g1.function_color = GREEN
        self.g1.x_min = -10
        self.g1.x_max = 10
        self.g1.y_min = 0
        self.g1.y_max = 10
        self.g1.x_axis_label = "$m$"
        self.g1.y_axis_label = "$E$"
        self.g1.x_labeled_nums = list(np.linspace(-10, 10, 5, dtype='int'))
        self.g1.y_labeled_nums = list(np.linspace(0, 10, 11, dtype='int'))
        self.g1.center_point = 0
        self.g1.x_axis_width = 6
        self.g1.y_axis_height = 7

        self.functions = [lambda x: 0.1*x**2 + 2]


    def focus_graph(self, g, animate=False):
        self.__dict__.update(g.__dict__)
        self.setup_axes(animate=animate)


    def draw_graph(self, g, animate=True):
        self.focus_graph(g, animate=animate)


    def create_functions(self, g):
        self.focus_graph(g)
        self.function_lines = []
        for f in self.functions:
            self.function_lines.append(self.get_graph(f, self.function_color))


    def create_points_and_arrows(self, g):
        self.focus_graph(g)
        self.point1 = Dot(color=GREEN)
        self.point1.move_to(self.gp_to_rp([7,self.functions[0](7),0], g))
        self.arrow1 = Arrow(self.gp_to_rp([7,self.functions[0](7),0], g), self.gp_to_rp([7,self.functions[0](7),0], g) + 2*LEFT, color=RED)

        self.point2 = Dot(color=GREEN)
        self.point2.move_to(self.gp_to_rp([4,self.functions[0](4),0], g))
        self.arrow2 = Arrow(self.gp_to_rp([4,self.functions[0](4),0], g), self.gp_to_rp([2,self.functions[0](4),0], g) + 0.5*LEFT, color=RED)


    def play_points_and_arrows(self, g):
        self.focus_graph(g)
        self.play(ShowCreation(self.point1), ShowCreation(self.arrow1))
        self.wait(3)
        self.play(Transform(self.point1, self.point2), Transform(self.arrow1, self.arrow2))


    def create_text(self):
        self.text1 = TextMobject('Gradient Descent')
        self.text1.move_to(3*LEFT + 3*UP)

        self.line = Line(LEFT*2, RIGHT*2, stroke_width=2.0, color=WHITE)
        self.line.next_to(self.text1, 1*DOWN)

        self.text2 = TexMobject(r"E(m,c)=\frac{1}{N} \sum_{i=1}^{N} {(y_i - (mx_i + c))}^2", color=WHITE)
        self.text2.next_to(self.text1, 3*DOWN)

        self.text3 = TexMobject(r"\frac{\partial E}{\partial m}=-\frac{2}{N} \sum_{i=1}^{N} x_i (y_i - (mx_i + c))", color=GREEN)
        self.text3.next_to(self.text2, DOWN)

        self.text4 = TexMobject(r"\frac{\partial E}{\partial c}=-\frac{2}{N} \sum_{i=1}^{N} (y_i - (mx_i + c))", color=GREEN)
        self.text4.next_to(self.text3, DOWN)

        self.text5 = TexMobject(r"m \rightarrow m + L\frac{\partial E}{\partial m}", color=RED)
        self.text5.next_to(self.text2, DOWN)

        self.text6 = TexMobject(r"c \rightarrow c + L\frac{\partial E}{\partial c}", color=RED)
        self.text6.next_to(self.text3, DOWN)


    def play_text1(self):
        self.play(Write(self.text1), ShowCreation(self.line))


    def play_text2(self):
        self.play(Write(self.text2))


    def play_text3(self):
        self.play(Write(self.text3), Write(self.text4))


    def play_text4(self):
        self.play(Transform(self.text3, self.text5), Transform(self.text4, self.text6))


    def gp_to_rp(self, gp, g):
        rp = [0,0,0]
        rp[0] = (gp[0]*g.x_axis_width)/(g.x_max - g.x_min) + g.graph_origin[0]
        rp[1] = (gp[1]*g.y_axis_height)/(g.y_max - g.y_min) + g.graph_origin[1]
        return rp


    def play_graph(self):
        self.focus_graph(self.g1)
        line = self.function_lines[0]
        self.placeholder = VectorizedPoint(self.input_to_graph_point(self.center_point, self.function_lines[0]))
        self.play(Transform(self.placeholder, line, run_time=2))


    def construct(self):

        # initialise
        print('initialising...')
        np.random.seed(2)
        self.initialise()

        # draw text
        print('showing text...')
        self.create_text()
        self.play_text1()
        self.wait(3)
        self.play_text2()
        self.wait(3)
        self.play_text3()
        self.wait(3)
        self.play_text4()
        self.wait(3)

        # draw axis
        print('drawing axis...')
        self.draw_graph(self.g1)

        # initialise functions
        print('creating functions...')
        self.create_functions(self.g1)

        # draw graph
        print('drawing graph...')
        self.play_graph()
        self.wait(3)

        # draw points
        print('drawing points...')
        self.create_points_and_arrows(self.g1)
        self.play_points_and_arrows(self.g1)

        # wait at the end of each slide
        self.wait(3)


class LinearRegressionTrain(GraphScene):

    def initialise(self, seed=1):
        self.g1 = Struct()
        self.g1.graph_origin = ORIGIN + 6*LEFT + 2*DOWN
        self.g1.axes_color = WHITE
        self.g1.function_color = YELLOW
        self.g1.x_min = 0
        self.g1.x_max = 10
        self.g1.y_min = 0
        self.g1.y_max = 10
        self.g1.x_axis_label = "$x$"
        self.g1.y_axis_label = "$y$"
        self.g1.x_labeled_nums = list(np.linspace(0, 10, 11, dtype='int'))
        self.g1.y_labeled_nums = list(np.linspace(0, 10, 11, dtype='int'))
        self.g1.center_point = 0
        self.g1.x_axis_width = 5
        self.g1.y_axis_height = 5

        self.g2 = Struct()
        self.g2.graph_origin = ORIGIN + 1.5*RIGHT + 2*DOWN
        self.g2.axes_color = BLUE
        self.g2.function_color = BLUE
        self.g2.x_min = 0
        self.g2.x_max = 3
        self.g2.y_min = 0
        self.g2.y_max = 3
        self.g2.x_axis_label = "$m$"
        self.g2.y_axis_label = "$c$"
        self.g2.x_labeled_nums = list(np.linspace(0, 3, 4, dtype='int'))
        self.g2.y_labeled_nums = list(np.linspace(0, 3, 4, dtype='int'))
        self.g2.center_point = 0
        self.g2.x_axis_width = 5
        self.g2.y_axis_height = 5

        self.m_real = 0.8
        self.c_real = 1.0

        self.m = [0.0, 0.4, 0.7, 0.8]
        self.c = [0.5, 0.8, 0.9, 1.0]
        self.functions = [lambda x: self.m[0]*x +self. c[0],
            lambda x: self.m[1]*x + self.c[1],
            lambda x: self.m[2]*x + self.c[2],
            lambda x: self.m[3]*x + self.c[3]]


    def focus_graph(self, g, animate=False):
        self.__dict__.update(g.__dict__)
        self.setup_axes(animate=animate)


    def draw_graph(self, g, animate=True):
        self.focus_graph(g, animate=animate)


    def create_functions(self, g):
        self.focus_graph(g)
        self.function_lines = []
        for f in self.functions:
            self.function_lines.append(self.get_graph(f, self.function_color))


    def create_data(self, g):
        self.focus_graph(g)
        x = np.linspace(1,10,10)
        N = 2.0
        y = self.m_real*x + self.c_real + N*np.random.random(len(x))*2 - N
        x = list(x)
        y = list(y)
        data = []
        for i in range(len(x)):
            p = Dot(color=RED)
            p.move_to(self.gp_to_rp([x[i],y[i],0], g))
            data.append(p)
        self.data = VGroup(*data)


    def create_point(self, g):
        self.focus_graph(g)
        self.point = Dot(color=BLUE)
        self.point.move_to(self.gp_to_rp([self.m[0],self.c[0],0], g))


    def gp_to_rp(self, gp, g):
        rp = [0,0,0]
        rp[0] = (gp[0]*g.x_axis_width)/(g.x_max - g.x_min) + g.graph_origin[0]
        rp[1] = (gp[1]*g.y_axis_height)/(g.y_max - g.y_min) + g.graph_origin[1]
        return rp


    def play_data(self):
        self.play(FadeIn(self.data))


    def play_guess(self):
        self.focus_graph(self.g1)
        line = self.function_lines[0]
        self.placeholder = VectorizedPoint(self.input_to_graph_point(self.center_point, self.function_lines[0]))
        self.play(Transform(self.placeholder, line, run_time=2), ShowCreation(self.point, run_time=2))


    def play_search(self):
        self.focus_graph(self.g1)
        for i, line in enumerate(self.function_lines):
            if i == 0:
                pass
            else:
                self.play(Transform(self.placeholder, line, run_time=2), ApplyMethod(self.point.move_to,self.gp_to_rp([self.m[i],self.c[i],0],self.g2), run_time=3))
            self.wait(1)


    def construct(self):

        # initialise
        print('initialising...')
        np.random.seed(2)
        self.initialise()

        # draw left axis
        print('drawing left axis...')
        self.draw_graph(self.g1)

        # initialise data and functions
        print('creating data...')
        self.create_data(self.g1)
        self.create_functions(self.g1)

        # show data
        print('showing data...')
        self.play_data()

        # draw right axis
        print('drawing right axis...')
        self.draw_graph(self.g2)

        # initialise functions and point
        print('creating point and guess...')
        self.create_point(self.g2)
        self.play_guess()
        self.wait(3)

        # play search animation
        print('playing search animation...')
        self.play_search()

        # wait at the end of each slide
        self.wait(3)


#########################################################################################
###
### SECTION 2.3
###
#########################################################################################


class LogisticRegressionIntro(Scene):

    def initialise(self):
        self.line=TextMobject("Logistic Regression: Predicting binary values")

    def animation1(self):
        self.play(Write(self.line))


    def construct(self):

        # initialise
        print('initialising...')
        self.initialise()

        # animation 1
        print('animation 1...')
        self.animation1()
        self.wait(3)


class LogisticRegressionGraph(GraphScene):

    def initialise(self, seed=1):
        self.g1 = Struct()
        self.g1.graph_origin = ORIGIN
        self.g1.axes_color = WHITE
        self.g1.function_color = BLUE
        self.g1.x_min = -10
        self.g1.x_max = 10
        self.g1.y_min = -2
        self.g1.y_max = 2
        self.g1.x_axis_label = "$x$"
        self.g1.y_axis_label = "$y$"
        self.g1.x_labeled_nums = list(np.linspace(-10, 10, 5, dtype='int'))
        self.g1.y_labeled_nums = list(np.linspace(-2, 2, 5, dtype='int'))
        self.g1.center_point = 0
        self.g1.x_axis_width = 13
        self.g1.y_axis_height = 7

        self.a = [1.0, 2.0, 3.0, 1.0, 1.0]
        self.b = [0.0, 0.5, -0.5, 1.0, 0.0]
        self.functions = [lambda x: 1.0/(1 + math.exp(-self.a[0] * (x - self.b[0]))),
            lambda x: 1.0/(1 + math.exp(-self.a[1] * (x - self.b[1]))),
            lambda x: 1.0/(1 + math.exp(-self.a[2] * (x - self.b[2]))),
            lambda x: 1.0/(1 + math.exp(-self.a[3] * (x - self.b[3]))),
            lambda x: 1.0/(1 + math.exp(-self.a[4] * (x - self.b[4])))]


    def focus_graph(self, g, animate=False):
        self.__dict__.update(g.__dict__)
        self.setup_axes(animate=animate)


    def draw_graph(self, g, animate=True):
        self.focus_graph(g, animate=animate)


    def create_functions(self, g):
        self.focus_graph(g)
        self.function_lines = []
        for f in self.functions:
            self.function_lines.append(self.get_graph(f, self.function_color))


    def create_data(self, g):
        self.focus_graph(g)
        x = [-8., -6., -4., -2.,  0.,  2.,  4.,  6.,  8.]
        y = [0, -0, 0, 0,  1,  0,  1, 1, 1]
        data = []
        for i in range(len(x)):
            p = Dot(color=DARK_BLUE)
            p.move_to(self.gp_to_rp([x[i],y[i],0], g))
            data.append(p)
        self.data = VGroup(*data)


    def create_text(self):
        self.text = TexMobject(r"y = \frac{1}{1 + e^{-a(x-b)}}", color=BLUE)
        self.text.move_to(self.gp_to_rp([7,-1.5,0], self.g1))


    def play_text(self):
        self.play(Write(self.text))


    def gp_to_rp(self, gp, g):
        rp = [0,0,0]
        rp[0] = (gp[0]*g.x_axis_width)/(g.x_max - g.x_min) + g.graph_origin[0]
        rp[1] = (gp[1]*g.y_axis_height)/(g.y_max - g.y_min) + g.graph_origin[1]
        return rp


    def play_data(self):
        self.play(FadeIn(self.data))


    def play_guess(self):
        line = self.function_lines[0]
        self.placeholder = VectorizedPoint(self.input_to_graph_point(self.center_point, self.function_lines[0]))
        self.play(Transform(self.placeholder, line, run_time=2))


    def play_random_search(self):
        for i, line in enumerate(self.function_lines):
            if i == 0:
                pass
            else:
                self.play(Transform(self.placeholder, line, run_time=2))
            self.wait(1)


    def construct(self):

        # initialise
        print('initialising...')
        np.random.seed(2)
        self.initialise()

        # draw left axis
        print('drawing left axis...')
        self.draw_graph(self.g1)

        # initialise data and functions
        print('creating data...')
        self.create_functions(self.g1)
        self.create_data(self.g1)

        # show data
        print('showing data...')
        self.play_data()
        self.wait(3)

        # draw text
        print('showing text...')
        self.create_text()
        self.play_text()
        self.wait(3)

        # play search animation
        print('playing search animation...')
        self.play_guess()
        self.play_random_search()

        # wait at the end of each slide
        self.wait(3)


#########################################################################################
###
### SECTION 2.4 + 2.5
###
#########################################################################################


class MonteCarlo(GraphScene):

    def initialise(self, seed=1):
        self.g1 = Struct()
        self.g1.graph_origin = ORIGIN + 3.8*RIGHT
        self.g1.axes_color = WHITE
        self.g1.function_color = BLUE
        self.g1.x_min = -10
        self.g1.x_max = 10
        self.g1.y_min = -2
        self.g1.y_max = 2
        self.g1.x_axis_label = "$x$"
        self.g1.y_axis_label = "$y$"
        self.g1.x_labeled_nums = list(np.linspace(-10, 10, 5, dtype='int'))
        self.g1.y_labeled_nums = list(np.linspace(-2, 2, 5, dtype='int'))
        self.g1.center_point = 0
        self.g1.x_axis_width = 6
        self.g1.y_axis_height = 6

        self.a = [1.0]
        self.b = [0.0]
        self.functions = [lambda x: 1.0/(1 + math.exp(-self.a[0] * (x - self.b[0])))]


    def focus_graph(self, g, animate=False):
        self.__dict__.update(g.__dict__)
        self.setup_axes(animate=animate)


    def draw_graph(self, g, animate=True):
        self.focus_graph(g, animate=animate)


    def create_functions(self, g):
        self.focus_graph(g)
        self.function_lines = []
        for f in self.functions:
            self.function_lines.append(self.get_graph(f, self.function_color))


    def create_data(self, g):
        self.focus_graph(g)
        x = [-8., -6., -4., -2.,  0.,  2.,  4.,  6.,  8.]
        y = [0, -0, 0, 0,  1,  0,  1, 1, 1]
        data = []
        for i in range(len(x)):
            p = Dot(color=DARK_BLUE)
            p.move_to(self.gp_to_rp([x[i],y[i],0], g))
            data.append(p)
        self.data = VGroup(*data)


    def create_text(self):
        self.text1 = TextMobject('Monte Carlo')
        self.text1.move_to(3*LEFT + 3*UP)

        self.line = Line(LEFT*2, RIGHT*2, stroke_width=2.0, color=WHITE)
        self.line.next_to(self.text1, 1*DOWN)

        self.text2 = TextMobject("Logistic Regression", color=WHITE)
        self.text2.next_to(self.text1, 10*DOWN)

        self.text3 = TextMobject("For each value use the LR model", color=RED)
        self.text3.next_to(self.text1, 5*DOWN)

        self.text4 = TextMobject("Randomise outcome", color=RED)
        self.text4.next_to(self.text1, 10*DOWN)

        self.text5 = TextMobject("Enter into the overall model", color=RED)
        self.text5.next_to(self.text1, 15*DOWN)

        self.text6 = TextMobject("Application: Hospitals", color=GREEN)
        self.text6.next_to(self.text1, 20*DOWN)

        self.text7 = TextMobject("Application: Debt Purchasing", color=GREEN)
        self.text7.next_to(self.text1, 20*DOWN)


    def play_text1(self):
        self.play(Write(self.text1), ShowCreation(self.line))


    def play_text2(self):
        self.play(Write(self.text2))


    def play_text3(self):
        self.play(Transform(self.text2, self.text3), Write(self.text4), Write(self.text5))


    def play_text4(self):
        self.play(Write(self.text6))


    def play_text5(self):
        self.play(Transform(self.text6, self.text7))


    def gp_to_rp(self, gp, g):
        rp = [0,0,0]
        rp[0] = (gp[0]*g.x_axis_width)/(g.x_max - g.x_min) + g.graph_origin[0]
        rp[1] = (gp[1]*g.y_axis_height)/(g.y_max - g.y_min) + g.graph_origin[1]
        return rp


    def play_data(self):
        self.play(FadeIn(self.data))


    def play_guess(self):
        line = self.function_lines[0]
        self.placeholder = VectorizedPoint(self.input_to_graph_point(self.center_point, self.function_lines[0]))
        self.play(Transform(self.placeholder, line, run_time=2))


    def construct(self):

        # initialise
        print('initialising...')
        np.random.seed(2)
        self.initialise()

        # draw left axis
        print('drawing axis...')
        self.draw_graph(self.g1)

        # initialise data and functions
        print('creating data...')
        self.create_data(self.g1)
        self.create_functions(self.g1)

        # show data
        print('showing data...')
        self.play_data()
        self.play_guess()
        self.wait(3)

        # draw text
        print('showing text...')
        self.create_text()
        self.play_text1()
        self.wait(3)
        self.play_text2()
        self.wait(3)
        self.play_text3()
        self.wait(3)
        self.play_text4()
        self.wait(3)
        self.play_text5()
        self.wait(3)


#########################################################################################
###
### SECTION 3.1
###
#########################################################################################


class NeuralNetworksIntro(Scene):

    def initialise(self):
        self.line1 = TextMobject("Regression")
        self.line2 = TextMobject("Neural Networks")
        self.line3 = TextMobject("Evolutionary Algorithms")
        self.line4 = TextMobject("Applications")
        self.line1.move_to(4*LEFT + 3*UP)
        self.line2.move_to(4*LEFT + 0*UP)
        self.line3.move_to(4*LEFT + 3*DOWN)
        self.line4.move_to(4*RIGHT + 0*UP)

        self.box = Rectangle(height=1, width=3)
        self.box.surround(self.line2)

        self.arrow_1 = Arrow(1*LEFT + 3*UP, 2.7*RIGHT+0.3*UP)
        self.arrow_2 = Arrow(1*LEFT + 0*UP, 2.7*RIGHT)
        self.arrow_3 = Arrow(1*LEFT + 3*DOWN, 2.7*RIGHT+0.3*DOWN)


    def animation1(self):
        self.add(self.line1)
        self.add(self.line2)
        self.add(self.line3)
        self.add(self.line4)
        self.add(self.arrow_1)
        self.add(self.arrow_2)
        self.add(self.arrow_3)


    def animation2(self):
        self.play(ShowCreation(self.box))


    def construct(self):

        # initialise
        print('initialising...')
        self.initialise()

        # animation 1
        print('animation 1...')
        self.animation1()
        self.wait(3)

        # animation 2
        print('animation 2...')
        self.animation2()
        self.wait(3)


class NeuralNetworksDefinition(Scene):

    def initialise(self):
        self.line1 = TextMobject("Propagation", color=RED)
        self.line2 = TextMobject("Neural Network", color=DARKER_GRAY)
        self.line3 = TextMobject("Training", color=GREEN)
        self.line4 = TextMobject("Data In")
        self.line5 = TextMobject("Data Out")
        self.line1.next_to(self.line2, 8*UP)
        self.line3.next_to(self.line2, 8*DOWN)
        self.line4.next_to(self.line2, 7*LEFT)
        self.line5.next_to(self.line2, 6*RIGHT)

        self.box = Rectangle(height=3, width=5, fill_color=WHITE, fill_opacity=1)
        self.box.surround(self.line2)

        self.arrow1 = Arrow(ORIGIN, RIGHT, stroke_width=5.0)
        self.arrow2 = Arrow(ORIGIN, RIGHT, stroke_width=5.0)
        self.arrow1.next_to(self.line2, 3.5*LEFT)
        self.arrow2.next_to(self.line2, 2.5*RIGHT)


    def animation1(self):
        self.play(FadeIn(self.box), FadeIn(self.line2))
        self.play(FadeIn(self.line4), FadeIn(self.line5), FadeIn(self.arrow1), FadeIn(self.arrow2))


    def animation2(self):
        self.play(Write(self.line1))
        self.wait(3)
        self.play(Write(self.line3))


    def construct(self):

        # initialise
        print('initialising...')
        self.initialise()

        # animation 1
        print('animation 1...')
        self.animation1()
        self.wait(3)

        # animation 2
        print('animation 2...')
        self.animation2()
        self.wait(3)


#########################################################################################
###
### SECTION 3.2
###
#########################################################################################


class NeuralNetwork(Scene):

    def initialise(self):
        self.size = [4,2,2,1] # must have even number of elements

        self.weights = []
        for i in range(0, len(self.size) - 1):
            w = np.ones(shape=(self.size[i], self.size[i+1]))
            self.weights.append(w)

        self.biases = []
        for i in range(1, len(self.size)):
            b = np.ones(shape=(self.size[i]))
            self.biases.append(b)

        self.values = []
        for i in range(0, len(self.size)):
            v = np.ones(shape=(self.size[i]))
            self.values.append(v)

        self.scale = 2.0


    def randomise(self):
        for i,w in enumerate(self.weights):
            r = np.random.random(size=w.shape)
            self.weights[i] = 2.0*r - 1.0

        for i,b in enumerate(self.biases):
            r = np.random.random(size=b.shape)
            self.biases[i] = 2.0*r - 1.0

        self.values[0] = np.random.random(size=self.values[0].shape)


    def evaulate(self):
        for i in range(1, len(self.size)):
             v = np.dot(self.weights[i-1].T, self.values[i-1]) + self.biases[i-1]
             self.values[i] = self.activation(v)


    def activation(self, x):
        return 1.0 / (1.0 + np.exp(-1.0*x))


    def frame(self, point):
        p = point*self.scale
        return p


    def value_to_color(self, value, type):
        if type == 'node':
            color = rgb_to_color((value, value, value))
        if type == 'connection':
            if value >= 0:
                color = rgb_to_color((0, value, 0))
            else:
                color = rgb_to_color((-value, 0, 0))
        return color


    def create(self):
        self.layers = []
        for i in range(len(self.size)):
            layer = []
            for j in range(self.size[i]):
                x = self.frame(1.0*(float(i) - float(len(self.size)-1)/2.0))
                y = self.frame(-1.0*(float(j) - float(self.size[i]-1)/2.0))
                node = Circle(color=WHITE, fill_color=self.value_to_color(self.values[i][j], type='node'), fill_opacity=1, radius=self.scale/5, x=x, y=y)
                z = 0
                node.move_to([x,y,z])
                layer.append(node)
            self.layers.append(layer)

        self.nets = []
        for i,w in enumerate(self.weights):
            net = []
            for j in range(w.shape[0]):
                for k in range(w.shape[1]):
                    start = np.array([self.layers[i][j].x + self.layers[i][j].radius, self.layers[i][j].y, 0])
                    end = np.array([self.layers[i+1][k].x - self.layers[i+1][k].radius, self.layers[i+1][k].y, 0])
                    color = self.value_to_color(w[j,k], type='connection')
                    line = Line(start, end, color=color)
                    net.append(line)
            self.nets.append(net)


    def draw(self):
        for l in self.layers:
            layer_v = VGroup(*l)
            self.play(ShowCreation(layer_v))

        for n in self.nets:
            net_v = VGroup(*n)
            self.play(ShowCreation(net_v))


    def construct(self):
        # initialise
        print('initialising...')
        self.initialise()
        np.random.seed(17)
        self.randomise()
        self.evaulate()
        self.create()

        # draw network
        print('drawing...')
        self.draw()

        # wait at the end of each slide
        self.wait(3)


class SingleNeuroneCreate(Scene):

    def initialise(self, x=3, y=1):
        self.MAX_VALUE = 1.0

        self.body_pos = ORIGIN
        self.body_size = 0.7
        self.n_inputs = x # must be odd
        self.n_outputs = y # must be odd

        self.inputs = list(np.ones(self.n_inputs))
        self.weights = list(np.ones(self.n_inputs))
        self.bias = 1.0
        self.value = 1.0
        self.outputs = list(np.ones(self.n_inputs))


    def randomise_inputs(self):
        self.inputs = list(2*self.MAX_VALUE*np.random.random(self.n_inputs) - self.MAX_VALUE)


    def randomise_weights(self):
        self.weights = list(2*self.MAX_VALUE*np.random.random(self.n_inputs) - self.MAX_VALUE)


    def randomise_bias(self):
        self.bias = 2*self.MAX_VALUE*np.random.random() - self.MAX_VALUE


    def activation(self, x):
        return 1.0 / (1.0 + np.exp(-1.0*x))


    def evaluate(self):
        self.value = 0.0
        for i in range(self.n_inputs):
            self.value += self.weights[i]*self.inputs[i]
        self.value += self.bias
        self.value = self.activation(self.value)

        self.outputs = []
        for i in range(self.n_outputs):
            self.outputs.append(self.value)


    def update_colors(self):
        self.weights_c = []
        for w in self.weights:
            if w >= 0:
                self.weights_c.append(rgb_to_color((0,w/self.MAX_VALUE,0)))
            else:
                self.weights_c.append(rgb_to_color((-w/self.MAX_VALUE,0,0)))

        if self.bias >= 0:
            self.bias_c = rgb_to_color((0,self.bias/self.MAX_VALUE,0))
        else:
            self.bias_c = rgb_to_color((-self.bias/self.MAX_VALUE,0,0))

        if self.value >= 0:
            self.value_c = rgb_to_color((self.value/self.MAX_VALUE,self.value/self.MAX_VALUE,self.value/self.MAX_VALUE))
        else:
            raise ValueError('The value of the neurone is negative, this should be impossible...')


    def create(self):
        self.body = Circle(color=WHITE, fill_color=self.value_c, fill_opacity=1, radius=self.body_size)
        self.body.move_to(self.body_pos)

        self.in_text = []
        start_in = np.array([-self.body.radius,0,0]+self.body_pos)
        y_in = list(np.linspace(((self.n_inputs-1)/2),-((self.n_inputs-1)/2),2*((self.n_inputs-1)/2) + 1))
        for i in range(self.n_inputs):
            it = TexMobject("I_{0} = {1:.2f}".format(i, self.inputs[i]))
            it.move_to(start_in + 3.5*LEFT + 2*self.body_size*y_in[i]*UP)
            self.in_text.append(it)

        self.out_text = []
        start_out = np.array([self.body.radius,0,0]+self.body_pos)
        y_out = list(np.linspace(((self.n_outputs-1)/2),-((self.n_outputs-1)/2),2*((self.n_outputs-1)/2) + 1))
        for i in range(self.n_outputs):
            ot = TexMobject("U = {0:.2f}".format(self.outputs[i]))
            ot.move_to(start_out + 3.5*RIGHT + 2*self.body_size*y_out[i]*UP)
            self.out_text.append(ot)

        self.in_lines = []
        for i in range(self.n_inputs):
            self.in_lines.append(Line(start_in + 2*LEFT + 2*self.body_size*y_in[i]*UP, start_in, color=self.weights_c[i]))

        self.out_lines = []
        for i in range(self.n_outputs):
            self.out_lines.append(Line(start_out, start_out + 2*RIGHT + 2*self.body_size*y_out[i]*UP, color=WHITE))

        self.bias_dot = Dot(color=self.bias_c, radius=0.2*self.body_size)
        self.bias_dot.move_to(start_in)


    def play_draw_in_text(self):
        in_text = VGroup(*self.in_text)
        self.play(Write(in_text))


    def play_draw_in_lines(self):
        in_lines = VGroup(*self.in_lines)
        self.play(ShowCreation(in_lines))


    def play_draw_bias_dot(self):
        self.play(FadeIn(self.bias_dot))


    def play_draw_body(self):
        self.play(FadeIn(self.body))


    def play_draw_out_lines(self):
        out_lines = VGroup(*self.out_lines)
        self.play(ShowCreation(out_lines))


    def play_draw_out_text(self):
        out_text = VGroup(*self.out_text)
        self.play(Write(out_text))


    def play_draw_all(self):
        self.play_draw_in_text()
        self.play_draw_in_lines()
        self.play_draw_bias_dot()
        self.play_draw_body()
        self.play_draw_out_lines()
        self.play_draw_out_text()


    def play_update_in_text(self):
        in_text_old = VGroup(*self.in_text)
        self.in_text = []
        start_in = np.array([-self.body.radius,0,0]+self.body_pos)
        y_in = list(np.linspace(((self.n_inputs-1)/2),-((self.n_inputs-1)/2),2*((self.n_inputs-1)/2) + 1))
        for i in range(self.n_inputs):
            it = TexMobject("I_{0} = {1:.2f}".format(i, self.inputs[i]))
            it.move_to(start_in + 3.5*LEFT + 2*self.body_size*y_in[i]*UP)
            self.in_text.append(it)
        in_text = VGroup(*self.in_text)
        self.play(Transform(in_text_old, in_text))


    def play_update_in_lines(self):
        in_lines_old = VGroup(*self.in_lines)
        self.in_lines = []
        start_in = np.array([-self.body.radius,0,0]+self.body_pos)
        y_in = list(np.linspace(((self.n_inputs-1)/2),-((self.n_inputs-1)/2),2*((self.n_inputs-1)/2) + 1))
        for i in range(self.n_inputs):
            self.in_lines.append(Line(start_in + 2*LEFT + 2*self.body_size*y_in[i]*UP, start_in, color=self.weights_c[i]))
        in_lines = VGroup(*self.in_lines)
        self.play(ShowCreation(in_lines))


    def play_update_bias_dot(self):
        start_in = np.array([-self.body.radius,0,0]+self.body_pos)
        self.bias_dot = Dot(color=self.bias_c, radius=0.2*self.body_size)
        self.bias_dot.move_to(start_in)
        self.play(ShowCreation(self.bias_dot))


    def play_update_body(self):
        self.body = Circle(color=WHITE, fill_color=self.value_c, fill_opacity=1, radius=self.body_size)
        self.body.move_to(self.body_pos)
        self.play(ShowCreation(self.body))


    def play_update_out_lines(self):
        out_lines_old = VGroup(*self.out_lines)
        self.out_lines = []
        start_out = np.array([self.body.radius,0,0]+self.body_pos)
        y_out = list(np.linspace(((self.n_outputs-1)/2),-((self.n_outputs-1)/2),2*((self.n_outputs-1)/2) + 1))
        for i in range(self.n_outputs):
            self.out_lines.append(Line(start_out + 2*RIGHT + 2*self.body_size*y_out[i]*UP, start_out, color=WHITE))
        out_lines = VGroup(*self.out_lines)
        self.play(ShowCreation(out_lines))


    def play_update_out_text(self):
        out_text_old = VGroup(*self.out_text)
        self.out_text = []
        start_out = np.array([self.body.radius,0,0]+self.body_pos)
        y_out = list(np.linspace(((self.n_outputs-1)/2),-((self.n_outputs-1)/2),2*((self.n_outputs-1)/2) + 1))
        for i in range(self.n_outputs):
            ot = TexMobject("U = {0:.2f}".format(self.outputs[i]))
            ot.move_to(start_out + 3.5*RIGHT + 2*self.body_size*y_out[i]*UP)
            self.out_text.append(ot)
        out_text = VGroup(*self.out_text)
        self.play(Transform(out_text_old, out_text))


    def play_update_all(self):
        self.play_update_in_text()
        self.play_update_in_lines()
        self.play_update_bias_dot()
        self.play_update_body()
        self.play_update_out_lines()
        self.play_update_out_text()


    def play_text(self):
        self.text = TexMobject(r"U = \sigma \left( \sum_i", r"w_i", r"I_i + ", r"b",  r"\right)")
        self.text.set_color_by_tex_to_color_map({"w_i": GREEN,"b": GREEN})
        self.text.move_to(3*UP)

        self.play(Write(self.text))


    def construct(self):

        # initialise
        print('initialising...')
        self.initialise(x=3, y=3)
        self.update_colors()
        self.create()

        # animation 1
        print('drawing blank neurone...')
        self.play_draw_all()
        self.wait(3)

        # animation 2
        print('drawing text...')
        self.play_text()
        self.wait(3)

        # animation 3
        print('randomising neurone...')
        np.random.seed(17)
        self.initialise(x=3, y=3)
        self.randomise_inputs()
        self.randomise_weights()
        self.randomise_bias()
        self.evaluate()
        self.update_colors()
        self.play_update_all()
        self.wait(3)


class ActivationGraph(GraphScene):

    def initialise(self, seed=1):
        self.g1 = Struct()
        self.g1.graph_origin = ORIGIN
        self.g1.axes_color = WHITE
        self.g1.function_color = ORANGE
        self.g1.x_min = -10
        self.g1.x_max = 10
        self.g1.y_min = -2
        self.g1.y_max = 2
        self.g1.x_axis_label = "$x$"
        self.g1.y_axis_label = "$\sigma$"
        self.g1.x_labeled_nums = list(np.linspace(-10, 10, 5, dtype='int'))
        self.g1.y_labeled_nums = list(np.linspace(-2, 2, 5, dtype='int'))
        self.g1.center_point = 0
        self.g1.x_axis_width = 13
        self.g1.y_axis_height = 7

        self.a = [1.0]
        self.b = [0.0]
        self.functions = [lambda x: 1.0/(1 + math.exp(-self.a[0] * (x - self.b[0])))]


    def focus_graph(self, g, animate=False):
        self.__dict__.update(g.__dict__)
        self.setup_axes(animate=animate)


    def draw_graph(self, g, animate=True):
        self.focus_graph(g, animate=animate)


    def create_functions(self, g):
        self.focus_graph(g)
        self.function_lines = []
        for f in self.functions:
            self.function_lines.append(self.get_graph(f, self.function_color))


    def create_text(self):
        self.text = TexMobject(r"\sigma (x) = \frac{1}{1 + e^{-x}}", color=ORANGE)
        self.text.move_to(self.gp_to_rp([7,-1.5,0], self.g1))


    def play_text(self):
        self.play(Write(self.text))


    def gp_to_rp(self, gp, g):
        rp = [0,0,0]
        rp[0] = (gp[0]*g.x_axis_width)/(g.x_max - g.x_min) + g.graph_origin[0]
        rp[1] = (gp[1]*g.y_axis_height)/(g.y_max - g.y_min) + g.graph_origin[1]
        return rp


    def play_guess(self):
        line = self.function_lines[0]
        self.placeholder = VectorizedPoint(self.input_to_graph_point(self.center_point, self.function_lines[0]))
        self.play(Transform(self.placeholder, line, run_time=2))


    def construct(self):

        # initialise
        print('initialising...')
        np.random.seed(2)
        self.initialise()

        # draw left axis
        print('drawing axis...')
        self.draw_graph(self.g1)

        # initialise data and functions
        print('creating data...')
        self.create_functions(self.g1)

        # draw text
        print('showing...')
        self.create_text()
        self.play_text()
        self.play_guess()
        self.wait(3)


class NeuralNetworkAgain(Scene):

    def initialise(self):
        self.size = [4,2,2,1] # must have even number of elements

        self.weights = []
        for i in range(0, len(self.size) - 1):
            w = np.ones(shape=(self.size[i], self.size[i+1]))
            self.weights.append(w)

        self.biases = []
        for i in range(1, len(self.size)):
            b = np.ones(shape=(self.size[i]))
            self.biases.append(b)

        self.values = []
        for i in range(0, len(self.size)):
            v = np.ones(shape=(self.size[i]))
            self.values.append(v)

        self.scale = 2.0


    def randomise(self):
        for i,w in enumerate(self.weights):
            r = np.random.random(size=w.shape)
            self.weights[i] = 2.0*r - 1.0

        for i,b in enumerate(self.biases):
            r = np.random.random(size=b.shape)
            self.biases[i] = 2.0*r - 1.0

        self.values[0] = np.random.random(size=self.values[0].shape)


    def evaulate(self):
        for i in range(1, len(self.size)):
             v = np.dot(self.weights[i-1].T, self.values[i-1]) + self.biases[i-1]
             self.values[i] = self.activation(v)


    def activation(self, x):
        return 1.0 / (1.0 + np.exp(-1.0*x))


    def frame(self, point):
        p = point*self.scale
        return p


    def value_to_color(self, value, type):
        if type == 'node':
            color = rgb_to_color((value, value, value))
        if type == 'connection':
            if value >= 0:
                color = rgb_to_color((0, value, 0))
            else:
                color = rgb_to_color((-value, 0, 0))
        return color


    def create(self):
        self.layers = []
        for i in range(len(self.size)):
            layer = []
            for j in range(self.size[i]):
                x = self.frame(1.0*(float(i) - float(len(self.size)-1)/2.0))
                y = self.frame(-1.0*(float(j) - float(self.size[i]-1)/2.0))
                node = Circle(color=WHITE, fill_color=self.value_to_color(self.values[i][j], type='node'), fill_opacity=1, radius=self.scale/5, x=x, y=y)
                z = 0
                node.move_to([x,y,z])
                layer.append(node)
            self.layers.append(layer)

        self.nets = []
        for i,w in enumerate(self.weights):
            net = []
            for j in range(w.shape[0]):
                for k in range(w.shape[1]):
                    start = np.array([self.layers[i][j].x + self.layers[i][j].radius, self.layers[i][j].y, 0])
                    end = np.array([self.layers[i+1][k].x - self.layers[i+1][k].radius, self.layers[i+1][k].y, 0])
                    color = self.value_to_color(w[j,k], type='connection')
                    line = Line(start, end, color=color)
                    net.append(line)
            self.nets.append(net)


    def draw(self):
        for l in self.layers:
            layer_v = VGroup(*l)
            self.play(ShowCreation(layer_v))

        for n in self.nets:
            net_v = VGroup(*n)
            self.play(ShowCreation(net_v))


    def construct(self):
        # initialise
        print('initialising...')
        self.initialise()
        np.random.seed(17)
        self.randomise()
        self.evaulate()
        self.create()

        # draw network
        print('drawing...')
        self.draw()

        # wait at the end of each slide
        self.wait(3)


class SingleNeuroneAgain(Scene):

    def initialise(self, x=3, y=1):
        self.MAX_VALUE = 1.0

        self.body_pos = ORIGIN
        self.body_size = 0.7
        self.n_inputs = x # must be odd
        self.n_outputs = y # must be odd

        self.inputs = list(np.ones(self.n_inputs))
        self.weights = list(np.ones(self.n_inputs))
        self.bias = 1.0
        self.value = 1.0
        self.outputs = list(np.ones(self.n_inputs))


    def randomise_inputs(self):
        self.inputs = list(2*self.MAX_VALUE*np.random.random(self.n_inputs) - self.MAX_VALUE)


    def randomise_weights(self):
        self.weights = list(2*self.MAX_VALUE*np.random.random(self.n_inputs) - self.MAX_VALUE)


    def randomise_bias(self):
        self.bias = 2*self.MAX_VALUE*np.random.random() - self.MAX_VALUE


    def activation(self, x):
        return 1.0 / (1.0 + np.exp(-1.0*x))


    def evaluate(self):
        self.value = 0.0
        for i in range(self.n_inputs):
            self.value += self.weights[i]*self.inputs[i]
        self.value += self.bias
        self.value = self.activation(self.value)

        self.outputs = []
        for i in range(self.n_outputs):
            self.outputs.append(self.value)


    def update_colors(self):
        self.weights_c = []
        for w in self.weights:
            if w >= 0:
                self.weights_c.append(rgb_to_color((0,w/self.MAX_VALUE,0)))
            else:
                self.weights_c.append(rgb_to_color((-w/self.MAX_VALUE,0,0)))

        if self.bias >= 0:
            self.bias_c = rgb_to_color((0,self.bias/self.MAX_VALUE,0))
        else:
            self.bias_c = rgb_to_color((-self.bias/self.MAX_VALUE,0,0))

        if self.value >= 0:
            self.value_c = rgb_to_color((self.value/self.MAX_VALUE,self.value/self.MAX_VALUE,self.value/self.MAX_VALUE))
        else:
            raise ValueError('The value of the neurone is negative, this should be impossible...')


    def create(self):
        self.body = Circle(color=WHITE, fill_color=self.value_c, fill_opacity=1, radius=self.body_size)
        self.body.move_to(self.body_pos)

        self.in_text = []
        start_in = np.array([-self.body.radius,0,0]+self.body_pos)
        y_in = list(np.linspace(((self.n_inputs-1)/2),-((self.n_inputs-1)/2),2*((self.n_inputs-1)/2) + 1))
        for i in range(self.n_inputs):
            it = TexMobject("I_{0} = {1:.2f}".format(i, self.inputs[i]))
            it.move_to(start_in + 3.5*LEFT + 2*self.body_size*y_in[i]*UP)
            self.in_text.append(it)

        self.out_text = []
        start_out = np.array([self.body.radius,0,0]+self.body_pos)
        y_out = list(np.linspace(((self.n_outputs-1)/2),-((self.n_outputs-1)/2),2*((self.n_outputs-1)/2) + 1))
        for i in range(self.n_outputs):
            ot = TexMobject("U = {0:.2f}".format(self.outputs[i]))
            ot.move_to(start_out + 3.5*RIGHT + 2*self.body_size*y_out[i]*UP)
            self.out_text.append(ot)

        self.in_lines = []
        for i in range(self.n_inputs):
            self.in_lines.append(Line(start_in + 2*LEFT + 2*self.body_size*y_in[i]*UP, start_in, color=self.weights_c[i]))

        self.out_lines = []
        for i in range(self.n_outputs):
            self.out_lines.append(Line(start_out, start_out + 2*RIGHT + 2*self.body_size*y_out[i]*UP, color=WHITE))

        self.bias_dot = Dot(color=self.bias_c, radius=0.2*self.body_size)
        self.bias_dot.move_to(start_in)


    def play_draw_in_text(self):
        in_text = VGroup(*self.in_text)
        self.play(Write(in_text))


    def play_draw_in_lines(self):
        in_lines = VGroup(*self.in_lines)
        self.play(ShowCreation(in_lines))


    def play_draw_bias_dot(self):
        self.play(FadeIn(self.bias_dot))


    def play_draw_body(self):
        self.play(FadeIn(self.body))


    def play_draw_out_lines(self):
        out_lines = VGroup(*self.out_lines)
        self.play(ShowCreation(out_lines))


    def play_draw_out_text(self):
        out_text = VGroup(*self.out_text)
        self.play(Write(out_text))


    def play_draw_all(self):
        self.play_draw_in_text()
        self.play_draw_in_lines()
        self.play_draw_bias_dot()
        self.play_draw_body()
        self.play_draw_out_lines()
        self.play_draw_out_text()


    def play_update_in_text(self):
        in_text_old = VGroup(*self.in_text)
        self.in_text = []
        start_in = np.array([-self.body.radius,0,0]+self.body_pos)
        y_in = list(np.linspace(((self.n_inputs-1)/2),-((self.n_inputs-1)/2),2*((self.n_inputs-1)/2) + 1))
        for i in range(self.n_inputs):
            it = TexMobject("I_{0} = {1:.2f}".format(i, self.inputs[i]))
            it.move_to(start_in + 3.5*LEFT + 2*self.body_size*y_in[i]*UP)
            self.in_text.append(it)
        in_text = VGroup(*self.in_text)
        self.play(Transform(in_text_old, in_text))


    def play_update_in_lines(self):
        in_lines_old = VGroup(*self.in_lines)
        self.in_lines = []
        start_in = np.array([-self.body.radius,0,0]+self.body_pos)
        y_in = list(np.linspace(((self.n_inputs-1)/2),-((self.n_inputs-1)/2),2*((self.n_inputs-1)/2) + 1))
        for i in range(self.n_inputs):
            self.in_lines.append(Line(start_in + 2*LEFT + 2*self.body_size*y_in[i]*UP, start_in, color=self.weights_c[i]))
        in_lines = VGroup(*self.in_lines)
        self.play(ShowCreation(in_lines))


    def play_update_bias_dot(self):
        start_in = np.array([-self.body.radius,0,0]+self.body_pos)
        self.bias_dot = Dot(color=self.bias_c, radius=0.2*self.body_size)
        self.bias_dot.move_to(start_in)
        self.play(ShowCreation(self.bias_dot))


    def play_update_body(self):
        self.body = Circle(color=WHITE, fill_color=self.value_c, fill_opacity=1, radius=self.body_size)
        self.body.move_to(self.body_pos)
        self.play(ShowCreation(self.body))


    def play_update_out_lines(self):
        out_lines_old = VGroup(*self.out_lines)
        self.out_lines = []
        start_out = np.array([self.body.radius,0,0]+self.body_pos)
        y_out = list(np.linspace(((self.n_outputs-1)/2),-((self.n_outputs-1)/2),2*((self.n_outputs-1)/2) + 1))
        for i in range(self.n_outputs):
            self.out_lines.append(Line(start_out + 2*RIGHT + 2*self.body_size*y_out[i]*UP, start_out, color=WHITE))
        out_lines = VGroup(*self.out_lines)
        self.play(ShowCreation(out_lines))


    def play_update_out_text(self):
        out_text_old = VGroup(*self.out_text)
        self.out_text = []
        start_out = np.array([self.body.radius,0,0]+self.body_pos)
        y_out = list(np.linspace(((self.n_outputs-1)/2),-((self.n_outputs-1)/2),2*((self.n_outputs-1)/2) + 1))
        for i in range(self.n_outputs):
            ot = TexMobject("U = {0:.2f}".format(self.outputs[i]))
            ot.move_to(start_out + 3.5*RIGHT + 2*self.body_size*y_out[i]*UP)
            self.out_text.append(ot)
        out_text = VGroup(*self.out_text)
        self.play(Transform(out_text_old, out_text))


    def play_update_all(self):
        self.play_update_in_text()
        self.play_update_in_lines()
        self.play_update_bias_dot()
        self.play_update_body()
        self.play_update_out_lines()
        self.play_update_out_text()


    def play_text(self):
        self.text = TexMobject(r"U = \sigma \left( \sum_i", r"w_i", r"I_i + ", r"b",  r"\right)")
        self.text.set_color_by_tex_to_color_map({"w_i": GREEN,"b": GREEN})
        self.text.move_to(3*UP)

        self.play(Write(self.text))


    def construct(self):

        # initialise
        print('initialising...')
        np.random.seed(17)
        self.initialise(x=3, y=3)
        self.randomise_inputs()
        self.randomise_weights()
        self.randomise_bias()
        self.evaluate()
        self.update_colors()
        self.create()

        # animation 2
        print('drawing text...')
        self.play_text()
        self.wait(3)

        # animation 1
        print('drawing neurone...')
        self.play_draw_all()
        self.wait(3)


#########################################################################################
###
### SECTION 3.3
###
#########################################################################################


class NeuralNetworkTraining(Scene):

    def initialise(self):
        self.size = [4,2,2,1] # must have even number of elements

        self.weights = []
        for i in range(0, len(self.size) - 1):
            w = np.ones(shape=(self.size[i], self.size[i+1]))
            self.weights.append(w)

        self.biases = []
        for i in range(1, len(self.size)):
            b = np.ones(shape=(self.size[i]))
            self.biases.append(b)

        self.values = []
        for i in range(0, len(self.size)):
            v = np.ones(shape=(self.size[i]))
            self.values.append(v)

        self.scale = 2.0


    def randomise(self):
        for i,w in enumerate(self.weights):
            r = np.random.random(size=w.shape)
            self.weights[i] = 2.0*r - 1.0

        for i,b in enumerate(self.biases):
            r = np.random.random(size=b.shape)
            self.biases[i] = 2.0*r - 1.0

        self.values[0] = np.random.random(size=self.values[0].shape)


    def evaulate(self):
        for i in range(1, len(self.size)):
             v = np.dot(self.weights[i-1].T, self.values[i-1]) + self.biases[i-1]
             self.values[i] = self.activation(v)


    def activation(self, x):
        return 1.0 / (1.0 + np.exp(-1.0*x))


    def frame(self, point):
        p = point*self.scale
        return p


    def value_to_color(self, value, type):
        if type == 'node':
            color = rgb_to_color((value, value, value))
        if type == 'connection':
            if value >= 0:
                color = rgb_to_color((0, value, 0))
            else:
                color = rgb_to_color((-value, 0, 0))
        return color


    def create(self):
        self.layers = []
        for i in range(len(self.size)):
            layer = []
            for j in range(self.size[i]):
                x = self.frame(1.0*(float(i) - float(len(self.size)-1)/2.0))
                y = self.frame(-1.0*(float(j) - float(self.size[i]-1)/2.0))
                node = Circle(color=WHITE, fill_color=self.value_to_color(self.values[i][j], type='node'), fill_opacity=1, radius=self.scale/5, x=x, y=y)
                z = 0
                node.move_to([x,y,z])
                layer.append(node)
            self.layers.append(layer)

        self.nets = []
        for i,w in enumerate(self.weights):
            net = []
            for j in range(w.shape[0]):
                for k in range(w.shape[1]):
                    start = np.array([self.layers[i][j].x + self.layers[i][j].radius, self.layers[i][j].y, 0])
                    end = np.array([self.layers[i+1][k].x - self.layers[i+1][k].radius, self.layers[i+1][k].y, 0])
                    color = self.value_to_color(w[j,k], type='connection')
                    line = Line(start, end, color=color)
                    net.append(line)
            self.nets.append(net)


    def draw(self):
        for l in self.layers:
            layer_v = VGroup(*l)
            self.play(FadeIn(layer_v))

        for n in self.nets:
            net_v = VGroup(*n)
            self.play(FadeIn(net_v))


    def text(self):
        self.line1 = TextMobject('Training: Backpropagation', color=BLUE)
        self.line1.move_to(4*RIGHT + 3*DOWN)
        self.line2 = TextMobject('Training: Gradient Descent!', color=BLUE)
        self.line2.move_to(4*RIGHT + 3*DOWN)
        self.play(Write(self.line1))
        self.wait(3)
        self.play(Transform(self.line1, self.line2))


    def construct(self):
        # initialise
        print('initialising...')
        self.initialise()
        np.random.seed(17)
        self.randomise()
        self.evaulate()
        self.create()

        # draw network
        print('drawing...')
        self.draw()

        # draw network
        print('text...')
        self.text()

        # wait at the end of each slide
        self.wait(30)


#########################################################################################
###
### SECTION 3.4
###
#########################################################################################


class NeuralNetworkApplications(Scene):

    def initialise(self):
        self.size = [60,20,20,20,10,1] # must have even number of elements

        self.weights = []
        for i in range(0, len(self.size) - 1):
            w = np.ones(shape=(self.size[i], self.size[i+1]))
            self.weights.append(w)

        self.biases = []
        for i in range(1, len(self.size)):
            b = np.ones(shape=(self.size[i]))
            self.biases.append(b)

        self.values = []
        for i in range(0, len(self.size)):
            v = np.ones(shape=(self.size[i]))
            self.values.append(v)

        self.scale = 0.1


    def randomise(self):
        for i,w in enumerate(self.weights):
            r = np.random.random(size=w.shape)
            self.weights[i] = 2.0*r - 1.0

        for i,b in enumerate(self.biases):
            r = np.random.random(size=b.shape)
            self.biases[i] = 2.0*r - 1.0

        self.values[0] = np.random.random(size=self.values[0].shape)


    def evaulate(self):
        for i in range(1, len(self.size)):
             v = np.dot(self.weights[i-1].T, self.values[i-1]) + self.biases[i-1]
             self.values[i] = self.activation(v)


    def activation(self, x):
        return 1.0 / (1.0 + np.exp(-1.0*x))


    def frame(self, point, s=1.0):
        p = point*self.scale*s
        return p


    def value_to_color(self, value, type):
        if type == 'node':
            color = rgb_to_color((value, value, value))
        if type == 'connection':
            if value >= 0:
                color = rgb_to_color((0, value, 0))
            else:
                color = rgb_to_color((-value, 0, 0))
        return color


    def create(self):
        self.layers = []
        for i in range(len(self.size)):
            layer = []
            for j in range(self.size[i]):
                x = self.frame(1.0*(float(i) - float(len(self.size)-1)/2.0), s=10.0)
                y = self.frame(-1.0*(float(j) - float(self.size[i]-1)/2.0))
                node = Circle(color=WHITE, fill_color=self.value_to_color(self.values[i][j], type='node'), fill_opacity=1, radius=self.scale/5, x=x, y=y, stroke_width=self.scale)
                z = 0
                node.move_to([x,y,z])
                layer.append(node)
            self.layers.append(layer)

        self.nets = []
        for i,w in enumerate(self.weights):
            net = []
            for j in range(w.shape[0]):
                for k in range(w.shape[1]):
                    start = np.array([self.layers[i][j].x + self.layers[i][j].radius, self.layers[i][j].y, 0])
                    end = np.array([self.layers[i+1][k].x - self.layers[i+1][k].radius, self.layers[i+1][k].y, 0])
                    color = self.value_to_color(w[j,k], type='connection')
                    line = Line(start, end, color=color, stroke_width=self.scale)
                    net.append(line)
            self.nets.append(net)


    def draw(self):
        for l in self.layers:
            layer_v = VGroup(*l)
            self.play(ShowCreation(layer_v))

        for n in self.nets:
            net_v = VGroup(*n)
            self.play(ShowCreation(net_v))


    def text(self):
        self.line1 = TextMobject('Applications: Hand Writing Recognition', color=ORANGE)
        self.line1.move_to(3.4*DOWN)
        self.line2 = TextMobject('Applications: Chess', color=ORANGE)
        self.line2.move_to(3.4*DOWN)
        self.line3 = TextMobject('Applications: Solving Schrodinger Equation', color=ORANGE)
        self.line3.move_to(3.4*DOWN)
        self.line4 = TextMobject('Applications: Total Energies of Molecules', color=ORANGE)
        self.line4.move_to(3.4*DOWN)
        self.play(Write(self.line1))
        self.wait(3)
        self.play(Transform(self.line1, self.line2))
        self.wait(3)
        self.play(Transform(self.line1, self.line3))
        self.wait(3)
        self.play(Transform(self.line1, self.line4))


    def construct(self):
        # initialise
        print('initialising...')
        self.initialise()
        np.random.seed(17)
        self.randomise()
        self.evaulate()
        self.create()

        # draw network
        print('drawing...')
        self.draw()
        self.wait(3)

        # draw text
        print('text...')
        self.text()

        # wait at the end of each slide
        self.wait(3)


#########################################################################################
###
### SECTION 4.1
###
#########################################################################################


class EvolutionIntro(Scene):

    def initialise(self):
        self.line1 = TextMobject("Regression")
        self.line2 = TextMobject("Neural Networks")
        self.line3 = TextMobject("Evolutionary Algorithms")
        self.line4 = TextMobject("Applications")
        self.line1.move_to(4*LEFT + 3*UP)
        self.line2.move_to(4*LEFT + 0*UP)
        self.line3.move_to(4*LEFT + 3*DOWN)
        self.line4.move_to(4*RIGHT + 0*UP)

        self.box = Rectangle(height=0.5, width=3)
        self.box.surround(self.line3)

        self.arrow_1 = Arrow(1*LEFT + 3*UP, 2.7*RIGHT+0.3*UP)
        self.arrow_2 = Arrow(1*LEFT + 0*UP, 2.7*RIGHT)
        self.arrow_3 = Arrow(1*LEFT + 3*DOWN, 2.7*RIGHT+0.3*DOWN)


    def animation1(self):
        self.add(self.line1)
        self.add(self.line2)
        self.add(self.line3)
        self.add(self.line4)
        self.add(self.arrow_1)
        self.add(self.arrow_2)
        self.add(self.arrow_3)


    def animation2(self):
        self.play(ShowCreation(self.box))


    def construct(self):

        # initialise
        print('initialising...')
        self.initialise()

        # animation 1
        print('animation 1...')
        self.animation1()
        self.wait(3)

        # animation 2
        print('animation 2...')
        self.animation2()
        self.wait(3)


#########################################################################################
###
### SECTION 4.2
###
#########################################################################################


class EvolutionFlow(Scene):

    def initialise(self):
        self.line1 = TextMobject("Initial Population")
        self.line2 = TextMobject("Compete")
        self.line3 = TextMobject("Select")
        self.line4 = TextMobject("Breed")
        self.line5 = TextMobject("Mutate")
        self.line1.move_to(3*UP)
        self.line2.next_to(self.line1, 4*DOWN)
        self.line3.next_to(self.line2, 4*DOWN)
        self.line4.next_to(self.line3, 4*DOWN)
        self.line5.next_to(self.line4, 4*DOWN)


        self.arrow_1 = Arrow(ORIGIN, DOWN)
        self.arrow_2 = Arrow(ORIGIN, DOWN)
        self.arrow_3 = Arrow(ORIGIN, DOWN)
        self.arrow_4 = Arrow(ORIGIN, DOWN)
        self.arrow_1.next_to(self.line1, DOWN)
        self.arrow_2.next_to(self.line2, DOWN)
        self.arrow_3.next_to(self.line3, DOWN)
        self.arrow_4.next_to(self.line4, DOWN)


    def animation1(self):
        self.play(Write(self.line1))
        self.play(ShowCreation(self.arrow_1))
        self.play(Write(self.line2))
        self.play(ShowCreation(self.arrow_2))
        self.play(Write(self.line3))
        self.play(ShowCreation(self.arrow_3))
        self.play(Write(self.line4))
        self.play(ShowCreation(self.arrow_4))
        self.play(Write(self.line5))


    def construct(self):

        # initialise
        print('initialising...')
        self.initialise()

        # animation 1
        print('animation 1...')
        self.animation1()
        self.wait(3)


#########################################################################################
###
### SECTION 5.1
###
#########################################################################################


class Summary(Scene):

    def initialise(self):
        self.scale1 = 0.3
        self.scale2 = 4.2
        self.scale3 = 1.5
        self.line = TextMobject("Summary")
        self.line.move_to(3.5*UP)
        self.box1 = Rectangle(height=9*self.scale1, width=16*self.scale1)
        self.box1.move_to(self.scale3*UP + self.scale2*LEFT)
        self.box2 = Rectangle(height=9*self.scale1, width=16*self.scale1)
        self.box2.move_to(self.scale3*UP + self.scale2*RIGHT)
        self.box3 = Rectangle(height=9*self.scale1, width=16*self.scale1)
        self.box3.move_to(self.scale3*DOWN + self.scale2*LEFT)
        self.box4 = Rectangle(height=9*self.scale1, width=16*self.scale1)
        self.box4.move_to(self.scale3*DOWN + self.scale2*RIGHT)


    def animation1(self):
        self.play(Write(self.line))
        self.play(ShowCreation(self.box1), ShowCreation(self.box2), ShowCreation(self.box3), ShowCreation(self.box4))


    def construct(self):

        # initialise
        print('initialising...')
        self.initialise()

        # animation 1
        print('animation 1...')
        self.animation1()
        self.wait(50)
