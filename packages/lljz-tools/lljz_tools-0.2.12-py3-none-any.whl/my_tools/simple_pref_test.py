# coding=utf-8

"""
@fileName       :   simple_pref_test.py
@data           :   2024/4/19
@author         :   jiangmenggui@hosonsoft.com
"""
import queue
import random
import time
from concurrent.futures import ThreadPoolExecutor
from inspect import isfunction
from typing import TypedDict

from my_tools.console_table import ConsoleTable

data: queue.Queue["TaskResult"] = queue.Queue()


class TaskResult(TypedDict):
    name: str
    start: float
    end: float
    use_time: float
    message: str


def task(name: str, weight=1):
    """
    测试任务
    :param name: 任务名称
    :param weight: 任务执行权重
    :return:
    """

    def outer(func):
        def inner(*args, **kwargs):
            t1 = time.time()
            try:
                func(*args, **kwargs)
                t2 = time.time()
                data.put(TaskResult(**{'name': name, 'start': t1, 'end': t2, "use_time": t2 - t1, "message": ""}))
            except Exception as e:
                t2 = time.time()
                data.put(TaskResult(**{'name': name, 'start': t1, 'end': t2, "use_time": t2 - t1, "message": str(e)}))

        inner.is_task = True
        inner.weight = weight
        return inner

    return outer


def show_result():
    result: dict[str, dict] = {}
    while not data.empty():
        row = data.get()
        if row['name'] not in result:
            result[row['name']] = {
                "NAME": row['name'],
                "START_TIME": row['start'],
                "END_TIME": row['end'],
                "USE_TIME": [row['use_time']],
            }
        else:
            result[row['name']]['START_TIME'] = min(result[row['name']]['START_TIME'], row['start'])
            result[row['name']]['END_TIME'] = max(result[row['name']]['END_TIME'], row['end'])
            result[row['name']]['USE_TIME'].append(row['use_time'])
    table_data = []
    for value in result.values():
        use_time = sorted(value["USE_TIME"])
        table_data.append({
            "任务名称": value['NAME'],
            "任务执行次数": len(use_time),
            "开始时间": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(value['START_TIME'])),
            "结束时间": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(value['END_TIME'])),
            "中位数响应(ms)": f"{use_time[int(len(use_time) * 0.5)] * 1000:.1f}ms",
            "90%响应(ms)": f"{use_time[int(len(use_time) * 0.9)] * 1000:.1f}ms",
            "95%响应(ms)": f"{use_time[int(len(use_time) * 0.95)] * 1000:.1f}ms",
            "平均响应(ms)": f"{sum(value['USE_TIME']) * 1000 / len(value['USE_TIME']):.1f}ms",
            "最小响应(ms)": f"{use_time[0] * 1000:.1f}ms",
            "最大响应(ms)": f"{use_time[-1] * 1000:.1f}ms",
        })
    print(ConsoleTable(table_data, caption="性能测试结果"))


class PrefRunner:
    def __init__(self, module, virtual_users=10, user_add_interval=0.1, run_seconds=10):
        self.tasks = []

        for v in module.__dict__.values():
            if isfunction(v) and getattr(v, 'is_task', False):
                self.tasks.extend((v for _ in range(getattr(v, 'weight', 1))))
        self.run_seconds = run_seconds
        self.user_add_interval = user_add_interval
        self.virtual_users = virtual_users
        self.pool = ThreadPoolExecutor(virtual_users)

    def run_task(self, *args, **kwargs):
        start = time.time()
        while time.time() - start < self.run_seconds:
            random.choice(self.tasks)(*args, **kwargs)

    def start(self, *args, **kwargs):
        for _ in range(self.virtual_users):
            self.pool.submit(self.run_task, *args, **kwargs)
            time.sleep(self.user_add_interval)
        self.pool.shutdown(wait=True)
        show_result()


# show_result()

if __name__ == '__main__':
    pass
