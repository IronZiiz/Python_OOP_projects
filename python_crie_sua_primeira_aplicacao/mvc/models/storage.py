import json
import os
from typing import Dict, List


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "restaurants.json")

DEFAULT_RESTAURANTS: List[Dict[str, object]] = [
    {"nome": "Elvis Bar", "categoria": "Arabe", "ativo": False},
    {"nome": "Comida Rapida", "categoria": "Fast Food", "ativo": False},
    {"nome": "Japoni", "categoria": "Japonesa", "ativo": False},
    {"nome": "Gaudeiro", "categoria": "Brasileira", "ativo": False},
]


def _ensure_data_dir() -> None:
    """Garante que o diretório de dados exista.

    Inputs:
        Nenhum.

    Returns:
        None.
    """
    if not os.path.isdir(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)


def load_data() -> List[Dict[str, object]]:
    """Carrega a lista de restaurantes do arquivo JSON.

    Inputs:
        Nenhum.

    Returns:
        List[Dict[str, object]]: Lista de restaurantes no formato
        {"nome": str, "categoria": str, "ativo": bool}. Caso o arquivo
        não exista ou esteja inválido, retorna uma cópia de DEFAULT_RESTAURANTS.
    """
    _ensure_data_dir()
    if not os.path.exists(DATA_FILE):
        return list(DEFAULT_RESTAURANTS)
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return list(DEFAULT_RESTAURANTS)
    except (json.JSONDecodeError, OSError):
        return list(DEFAULT_RESTAURANTS)


def save_data(restaurantes: List[Dict[str, object]]) -> None:
    """Salva a lista de restaurantes no arquivo JSON.

    Inputs:
        restaurantes (List[Dict[str, object]]): Lista de registros no formato
            {"nome": str, "categoria": str, "ativo": bool} a ser persistida.

    Returns:
        None.
    """
    _ensure_data_dir()
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(restaurantes, f, ensure_ascii=False, indent=2)


