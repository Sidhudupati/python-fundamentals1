expenses=[]
total=0
expense=int(input("Enter no. of expenses:\n"))
for i in range(expense):
    expenses.append(float(input("Enter a number:")))
total=sum(expenses)
print(total)    