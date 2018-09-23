import validation as val
def entering():
    number = input("Enter number:")
    answer = input("Want to exit ?('yes',something else)")
    if(not val.int_valid(number)):
        print("Enter sommething that more 'intrative' =)")
        return entering()
    else:
        if(answer == "yes" or answer == "Yes"):
            return number
        return number+"/"+entering()
    return "0"
def bigger(numbers_set):
    number = int(numbers_set.pop())
    second_number = False
    if(len(numbers_set)!=0):
        second_number = bigger(numbers_set)
    if(second_number and number<second_number):
        print(number<second_number)
        print(str(second_number)+"B")
        print(str(number)+"A")
        return second_number
    else:
        print(number)
        return number

numbers_string = entering()
numbers_set = set(numbers_string.split("/"))
print(bigger(numbers_set))


