# import requests

# url = "http://localhost:8000/upload"
# files = {"file": open("C:/Users/ritik/Projects/AI project 2/resume-job-matcher/data/sample_resumes/john_doe.txt", "rb")}
# response = requests.post(url, files=files)

# print(response.json())

import requests

url = "http://localhost:8000/upload"
file_path = "../data/sample_resumes/john_doe.txt"

with open(file_path, "rb") as f:
    files = {"file": ("john_doe.txt", f, "text/plain")}
    response = requests.post(url, files=files)

print(response.json())
