import os


class Sample(list):
    def __init__(self):
        print(os.getcwd())