MIMETYPES = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
    "default": "application/octet-stream",
}


def check_extension(filename: str) -> str:

    filename, extension = filename.lower().split(".")

    if extension in MIMETYPES.keys():
        return MIMETYPES[extension]
    else:
        return MIMETYPES["default"]


def main():
    filename = input("File name: ")
    print(check_extension(filename))


main()
