from pathlib import Path
import argparse

def display_tree(path: Path, prefix: str = "", ignore_hidden: bool = False) -> None:
    """Рекурсивно отображает структуру директорий в стиле команды tree."""
    # Получаем список всех элементов в директории
    items = sorted(path.iterdir())
    
    for i, item in enumerate(items):
        # Игнорируем скрытые файлы и директории, если ignore_hidden=True
        if ignore_hidden and item.name.startswith("."):
            continue
        # Проверяем, последний ли это элемент в директории
        is_last = (i == len(items) - 1)
        # Выводим текущий элемент
        print(prefix + ("└── " if is_last else "├── ") + item.name)
        if item.is_dir():
            # Рекурсивно вызываем функцию для поддиректорий
            display_tree(item, prefix + ("    " if is_last else "│   "), ignore_hidden)

def main() -> None:
    """Точка входа для команды tree."""
    parser = argparse.ArgumentParser(description="Display directory structure in a tree-like format.")
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="The directory to display. Defaults to the current directory.",
    )
    parser.add_argument(
        "-i",
        "--ignore-hidden",
        action="store_true",
        help="Ignore hidden files and directories (those starting with '.').",
    )
    
    args = parser.parse_args()
    
    root = Path(args.path)
    if not root.exists():
        print(f"Ошибка: Директория '{args.path}' не существует.")
        return
    print(root.name)
    display_tree(root, ignore_hidden=args.ignore_hidden)