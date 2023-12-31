#!/usr/bin/env python

import subprocess
from dataclasses import dataclass
from random import choice
from string import ascii_letters, digits
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent


@dataclass
class EnvVar:
    name: str
    value: str


def main():
    """
    This function create the .env file with the needed
    environment variables.
    """

    database = [
        EnvVar(name="AZURE_STORAGEACCOUNT", value=""),
        EnvVar(name="AZURE_ACCOUNTKEY", value=""),
        EnvVar(name="AWS_ACCESS_KEY_ID", value="AKIAxxxx"),
        EnvVar(name="AWS_ACCESS_KEY", value=""),
        EnvVar(name="BUCKETNAME", value=""),
        EnvVar(name="DB_PATH", value="/app/database/prod.sqlite3"),
        EnvVar(name="DB_REPLICA_PATH", value="/data/database/prod.sqlite3"),
    ]
    settings_file = "habitstacker.settings.dev"
    secret = "".join(choice(ascii_letters + digits) for _ in range(50))
    django = [
        EnvVar(name="SECRET_KEY", value=secret),
        EnvVar(name="ALLOWED_HOSTS", value="*"),
        EnvVar(name="DJANGO_SETTINGS_MODULE", value=settings_file),
        EnvVar(name="CSRF_TRUSTED_ORIGINS", value="http://localhost:8000"),
    ]

    # Create .env file
    env_path = PROJECT_ROOT / ".env"
    with open(env_path, "w") as env:
        env.write("# DATABASE SETTINGS\n")
        for var in database:
            env.write(f"{var.name}={var.value}\n")
        env.write("\n# DJANGO SETTINGS\n")
        for var in django:
            env.write(f"{var.name}={var.value}\n")

    subprocess.run(["yarn", "install"], shell=True)
    subprocess.run(["yarn", "build:prod"])
    subprocess.run(["pre-commit", "install"], shell=True)
    subprocess.run(["python", "manage.py", "migrate"])


if __name__ == "__main__":
    main()
