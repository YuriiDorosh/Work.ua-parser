from work_ua_parser import WorkUaParser
from settings import urls, path_to_csv_file


def main() -> None:
    """
    Main function to initiate the parsing process.
    """

    parser = WorkUaParser(links_list=urls, path_to_csv=path_to_csv_file)
    parser.get_all_vacancies()
    parser.remove_duplicates()
    parser.save_to_csv()
    print("Parsing ended.")


if __name__ == "__main__":
    main()
