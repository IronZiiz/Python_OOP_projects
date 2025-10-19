from typing import Dict, List, Optional
from .storage import load_data, save_data

def adicionar(nome: str, categoria: str) -> None:
    """Adiciona um novo restaurante ao armazenamento.

    Inputs:
        nome (str): Nome único do restaurante.
        categoria (str): Categoria culinária do restaurante.

    Returns:
        None.
    """
    restaurantes = load_data()
    restaurantes.append({"nome": nome, "categoria": categoria, "ativo": False})
    save_data(restaurantes)

def listar() -> List[Dict[str, object]]:
    """Retorna todos os restaurantes persistidos.

    Inputs:
        Nenhum.

    Returns:
        List[Dict[str, object]]: Registros no formato
        {"nome": str, "categoria": str, "ativo": bool}.
    """
    return list(load_data())

def alternar_status(nome: str) -> bool:
    """Alterna o campo 'ativo' de um restaurante (True/False).

    Inputs:
        nome (str): Nome do restaurante a ser atualizado.

    Returns:
        bool: True se o registro foi encontrado e atualizado; False caso contrário.
    """
    restaurantes = load_data()
    for restaurante in restaurantes:
        if restaurante.get("nome") == nome:
            restaurante["ativo"] = not bool(restaurante.get("ativo"))
            save_data(restaurantes)
            return True
    return False

def buscar_por_nome(nome: str) -> Optional[Dict[str, object]]:
    """Busca um restaurante pelo nome exato.

    Inputs:
        nome (str): Nome a ser procurado.

    Returns:
        Optional[Dict[str, object]]: Registro encontrado ou None se não existir.
    """
    for restaurante in load_data():
        if restaurante.get("nome") == nome:
            return restaurante
    return None

def excluir(nome: str) -> bool:
    """Exclui um restaurante pelo nome.

    Inputs:
        nome (str): Nome do restaurante a ser excluído.

    Returns:
        bool: True se o registro foi encontrado e excluído; False caso contrário.
    """
    restaurantes = load_data()
    for idx, restaurante in enumerate(restaurantes):
        if restaurante.get("nome") == nome:
            del restaurantes[idx]
            save_data(restaurantes)
            return True
    return False
