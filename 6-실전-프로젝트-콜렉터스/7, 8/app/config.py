import json
from pathlib import Path
from typing import Optional


BASE_DIR = Path(__file__).resolve().parent.parent


def get_secret(
    key: str,
    default_value: Optional[str] = None,
    json_path: str = str(BASE_DIR / "secrets.json"),
):
    with open(json_path) as f:
        secrets = json.loads(f.read())
    try:
        return secrets[key]
    except KeyError:
        if default_value:
            return default_value
        raise EnvironmentError(f"Set the {key} environment variable.")


MONGO_DB_NAME = get_secret("MONGO_DB_NAME")
MONGO_URL = get_secret("MONGO_URL")
NAVER_API_ID = get_secret("NAVER_API_ID")
NAVER_API_SECRET = get_secret("NAVER_API_SECRET")

if __name__ == "__main__":
    world = get_secret("hello")
    print(world)
