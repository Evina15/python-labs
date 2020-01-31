'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(example_list):
  print(max(example_list))
  print(min(example_list))
  print(sum(example_list) / len(example_list))
  print(sum(example_list))


# call the function below here
stats(example_list)