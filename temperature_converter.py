def f_to_c(f): return (f - 32) * 5 / 9
def c_to_f(c): return c * 9 / 5 + 32

lang = input("Language/语言 (en/zh): ").strip().lower()
zh = lang == "zh"

print("1. F->C  2. C->F" if not zh else "1. 华氏->摄氏  2. 摄氏->华氏")
choice = input("Choice/选择: ").strip()
value = float(input("Temp/温度: "))

if choice == "1":
    print(f"{value}°F = {f_to_c(value):.2f}°C")
else:
    print(f"{value}°C = {c_to_f(value):.2f}°F")
