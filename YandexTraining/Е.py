import json

income = {}
expired = {}
skipped = {}

with open('logs.jsonl', 'r') as f:
    for line in f:
        record = json.loads(line)
        assignment_id = record['assignment_id']
        start_ts = record['start_ts']
        end_ts = record['end_ts']
        status = record['status']
        task_id = record['task_id']
        worker_id = record['worker_id']
        skill_value = record['skill_value']

        if status == "APPROVED":
            time_spent = min((end_ts - start_ts) / 3600, 1)

            if skill_value < 50:
                rate_per_hour = 0
            elif skill_value <= 100:
                rate_per_hour = 40 + (skill_value - 50) * (60 - 40) / (100 - 50)
            else:
                rate_per_hour = 60

            payment = time_spent * rate_per_hour

            if task_id in expired and (start_ts > expired[task_id][0] or start_ts > expired[task_id][1]):
                payment *= 2

            elif task_id in skipped:
                if skipped[task_id]:
                    payment *= 2
                    skipped[task_id] = False

            if worker_id not in income:
                income[worker_id] = 0
            income[worker_id] += payment

        elif status == "EXPIRED":
            expired[task_id] = [start_ts, end_ts]

        else:
            skipped[task_id] = True
best_worker = max(income, key=income.get)

print(f"{sum(income.values()):.3f}")
print(f"{best_worker} {income[best_worker]:.3f}")
