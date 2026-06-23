



def input_marks():
  marks= []
  x= int(input("Enter number of subjects:"))

  for i in range(x):
    mark= float(input(f"Enter marks for subject {i+1}:"))
    marks.append(mark)
  return marks

def calculate_total(marks):
  total= sum(marks)
  return total

def calculate_average(total,x):
  average= total/x
  return average

def print_report(marks,total,average):
  print("/x---Report---")
  print("Marks:",marks)
  print("Total:",total)
  print("Average:",average)

marks= input_marks()
total= calculate_total(marks)
average= calculate_average(total,len(marks))
print_report(marks,total,average)
