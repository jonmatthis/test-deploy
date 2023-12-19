from kfai_env import Environment


def app_init():
    e = Environment('src/env')
    e.load_env()
