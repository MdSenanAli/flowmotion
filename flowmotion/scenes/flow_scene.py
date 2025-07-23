from manim import *


class FlowScene(Scene):
    def __init__(self, **kwargs):
        self.ribbon_color = "#121212"
        config.background_color = "#181818"
        config.pixel_width = 1920
        config.pixel_height = 1080
        config.verbosity = "ERROR"
        config.progress_bar = "none"

        super().__init__(**kwargs)

        self.ribbon = None
        self.hamburger = None
        self.title = None

        self.colors = {"RED": "#FF5F56", "YELLOW": "#FFBD2E", "GREEN": "#27C93F"}

        self.ribbon = self.add_ribbon()
        self.hamburger = self.add_hamburger()

    def add_ribbon(self):
        width = config.frame_width
        ribbon = Rectangle(
            width=width, height=0.5, color=self.ribbon_color, fill_opacity=1
        )
        ribbon.shift(UP * (config.frame_height / 2 - ribbon.height / 2))
        self.add(ribbon)
        return ribbon

    def add_hamburger(self):
        group = VGroup()
        for _, color in self.colors.items():
            circle = Circle(radius=0.06, color=color, fill_opacity=1)
            group.add(circle)

        group.arrange(RIGHT, buff=0.175)
        group.to_corner(UL, buff=0.2).shift(RIGHT * 0.1)
        self.add(group)
        return group

    def add_title(
        self, title="Sample Video Preview Title", custom_font="JetBrains Mono"
    ):
        if self.ribbon:
            title_text = Text(rf"{title.upper()}", font=custom_font, color="#DFDCD3")
            title_text.move_to(self.ribbon).scale_to_fit_height(0.125)
            self.title = title_text
            self.add(self.title)
