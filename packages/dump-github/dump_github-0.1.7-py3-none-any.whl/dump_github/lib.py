import requests


def get_page_of_repos(username, page, token=""):
    url = "https://api.github.com/users/{}/repos?per_page=200&page={}".format(
        username, page
    )
    headers = {"Authorization": token}
    if token != "":
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        return repos
    else:
        return []


def serach_user_repos(username, token=""):
    page = 0
    res_repos = []

    while True:
        page += 1
        repos = get_page_of_repos(username, page, token)
        if len(repos) == 0:
            break
        res_repos += repos

    return res_repos
