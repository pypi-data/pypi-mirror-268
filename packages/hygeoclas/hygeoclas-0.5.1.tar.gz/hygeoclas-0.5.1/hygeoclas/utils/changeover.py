def rgb_to_matplotlib(rgb: tuple) -> tuple:
    """
    Converts an RGB color to a format that matplotlib can interpret.

    Args:
        rgb (tuple): A tuple of three elements representing the RGB values.

    Returns:
        tuple: A tuple of three elements representing the normalized RGB values (between 0 and 1).
    """
    return tuple(val/255 for val in rgb)