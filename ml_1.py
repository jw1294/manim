import numpy as np
from big_ol_pile_of_manim_imports import *


class Struct():
    pass


class LinearRegressionStencil(GraphScene):

    def initialise(self):
        # properties of graph 1
        self.g1 = Struct()
        self.g1.graph_origin = ORIGIN + 6*LEFT + 2.5*DOWN
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

        # properties of graph 2
        self.g2 = Struct()
        self.g2.graph_origin = ORIGIN + 2*RIGHT + 2.5*DOWN
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

        # custom values
        self.m_real = 0.8
        self.c_real = 1.0

        # functions to plot
        self.m = [1.0, 0.5, 0.5, 1.0, 0.5, 1.0]
        self.c = [1.0, 0.5, 1.5, 0.0, 2.5, 0.5]
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
        np.random.seed(2)
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


    def construct(self):
        pass


class LinearRegressionRandom(LinearRegressionStencil):

    def construct(self):
        # initialise
        print('initialising...')
        self.initialise()

        # draw axis
        print('drawing axis...')
        self.draw_graph(self.g1)
        self.draw_graph(self.g2)

        # initialise functions and data
        print('creating functions...')
        self.create_functions(self.g1)
        self.create_data(self.g1)
        self.create_point(self.g2)

        # show data
        print('showing data...')
        self.play(FadeIn(self.data))

        # play search animation
        print('playing search animation...')
        self.focus_graph(self.g1)
        placeholder = VectorizedPoint(self.input_to_graph_point(self.center_point, self.function_lines[0]))
        for i, line in enumerate(self.function_lines):
            if i == 0:
                self.play(Transform(placeholder, line, run_time=2), ShowCreation(self.point, run_time=2))
            else:
                self.play(Transform(placeholder, line, run_time=2), ApplyMethod(self.point.move_to,self.gp_to_rp([self.m[i],self.c[i],0],self.g2), run_time=2))
            wait(1)
