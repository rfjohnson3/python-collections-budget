from . import Expense
import matplotlib.pyplot as plt
import timeit

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()

    if not divided_set_comp == divided_for_loop:
        print("Sets are NOT equal by == test")

    for a, b in zip(divided_for_loop, divided_set_comp):
        if not (a.issubset(b) and b.issubset(a)):
            print("Sets are NOT equal by subset test")

timeit.timeit()
stmt = ("expenses.categorize_for_loop")
setup = '''from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')'''
number=100000
print()

fix,ax=plt.subplots()
labels = ('Necessary', 'Food", Unnecessary')

plt.show()


if __name__ == "__main__":
    main()