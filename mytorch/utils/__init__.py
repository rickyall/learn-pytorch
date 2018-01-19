import requests


def download(url, filepath):
    """下载文件
    """
    print("downloading with requests")
    r = requests.get(url)
    with open(filepath, "wb") as code:
        code.write(r.content)
