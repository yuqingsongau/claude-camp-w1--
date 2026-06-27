# Tip calculator

bill = input("请输入餐费金额: ")
tip_percent = input("请输入小费比例(例如输入15代表15%): ")

try:
    bill_amount = float(bill)
    tip_rate = float(tip_percent)
except ValueError:
    print("请输入有效的数字哦~")
else:
    tip_amount = bill_amount * (tip_rate / 100)
    total = bill_amount + tip_amount

    print(f"餐费金额: ${bill_amount:.2f}")
    print(f"小费金额: ${tip_amount:.2f}")
    print(f"总金额: ${total:.2f}")