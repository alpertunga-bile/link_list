import requests
import re
import tqdm
from time import sleep

if __name__ == "__main__":
    link_regex = re.compile(r"\(http(.*)\)")

    with open("README.md", "r") as file:
        file_content = file.read()

    links = [("http" + link) for link in link_regex.findall(file_content)]
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"
    }

    failed_link_file = open("failed_links.txt", "w")

    for link in tqdm.tqdm(links, desc="Checking Links"):
        try:
            response = requests.head(link, headers=headers, timeout=10)
        except:
            failed_link_file.write(link + "\n")
            continue

        if not response.ok:
            failed_link_file.write(link + "\n")

        sleep(6.0)

    failed_link_file.close()
