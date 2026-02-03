from core import Todo_list
import sys

class TodoCLI:
    def __init__(self):
        self.todo = Todo_list()
        #self.load_data()

    def menu_task(self):
        print("\n" + "=" * 40)
        print("欢迎使用个人数据管理系统！")
        print("=" * 40)
        print("1. 📝 添加新任务")
        print("2. 📋 查看所有任务")
        print("3. ✅ 标记任务状态")
        print("4. 🗑️  删除任务")
        print("5. 🔍 搜索任务")
        print("6. 📊 数据统计")
        print("7. 💾 保存并退出")
        print("-" * 40)

    def Get_menu_choice(self):
        while True:
            choice = input("\n请选择操作(1-7)").strip()
            #如果没有输入、报错
            if choice == "":
                print("⚠️  请输入选项编号")
                continue

            if choice.isdigit():
                num = int(choice)
                if 1 <= num <= 7:
                    return num
            else:
                print("❌ 请输入1-7之间的数字")

    def handle_add_tasks(self):
         while True:
             description = input("请输入任务描述：\n").strip()
             if not description:
                 print("描述不能为空")
                 break
             task = self.todo.add_task(description)
             print(f"✅ 已添加: {task}")

    def handle_print_all_tasks(self):
        """查看所有任务"""
        print("\n" + "-" * 30)
        print("📋 所有任务")
        print("-" * 30)
        if not self.todo.tasks:
            print("📭 还没有任务，快去添加一个吧！")
            return
        self.todo.print_all()

        #显示统计信息
        total = len(self.todo.tasks)
        completed = sum(1 for t in self.todo.tasks if t.status)
        print(f"\n📊 统计: 共{total}个任务，已完成{completed}个 "
              f"({completed / total * 100:.0f}%)")

    def handle_mark_down(self):
        print("\n" + "-" * 30)
        print("标记任务完成")
        print("-" * 30)

        if not self.todo.tasks:
            print("📭 还没有任务，快去添加一个吧！")
            return
        # 先显示当前任务
        #    show_tasks(tasks)
        self.todo.print_all()
        # 获取用户输入
        try:
            mark_task_id= int(input("\n请输入要完结的任务序号:").strip())
            task = self.todo.get_task(mark_task_id) # ← get_task返回(task, index)
            if task:
                task.mark_status()
                print(f"✅ 任务 {mark_task_id} 已标记完成！")
            else:
                 print(f"❌ 找不到ID为{mark_task_id}的任务")
        except ValueError:
            print(f"❌ 请输入有效的任务ID")


    def handle_delete_task(self):
        print("\n" + "-" * 30)
        print("删除任务")
        print("-" * 30)
        if not self.todo.tasks:
            print("📭 还没有任务，快去添加一个吧！")
            return
        # 先显示当前任务
        self.todo.print_all()
        # 获取用户输入
        try:
            delete_task_id = int(input("\n请输入要删除的任务序号:").strip())
            delete_task = self.todo.delete_task(delete_task_id)
            if delete_task:
                print(f"✅ 任务 {delete_task.description} 已删除！")
            else:
                print(f"❌ 找不到ID为{delete_task_id}的任务")
        except ValueError:
            print(f"❌ 请输入有效的任务ID")

    def handle_search_task(self):
        print("\n" + "-" * 30)
        print("查找任务")
        print("-" * 30)
        if not self.todo.tasks:
            print("📭 还没有任务，快去添加一个吧！")
            return
        # 先显示当前任务
        self.todo.print_all()
        search_keyword = input("\n请输入要搜索的任务内容或关键字:").strip()
        if not search_keyword:
            print("输入不能为空")
            return

        search_task_results = self.todo.search_task(search_keyword)
        if search_task_results:
            print(f"找到{len(search_task_results)}个相关任务")
            for task in search_task_results:
                print(task)
        print(f"没有找到与{search_keyword}相关的任务")


    def handle_task_data(self):
        print("\n" + "-" * 30)
        print("显示任务数据")
        print("-" * 30)
        if not self.todo.tasks:
            print("📭 还没有任务，快去添加一个吧！")
            return


    def run(self):
        while True:
            self.menu_task()
            choice = self.Get_menu_choice()
            if choice == 1:
                self.handle_add_tasks()
                pass
            elif choice == 2:
                self.handle_print_all_tasks()
                pass
            elif choice == 3:
                self.handle_mark_down()
                pass
            elif choice == 4:
                self.handle_delete_task()
                pass
            elif choice == 5:
                self.handle_search_task()
                pass
            elif choice == 6:
                self.handle_task_data()
                pass
            elif choice ==7:
                print("💾 保存数据...")
                # TODO: 实现保存功能
                print("👋 再见！")
                break  # ← 退出循环






