# coding: utf-8


class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    uncovered_subjects = set(subjects)
    schedule = []

    while uncovered_subjects:
        best_teacher = None
        best_coverage = set()

        for teacher in teachers:
            available = teacher.can_teach_subjects & uncovered_subjects
            if not available:
                continue

            if (
                not best_teacher
                or len(available) > len(best_coverage)
                or (
                    len(available) == len(best_coverage)
                    and teacher.age < best_teacher.age
                )
            ):
                best_teacher = teacher
                best_coverage = available

        if not best_teacher:
            return None  # Неможливо покрити всі предмети

        best_teacher.assigned_subjects = best_coverage
        schedule.append(best_teacher)
        uncovered_subjects -= best_coverage
        teachers.remove(best_teacher)

    return schedule


if __name__ == "__main__":
    # Множина предметів
    subjects = {
        "Закляття",
        "Зіллєваріння",
        "Трансфігурація",
        "Захист від темних мистецтв",
        "Травологія",
    }

    # Створення списку викладачів
    teachers = [
        Teacher(
            "Северус",
            "Снейп",
            38,
            "s.snape@hogwarts.edu",
            {"Зіллєваріння", "Захист від темних мистецтв"},
        ),
        Teacher(
            "Мінерва", "Макґонеґел", 60, "m.mcgonagall@hogwarts.edu", {"Трансфігурація"}
        ),
        Teacher(
            "Філіус",
            "Флитвік",
            55,
            "f.flitwick@hogwarts.edu",
            {"Закляття", "Трансфігурація"},
        ),
        Teacher("Професор", "Спраут", 58, "p.sprout@hogwarts.edu", {"Травологія"}),
        Teacher(
            "Ремус",
            "Люпин",
            33,
            "r.lupin@hogwarts.edu",
            {"Захист від темних мистецтв", "Закляття"},
        ),
        Teacher("Горацій", "Слизоріг", 65, "h.slughorn@hogwarts.edu", {"Зіллєваріння"}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:\n")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
