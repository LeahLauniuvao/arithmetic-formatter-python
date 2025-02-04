def arithmetic_arranger(problems, show_answers=False):
    # check if within problem number range
    if len(problems) > 5:
        return "Error: Too many problems."

    # check for valid operator symbol/ problem length / valid numbers
    for problem in problems:
        parts = problem.split()

        # check valid operator
        if parts[1] not in ["+",'-']:
            return "Error: Operator must be '+' or '-'."
        
        # check for valid numbers
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return "Error: Numbers must only contain digits."
        
        # check length of parts
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # empty lists, see format_problem
    top_row = []
    bottom_row = []
    dashes = []
    answers = []

    for problem in problems:
        top, bottom, dash, answer = format_problem(problem, show_answers)
        # place strings
        top_row.append(top)
        bottom_row.append(bottom)
        dashes.append(dash)

        if show_answers:
            answers.append(answer)
    
    # Join rows
    top_row_str = "    ".join(top_row)
    bottom_row_str = "    ".join(bottom_row)
    dashes_str = "    ".join(dashes)
    answers_str = "    ".join(answers) if show_answers else ""
    
    # arrange
    if show_answers:
        arranged_problems = f"{top_row_str}\n{bottom_row_str}\n{dashes_str}\n{answers_str}"
    else:
        arranged_problems = f"{top_row_str}\n{bottom_row_str}\n{dashes_str}"
    
    return arranged_problems
        
def format_problem(problem, show_answer=False):
    
    # separate elements
    parts = problem.split()
    num1 = parts[0]
    operator = parts[1]
    num2 = parts[2]
    width = max(len(num1), len(num2)) + 2  

    # format each part
    top = num1.rjust(width)
    bottom = operator + " " + num2.rjust(width - 2)
    dash = "-" * width # bottom line
    answer = None

    if show_answer:
        if operator == '+':
            answer = str(int(num1)+ int(num2)).rjust(width)
        elif operator == '-':
            answer = str(int(num1)- int(num2)).rjust(width)
    
    return top, bottom, dash, answer
    

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
