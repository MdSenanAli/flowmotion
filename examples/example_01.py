import os
from flowmotion import *


class Example(FlowScene):
    def construct(self):
        flow, wait = self.flow, self.wait
        self.add_title("writing this file itself")

        code = FlowCode(os.path.abspath(__file__))

        for elem in code:
            flow(elem.show())
            wait()
            flow(elem.hide())


scene = Example()
scene.render()
