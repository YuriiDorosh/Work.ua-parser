# Work.ua Parser

This is a Python script for parsing job vacancies from the Work.ua website. It retrieves job vacancies related to Python and Django development, excluding positions with "middle" or "senior" in the title. Duplicate vacancies are removed before saving the results to a CSV file.

## Requirements

- Python 3.x
- BeautifulSoup4
- requests


## Usage

### Clone the repository
```bash
git clone https://github.com/YuriiDorosh/Work.ua-parser
```

---

### Install the reqirements

You can install the required libraries using pip:

```bash
pip3 install -r requirements.txt
```

or

```bash
pip3 install beautifulsoup4 requests
```

---

### Customize the settings

### You can customize:

### <li>urls</li>

open settings.py and change this:

```bash
urls: list[str] = [
    "https://www.work.ua/jobs-python/",
    "https://www.work.ua/jobs-python+trainee/",
    "https://www.work.ua/jobs-python+junior/",
    "https://www.work.ua/jobs-python+developer/",
    "https://www.work.ua/jobs-django/",
]
```

### <li>path to directory</li>

open settings.py and change this:

```bash
path_to_directory: str = ""  # Path to directory where you want to save file with vacancies.
```

### <li>name of csv file</li>

open settings.py and change this:

```bash
csv_file_name: str = "Work-ua-parser.csv"  # Name of your file(word ending: .csv)
```

### <li>keywords in the title</li>

open settings.py and change this:

```bash
key_words: list[str] = [
    "python",
    "django",
]
```

### <li>do not add vacancies that include these words</li>

open settings.py and change this:

```bash
ban_words: list[str] = [
    "middle",
    "senior",
]
```

---

### Run the script using the following command
```bash
python3 main.py
```

---

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.






