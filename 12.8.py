class MyString:
    def __init__(self, content):
        self.content = content

    def __iadd__(self, other):
        self.content += other
        return self

    def toLower(self):
        self.content = self.content.lower()

    def toUpper(self):
        self.content = self.content.upper()

    def __str__(self):
        return self.content
