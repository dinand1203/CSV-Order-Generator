import csv
import random
from tabulate import tabulate


def main():

    name = input("Give me your name for the order: ")
    order_id = get_id()

    while True:
        import_csv = input("Give me your pricelist in csv: ").lower().strip()
        if validate_csv(import_csv):
            break
        print("Provide an filename ending with '.csv'")



    while True:
        item_colum = input("Give me the first columname: ").lower().strip()
        price_colum = input("Give me the second columname: ").lower().strip()

        try:
            pricelist = read_pricelist(import_csv, item_colum, price_colum)
            show_pricelist(pricelist, item_colum, price_colum)
            break
        except FileNotFoundError:
            print("File not found:", import_csv)
        except KeyError:
            print("These column names were not found in the CSV headers. Try again.")



    print("\nType items one by one. Press Enter on empty line to finish.")

    ordered_items = []
    while True:
        item = input("Item: ").strip()
        if item == "":
            break
        ordered_items.append(item)

    if not ordered_items:
        print("No order")
        return


    write_order_csv("order.csv", name, order_id, ordered_items, pricelist)
    print("\nCreated order.csv succesfully.")



def validate_csv(file):
    return file.strip().lower().endswith(".csv")





def read_pricelist(file, item_colum, price_colum):

    pricelist = {}

    with open(file, newline="") as input_file:
        reader = csv.DictReader(input_file)
        for row in reader:
            item = row[item_colum].strip()
            price = row[price_colum].strip()
            pricelist[item] = price
        return pricelist




def show_pricelist(pricelist, item_colum, price_colum):
    rows = []
    for item in sorted(pricelist):
        price = pricelist[item]
        rows.append({item_colum: item, price_colum: price})
    print(tabulate(rows, headers="keys", tablefmt="grid"))





def get_id():
    return random.randint(1, 999)




def write_order_csv(output_file, name, order_id, ordered_items, pricelist):

    with open(output_file, "a+", newline="") as file:
        fieldnames = ["name", "id", "item", "price"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        file.seek(0)
        is_empty = (file.read(1) == "")
        file.seek(0, 2)

        if is_empty:
            writer.writeheader()


        for item in ordered_items:
            if item not in pricelist:
                print(f"{item} not on the menu")
                continue

            writer.writerow({"name": name, "id": order_id, "item": item, "price": '$' + pricelist[item]})



if __name__ == "__main__":
    main()
