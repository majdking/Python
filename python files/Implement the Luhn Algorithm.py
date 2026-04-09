#testing slicing str
#  card_number = '4111111111111111'
# print(len(card_number))
# print(card_number[:-1][::-2])
# print(len(card_number[:-1][::-2]))

# print(card_number[:-1][-2::-2])
# print(len(card_number[:-1][-2::-2]))
# print(len(card_number[:-1]))


def verify_card_number(card_number: str) -> str:
    if " " in card_number:
        card_number = card_number.replace(' ', '')
    elif '-' in card_number:
        card_number = card_number.replace('-', '')
    if not card_number.isdigit():
        raise ValueError('Card number contains only digits.')
    sum_all_number = 0
    sum_all_number += int(card_number[-1])
    for i in card_number[:-1][-2::-2]:
        print(i, card_number.index(i))       
        sum_all_number += int(i)
        print(sum_all_number)               
    for i in card_number[:-1][::-2]:
        #print(i)
        i = 2 * int(i)
        #print(i)
        if i > 9:
            i -= 9
        sum_all_number += i 
        print(sum_all_number)               
    print(sum_all_number)               

    if sum_all_number % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"

    #print(sum_all_number)

    #return card_number






print(verify_card_number('453914889'))
print(verify_card_number('4111-1111-1111-1111'))
print(verify_card_number('453914881'))
print(verify_card_number('1234 5678 9012 3456'))