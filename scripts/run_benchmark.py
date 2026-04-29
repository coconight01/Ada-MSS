from ada_mss.benchmark import run_benchmark
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Ada-MSS benchmark")
    parser.add_argument("--config", "-c", default="configs/default.json",
                        help="Path to config file")
    parser.add_argument("--dataset", "-d", default="data/processed/repair_tasks_demo.jsonl",
                        help="Path to dataset JSONL file")
    args = parser.parse_args()

    summary = run_benchmark(
        config_path=args.config,
        dataset_path=args.dataset,
    )
    print(f"Total: {summary.total}")
    print(f"Success: {summary.success}")
    print(f"Success rate: {summary.success_rate:.2%}")
    for item in summary.items:
        print(f"- {item.task_id}: {item.status}, attempts={item.attempts}, level={item.final_level}")
