"""Arquivo que estudantes devem editar"""


def count_slashes_file(string):
    return string.count("/")


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = max(context["all_files"], key=count_slashes_file)
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if not case_sensitive:
            lower_file_name = file_name.lower()
            lower_search_term = search_term.lower()

            if lower_search_term in lower_file_name:
              found_files.append(path)

        elif search_term in file_name:  
            found_files.append(path)

    return found_files
