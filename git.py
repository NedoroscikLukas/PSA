import os

repo_path = "C:\\Users\\lukne\\Desktop\\PSA"
repo_name = "PSA"
repo_url = "https://github.com/NedoroscikLukas/PSA.git"


def clone_repo(path, url):
    os.chdir(path)
    os.system("git clone " + url)

def add_file(filename, path, reponame):
    os.chdir(path + reponame)
    os.system("git add " + filename)

def git_commit(path, reponame, commit_message):
    os.chdir(path + reponame)
    os.system("git commit -m \"" + commit_message + "\"")

def git_push(path, reponame):
    os.chdir(path + reponame)
    os.system("git push")


clone_repo(repo_path, repo_name)
add_file("novy.txt", repo_path, repo_name)
git_commit(repo_path, repo_name, "sprava spravy na commit")
git_push(repo_path, repo_name)