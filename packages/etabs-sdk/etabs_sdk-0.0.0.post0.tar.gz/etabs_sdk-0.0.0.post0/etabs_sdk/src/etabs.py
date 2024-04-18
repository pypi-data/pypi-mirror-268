"""Etabs api."""

import contextlib
from ctypes import ArgumentError
from pathlib import Path
from typing import Any

import comtypes
import comtypes.client
from tabulate import tabulate

from .enums import LoadPatternType, Unidades
from .excepciones import InstanciaActivaNoEncontradaError, ModeloNoEncontradoError, NuevoModeloError


class Etabs:
    """Maneja la comunicación con la API de Etabs."""

    def __init__(self, cerrar_intancia_abierta: bool = False, adjuntar_a_instancia: bool = False) -> None:
        """Método init para la case Etabs."""
        self.etabs_object = self._conectar_etabs(cerrar_intancia_abierta, adjuntar_a_instancia)
        self.model = self.etabs_object.SapModel

    def _conectar_etabs(self, cerrar_instancia_abierta: bool, adjuntar_a_instancia: bool) -> Any:
        """Conectar al modelo indicado o a la instancia activa."""
        if cerrar_instancia_abierta:
            with contextlib.suppress(OSError, comtypes.COMError):
                etabs_object = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
                if etabs_object is not None:
                    etabs_object.ApplicationExit(True)

        helper = comtypes.client.CreateObject("ETABSv1.Helper")
        helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)

        if adjuntar_a_instancia:
            try:
                return helper.GetObject("CSI.ETABS.API.ETABSObject")
            except (OSError, comtypes.COMError) as error:
                raise InstanciaActivaNoEncontradaError(error=error) from error

        try:
            return helper.CreateObjectProgID("CSI.ETABS.API.ETABSObject")
        except Exception as error:
            raise ValueError("No se pudo crear el Objeto Etabs") from error

    def iniciar_modelo(self, unidad: Unidades | None = None) -> None:
        """Inicial el modelo nuevo."""
        try:
            self.etabs_object.ApplicationStart()
            if unidad is not None:
                self.model.InitializeNewModel(unidad.value)
            else:
                self.unidades_del_modelo(Unidades.TON_M_C)
            self.model.File.NewBlank()
        except Exception as error:
            raise NuevoModeloError(error) from error

    def abrir_modelo(self, path: Path) -> None:
        """Abrir modelo etabs dado un path.

        Unidades por defecto Toneladas/Metros/Celsius
        """
        try:
            self.etabs_object.ApplicationStart()
            self.model.File.Openfile(str(path))
            self.unidades_del_modelo(Unidades.TON_M_C)
            self.model.File.Save()
        except Exception as error:
            raise ModeloNoEncontradoError(path=path, error=error) from error

    def cerrar_modelo(self, guardar: bool = True) -> None:
        """Cerrar modelo."""
        valor = self.etabs_object.ApplicationExit(guardar)  # llave true es para guardar antes de salir
        if valor != 0:
            raise TypeError("Error cerrando el modelo")

    def guardar_modelo(self, path: Path | None = None) -> None:
        """Guardar modelo en el directorio indicado."""
        if path is not None:
            valor = self.model.File.Save(str(path))
        else:
            valor = self.model.File.Save()

        if valor != 0:
            raise TypeError("No se pudo guardar el modelo. Verificar si existe el directorio")

    def unidades_del_modelo(self, unidad: Unidades) -> None:
        """Configura las unidades internas del modelo."""
        try:
            self.model.SetPresentUnits(unidad.value)
        except KeyError as error:
            raise ValueError(f"Unidad '{unidad}' no es válida.") from error

    def columnas_tabla(self, tabla: str, printable: bool = False) -> dict:
        """Columnas de una tabla.

        Obtiene y retorna un diccionario con la estructura y metadatos de los campos
        de una tabla específica dentro de un modelo de ETABS. Este método es útil para
        explorar las propiedades de las tablas dentro de un modelo estructural definido
        en ETABS.

        Args:
            tabla (str): Nombre de la tabla dentro del modelo de ETABS de la cual se desean
                        obtener los campos. Este nombre debe corresponder exactamente al
                        identificador de la tabla en el modelo.
            printable (bool, opcional): Si es True, la función imprimirá una tabla formateada
                                        en la consola que resume los campos de la tabla especificada,
                                        incluyendo el nombre del campo, su descripción y unidad.
                                        Por defecto es False.

        Retorna:
            dict: Un diccionario que contiene la versión de la tabla, la cantidad de columnas
                y un diccionario detallado de las columnas, incluyendo el nombre, descripción
                y unidad de cada campo. La estructura es la siguiente:
                {
                    "version_tabla": str,
                    "cantidad_columnas": int,
                    "columnas": {
                        key: {
                            "nombre": str,
                            "descripcion": str,
                            "unidad": str
                        }
                    }
                }

        Efectos secundarios:
            Si `printable` es True, imprime en la consola una tabla con los campos de la tabla
            especificada, utilizando la librería `tabulate` para formatear la salida.

        Ejemplo de uso:
            >>> modelo_etabs.campos_tabla("MiTablaEtabs", printable=True)
            +------+--------+---------------------+-------+
            | Key  | Nombre | Descripción         | Unidad|
            +------+--------+---------------------+-------+
            | id   | ID     | Identificador único |       |
            | nom  | Nombre | Nombre completo     |       |
            +------+--------+---------------------+-------+
        """
        datos = self.model.DatabaseTables.GetAllFieldsInTable(tabla)
        if printable:
            headers = ["Key", "Nombre", "Descripción", "Unidad"]
            tabla_datos = [
                [key, nombre, descripcion, unidad]
                for key, nombre, descripcion, unidad in zip(datos[2], datos[3], datos[4], datos[5], strict=True)
            ]
            print(tabulate(tabla_datos, headers=headers, tablefmt="grid"))

        return {
            "version_tabla": datos[0],
            "cantidad_columnas": datos[1],
            "columnas": {
                key: {"nombre": nombre, "descripcion": descripcion, "unidad": unidad}
                for key, nombre, descripcion, unidad in zip(datos[2], datos[3], datos[4], datos[5], strict=True)
            },
        }

    def datos_tabla(self, tabla: str, columnas: list[str] | None = None) -> dict[str, tuple]:
        """Datos de una tabla.

        Recupera y organiza los datos de una tabla específica dentro de un modelo de ETABS,
        permitiendo la selección opcional de columnas específicas. Este método es útil para
        obtener una vista estructurada de los datos contenidos en una tabla, adaptándose
        dinámicamente a las columnas especificadas por el usuario.

        Args:
            tabla (str): El nombre de la tabla de la cual se desean obtener los datos.
                        Este nombre debe coincidir exactamente con el identificador de
                        la tabla en el modelo.
            columnas (list[str] | None, opcional): Una lista de strings que especifica las
                                                columnas cuyos datos se quieren recuperar.
                                                Si se omite o es None, se recuperarán los
                                                datos de todas las columnas disponibles
                                                en la tabla. Por defecto es None.

        Retorna:
            dict[str, tuple]: Un diccionario que contiene dos pares clave-valor:
                - "columnas": Una lista de los nombres de las columnas recuperadas.
                - "valores": Una tupla de tuplas, donde cada tupla interna representa los
                            valores de una columna específica, en el mismo orden que las
                            columnas enumeradas en "columnas".

        La función primero verifica si se han especificado columnas; de no ser así, utiliza
        el método `columnas_tabla` para obtener todas las columnas disponibles en la tabla.
        Luego, recupera los datos de la tabla especificada, organizando los valores de cada
        columna en tuplas separadas para facilitar el acceso y la manipulación de los datos.

        Ejemplo de uso:
            >>> modelo_etabs.datos_tabla("MiTablaEtabs", columnas=["ID", "Nombre"])
            {
                "columnas": ["ID", "Nombre"],
                "valores": (("1", "2", "3"), ("Alice", "Bob", "Charlie"))
            }
        """
        if columnas is None:
            datos_columnas = self.columnas_tabla(tabla)
            columnas = datos_columnas["columnas"].keys()

        datos = self.model.DatabaseTables.GetTableForDisplayArray(tabla, columnas, "")
        ncol = len(columnas)
        return {
            "columnas": datos[0],
            "valores": tuple(datos[4][col::ncol] for col in range(ncol)),
        }

    def add_load_pattern(
        self,
        name: str,
        load_pattern_type: LoadPatternType,
        multiplier: float | None = None,
        add_case: bool | None = None,
    ) -> None:
        """Add new load pattern to model.

        Args:
            name (str): Name of the load pattern
            load_pattern_type (LoadPatternType): Load Pattern type
            multiplier (float | None, optional): Load Pattern multiplier. Defaults to 0.
            add_case (bool | None, optional): Flag for adding Load Case. Defaults to True.

        Raises:
            ValueError:If load pattern culd not be added
            Exception: If an unkwnown exception ocurrs
        """
        if multiplier is None:
            multiplier = 0

        if add_case is None:
            add_case = True

        try:
            value = self.model.LoadPatterns.Add(name, load_pattern_type, multiplier, add_case)
            if value != 0:
                raise ValueError(f"The load pattern could not be added: {name}")

        except Exception as error:
            # sourcery skip: raise-specific-error
            raise Exception from error
