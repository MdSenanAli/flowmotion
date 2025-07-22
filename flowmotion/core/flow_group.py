from manim import *
from ..logger import FlowLogger


class FlowGroup(VGroup):
    # Class-level counters to track total and per-class instances
    _total_count = 0
    _instance_counts = {}

    def __init__(self, *vmobjects, **kwargs):
        super().__init__(*vmobjects, **kwargs)

        # Track which numbered instance this object is
        self.instance_index = self._assign_instance_index()

        # Set up logger and log instantiation
        self.logger = self._setup_logger()
        self.logger.log("Instantiated")

    def _assign_instance_index(self) -> int:
        """
        Assigns and returns a unique index for this instance
        based on its class, to help with logging or identification.
        """
        instantiated_class = self.__class__
        FlowGroup._instance_counts.setdefault(instantiated_class, 0)
        FlowGroup._instance_counts[instantiated_class] += 1
        FlowGroup._total_count += 1
        return FlowGroup._instance_counts[instantiated_class]

    def _setup_logger(self) -> FlowLogger:
        """
        Creates and registers a logger with this instance.
        Returns the configured FlowLogger object.
        """
        logger = FlowLogger()
        logger.register(self)
        return logger
