import requests

headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MDhmYTVmMTExYTljY2ZiNzc1ZjVhZWEwMWNkZWQ1ZiIsIm5iZiI6MTczMjkyMDcyMi45ODU5OTk4LCJzdWIiOiI2NzRhNDU5MjZmZDgzYTY2MzA5ZDZlNjkiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ICl4T2FdSj5hyU_NwY6r-ScuneIVX6wzNW7Oiw8VcK8"
    }


def buscarFilme(nome):
    url = f"https://api.themoviedb.org/3/search/movie?query={nome}&include_adult=false&language=pt&page=1"
    return requests.get(url=url, headers=headers).json()


def detalhesFilme(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    return requests.get(url=url, headers=headers).json()