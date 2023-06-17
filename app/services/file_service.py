import os
import zipfile
import shutil


def setup_data_directory(parsed_target_url, id: int):
    data_dir = f'public/{id}_{str(parsed_target_url.netloc)}'
    # let's create a directory for data
    if not os.path.exists(f'public/{id}_{str(parsed_target_url.netloc)}'):
        os.makedirs(data_dir)

    return data_dir


def write_text_to_file(web_page_text: str, formatted_path: str,  counter: int, parsed_target_url, user_id: int):
    # we use the counter to map the files in the directory to the same cacnonical order as the nav
    text_file_location = "public/{id}_{domain}/{pgindex}_{fmtdpath}.txt".format(id=str(user_id),
                                                                                domain=parsed_target_url.netloc, pgindex=str(counter), fmtdpath=formatted_path)
    # lets open/create a new file called in the website data directory and overwrite its contents if its been indexed before
    with open(text_file_location, "w") as text_file:
        # lets write the text content to the new file we created
        text_file.write(web_page_text)
    # let's return the file location to pass onto the next function
    return text_file_location


def strip_whitespace_from_file(text_file_location: str):
    stripped_text = []
    with open(text_file_location, "r") as parsed_text_file:
        for line in parsed_text_file:
            if line := line.rstrip().lstrip():
                stripped_text.append(line)
    return "\n".join(stripped_text)


def compress_directory(dir: str):
    with zipfile.ZipFile('{folder}.zip'.format(folder=dir), 'w') as zip:
        for file in os.listdir(dir):
            zip.write(os.path.join(dir, file))

    return zip


def delete_data_directory(dir):
    if os.path.exists(dir) and os.path.isdir(dir):
        print('{dir} is a directory'.format(dir=dir))
