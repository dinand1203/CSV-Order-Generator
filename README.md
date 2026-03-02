# CSV Order Generator

#### Video Demo: <https://youtu.be/RgRzjliAAts>
#### Description: A command-line Python tool that turns any CSV pricelist into an order system. Load a menu, pick your items, and get a clean `order.csv` with names, IDs, and prices — all from the terminal.

---

## Features

- Works with **any CSV pricelist** — you choose the column names
- Displays the menu as a clean **ASCII table** before ordering
- **Validates input** at every step (file extension, file existence, column names, unknown items)
- Writes orders to `order.csv`, **appending without duplicating headers**
- Each order gets a **randomly generated ID**

---

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd CSV_Order_Generator

# Install dependencies
pip install -r requirements.txt
```

---

## Quick Start

A sample `menu.csv` is included so you can try it right away:

```bash
python project.py
```

Example session:

```
Give me your name for the order: Alice
Give me your pricelist in csv: menu.csv
Give me the first columname: cocktail
Give me the second columname: costs

+-----------------+--------+
| cocktail        | costs  |
+=================+========+
| Aperol Spritz   | 10     |
| Cosmopolitan    | 11     |
| Daiquiri        | 9      |
| Espresso Martini| 12     |
| Margarita       | 10     |
| Mojito          | 9      |
| Moscow Mule     | 11     |
| Negroni         | 12     |
| Old Fashioned   | 13     |
| Pina Colada     | 10     |
+-----------------+--------+

Type items one by one. Press Enter on empty line to finish.
Item: Mojito
Item: Negroni
Item:

Created order.csv successfully.
```

The resulting `order.csv`:

```
name,id,item,price
Alice,412,Mojito,$9
Alice,412,Negroni,$12
```

---

## How the Program Works

When the program starts, it first asks for the customer name and generates an `order_id` using a helper function. Next, the program asks the user for a filename of the pricelist CSV. To avoid mistakes, the program validates that the filename ends with `.csv`. If the user enters something else, the program keeps prompting until a valid `.csv` filename is provided.

After that, the program asks for two column names: one column for the item names and one column for the prices. This makes the program flexible — different CSV files can use different header names (for example `item,price` or `cocktail,costs`). The program then tries to read the pricelist using `csv.DictReader`. If the file does not exist, the user gets a "File not found" message. If the column names do not match the CSV headers, the program shows an error and keeps prompting the user until the correct column names are entered.

Once the CSV is read successfully, the program prints the menu in a clean ASCII table using the `tabulate` library, so the user can see what can be ordered. Then the user can type order items one by one. Pressing Enter on an empty line ends the ordering process.

Finally, the program writes the output to `order.csv`. Each item in the order becomes one row in the output file with the fields `name`, `id`, `item`, and `price`. If an item is not found in the menu, the program prints a warning and skips that item instead of crashing.

---

## Files in This Project

| File | Description |
|------|-------------|
| `project.py` | Core program — handles all user interaction, CSV reading, and output writing |
| `test_project.py` | Pytest test suite covering validation, ID generation, reading, and writing |
| `menu.csv` | Sample cocktail pricelist for testing and demonstration |
| `requirements.txt` | External dependencies (`tabulate`) |

---

## Design Choices

1. **Column names are provided by the user** — instead of forcing a fixed header like `item,price`, the program asks for the header names, making it work with many different CSV formats.

2. **Show the menu with tabulate** — the `tabulate` library displays the menu as an ASCII table so the user can clearly see available items and prices before ordering.

3. **Append output while avoiding duplicate headers** — the output file is opened in append mode so multiple orders can be saved in the same `order.csv`. The program checks whether the file is empty and only writes the header once.

4. **Graceful handling of invalid input** — loops and exceptions handle common mistakes (wrong file extension, missing file, wrong column names, items not on the menu) without crashing.

---

## Running Tests

```bash
pytest test_project.py
```
