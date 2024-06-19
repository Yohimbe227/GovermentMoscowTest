import json


def print_json(file_path: str, indent: int = 0) -> None:
    """
    Загружает JSON-данные из файла, проверяет и выводит их содержимое с
    использованием рекурсивного вывода в виде ключ-значение с отступами для
    вложенных структур.

    Args:
        file_path: Путь к файлу JSON.
        indent: Уровень отступа для вложенных структур(по умолчанию 0).
    """
    def _print_json(data: dict, current_indent: int) -> None:
        """
        Рекурсивная функция для вывода JSON-данных в формате ключ-значение
        с отступами.

        Args:
            data: JSON-объект, представленный в виде словаря.
            current_indent: Текущий уровень отступа.
        """
        indent_str = "\t" * current_indent
        for key, value in data.items():
            if isinstance(value, dict):
                print(f"{indent_str}{key}:")
                _print_json(value, current_indent + 1)
            else:
                print(f"{indent_str}{key}: {value}")

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            _print_json(data, indent)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Ошибка: {e}")
        return


def main() -> None:
    """
    Выполняет загрузку JSON-данных из файла и вызов функции print_json для их
    вывода.
    """
    print_json("data.json")


if __name__ == "__main__":
    main()
