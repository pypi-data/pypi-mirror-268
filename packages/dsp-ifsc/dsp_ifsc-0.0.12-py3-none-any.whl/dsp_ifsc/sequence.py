import numpy
from typing import Tuple


def impulse(position: int, n_start: int, n_end: int) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """
    Generates x(n) = delta(n - n0); n_start <= n <= n_end
    Args:
        position: The position of the impulse.
        n_start: The start of the sequence.
        n_end: The end of the sequence.

    Returns:
        x: The impulse sequence.
        n: The sequence of n values from n_start to n_end.
    """

    n = numpy.arange(n_start, n_end + 1)
    x = (n == position).astype(int)

    return x, n


def step(position: int, n_start: int, n_end: int) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """
    Generates x(n) = u(n - n0); n_start <= n <= n_end
    Args:
        position: The position of the step.
        n_start: The start of the sequence.
        n_end: The end of the sequence.

    Returns:
        x: The step sequence.
        n: The sequence of n values from n_start to n_end.
    """

    n = numpy.arange(n_start, n_end + 1)
    x = ((n - position) >= 0).astype(int)

    return x, n


def ramp(slope: float, position: int, n_start: int, n_end: int) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """
    Generates x(n) = (n - n0) * a; n_start <= n <= n_end
    Args:
        slope: The slope of the ramp.
        position: The position of the ramp.
        n_start: The start of the sequence.
        n_end: The end of the sequence.

    Returns:
        x: The ramp sequence.
        n: The sequence of n values from n_start to n_end.
    """

    n = numpy.arange(n_start, n_end + 1)
    x = (n - position) * slope

    return x, n


def exponential(amplitude: float, alpha: float, position: int, n_start: int, n_end: int) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """
    Generates x(n) = a * exp(-b * (n - n0)); n_start <= n <= n_end
    Args:
        amplitude: The amplitude of the exponential.
        decay: The decay of the exponential.
        position: The position of the exponential.
        n_start: The start of the sequence.
        n_end: The end of the sequence.

    Returns:
        x: The exponential sequence.
        n: The sequence of n values from n_start to n_end.
    """

    n = numpy.arange(n_start, n_end + 1)
    x = amplitude * numpy.exp(alpha * (n - position))

    return x, n


def sine(amplitude: float, omega: float, phase: float, n_start: int, n_end: int) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """
    Generates x(n) = a * cos(w * n + p); n_start <= n <= n_end
    Args:
        amplitude: The amplitude of the sinusoidal.
        omega: The frequency of the sinusoidal.
        phase: The phase of the sinusoidal.
        n_start: The start of the sequence.
        n_end: The end of the sequence.

    Returns:
        x: The sinusoidal sequence.
        n: The sequence of n values from n_start to n_end.
    """

    n = numpy.arange(n_start, n_end + 1)
    x = amplitude * numpy.sin(omega * n + phase)

    return x, n


def cosine(amplitude: float, omega: float, phase: float, n_start: int, n_end: int) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """
    Generates x(n) = a * cos(w * n + p); n_start <= n <= n_end
    Args:
        amplitude: The amplitude of the cosine.
        omega: The frequency of the cosine.
        phase: The phase of the cosine.
        n_start: The start of the sequence.
        n_end: The end of the sequence.

    Returns:
        x: The cosine sequence.
        n: The sequence of n values from n_start to n_end.
    """

    n = numpy.arange(n_start, n_end + 1)
    x = amplitude * numpy.cos(omega * n + phase)

    return x, n
