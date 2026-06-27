import re
from datetime import datetime
managers = {}  # {姓名: {"email":..., "join_date":...}}
def add():
    name = input("姓名：").strip()
    if not name or name in managers:
        print("⚠️ 姓名为空或已存在\n"); return
    while True:
        email = input("邮箱：").strip()
        if re.match(r"^[\w.\-]+@[\w\-]+\.[\w.\-]+$", email):
            break
        print("⚠️ 邮箱格式错误，请重新输入")
    while True:
        date = input("加入日期(YYYY-MM-DD)：").strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("⚠️ 日期格式错误，请重新输入")
    managers[name] = {"email": email, "join_date": date}
    print(f"✅ 已添加 {name}\n")
def query():
    name = input("查询姓名(留空查全部)：").strip()
    items = managers.items() if not name else \
        ([(name, managers[name])] if name in managers else [])
    if not items:
        print("⚠️ 未找到记录\n" if name else "暂无记录\n"); return
    for n, i in items:
        print(f"{n} | {i['email']} | {i['join_date']}")
    print()
def delete():
    name = input("删除姓名：").strip()
    if name in managers:
        del managers[name]
        print(f"🗑️ 已删除 {name}\n")
    else:
        print("⚠️ 未找到该记录\n")
def main():
    actions = {"1": add, "2": query, "3": delete}
    while True:
        choice = input("1.添加 2.查询 3.删除 4.退出 请选择：").strip()
        if choice == "4":
            print("再见！"); break
        try:
            actions[choice]()
        except KeyError:
            print("⚠️ 无效输入\n")
        except Exception as e:
            print(f"⚠️ 出错：{e}\n")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n已退出")
        