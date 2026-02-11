def create_report(data_file_name: str, report_file_name: str) -> None:
    file = open(data_file_name, "r")
    supply_total = 0
    buy_total = 0
    for line in file:
        if not line.strip():
            continue
        operation, amount = line.split(",")
        operation = operation.strip()
        amount = int(amount)

        if operation == "supply":
            supply_total += amount
        elif operation == "buy":
            buy_total += amount
    result = supply_total - buy_total
    file_1 = open(report_file_name, "w")
    file_1.write(f"supply,{supply_total}\n")
    file_1.write(f"buy,{buy_total}\n")
    file_1.write(f"result,{result}\n")
    file.close()
    file_1.close()