"""Script para rescatar las reacciones desde un modelo etabs a un archivo excel."""

from etabs_sdk import Etabs

# def obtener_conexion() -> None:
#     """Funcion para gestionar la conexcion con etabs."""
#     return Etabs()


def obtener_reacciones(modelo: Etabs) -> None:
    """Obtener las reacciones desde etabs.

    Args:
        modelo (Any): Instancia del modelo.
    """
    reacciones = Etabs.obtener_reacciones()


def escribir_excel(reacciones: list[tuple[float]]) -> None:
    """Escribe excel con las reacciones."""
    ...


def main() -> None:
    """Punto de entrada del script."""
    modelo = Etabs()
    reacciones = obtener_reacciones(modelo)
    escribir_excel(recciones)


if __name__ == "__main__":
    main()
