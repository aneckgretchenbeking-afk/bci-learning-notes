filename = input("File name: ").strip().lower()
if filename[-5:] == ".jpeg":
    print("image/jpeg")
else:
    match filename[-4:]:
        case".gif":
            print("image/jpeg")
        case ".jpg" | ".jpeg":
            print("image/jpeg")
        case ".png":
            print("image/png")
        case ".pdf":
            print("application/pdf")
        case ".txt":
            print("text/plain")
        case ".zip":
            print("application/zip")
        case _:
            print("application/octet-stream")
