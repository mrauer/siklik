import siklik


def test_compute_variations_simple():
    """Compute a 20% increase."""
    assert siklik.compute_variations(100.0, 120.0) == 20.0


def test_compute_variations_negative():
    """Compute a 20% decrease."""
    assert siklik.compute_variations(100.0, 80.0) == -20.0
