name = input("请输入你的姓名: ")
age_input = input("请输入你的年龄: ")

try:
    age = int(age_input)
except ValueError:
    print("年龄请输入数字哦~")
else:
    if age < 18:
        stage = "未成年"
    elif age < 60:
        stage = "成年人"
    else:
        stage = "长辈"

    print (f"你好, {name}! 你今年 {age} 岁, 属于「{stage}」阶段, 祝你身体健康, 万事如意! 🎉")