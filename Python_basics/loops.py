"""Break Statement"""
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


"""Continue statement"""
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


"""else statement"""
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")



"""................for loop....................."""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)



"""....Nested Loop......."""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