####################测试代码###############################
class TodoCLITester:
    """测试TodoCLI的完整功能"""
    def __init__(self):
        self.cli = TodoCLI()
        self.test_result = []

    def run_test(self):
        """运行所有测试"""
        print("开始运行所有TodoCLI测试套件")
        print("=" * 50)

        #执行测试用例
        self.test_add_task()
        self.test_print_all_task()
        self.test_mark_test_status()
        self.test_delete_task()
        #self.test_search_task()
        #self.test_data_stats()
        #self.test_invalid_input()
        self.test_edge_cases()

        #显示测试结果
        self.print_results()

    def assert_equal(self,actual,expected,test_name):
        """断言辅助函数"""
        if actual ==expected:
            self.test_result.append(f"✅{test_name}")
            return True
        else:
            self.test_result.append(f"❌{test_name},"
                                    f"expected={expected},"
                                    f"actual={actual}")
            return False

    """具体测试用例"""
    def test_add_task(self):
        """测试添加任务功能"""
        print("\n1. 测试添加任务..." )

        #重置状态
        self.cli.todo.tasks = []
        self.cli.todo.next_id = 1

        #模拟添加任务
        task = self.cli.todo.add_task("测试任务1")
        #task = self.cli.todo.add_task("测试任务2")

        #验证
        success = True
        success &= self.assert_equal(len(self.cli.todo.tasks), 1, "任务列表长度")
        success &= self.assert_equal(task.id, 1, "任务ID")
        success &= self.assert_equal(task.description, "测试任务1", "任务描述")
        success &= self.assert_equal(task.status, False, "任务状态（未完成）")

        if success:
            print("   ✅ 添加任务测试通过")
        else:
            print("   ❌ 添加任务测试失败")

    def test_print_all_task(self):
        """测试查看任务功能"""
        print("\n2. 测试查看任务...")

        # 准备测试数据
        self.cli.todo.tasks = []
        self.cli.todo.next_id = 1
        self.cli.todo.add_task("任务A")
        self.cli.todo.add_task("任务B")

        # 验证
        success = True
        success &= self.assert_equal(len(self.cli.todo.tasks), 2, "任务数量")

        # 检查任务顺序和内容
        if self.cli.todo.tasks:
            success &= self.assert_equal(self.cli.todo.tasks[0].description, "任务A", "第一个任务")
            success &= self.assert_equal(self.cli.todo.tasks[1].description, "任务B", "第二个任务")

        if success:
            print("   ✅ 查看任务测试通过")
        else:
            print("   ❌ 查看任务测试失败")

    def test_mark_test_status(self):
        """测试标记任务完成"""
        print("\n3. 测试标记任务完成...")

        # 准备数据
        self.cli.todo.tasks = []
        self.cli.todo.next_id = 1
        task = self.cli.todo.add_task("待完成的任务")

        # 标记完成
        task.mark_status()

        # 验证
        success = self.assert_equal(task.status, True, "任务状态应为完成")

        if success:
            print("   ✅ 标记任务完成测试通过")
        else:
            print("   ❌ 标记任务完成测试失败")

    def test_delete_task(self):
        """测试删除任务及重新编号"""
        print("\n4. 测试删除任务...")

        # 准备数据（3个任务）
        self.cli.todo.tasks = []
        self.cli.todo.next_id = 1
        self.cli.todo.add_task("任务1")
        self.cli.todo.add_task("任务2")
        self.cli.todo.add_task("任务3")

        # 删除中间的任务（ID=2）
        deleted = self.cli.todo.delete_task(2)

        # 验证删除结果
        success = True
        success &= self.assert_equal(deleted.description, "任务2", "删除的任务描述")
        success &= self.assert_equal(len(self.cli.todo.tasks), 2, "删除后任务数量")

        # 验证重新编号
        if len(self.cli.todo.tasks) >= 2:
            success &= self.assert_equal(self.cli.todo.tasks[0].id, 1, "第一个任务ID")
            success &= self.assert_equal(self.cli.todo.tasks[1].id, 2, "第二个任务ID（原ID=3）")

        if success:
            print("   ✅ 删除任务测试通过")
        else:
            print("   ❌ 删除任务测试失败")

    def test_edge_cases(self):
        """测试边界情况"""
        print("\n5. 测试边界情况...")

        success = True

        # 测试空列表操作
        self.cli.todo.tasks = []
        self.cli.todo.next_id = 1

        # 测试删除不存在的任务
        result = self.cli.todo.delete_task(999)
        success &= self.assert_equal(result, None, "删除不存在的任务应返回None")

        # 测试查找不存在的任务
        task, index = self.cli.todo.get_task(999)
        success &= self.assert_equal(task, None, "查找不存在的任务应返回None")
        success &= self.assert_equal(index, -1, "查找不存在的任务索引应为-1")

        if success:
            print("   ✅ 边界情况测试通过")
        else:
            print("   ❌ 边界情况测试失败")


    def print_results(self):
        """打印测试结果汇总"""
        print("\n" + "=" * 50)
        print("📊 测试结果汇总")
        print("=" * 50)

        for result in self.test_result:
            print(result)

        total = len(self.test_result)
        passed = sum(1 for r in self.test_result if r.startswith("✅"))
        failed = total - passed

        print(f"\n📈 统计: 共{total}项测试，通过{passed}项，失败{failed}项")

        if failed == 0:
            print("🎉 所有测试通过！")
        else:
            print("⚠️  有测试失败，请检查")


if __name__ == "__main__":
    # 检查是否有测试参数
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # 运行测试
        tester = TodoCLITester()
        tester.run_test()
    else:
        # 正常运行程序
        app = TodoCLI()
        app.run()
# 你的设计：
# 1. 这里应该先做什么？显示菜单
# 2. 如何获取用户选择？输入选项
# 3. 如何根据选择调用不同功能？if-elif-else
# 4. 如何退出程序？
