from big_ol_pile_of_manim_imports import *


class Shapes(Scene):
    #A few simple shapes
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=BLUE)
        #line=Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]), color=BLUE)

        #self.add(line)
        self.play(GrowFromCenter(circle))
        self.play(Transform(circle,square))
        self.remove(circle)
        self.play(Transform(square,triangle))
        self.remove(square)
        self.play(ApplyMethod(triangle.next_to,circle,UP))


class MoreShapes(Scene):
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse=Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        print(UP,DOWN,LEFT,RIGHT)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)
        self.play(GrowArrow(arrow))
        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))


class ArrowField(Scene):
    def construct(self):
        # create list of arrows
        N = 10
        arrows = []
        start = LEFT*5.0
        a0 = Arrow(start, start+UP+RIGHT)
        arrows.append(a0)
        for n in range(1, N):
            a = Arrow(ORIGIN, UP+RIGHT)
            a.next_to(arrows[n-1], RIGHT)
            arrows.append(a)

        # show arrows
        self.play(tupleGrowArrow(tuple(arrows)))


class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        first_line=TextMobject("Writing with manim is fun")
        second_line=TextMobject("and easy to do!")
        second_line.next_to(first_line,DOWN)
        third_line=TextMobject("for me and you!")
        third_line.next_to(first_line,DOWN)

        self.add(first_line, second_line)
        self.wait(2)
        self.play(Transform(second_line,third_line))
        self.wait(2)
        self.remove(second_line)
        self.play(ApplyMethod(first_line.shift,3*UP),ApplyMethod(third_line.shift,2*DOWN))


class AddingMoreText(Scene):
    #Playing around with text properties
    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)
        author=TextMobject("-Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)

        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote,quote2),
          ApplyMethod(author.move_to,quote2.get_corner(DOWN+RIGHT)+DOWN+2*LEFT))

        # self.play(ApplyMethod(author.scale,1.5))
        # author.match_color(quote2)
        self.play(FadeOut(quote), FadeOut(author))


class RotateAndHighlight(Scene):
    #Rotation of text and highlighting with surrounding geometries
    def construct(self):
        square=Square(side_length=5,fill_color=YELLOW, fill_opacity=1)
        label=TextMobject("Text at an angle")
        label.bg=BackgroundRectangle(label,fill_opacity=1)
        label_group=VGroup(label.bg,label)  #Order matters
        label_group.rotate(TAU/8)
        label2=TextMobject("Boxed text",color=BLACK)
        label2.bg=SurroundingRectangle(label2,color=BLUE,fill_color=RED, fill_opacity=.5)
        label2_group=VGroup(label2,label2.bg)
        label2_group.next_to(label_group,DOWN)
        label3=TextMobject("Rainbow")
        label3.scale(2)
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        label3.to_edge(DOWN)

        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))


class BasicEquations(Scene):
    #A short script showing how to use Latex commands
    def construct(self):
        eq11=TexMobject(r"G = G_0 + G_0 \Sigma ")
        eq12=TexMobject(r"G")
        eq22=TexMobject(r"G_0 + ")
        eq23=TexMobject(r"\dots")
        eq33=TexMobject(r"G_0 \Sigma G_0 + \dots")

        eq12.next_to(eq11,RIGHT)
        eq22.next_to(eq11,RIGHT)
        eq23.next_to(eq22,RIGHT)
        eq33.next_to(eq22,RIGHT)

        eq12.shift(0.03*UP)
        eq22.shift(0.02*UP + 0.1*LEFT)
        eq23.shift(0.02*UP + 0.1*LEFT)
        eq33.shift(0.02*UP + 0.1*LEFT)

        self.play(Write(eq11), Write(eq12))
        self.wait(5)
        self.play(Transform(eq12, eq22), FadeIn(eq23))
        self.wait(5)
        self.play(Transform(eq23, eq33))


class UsingBraces(Scene):
    #Using braces to group text together
    def construct(self):
        eq1A = TextMobject("4x + 3y")
        eq1B = TextMobject("=")
        eq1C = TextMobject("0")
        eq2A = TextMobject("5x -2y")
        eq2B = TextMobject("=")
        eq2C = TextMobject("3")
        eq1B.next_to(eq1A,RIGHT)
        eq1C.next_to(eq1B,RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A,LEFT)
        eq2B.align_to(eq1B,LEFT)
        eq2C.align_to(eq1C,LEFT)

        eq_group=VGroup(eq1A,eq2A)
        braces=Brace(eq_group,LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces),Write(eq_text))


class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),
    }
    def construct(self):
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        func_graph2=self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label = "\\cos(x)")
        graph_lab2=self.get_graph_label(func_graph2,label = "\\sin(x)", x_val=-10, direction=UP/2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU,func_graph)
        two_pi.next_to(label_coord,RIGHT+UP)

        self.play(ShowCreation(func_graph),ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2),ShowCreation(two_pi))

    def func_to_graph(self,x):
        return np.cos(x)

    def func_to_graph2(self,x):
        return np.sin(x)


class PlotData(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 10,
        "y_min" : 0,
        "y_max" : 10,
        "x_axis_width": 6,
        "y_axis_height": 6,
        "graph_origin" : ORIGIN + 6*LEFT + 2.5*DOWN,
        "function_color" : YELLOW ,
        "axes_color" : WHITE,
        "x_labeled_nums" :range(0,12,2),
        "y_labeled_nums" :range(0,12,2),
    }
    def construct(self):
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,color=self.function_color,x_min=0,m_max=10)
        graph_lab=self.get_graph_label(func_graph, label = r"y=mx+c")
        self.play(ShowCreation(func_graph),ShowCreation(graph_lab))

    def func_to_graph(self,x):
        return 0.01*x + 1.0



m = [0.1,0.2,0.3,0.4,0.5,-1,-2]
c = [0,0.5,0.8,0.1,3.0,5.0,8.0]

class ExampleApproximation(GraphScene):
    # define functions


    CONFIG = {
        "function_color" : YELLOW,
        "center_point" : 0,
        "x_min" : 0,
        "x_max" : 10,
        "y_min" : 0,
        "y_max" : 10,
        "graph_origin" : ORIGIN,
        "x_labeled_nums" : range(0,12,2),
        "functions" : [lambda x: m[0]*x + c[0],
            lambda x: m[1]*x + c[1],
            lambda x: m[2]*x + c[2],
            lambda x: m[3]*x + c[3],
            lambda x: m[4]*x + c[4],
            lambda x: m[5]*x + c[5]]
    }

    def construct(self):
        # draw axis
        self.setup_axes(animate=True)

        # build graphs
        graphs = []
        for f in self.functions:
            graphs.append(self.get_graph(f, self.function_color))

        # draw graphs
        placeholder = VectorizedPoint(self.input_to_graph_point(self.center_point, graphs[0]))
        for graph in graphs:
            self.play(Transform(placeholder, graph, run_time=3))
            self.wait(2)
