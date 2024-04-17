from . import _UTIL_SCRAMBLER, trim

# ------------------------------------------------------------------------------


@trim
def get_bicube_scramble():
    """Returns a scramble for a BiCube, aka Meffert's Bandaged Cube."""
    return _UTIL_SCRAMBLER.call("util_scramble.getBicubeScramble")
