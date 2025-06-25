from typing import Optional
from pathlib import Path
import argparse

def display_tree(path: Path, prefix: str = "", ignore_hidden: bool = False, max_depth: Optional[int] = None, current_depth: int = 0) -> None:
    """
    Рекурсивно отображает структуру директорий в стиле команды tree.
    
    Args:
        path: Путь к текущей директории
        prefix: Префикс для вывода (используется для отступов)
        ignore_hidden: Игнорировать ли скрытые файлы и директории
        max_depth: Максимальная глубина обхода дерева (None для неограниченной глубины)
        current_depth: Текущая глубина обхода
    """
    # Проверяем, не превышена ли максимальная глубина
    if max_depth is not None and current_depth > max_depth:
        return
    
    # Получаем список всех элементов в директории
    items = sorted(path.iterdir())
    
    # Фильтруем скрытые файлы, если нужно
    if ignore_hidden:
        items = [item for item in items if not item.name.startswith(".")]
    
    for i, item in enumerate(items):
        # Проверяем, последний ли это элемент в директории
        is_last = (i == len(items) - 1)
        
        # Выводим текущий элемент
        print(prefix + ("└── " if is_last else "├── ") + item.name)
        
        # Рекурсивно вызываем функцию для поддиректорий
        if item.is_dir():
            # Если достигли максимальной глубины, но все еще есть директории,
            # показываем многоточие для указания на то, что дерево обрезано
            if max_depth is not None and current_depth == max_depth:
                new_prefix = prefix + ("    " if is_last else "│   ")
                print(new_prefix + "...")
            else:
                display_tree(
                    item,
                    prefix + ("    " if is_last else "│   "),
                    ignore_hidden,
                    max_depth,
                    current_depth + 1
                )

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
    parser.add_argument(
        "-d",
        "--max-depth",
        type=int,
        default=None,
        help="Maximum depth of the directory tree to display. Default is unlimited.",
    )
    
    args = parser.parse_args()
    
    root = Path(args.path)
    if not root.exists():
        print(f"Ошибка: Директория '{args.path}' не существует.")
        return
    
    print(root.name)
    display_tree(
        root, 
        ignore_hidden=args.ignore_hidden, 
        max_depth=args.max_depth
    )

if __name__ == "__main__":
    main()