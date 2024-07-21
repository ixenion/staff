from pathlib import Path

# Создание папки с указанием параметров parents и exist_ok
# Если параметр parents установлен в True, то любые отсутствующие
# родительские папки будут созданы по мере необходимости.
# Если параметр exist_ok установлен в True, то исключения типа FileExistsError
# будут проигнорированы, если целевая папка уже существует.
path = Path("/my/directory")
path.mkdir(parents=True, exist_ok=True)
