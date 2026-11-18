"""Punto de entrada: ``python -m sistemarural``."""
import os
from pathlib import Path

from .almacen import AlmacenJSON
from .centro_salud import CentroSalud
from .consola import InterfazConsola
from .excepciones import SistemaRuralError
from .seguridad import GestorSeguridad


def principal() -> None:
    carpeta = Path(
        os.environ.get(
            "SISTEMARURAL_DATOS",
            Path(__file__).resolve().parents[2] / "datos",
        )
    )
    try:
        seguridad = GestorSeguridad(carpeta / "sal.bin")
        almacen = AlmacenJSON(carpeta / "centro.json")
        centro = CentroSalud.obtener_instancia(seguridad, almacen)
    except SistemaRuralError as error:
        print(f"No se pudo iniciar el sistema: {error}")
        return
    InterfazConsola(centro).ejecutar()


if __name__ == "__main__":
    principal()