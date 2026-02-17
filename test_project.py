import project



def test_validate_csv():
    assert project.validate_csv("menu.csv") == True
    assert project.validate_csv("MENU.CSV") == True
    assert project.validate_csv(" menu.csv  ") == True
    assert project.validate_csv("menu.txt") == False
    assert project.validate_csv("menu") == False


def test_get_id():
    order_id = project.get_id()
    assert isinstance(order_id, int)
    assert 1 <= order_id <= 999


def test_read_pricelist():
    pricelist = project.read_pricelist("menu.csv", "cocktail", "costs")

    assert pricelist is not None
    assert type(pricelist) == dict
    assert len(pricelist) > 0


def test_write_order_csv_writes_header_and_rows():
    output_file = f"test_order_{project.get_id()}.csv"

    pricelist = project.read_pricelist("menu.csv", "cocktail", "costs")
    first_item = list(pricelist.keys())[0]

    project.write_order_csv(output_file, "Alice", 123, [first_item], pricelist)

    with open(output_file, "r", newline="") as f:
        lines = [line.strip() for line in f.read().splitlines() if line.strip()]

    assert lines[0] == "name,id,item,price"
    assert any(line.startswith("Alice,123,") for line in lines[1:])
    assert any(f",{first_item}," in line for line in lines[1:])


def test_write_order_csv_skips_unknown_item():
    output_file = f"test_order_{project.get_id()}_unknown.csv"
    pricelist = project.read_pricelist("menu.csv", "cocktail", "costs")

    project.write_order_csv(output_file, "Bob", 5, ["this_item_does_not_exist"], pricelist)

    with open(output_file, "r", newline="") as f:
        lines = [line.strip() for line in f.read().splitlines() if line.strip()]

    assert lines[0] == "name,id,item,price"
    assert len(lines) == 1
