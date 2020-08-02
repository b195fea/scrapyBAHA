class Test:
    # name = '鍾嘉豪'
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


if __name__ == '__main__':
    t = Test("123")
    print(t.getName())
