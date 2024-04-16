from typing import Self, Optional, Callable
# External
import numpy
# Signals
from dsp_ifsc.signal import Signal


class System:
    """
    The System class represents a system.

    Attributes:
        system: The system function.
        rng: The random number generator.
    """

    def __init__(self, system: Callable[[Signal], Signal]):
        """
        Initializes the System class.

        Args:
            system: The system function.
        """

        self.sys = system

        self.rng = numpy.random.default_rng(seed = 42)


    # Properties

    @property
    def is_linear(self) -> bool:
        """
        Returns:
            bool: True if the system is linear, False otherwise.
        """

        n = numpy.arange(100)
        x1 = Signal(self.rng.random(len(n)), n)
        x2 = Signal(numpy.sqrt(10) * self.rng.standard_normal(len(n)), n)

        y1 = self.sys(x1)
        y2 = self.sys(x2)

        y = self.sys(x1 + x2)

        return numpy.sum(numpy.abs(y.x - (y1.x + y2.x))) < 1e-5

    @property
    def is_time_invariant(self) -> bool:
        """
        Returns:
            bool: True if the system is time-invariant, False otherwise.
        """

        n = numpy.arange(-100, 100)
        x = Signal(self.rng.random(len(n)), n)

        total_diff_x = 0.0
        total_diff_n = 0.0
        for i in range(-20, 20):
            rnd_shift = self.rng.random() * i
            y1 = self.sys(x) << rnd_shift
            y2 = self.sys(x << rnd_shift)

            total_diff_x += numpy.sum(numpy.abs(y1.x - y2.x))
            total_diff_n = numpy.sum(numpy.abs(y1.n - y2.n))

        return (total_diff_x + total_diff_n) < 1e-5
