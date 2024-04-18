"""Enums del proyecto."""

from enum import Enum, IntEnum


class Unidades(Enum):
    """Unidades dispobibles para el modelo."""

    LB_IN_F = 1
    LB_FT_F = 2
    KIP_IN_F = 3
    KIP_FT_F = 4
    KN_MM_C = 5
    KN_M_C = 6
    KGF_MM_C = 7
    KGF_M_C = 8
    N_MM_C = 9
    N_M_C = 10
    TON_MM_C = 11
    TON_M_C = 12
    KN_CM_C = 13
    KGF_CM_C = 14
    N_CM_C = 15
    TON_CM_C = 16


class LoadPatternType(IntEnum):
    """Load patterns types."""

    DEAD = 1
    SUPER_DEAD = 2
    LIVE = 3
