
def delete_digit_at_index(num, index):
    return num[:index] + num[index+1:]


def check_prime(num: int):
    i = 3
    if num % 10 in [0, 2, 4, 5, 6, 8] and num > 2:
        return False

    while i * i < num + 1:
        if num % i == 0:
            return False
        i = i + 2
    return True


def create_subnumers(potential_numbers, num, correct_count):

    for index in range(0, len(num)):
        new_num = delete_digit_at_index(num, index)
        if len(new_num) == 1:
            if new_num in ['2','3','5','7']:
                correct_count += 1
        else:
            if check_prime(int(new_num)):
                potential_numbers.append(new_num)
    return correct_count
        

def solve(potential_numbers, num):
    correct_count = 0
    potential_numbers.append(num)
    while len(potential_numbers) > 0:
        correct_count = create_subnumers(potential_numbers,potential_numbers.pop(), correct_count)
    print(correct_count)


if __name__ == '__main__':

    f = open("file.txt", "r")
    line = f.readline()

    while line:
        line = line.strip()
        print(line)
        solve([], line)
        line = f.readline()
    
    f.close()



    

