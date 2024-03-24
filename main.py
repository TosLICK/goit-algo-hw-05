import sys

def parse_log_line(line: str) -> dict:
    elements = line.split(" ", 3) # рядок логу тричі розбиває на елементи по пробілу
    parsed_log_lines = {}
    parsed_log_lines["date"] = elements[0] 
    parsed_log_lines["time"] = elements[1]
    parsed_log_lines["level"] = elements[2]
    parsed_log_lines["message"] = elements[3]
    return parsed_log_lines

def load_logs(file_path: str) -> list[dict]:
    with open(file_path, "r", encoding="utf-8") as file:
        log_lines = [parse_log_line(line.strip()) for line in file.readlines()]
    return log_lines # повертає список з рядками логу, кожен з яких обробляє функцією parse_log_line

def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
    logs_by_level = [el for el in logs if el["level"] == level.upper()]
    return logs_by_level # повертає рядки логу за вказаним рівнем логування

def count_logs_by_level(logs: list[dict]) -> dict:
    logs_counter = {}
    for log in logs:
        logs_counter[log.get("level")] = logs_counter.get(log.get("level"), 0) + 1
    return logs_counter # повертає словник з рівнем логування (ключ) і кількістю відповідних рядків (значення)

def display_log_counts(counts: dict):
    width_left, width_right = 17, 11
    header = f"{"Рівень логування":^17}{"|"}{"Кількість":^11}" # Не знаю, як сюди передати змінні ширини
    separator = f"{"-"*width_left}|{"-"*width_right}"
    print(header)
    print(separator)
    for key, value in counts.items():
        print(f"{key:17}{"|"} {value:<10}")
    try:
        if sys.argv[2]: # якщо присутній опціональний аргумент
            level = sys.argv[2].upper()
            if level in counts:
                print(f"\nДеталі логів для рівня '{level}':")
                for dictionary in filter_logs_by_level(load_logs(sys.argv[1]), level): # перебираємо усі словники за заданим рівнем логування
                    print(f"{dictionary["date"]} {dictionary["time"]} - {dictionary["message"]}")
            else:
                print(f"\nThere is no level '{level}'")              
    except IndexError:
        pass

def main():
    try:
        display_log_counts(count_logs_by_level(load_logs(sys.argv[1])))
    except IndexError:
        print("Usage: 'python main.py file_path error_level(optional)")
    except AttributeError:
        print("File not found")
    except FileNotFoundError:
        print("File not found")

main()