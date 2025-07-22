from manim import *
from .flow_group import FlowGroup


class FlowPointer(FlowGroup):
    def __init__(self, label, direction=UP):
        super().__init__()
        self.logger.log(f"Direction: {direction}")
        self.logger.log(f"Label: {label}")

        self.direction = direction
        self.label = Tex(str(label))
        self.arrow = Vector(normalize(direction) * 0.8, color=YELLOW)

        self.group = VGroup(self.arrow, self.label)
        self.group.arrange(-1 * self.direction, buff=0.2)
        self.add(self.group)

        self.move_to(ORIGIN)

    def place(self, mobject: Mobject):
        """
        Move the pointer to point to a specific mobject.
        """
        target_pos = mobject.get_edge_center(-self.direction)
        pointer_pos = self.arrow.get_end()
        shift_vector = target_pos - pointer_pos
        return self.shift(shift_vector).shift(-normalize(self.direction) * 0.2)

    def point_to(self, mobject: Mobject):
        """
        Animate the pointer to point to a specific mobject.
        """
        return AnimationGroup(self.animate.place(mobject))
