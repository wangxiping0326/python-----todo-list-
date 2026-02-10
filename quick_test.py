# quick_test.py
from core import Todo_list

# 快速测试
todo = Todo_list("quick_test.json")

# 添加任务
todo.add_task("任务1: 测试JSON保存")
todo.add_task("任务2: 验证中文支持")

# 保存
print("正在保存...")
if todo.save_to_json():
    print("保存成功！")

    # 显示文件内容
    try:
        with open("quick_test.json", "r", encoding="utf-8") as f:
            content = f.read()
        print("\n文件内容:")
        print(content)
    except:
        print("无法读取文件")
else:
    print("保存失败")

# 清理
import os

if os.path.exists("quick_test.json"):
    os.remove("quick_test.json")