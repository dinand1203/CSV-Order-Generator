# CSV Order Generator
#### Video Demo:  <https://youtu.be/RgRzjliAAts>
#### Description: This project is a small command-line program written in Python that helps a user create an order file based on a menu/pricelist stored in a CSV file. The main idea is simple: the user provides a pricelist CSV (for example a cocktail menu with prices), chooses which columns represent the item names and the prices, and then types the items they want to order. After the user finishes the order, the program generates (or updates) an `order.csv` file that contains the customer name, a randomly generated order id, each ordered item, and the matching price from the pricelist.


## How the program works
When the program starts, it first asks for the customer name and generates an `order_id` using a helper function. Next, the program asks the user for a filename of the pricelist CSV. To avoid mistakes, the program validates that the filename ends with `.csv`. If the user enters something else, the program keeps prompting until a valid `.csv` filename is provided.

After that, the program asks for two column names: one column for the item names and one column for the prices. This makes the program flexible: different CSV files can use different header names (for example `item,price` or `cocktail,cost`). The program then tries to read the pricelist using `csv.DictReader`. If the file does not exist, the user gets a “File not found” message. If the column names do not match the CSV headers, the program shows an error and keeps prompting the user until the correct column names are entered.

Once the CSV is read successfully, the program prints the menu in a clean ASCII table using the `tabulate` library, so the user can see what can be ordered. Then the user can type order items one by one. Pressing Enter on an empty line ends the ordering process.

Finally, the program writes the output to `order.csv`. Each item in the order becomes one row in the output file with the fields `name`, `id`, `item`, and `price`. If an item is not found in the menu, the program prints a warning and skips that item instead of crashing.


## Files in This Project
- **project.py** (or your main Python file):
  This is the core program. It contains the `main()` function and all helper functions. It handles user interaction, reads the pricelist, prints the menu, collects order items, and writes the output CSV.

- **requirements.txt**:
  This file lists any external libraries needed to run the project. In this project, the standard libraries `csv` and `random` do not need to be installed. However, `tabulate` is a third-party library, so it must be listed here.

- **README.md**:
  This documentation file explains what the project is, how it works, and why certain design choices were made.

- **pricelist.csv** (optional example file):
  A sample CSV menu that a user can test with. This file is not required, but it is helpful for demonstrating the project.

- **order.csv** (output file):
  The program generates or appends to this file. It contains the final order details.


## Design Choices
A few design choices were made to keep the program simple and user-friendly:

1. **Column names are provided by the user**
   Instead of forcing a fixed header like `item,price`, the program asks the user for the header names. This makes it work with many different pricelist formats.

2. **Show the menu with tabulate**
   The `tabulate` library is used to show the menu as an ASCII table. This improves usability because the user can clearly see the available items and their prices before ordering.

3. **Append output while avoiding duplicate headers**
   The output file is opened in append mode so multiple orders can be saved in the same `order.csv` file. To prevent repeated headers, the program checks whether the file is empty and only writes the header once.

4. **Graceful handling of invalid input**
   The program uses loops and exceptions to handle common mistakes (wrong file extension, missing file, wrong column names, and items not on the menu) without crashing.

