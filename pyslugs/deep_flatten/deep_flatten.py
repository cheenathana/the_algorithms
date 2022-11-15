def deep_flatten(data):
   val = []
   for i in data:
      for j in i:
         if isinstance(j, (list, tuple):
            val.extend(j)
         else:
            val.append(j)
         
