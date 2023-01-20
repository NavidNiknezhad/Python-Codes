import os
import github
#from github import Github


def create_repos():
    # Prompt user for GitHub username and Personal Access Token
    github_username = input("Enter your GitHub username: ")
    github_token = input("Enter your GitHub Personal Access Token: ")

    # Prompt user for folder path
    folder_path = input("Enter the path to the folder: ")

    # Connect to GitHub API
    gh = github.Github(github_token)


    #gh = Github(github_token)
    user = gh.get_user()

    # Get the current user
    #user = gh.get_user(github_username)
    #user = gh.get_authenticated_user()

    # Iterate over files in the given folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        # Check if the file is a regular file (not a directory)
        if os.path.isfile(file_path):
           # Get the file name without the extension
            repo_name = os.path.splitext(file_name)[0]
            # Create a new repository on GitHub with the same name as the file
            repo = user.create_repo(repo_name)
            # Create a README.md file in the repository
            repo.create_file("README.md", "Initial commit", "")
            print(f"Successfully created repository {file_name}")

create_repos()
