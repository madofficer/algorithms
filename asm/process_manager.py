import os
import psutil
import threading
import time

class ProcessManager:
    def __init__(self):
        self.processes = {}

    def create_process(self, command_args, priority=10):
        pid = os.fork()
        if pid == 0:
            os.nice(priority)
            try:
                # Запуск приложения с аргументами
                os.execvp(command_args[0], command_args)
            except FileNotFoundError:
                print(f"Ошибка: Приложение '{command_args[0]}' не найдено")
                os._exit(1)
        else:
            self.processes[pid] = {
                "priority": priority,
                "command": " ".join(command_args)
            }
            print(f"Запущен процесс {pid}: {' '.join(command_args)}")

    def terminate_process(self, pid):
        if pid in self.processes:
            os.kill(pid, 9)
            del self.processes[pid]
            print(f"Процесс {pid} завершен")
        else:
            print(f"Процесс {pid} не найден")

    def suspend_resume_thread(self, thread):
        if thread.is_alive():
            print(f"Приостанавливаю поток {thread.name}")
            thread.suspend = True
        else:
            print(f"Возобновляю поток {thread.name}")
            thread.suspend = False

    def show_process_tree(self):
        for proc in psutil.process_iter(['pid', 'ppid', 'name']):
            print(f"PID: {proc.info['pid']}, PPID: {proc.info['ppid']}, Name: {proc.info['name']}")

    def process_info(self, pid):
        if pid in self.processes:
            proc = psutil.Process(pid)
            mem = proc.memory_info().rss
            threads = len(proc.threads())
            print(f"Процесс {pid}: память {mem} байт, потоки {threads}")
        else:
            print(f"Процесс {pid} не найден")

    def change_priority(self, pid, priority):
        if pid in self.processes:
            os.setpriority(os.PRIO_PROCESS, pid, priority)
            self.processes[pid]['priority'] = priority
            print(f"Приоритет процесса {pid} изменен на {priority}")
        else:
            print(f"Процесс {pid} не найден")


def start():
    print("Доступные команды:")
    print("  create <app> [args] - запустить приложение (например: create gedit ~/notes.txt)")
    print("  terminate <pid>     - завершить процесс")
    print("  tree                - показать дерево процессов")
    print("  info <pid>          - информация о процессе")
    print("  priority <pid> <n>  - изменить приоритет (от -20 до 19)")
    print("  exit                - выход")