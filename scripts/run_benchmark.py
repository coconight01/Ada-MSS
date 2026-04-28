from ada_mss.benchmark import run_benchmark


if __name__ == "__main__":
    summary = run_benchmark(
        config_path="configs/default.json",
        dataset_path="data/processed/repair_tasks_demo.jsonl",
    )
    print(f"Total: {summary.total}")
    print(f"Success: {summary.success}")
    print(f"Success rate: {summary.success_rate:.2%}")
    for item in summary.items:
        print(f"- {item.task_id}: {item.status}, attempts={item.attempts}, level={item.final_level}")
