# Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.

num = int(input("Enter a number:"))
s_or_p = input("sum or product:")

sum_num = 0

if s_or_p == "sum":
    for i in range(1, num + 1):
        sum_num = sum_num + i
    print(sum_num)

product_num = 1

if s_or_p == "product":
    for i in range(1, num + 1):
        product_num = product_num * i
    print(product_num)
