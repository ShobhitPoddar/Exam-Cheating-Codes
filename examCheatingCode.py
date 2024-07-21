# Compute the honking protocol for the exam cheaters

def compute_and_send_code(exam):
    code = [0] * 10
    # Don't change anything above this line
    # ==========================
    # TODO Add your solution here.
    length = len(code)-1
    for i in range(length):
            code[i] = exam[i]
        # count the number of 1s in the remaining exam indexes
    count = 0
    for i in range(length, len(exam)):
            count += exam[i]
        # if 1 is in the majority then code[len] = 1
    final = len(exam) - length
    if count >= (final/2):
            code[length] = 1
    else:
            code[length] = 0
    # ==========================
    # Don't change anything below this line
    return code


def enter_solution_based_on_code(code):
    answer = [0] * 20
    # Don't change anything above this line
    # ==========================
    # TODO Add your solution here.
    length = len(code)-1
    for i in range(length):
            answer[i] = code[i]

    for i in range(length, len(answer)):
            answer[i] = code[length]
    # ==========================
    # Don't change anything below this line
    return answer