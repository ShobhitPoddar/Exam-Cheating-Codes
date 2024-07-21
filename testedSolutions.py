# Encode the exam solutions
class Encoding:
    def direct(self, code, exam):
        for i in range(len(code)):
            code[i] = exam[i]
        return code
    
    def occurences(self, code, exam):
        pairs = [(exam[i], exam[i+1]) for i in range(len(exam)-1)]
        triplets = [(exam[i], exam[i+1], exam[i+2]) for i in range(len(exam)-2)]

    # Check frequency of pairs
        pair_freq = {}
        for pair in pairs:
            pair_freq[pair] = pair_freq.get(pair, 0) + 1

    # Check frequency of triplets
        triplet_freq = {}
        for triplet in triplets:
            triplet_freq[triplet] = triplet_freq.get(triplet, 0) + 1

    # Identify the most frequent pair and triplet
        most_common_pair = max(pair_freq, key=pair_freq.get)
        most_common_triplet = max(triplet_freq, key=triplet_freq.get)

    # Apply the identified pattern to generate the code
        code[:2] = most_common_pair
        code[2:5] = most_common_triplet
        # print ("exam:", exam)

        # print("Most common pair:", most_common_pair)
        # print("Most common triplet:", most_common_triplet)
        # print("Generated code:", code)

    def sets_of_two(self, code, exam):
        for i in range(len(code)):
            count = exam[2*i] + exam[2*i+1]
            if count > 0:
                code[i] = 1
            else:
                code[i] = 0
        return code

    # groupings of three
    def sets_of_three(self, code, exam):
        for i in range(len(code)):
            if 3*i+2 > 19:
                break
            count = exam[3*i] + exam[3*i+1] + exam[3*i+2]
            if count > 1:
                code[i] = 1
            else:
                code[i] = 0
        return code

    def sets_of_five(self, code, exam):
        for i in range(len(code)):
            if 5*i+4 > 19:
                break

            count = exam[5*i] + exam[5*i+1] + exam[5*i+2] + exam[5*i+3] + exam[5*i+4]
            if count > 2:
                code[i] = 1
            else:
                code[i] = 0
        return code

# Decode the exam solutions
class Decoding:
    # direct one-to-one mapping of 10 answers
    def direct(self, answer, code):
        
        for i in range(len(code)):
            answer[i] = code[i]

        return answer
    
    def occurences(self, answer, code):
        answer[:10] = code
        answer[10:] = code[:5] * 2

    # groupings of three
    def sets_of_two(self, answer, code):
        # decode in sets of three
        for i in range(len(code)):
            answer[2*i]     = code[i]
            answer[2*i+1]   = code[i]
        return answer

    # groupings of three
    def sets_of_three(self, answer, code):  
        # decode in sets of three
        for i in range(len(code)):
            if 3*i+2 > 19:
                break

            answer[3*i]     = code[i]
            answer[3*i+1]   = code[i]
            answer[3*i+2]   = code[i]
        return answer

    # groupings of five
    def sets_of_five(self, answer, code):
        # decode into 4 groups of five
        for i in range(len(code)):
            if 5*i+4 > 19:
                break

            answer[5*i]     = code[i]
            answer[5*i+1]   = code[i]
            answer[5*i+2]   = code[i]
            answer[5*i+3]   = code[i]
            answer[5*i+4]   = code[i]
        return answer