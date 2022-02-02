pip install PrettyTable

def main():
    from prettytable import PrettyTable
    my_table = PrettyTable()
    my_table.add_row([1, "Bob", 6, 11])
    my_table.add_row([2, "Freddy", 4, 10])
    my_table.add_row([3, "John", 7, 13])
    print(my_table)


if __name__ == "__main__":
    main()
