def sum_list(the_list):
  s = 0
  for item in the_list:
    s += item
  
  return s
  
l1 = [1,2,3,4,5,6,7,8,9]

print ("Sum list: {}".format(sum_list(l1)))