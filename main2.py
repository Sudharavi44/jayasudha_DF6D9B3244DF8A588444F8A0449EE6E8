def linearSearchProduct(productList, targetProduct):
  indices = [] 

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


products = ["pencil", "book", "dress", "pencil", "sandal", "pencil"]
target = "pencil"
target2="back"
result = linearSearchProduct(products,target)
print(result)
result=linearSearchProduct(products,target2)
print(result)
