"""Main."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from etabs_sdk import Etabs  # noqa: I001
from etabs_sdk import LoadPatternType

# path = Path("C:\\Users\\User\\Desktop\\Modelo en trabajo\\test.EDB")
# path2 = Path("C:\\Users\\User\\Desktop\\Modelo en trabajo\\test123.EDB")

etabs = Etabs(adjuntar_a_instancia=True)
columnas_tabla = etabs.columnas_tabla("Area Assignments - Pier Labels", printable=True)
datos_tabla = etabs.datos_tabla("Area Assignments - Pier Labels")
print(datos_tabla)

etabs.add_load_pattern("Dead", LoadPatternType.LIVE)

# etabs.abrir_modelo(path)
# etabs.cerrar_modelo()
# etabs = Etabs(modelo_nuevo=True)
