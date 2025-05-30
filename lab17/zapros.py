import sqlite3
from pypika import Query, Table, functions as fn

# Подключаемся к базе данных
conn = sqlite3.connect('software_development.db')
cur = conn.cursor()

# Определяем таблицы
developers = Table("developers")
projects = Table("projects")
managers = Table("managers")
project_developers = Table("project_developers")

# 1. Все разработчики и проекты, в которых они участвуют
print("Разработчики и их проекты:")
q1 = (Query.from_(developers)
     .join(project_developers).on(developers.id == project_developers.developer_id)
     .join(projects).on(project_developers.project_id == projects.id)
     .select(developers.name.as_("developer"), projects.name.as_("project"), project_developers.role)
     .orderby(developers.name))

sql1 = q1.get_sql()
cur.execute(sql1)
for row in cur.fetchall():
    print(f"Разработчик: {row[0]}, Проект: {row[1]}, Роль: {row[2]}")

# 2. Получить все проекты с их менеджерами
print("\nПроекты и их менеджеры:")
q2 = (Query.from_(projects)
     .join(managers).on(projects.manager_id == managers.id)
     .select(projects.name.as_("project"), managers.name.as_("manager"), 
             projects.start_date, projects.end_date))

sql2 = q2.get_sql()
cur.execute(sql2)
for row in cur.fetchall():
    print(f"Проект: {row[0]}, Менеджер: {row[1]}, Сроки: {row[2]} - {row[3]}")

# 3. Количество разработчиков на каждом проекте
print("\nКоличество разработчиков по проектам:")
q3 = (Query.from_(projects)
     .join(project_developers).on(projects.id == project_developers.project_id)
     .groupby(projects.name)
     .select(projects.name, fn.Count(project_developers.developer_id).as_("developers_count")))

sql3 = q3.get_sql()
cur.execute(sql3)
for row in cur.fetchall():
    print(f"Проект: {row[0]}, Разработчиков: {row[1]}")

# 4. Найти разработчиков с определенным навыком (Python)
skill_to_find = "Python"
print(f"\nРазработчики со знанием {skill_to_find}:")
q4 = (Query.from_(developers)
     .where(developers.skills.like(f"%{skill_to_find}%"))
     .select(developers.name, developers.skills))

sql4 = q4.get_sql()
cur.execute(sql4)
for row in cur.fetchall():
    print(f"Имя: {row[0]}, Навыки: {row[1]}")

conn.close()