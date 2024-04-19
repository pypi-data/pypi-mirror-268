import os
import shutil


def delete_all_screenshots_static_ghost():
    _dir = os.path.join(os.getcwd(), "static_ghost")
    for folder in os.listdir(_dir):
        new_dir = os.path.join(_dir, folder)
        shutil.rmtree(new_dir)


if __name__ == "__main__":
    delete_all_screenshots_static_ghost()
