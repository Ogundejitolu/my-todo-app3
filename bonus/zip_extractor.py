import zipfile


def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("\Users\ogund\PycharmProjects\App 1\bonus\compressed.zip",
                    "\Users\ogund\PycharmProjects\App 1")
