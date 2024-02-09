import re

def arithmetic_arranger(problems, solve = False):

  #list with all first numbers
  first_numbers = []

  #list with operands
  operand_list = []

  #list with all second numbers
  second_numbers = []

  #list with answers
  answers_list = []

  #list with longest number length of each problem
  lengths = []

  #error - more than 5 problems
  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    #find the first number
    first = problem.split(" ")[0]
    #find the second number
    second = problem.split(" ")[2]
    #find the operand
    operand = problem.split(" ")[1]
    #find longest number
    length = max(len(first), len(second))

    #error not only digits
    if not first.isdigit() or not second.isdigit(): 
      return "Error: Numbers must only contain digits."

    #error too big number
    if len(first) > 4 or len(second) > 4:
      return "Error: Numbers cannot be more than four digits."

    #error operators
    if not re.search(r'\+|-', problem):
      return "Error: Operator must be '+' or '-'."



    #return arranged_problems


    #add the first number to the list
    first_numbers.append(first)
    #add the operand to the list
    operand_list.append(operand)
    #add the second number to the list
    second_numbers.append(second)
    #add the length to the list
    lengths.append(length)

    #calculate the answer
    answer = 0
    if operand == "+":
      answer = int(first) + int(second)
    elif operand == "-":
      answer = int(first) - int(second)

    #add answer to list
    answers_list.append(answer)


  result = ""
  #print out all equations, line by line with first numbers first
  for i in range(len(first_numbers)):
    #if i is not the last number in the list
    if i != len(first_numbers)-1:
      #add the first number to the result with space for the longest number plus 
      #2 spaces (the operand and a space between number and operand) 
      #and 4 spaces seperating this problem and the next
      result += (first_numbers[i].rjust(lengths[i] + 2) + "    ")
    #if i is the last number in the list
    else:
      #do the same as above but without the 4 spaces as there is no more problems
      result += (first_numbers[i].rjust(lengths[i] + 2))

  #add the operand and second number on a new line
  result += "\n"

  #print out all equations, with operand, some spaces, and second numbers
  for i in range(len(second_numbers)):
    if i != len(second_numbers)-1:
      result += (operand_list[i] + " " + second_numbers[i].rjust(lengths[i]) + "    ")
    else:
      result += (operand_list[i] + " " + second_numbers[i].rjust(lengths[i]))

  #add the dashes on a new line
  result += "\n"

  #print out a line of dashes for each equation
  for i in range(len(lengths)):
    if i != len(lengths)-1:
      result += ("-" * (lengths[i] + 2) + "    ")
    else:
      result += ("-" * (lengths[i] + 2))

  #if the second parameter/argument is 'True', then add the answer to the problem
  if solve:
    result += "\n"
    for i in range(len(answers_list)):
      if i != len(answers_list)-1:
        result += (str(answers_list[i]).rjust(lengths[i] + 2) + "    ")
      else:
        result += (str(answers_list[i]).rjust(lengths[i] + 2))
     
  return result
