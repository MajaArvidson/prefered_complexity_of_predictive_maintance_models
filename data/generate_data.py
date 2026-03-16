import json
import random
import itertools
import pandas as pd
from datetime import datetime, timedelta

RANGES = {
    "cpu": {"low": (0,35), "high": (75,100)},
    "memory": {"low": (20,50), "high": (80,100)},
    "disk": {"low": (0,10), "high": (80,500)},
    "network": {"low": (5,40), "high": (120,500)},
}

MISLABEL_CHANCE = 0.10

def pick_value(metric, level, ranges):
    if random.random() < MISLABEL_CHANCE:
        level = "high" if level == "low" else "low"
    
    low, high = ranges[metric][level]
    value = random.uniform(low, high)

    return round(value, 1)

def generate_log(combo):
    return {
        "cpu_usage": pick_value("cpu", combo[0], RANGES),
        "memory_usage": pick_value("memory", combo[1], RANGES),
        "disk_io": pick_value("disk", combo[2], RANGES),
        "network_latency": pick_value("network", combo[3], RANGES)
    }

def generate_logs(n_rows, csv_file="system_states.csv", output_file="telemetry_data.jsonl"):
    df = pd.read_csv(csv_file)
    recommended_actions = df["Recommended_Action"].tolist()

    levels = ["low", "high"]
    combinations = list(itertools.product(levels, repeat=4))
    n_combos = len(combinations)

    timestamp = datetime(2026, 2, 27, 10, 55, 0)

    with open(output_file, "w") as f:
        for i in range(n_rows):
            combo_idx = i % n_combos
            combo = combinations[combo_idx]

            log_entry = {"timestamp": timestamp.isoformat()}
            timestamp += timedelta(seconds=random.randint(0, 60))

            log_entry.update(generate_log(combo))
            log_entry.update({
                "recommended_action": recommended_actions[combo_idx]
            })

            f.write(json.dumps(log_entry) + "\n")

if __name__ == "__main__":
    generate_logs(10000)