class SortedList(list):
  def __init__(self, list):
    for num in list:
      self.append(num)

  def append(self, value):
    super().append(value)
    self.sort()

  def extend(self, value):
    super().extend(value)
    self.sort()

list = SortedList([9, 2, 7])
print(list)

list.append(12)

print(list)

list.extend([5,6,13])
print(list)


class SuperDict(dict):
  fallback_value = "doesnt exist"
  def __init__(self, dic):
    super().__init__(dic)
    self.dic = dic
  def get(self, key):
    super().get(key)
    try:
      return self.dic[key]
    except KeyError:
      return self.fallback_value


d = SuperDict({"k": 10, "b": 5})

print(d.get("c"))