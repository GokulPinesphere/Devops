import os
import subprocess

REPO_DIR = "/home/ubuntu/files"
SERVICE_NAME = "Django"

def update_repo():
  os.chdir(Repo_Dir)
  subprocess.run(["git", "pull"], check=True)

def restart_service():
  subprocess.run(["systemctl", "restart", SERVICE_NAME], check=True)

if __name__ == "__main__":
  update_repo()
  restart_service()
