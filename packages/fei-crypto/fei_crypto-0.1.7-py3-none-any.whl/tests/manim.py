from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class Basic(Scene):
    def __init__(self, t: str):
        # config["frame_height"] = config["frame_height"]/2
        # config["frame_width"] = config["frame_width"] / 2
        # config["pixel_width"] = config["pixel_width"] / 2
        config["pixel_width"] = 900
        config["pixel_height"] = 160

        super().__init__()
        t2c_dict: dict = {}
        for i, c in enumerate(t):
            if c != ' ':
                r_color = random_color()
                if str(r_color) == '#000000':
                    r_color = '#ffffff'

                t2c_dict['[{0}:{1}]'.format(i, i + 1)] = r_color

        mtext = Text(t, t2c=t2c_dict, fill_opacity=1, weight='BOLD')
        self.play(Create(mtext))
        self.play(mtext.animate.scale(2))

        self.wait()


class Dz(Scene):
    def construct(self):
        text1 = Text(
            'Disneyland', font_size=60)
        text2 = Text(
            'Disneyland', font_size=60)
        self.play(Write(text2.shift(DOWN * 1)), Create(text1))
        self.wait()


if __name__ == '__main__':
    text = "1000PEOPLE-USDT"
    with tempconfig(
            {'quality': 'low_quality', 'preview': True, 'output_file': '2', 'format': 'gif'}):
        scene = Basic(t=text)
        scene.render()
