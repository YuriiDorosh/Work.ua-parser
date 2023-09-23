urls: list[str] = [
    "https://www.work.ua/jobs-python/",
    "https://www.work.ua/jobs-python+trainee/",
    "https://www.work.ua/jobs-python+junior/",
    "https://www.work.ua/jobs-python+developer/",
    "https://www.work.ua/jobs-django/",
]

path_to_directory: str = "/home/apacer/Desktop/Work.ua-parser"  # Path to directory where you want to save file with vacancies.
csv_file_name: str = "Work-ua-parser.csv"  # Name of your file(word ending: .csv)

path_to_csv_file: str = (
    path_to_directory + "/" + csv_file_name
)  # Total path to the file
