 def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(plate):
    length = len(plate)
    # check that only letters and numbers are used
    if plate.isalnum() == False:
        return False
    # Check plate starts with 2 letters
    if plate[:2].isalpha() == False:
        print(plate)
        return False

    # check correct length
    if 2 > length or length > 6:
            return False

     # Check that first digit != 0
    i = 0
    while i < length:
        if plate[i].isalpha()== False:
            if plate[i] == '0':
                return False
            else:
               break
        i+=1

    for j in range(length):
        if plate[j].isdigit():
            if not plate[j:].isdigit():
                return False



    return True





main()
