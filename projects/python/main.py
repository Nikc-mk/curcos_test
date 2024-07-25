#####################
# Welcome to Cursor #
#####################


"""
Step 1: Try generating with Cmd+K or Ctrl+K on a new line. Ask for CLI-based game of TicTacToe.

Step 2: Hit Cmd+L or Ctrl+L and ask the chat what the code does. 
   - Then, try running the code

Step 3: Try highlighting all the code with your mouse, then hit Cmd+k or Ctrl+K. 
   - Instruct it to change the game in some way (e.g. add colors, add a start screen, make it 4x4 instead of 3x3)

Step 4: To try out cursor on your own projects, go to the file menu (top left) and open a folder.
"""

import pandas as pd
import vertica_python
import shutil
import os
from datetime import datetime

# Параметры подключения к Vertica
conn_info = {
    "host": "your_vertica_host",
    "port": 5433,
    "user": "your_username",
    "password": "your_password",
    "database": "your_database",
    "autocommit": True,
}

# Путь к Excel файлу и папке архива
excel_file_path = "path/to/your/file.xlsx"
archive_folder = "path/to/archive/folder"

# Чтение данных из Excel файла
df = pd.read_excel(excel_file_path)

# Подключение к Vertica и загрузка данных
with vertica_python.connect(**conn_info) as connection:
    cursor = connection.cursor()
    for index, row in df.iterrows():
        values = tuple(row)
        placeholders = ", ".join(["%s"] * len(values))
        cursor.execute(f"INSERT INTO your_table_name VALUES ({placeholders})", values)

# Перемещение файла в папку архив с добавлением времени и даты загрузки
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
archive_file_path = os.path.join(archive_folder, f"file_{timestamp}.xlsx")
shutil.move(excel_file_path, archive_file_path)

print("Данные успешно загружены и файл перемещен в архив.")
