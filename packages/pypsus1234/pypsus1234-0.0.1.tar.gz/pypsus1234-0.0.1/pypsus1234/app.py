

class GetAppplication():
    def __init__(self) -> None:
        self.AppplicationCode = '''import tkinter as tk

# Функция для проверки логина, пароля и роли
def check_credentials():
    login = entry_login.get()
    password = entry_password.get()
    role = role_var.get()
    
    if (login == "admin" and password == "admin" and role == "Администратор"):
        label_result["text"] = "Авторизация успешна. Роль: Администратор"
    elif (login == "user" and password == "user" and role == "Пользователь"):
        label_result["text"] = "Авторизация успешна. Роль: Пользователь"
    elif (login == "guest" and password == "guest" and role == "Гость"):
        label_result["text"] = "Авторизация успешна. Роль: Гость"
    else:
        label_result["text"] = "Неверный логин, пароль или роль"

# Создаем окно приложения
root = tk.Tk()
root.title("Аутентификация")

# Создаем виджеты для ввода логина и пароля
label_login = tk.Label(root, text="Логин:")
label_login.pack()
entry_login = tk.Entry(root)
entry_login.pack()

label_password = tk.Label(root, text="Пароль:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Выбор роли
label_role = tk.Label(root, text="Роль:")
label_role.pack()
roles = ["Администратор", "Пользователь", "Гость"]
role_var = tk.StringVar(root)
role_var.set(roles[0])
role_menu = tk.OptionMenu(root, role_var, *roles)
role_menu.pack()

# Кнопка для отправки данных
btn_login = tk.Button(root, text="Войти", command=check_credentials)
btn_login.pack()

# Метка для вывода результата аутентификации
label_result = tk.Label(root, text="")
label_result.pack()

# Запускаем главный цикл обработки событий
root.mainloop()'''
        self.sql = '''import mysql.connector

def connect_to_database(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Соединение с базой данных установлено")
            return connection
    except mysql.connector.Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Запрос успешно выполнен")
    except mysql.connector.Error as e:
        print(f"Ошибка при выполнении запроса: {e}")

# Пример использования методов
connection = connect_to_database(host="localhost", user="root", password="password", database="mydatabase")

if connection:
    query = "SELECT * FROM users"
    execute_query(connection, query)

    connection.close()
    print("Соединение с базой данных закрыто")
'''
        self.app2 = '''import tkinter as tk

def login():
    input_user = entry_user.get()
    input_password = entry_password.get()
    role = var_role.get()  # Получение выбранной роли

    if input_user == "admin" and input_password == "admin123" and role == "Admin":
        root.destroy()
        admin_window()
    elif input_user == "manager" and input_password == "manager123" and role == "Manager":
        root.destroy()
        manager_window()
    elif input_user == "user" and input_password == "user123" and role == "User":
        root.destroy()
        user_window()
    else:
        label_error.config(text="Неверное имя пользователя, пароль или роль")

def admin_window():
    admin_root = tk.Tk()
    admin_root.title("Администратор")
    admin_root.mainloop()

def manager_window():
    manager_root = tk.Tk()
    manager_root.title("Менеджер")
    manager_root.mainloop()

def user_window():
    user_root = tk.Tk()
    user_root.title("Пользователь")
    user_root.mainloop()

# Создание окна авторизации
root = tk.Tk()
root.title("Форма авторизации")

label_user = tk.Label(root, text="Имя пользователя:")
label_user.pack()
entry_user = tk.Entry(root)
entry_user.pack()

label_password = tk.Label(root, text="Пароль:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

label_role = tk.Label(root, text="Роль:")
label_role.pack()
var_role = tk.StringVar(root)
var_role.set("Admin")  # Значение по умолчанию
roles = ["Admin", "Manager", "User"]
option_menu = tk.OptionMenu(root, var_role, *roles)
option_menu.pack()

button_login = tk.Button(root, text="Войти", command=login)
button_login.pack()

label_error = tk.Label(root, text="", fg="red")
label_error.pack()

root.mainloop()'''