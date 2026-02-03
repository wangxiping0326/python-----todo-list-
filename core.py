from operator import index
from symtable import Class
from datetime import datetime

from django.contrib.admin.templatetags.admin_list import results


class Task:#这个类明确分工管理任务信息

    # 1. 初始化属性
    def __init__(self,task_id,description,status =False):
        self.id =task_id
        self.description = description
        self.status = status
        self.created_at = datetime.now()  # 自动记录创建时间

    # 2. 方法：改变自己的状态
    def mark_status(self):
        self.status = True #标记任务完结

    # 3. 方法：提供自己的信息
    def __str__(self):
        """__str__ 是一个特殊方法（也叫魔法方法/dunder方法），
        它的作用是：定义当你的对象被转换为字符串时，应该显示什么内容。"""
        icon = "✓" if self.status else "□"
        return f"{self.id}. [{icon}] {self.description}"

    def get_info(self):
        """返回任务的详细信息（字典形式）"""
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

class Todo_list:

    def __init__(self):
        self.tasks = []#生成一个存储任务清单的列表
        self.next_id = 1

    def add_task(self,description):
        print("新建任务")
        new_task = Task(self.next_id,description)#创建一个新的task对象
        self.tasks.append(new_task)#将新的任务对象存放到任务清单列表里
        self.next_id += 1
        return new_task

    def print_all(self):
        """打印所有任务"""
        if not self.tasks:
            print("📭 还没有任务")
            return

        for task in self.tasks:
            print(task)

    def get_task(self,task_id):#task_id是用户输入参数传入
        for index,task in enumerate(self.tasks):
            if task.id == task_id:#task.id是任务属性自带参数
                return task,index#返回对应任务对象与序列

        return None,-1#没有找到

    def search_task(self,search_keyword):
        if not self.tasks:
            print("📭 还没有任务")
            return []

        search_task_results=[]
        for task in self.tasks:
            if search_keyword.lower() in task.description.lower():
                search_task_results.append(task)
        return search_task_results



    def delete_task(self,task_id):
        """删除任务并且自动重新编号"""
        task,index = self.get_task(task_id)

        if task is None:
            return None
        #删除任务
        removed_task = self.tasks.pop(index)
        print(f"任务：{removed_task}已被删除")
        #自动重新编号
        self._renumber_tasks()

        return removed_task

    def _renumber_tasks(self):
        """内部方法：重新编号所有任务"""
        for new_id, task in enumerate(self.tasks, 1):
            task.id = new_id
            # 更新下一个可用ID
        self.next_id = len(self.tasks) + 1


####################测试代码###############################3
if __name__ == "__main__":
    print("=== 测试Task类 ===")
    task = Task(1, "测试任务")
    print(f"任务显示: {task}")

    task.mark_status()
    print(f"标记完成后: {task}")

    print("\n=== 测试Todo_list类 ===")
    todo = Todo_list()

    # 测试空列表
    print("1. 空列表测试:")
    todo.print_all()

    # 测试添加任务
    print("\n2. 添加任务测试:")
    task1 = todo.add_task("学习面向对象编程")  # ✅ 现在有返回值了
    print(f"添加了: {task1}")

    task2 = todo.add_task("掌握Git使用")
    print(f"添加了: {task2}")

    # 测试显示
    print("\n3. 显示所有任务:")
    todo.print_all()

    # 测试查找
    print("\n4. 查找任务测试:")
    found_task, index = todo.get_task(1)
    print(f"找到ID=1: {found_task}, 位置: {index}")

    not_found, idx = todo.get_task(999)
    print(f"查找ID=999: 任务={not_found}, 位置={idx}")

    # 测试删除
    print("\n5. 删除任务测试:")
    print("删除前:")
    todo.print_all()

    success, msg = todo.delete_task(1)  # ✅ 删除第一个任务
    print(f"\n删除结果: {success}, 消息: {msg}")

    print("\n删除后（应该重新编号）:")
    todo.print_all()
    print(f"下一个ID应该是: {todo.next_id}")

    # 测试删除不存在的任务
    print("\n6. 删除不存在任务测试:")
    success, msg = todo.delete_task(100)
    print(f"结果: {success}, 消息: {msg}")