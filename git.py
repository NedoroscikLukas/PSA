import os

repo_path = "C:\\Users\\lukne\\Desktop\\PSA"
repo_name = "PSA"
repo_url = "https://github.com/NedoroscikLukas/PSA.git"

os.chdir(repo_path)
os.system("git clone " + repo_url)