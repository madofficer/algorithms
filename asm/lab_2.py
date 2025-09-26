from process_manager import ProcessManager,start

if __name__ == "__main__":
    manager = ProcessManager()
    while True:
       
        start()

        command = input("\nВведите команду: ").strip()

        if command.startswith("create"):
            parts = command.split()
            if len(parts) >= 2:
                manager.create_process(parts[1:])
            else:
                print("Ошибка: Укажите команду для запуска (например: create firefox)")

        elif command.startswith("terminate"):
            try:
                pid = int(command.split()[1])
                manager.terminate_process(pid)
            except (IndexError, ValueError):
                print("Ошибка: Укажите PID процесса")
        elif command == "tree":
            manager.show_process_tree()
        elif command == "info":
            pid = int(input("Введите PID: "))
            manager.process_info(pid)
        elif command == "priority":
            pid = int(input("Введите PID: "))
            priority = int(input("Введите приоритет: "))
            manager.change_priority(pid, priority)
        elif command == "exit":
            break


# create nano ~/notes.txt
# create open /Users/kuznetsov/downloads/_720_2097763199.mp4