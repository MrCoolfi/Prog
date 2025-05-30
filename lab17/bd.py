from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Developer, Manager, Project, project_developer, create_db
from datetime import date

def fill_data():
    engine = create_engine('sqlite:///software_development.db', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    # менеджеры
    manager1 = Manager(name="Иван Петров", email="ivan.petrov@company.com", department="Разработка")
    manager2 = Manager(name="Мария Сидорова", email="maria.sidorova@company.com", department="Тестирование")

    # разработчики
    dev1 = Developer(name="Алексей Иванов", email="alex.ivanov@company.com", skills="Python, SQL")
    dev2 = Developer(name="Елена Кузнецова", email="elena.kuznetsova@company.com", skills="JavaScript, React")
    dev3 = Developer(name="Дмитрий Смирнов", email="dmitry.smirnov@company.com", skills="Python, Django, Docker")
    dev4 = Developer(name="Ольга Васильева", email="olga.vasilyeva@company.com", skills="Java, Spring")

    # проекты
    project1 = Project(
        name="Веб-портал компании", 
        start_date=date(2025, 1, 15), 
        end_date=date(2025, 6, 30),
        manager=manager1
    )
    project2 = Project(
        name="Мобильное приложение", 
        start_date=date(2025, 3, 1), 
        end_date=date(2025, 9, 15),
        manager=manager1
    )
    project3 = Project(
        name="Система тестирования", 
        start_date=date(2025, 2, 10), 
        end_date=date(2025, 6, 20),
        manager=manager2
    )


    session.add_all([
        manager1, manager2,
        dev1, dev2, dev3, dev4,
        project1, project2, project3
    ])
    session.flush()


    session.execute(project_developer.insert(), [
        {'developer_id': dev1.id, 'project_id': project1.id, 'role': 'Team Lead', 'join_date': date(2025, 1, 10)},
        {'developer_id': dev2.id, 'project_id': project1.id, 'role': 'Frontend', 'join_date': date(2025, 1, 12)},
        {'developer_id': dev3.id, 'project_id': project1.id, 'role': 'Backend', 'join_date': date(2025, 1, 15)},
        {'developer_id': dev1.id, 'project_id': project2.id, 'role': 'Architect', 'join_date': date(2025, 3, 5)},
        {'developer_id': dev3.id, 'project_id': project2.id, 'role': 'DevOps', 'join_date': date(2025, 3, 10)},
        {'developer_id': dev4.id, 'project_id': project2.id, 'role': 'Backend', 'join_date': date(2025, 3, 15)},
        {'developer_id': dev2.id, 'project_id': project3.id, 'role': 'QA Lead', 'join_date': date(2025, 2, 15)},
        {'developer_id': dev4.id, 'project_id': project3.id, 'role': 'QA Engineer', 'join_date': date(2025, 2, 20)}
    ])
    
    session.commit()
    session.close()

create_db()
fill_data()