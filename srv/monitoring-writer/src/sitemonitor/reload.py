from watchfiles import run_process

from sitemonitor.main import run


if __name__ == "__main__":
    run_process(".", target=run)
