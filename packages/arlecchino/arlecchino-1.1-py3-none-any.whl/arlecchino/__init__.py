# %%
import random
from pathlib import PurePath
import hashlib

# %%
__COLORS: tuple[str]
__SHADES: tuple[str]

__root = PurePath(__file__).parent

with open(__root.joinpath("colors.txt"), "rt") as __f:
    __COLORS = tuple(e.strip() for e in __f.readlines())

with open(__root.joinpath("shades.txt"), "rt") as __f:
    __SHADES = tuple(e.strip() for e in __f.readlines())


__NC, __NS = len(__COLORS), len(__SHADES)


def draw(
    value: int | bytes | bytearray,
    seed: int | bytes | bytearray | None = 42,
) -> str:
    if isinstance(value, int):
        value = int.to_bytes(value)

    if isinstance(seed, int):
        seed = int.to_bytes(seed)

    m = hashlib.sha3_224()
    m.update(value)
    m.update(seed)
    value = int.from_bytes(m.digest())

    random.seed(seed)
    __colors = random.sample(__COLORS, __NC)
    __shades = random.sample(__SHADES, __NS)

    color = __colors[value // __NS % __NC]
    shade = __shades[value % __NS]

    return f"{color} {shade}"


# %%
