class Tags:

    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


tags = Tags()
tags.add("Python")
tags.add("python")
tags["java"] = 4

print(tags["python"])
print(tags["java"])
print(len(tags))
for tag in tags:
    print(tag)
