import requests


def get_content(url):
    if url is None:
        return None
    try:
        response = requests.get(url, headers=
        {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        })
        if response.status_code == 200:
            return str(response.content, encoding = "utf-8")
        return None
    except:
        return None