tasks = []

def add_task(name):
    task = {"name": name, "completed": False}
    tasks.append(task)
    print(f"Đã thêm công việc: {name}")

def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Đã đánh dấu hoàn thành: {tasks[task_index]['name']}")
    else:
        print("❌ Không tồn tại công việc này!")

def list_tasks():
    if not tasks:
        print("Chưa có công việc nào.")
    else:
        print("Danh sách công việc:")
        for i, task in enumerate(tasks, 1):
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['name']}")

if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập")
    complete_task(0)  # Đánh dấu công việc đầu tiên là hoàn thành
    list_tasks()
