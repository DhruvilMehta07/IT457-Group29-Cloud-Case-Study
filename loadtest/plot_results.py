"""
Print a summary table and draw comparison graphs from the Locust CSV files.

Run from the repo root after the load tests:
    pip install matplotlib
    python3 loadtest/plot_results.py

It looks for docs/measurements/stage<A|B|C>_u50*_stats.csv.
If a stage has several runs (run1, run2, run3) it shows all of them in the
table and uses the middle run (by average response time) in the graphs.
Graphs are saved in docs/measurements/.
"""
import csv
import glob
import os
import statistics

MEAS = "docs/measurements"
STAGES = [("A", "Stage A (laptop)"), ("B", "Stage B (EC2)"), ("C", "Stage C (RDS)")]


def aggregated(path):
    for row in csv.DictReader(open(path)):
        if row["Name"] == "Aggregated":
            return {
                "requests": int(row["Request Count"]),
                "failures": int(row["Failure Count"]),
                "avg": float(row["Average Response Time"]),
                "p95": float(row["95%"]),
                "rps": float(row["Requests/s"]),
            }
    return None


def history(path):
    """Seconds since start, average response time so far, requests per second."""
    rows = list(csv.DictReader(open(path)))
    start = int(rows[0]["Timestamp"])
    out = []
    for r in rows:
        try:
            out.append((int(r["Timestamp"]) - start,
                        float(r["Total Average Response Time"]),
                        float(r["Requests/s"])))
        except ValueError:
            pass
    return out


def main():
    summary = {}
    print(f"{'file':38} {'reqs':>6} {'fail':>5} {'avg ms':>7} {'p95 ms':>7} {'req/s':>6}")
    for code, _ in STAGES:
        files = sorted(glob.glob(f"{MEAS}/stage{code}_u50*_stats.csv"))
        files = [f for f in files if "_long" not in f]
        runs = []
        for f in files:
            agg = aggregated(f)
            if agg:
                runs.append((f, agg))
                print(f"{os.path.basename(f):38} {agg['requests']:>6} {agg['failures']:>5} "
                      f"{agg['avg']:>7.1f} {agg['p95']:>7.0f} {agg['rps']:>6.1f}")
        if runs:
            runs.sort(key=lambda x: x[1]["avg"])
            summary[code] = runs[len(runs) // 2]  # the middle run

    if not summary:
        print("No stats files found.")
        return

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("Install matplotlib to draw the graphs: pip install matplotlib")
        return

    names = {c: n for c, n in STAGES}
    codes = [c for c, _ in STAGES if c in summary]

    fig, ax = plt.subplots(figsize=(6, 4))
    width = 0.35
    xs = range(len(codes))
    ax.bar([x - width / 2 for x in xs], [summary[c][1]["avg"] for c in codes], width, label="Average")
    ax.bar([x + width / 2 for x in xs], [summary[c][1]["p95"] for c in codes], width, label="95th percentile")
    ax.set_xticks(list(xs))
    ax.set_xticklabels([names[c] for c in codes])
    ax.set_ylabel("Response time (ms)")
    ax.set_title("Response time at 50 users")
    ax.legend()
    fig.tight_layout()
    fig.savefig(f"{MEAS}/response-time-comparison.png", dpi=150)

    fig, ax = plt.subplots(figsize=(7, 4))
    for c in codes:
        h = history(summary[c][0].replace("_stats.csv", "_stats_history.csv"))
        ax.plot([p[0] for p in h], [p[1] for p in h], label=names[c])
    ax.set_xlabel("Seconds since test start")
    ax.set_ylabel("Average response time so far (ms)")
    ax.set_title("Average response time during the test")
    ax.legend()
    fig.tight_layout()
    fig.savefig(f"{MEAS}/response-time-over-time.png", dpi=150)
    print("Saved graphs in", MEAS)


if __name__ == "__main__":
    main()
