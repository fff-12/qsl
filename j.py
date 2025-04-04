import sqlite3

conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

def create_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS quiz(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS question(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Question VARCHAR,
                answer VARCHAR,
                wrong1 VARCHAR,
                wrong2 VARCHAR,
                wrong3 VARCHAR)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS quiz_content(
                id INTEGER PRIMARY KEY,
                quiz_id INTEGER,
                question_id INTEGER,
                FOREIGN KEY (quiz_id) REFERENCES quiz (id),
                FOREIGN KEY (question_id) REFERENCES question (id))''')

def quiz_db():
    quizes = ['Історія України', 'Географія світу', 'Література']
    questions = [
        ("Хто був першим гетьманом Війська Запорозького?", "Байда Вишневецький", "Іван Мазепа", "Байда Вишневецький", "Богдан Хмельницький"),
        ("У якому році Україна проголосила незалежність?", "1991", "1991", "2004", "2014"),
        ("Як називається перша Конституція України, створена Пилипом Орликом?", "Конституція Пилипа Орлика", "Конституція України", "Конституція Пилипа Орлика", "Основний закон"),
        ("Яке місто було столицею УНР?", "Київ", "Київ", "Львів", "Харків"),

        ("Яка найбільша річка України?", "Дніпро", "Дністер", "Дніпро", "Південний Буг"),
        ("Який найбільший за площею острів України?", "Джарилгач", "Джарилгач", "Зміїний", "Тендрівська коса"),
        ("Яка найвища гора України?", "Говерла", "Петрос", "Говерла", "Роман-Кош"),
        ("Скільки областей в Україні?", "24", "25", "24", "22"),

        ("Хто є автором твору 'Заповіт'?", "Тарас Шевченко", "Іван Франко", "Тарас Шевченко", "Леся Українка"),
        ("Який твір написав Іван Котляревський?", "Енеїда", "Енеїда", "Кайдашева сім’я", "Маруся"),
        ("Хто автор твору 'Лісова пісня'?", "Леся Українка", "Леся Українка", "Ольга Кобилянська", "Пантелеймон Куліш"),
        ("Який жанр має твір 'Кайдашева сім’я'?", "Соціально-побутова повість", "Історичний роман", "Соціально-побутова повість", "Фантастика")
    ]

    for i in range(len(quizes)):
        cursor.execute("INSERT INTO quiz(name) VALUES (?)", [quizes[i-1]])
    
    for i in range(len(questions)):
        cursor.execute("INSERT INTO question(Question, answer, wrong1, wrong2, wrong3) VALUES (?, ?, ?, ?, ?)", [questions[i-1][0], questions[i-1][1], questions[i-1][2], questions[i-1][3], questions[i-1][4]])

def quiz_content():
    while True:
        q = input("Чи хочете ви встановити зв1язок між питанням та вікториною? так\ні - ").lower()
        if q == "так":
            id_question = int(input("Введіть id питання - "))
            id_quiz = int(input("Введіть id вікторини - "))
            cursor.execute("INSERT INTO quiz_content(quiz_id, question_id) VALUES (?, ?)", [id_quiz, id_question])
        else:
            break

create_db()
quiz_db()
quiz_content()
conn.commit()
