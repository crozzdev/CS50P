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
    extensions = filename.split(".")

    if extensions[-1] in MIMETYPES.keys():
        return MIMETYPES[extensions[-1]]
    else:
        return MIMETYPES["default"]


def main():
    filename = input("File name: ").strip().lower()
    print(check_extension(filename))


main()
