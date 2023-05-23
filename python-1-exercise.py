
numbers = []
sum_of_numbers = 0
count = 1

while True:
    number = int(input("Please enter number #{}: ".format(count)))
    if number < 0:
        break

    numbers.append(number)
    sum_of_numbers += number
    average = sum_of_numbers / count

    print("Please enter number #{} (avg={:.2f}. Sum={})".format(count, average, sum_of_numbers))
    count += 1

print("Thank you. Goodbye.")
