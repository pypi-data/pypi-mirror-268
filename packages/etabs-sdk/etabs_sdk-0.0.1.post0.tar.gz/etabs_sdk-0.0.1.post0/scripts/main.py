"""Main."""

import sys
from pathlib import Path


sys.path.append(str(Path(__file__).parent.parent))

from etabs_sdk import Etabs  # noqa: I001
from etabs_sdk import LoadPatternType, TipoDeCombinacion, CasoOCombinacion

path = Path(r"C:\Users\User\Google Drive\software\iec\etabs-sdk\edificio_prueba\test.EDB")
etabs = Etabs(adjuntar_a_instancia=True)
etabs.abrir_modelo(path=Path())

# etabs.add_load_pattern("PP", LoadPatternType.DEAD, multiplier=1)
# etabs.add_load_pattern("SC", LoadPatternType.LIVE)

# etabs.agregar_combinacion("C01", [("PP", "SC"), (1.4, 0.9)])
etabs.agregar_combinacion(
    "C02",
    TipoDeCombinacion.ABSOLUTE_ADDITIVE,
    [("PP", 0.99, CasoOCombinacion.LOAD_CASE), ("C01", 2.9, CasoOCombinacion.LOAD_COMBO)],
)
