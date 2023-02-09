import extract_data


if __name__ == '__main__':
    with open("links.txt","r") as file:
        links = eval(file.read())
    links = list(set(links))
    extract_data(links)
