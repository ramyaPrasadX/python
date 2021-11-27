import statistics

stocks = {
    'info' : [600, 630, 620],
    'ril' : [1430, 1490, 1567],
    'mtl' : [234, 180, 160],

}

def print_all():
    for stock, price_list in stocks.items():
        avg = statistics.mean(price_list)
        print(f"{stock} ==> {price_list} ==> avg:", round(avg, 2))

def add():
    s = input("enter a stock ticket to add:")
    p = input("enter the price of the stock")
    p = float(p)

    if s in stocks:
        stocks[s].append(p)
    else:
        stocks[s] = [p]
    print_all()

def main():
    op = input("enter operation Print or add:")

    if op.lower() == 'print':
        print_all()
    elif op.lower() == 'add':
        add()
    else:
        print(" opearation not possible")

if __name__ == '__main__':

    main()
