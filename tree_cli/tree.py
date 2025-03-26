from pathlib import Path


def display_tree(path: Path, prefix: str = "") -> None:
    """Рекурсивно отображает структуру директорий в стиле команды tree."""
    # Получаем список всех элементов в директории
    items = list(path.iterdir())
    for i, item in enumerate(items):
        # Проверяем, последний ли это элемент в директории
        is_last = (i == len(items) - 1)
        # Выводим текущий элемент
        print(prefix + ("└── " if is_last else "├── ") + item.name)
        if item.is_dir():
            # Рекурсивно вызываем функцию для поддиректорий
            display_tree(item, prefix + ("    " if is_last else "│   "))


def main(path: str = ".") -> None:
    """Точка входа для команды tree."""
    root = Path(path)
    if not root.exists():
        print(f"Ошибка: Директория '{path}' не существует.")
        return
    print(root.name)
    display_tree(root)
