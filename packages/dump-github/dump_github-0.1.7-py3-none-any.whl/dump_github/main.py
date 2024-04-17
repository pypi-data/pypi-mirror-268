import argparse
import os
from .lib import *

parser = argparse.ArgumentParser(
    prog="dump-github",
    description="Backup users github repo.",
    epilog="https://github.com/Core2002/dump_github",
)

parser.add_argument("username")
parser.add_argument(
    "-d", "--download_zip", action="store_true", help="only download zip file"
)
parser.add_argument("-p", "--print", action="store_true", help="only print urls")
parser.add_argument("--token", action="store", default="", help="github token")
parser.add_argument(
    "--limit_size",
    type=int,
    default=100,
    help="limit size(MB) of download zip file, if 0 then no limit(default:100).",
)

args = parser.parse_args()


def clone_repo(repo):
    name = repo["name"]
    url = repo["clone_url"]
    size = repo["size"]
    print("Clone repo: {}".format(name))
    os.system("git clone {}".format(url))


def download_zip(user_name, reop):
    url = f"https://github.com/{user_name}/{reop['name']}/archive/refs/heads/{reop['default_branch']}.zip"
    max_size = args.limit_size * 1000 * 1000
    file_name = f"./{user_name}_{reop['name']}.zip"
    cmd = "curl -L --connect-timeout 5 --retry 3 --retry-delay 3 --max-filesize {} {} -o {}".format(
        max_size, url, file_name
    )
    print(f"Download {reop['name']} : {url}")
    os.system(cmd)
    if os.path.exists(file_name) and max_size < os.stat(file_name).st_size:
        os.remove(file_name)
        print(f"Removed {file_name} because it exceeds the limit size.")


def main():
    # print(args)
    repos = serach_user_repos(args.username, args.token)
    for repo in repos:
        if args.print == True:
            print(repo["clone_url"])
        elif args.download_zip == True:
            download_zip(args.username, repo)
        else:
            clone_repo(repo)


if __name__ == "__main__":
    main()
