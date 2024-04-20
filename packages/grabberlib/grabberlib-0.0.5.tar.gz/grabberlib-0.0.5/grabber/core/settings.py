import pathlib

from environs import Env

env = Env()
env.read_env()
APP_ROOT = pathlib.Path(__file__).parent.parent.parent
MEDIA_ROOT = APP_ROOT / "media"
KEY = env.str("KEY", "default")
