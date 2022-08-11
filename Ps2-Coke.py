due = 50
while due != 0:

    cents = int(input('Insert coin... '))
    ls = [25,10,5]
    if cents not in ls:
        print('Amount due: ',due)
    else:

        due = due - cents

        if due < 0 :
            change = due*-1
            print('Change owed: ', change)
            due = 0
        else:
            print('Amount due: ',due)
