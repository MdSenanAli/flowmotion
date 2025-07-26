from manim import *
from .flow_motion import FlowMotion


class FlowGroup(FlowMotion, VGroup):
    def __init__(self):
        FlowMotion.__init__(self)
        VGroup.__init__(self)

    def display(self, anim) -> AnimationGroup:
        # Return an animation that writes (displays) the object on screen
        return AnimationGroup(anim(self))

    def show(self) -> AnimationGroup:
        # Return an animation that writes (displays) the object on screen
        return self.display(Write)

    def hide(self) -> AnimationGroup:
        # Return an animation that fades out (hides) the object from screen
        return self.display(FadeOut)

    def choose_text_type(self, value, **kwargs):
        if isinstance(value, (int, float)):
            return Tex(str(value), **kwargs)
        else:
            return Text(str(value), **kwargs).scale(0.7)
