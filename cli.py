import argparse
from cybersignal.core import (
    human_signal_analysis,
    process_drift_analysis,
    shadow_it_scan,
    compute_risk_score
)

def main():
    parser = argparse.ArgumentParser(
        description="CyberSignal — Human + Technical Early Risk Detector"
    )
    parser.add_argument("scan", help="scan a directory", nargs="?")
    parser.add_argument("path", help="path to scan", nargs="?")
    args = parser.parse_args()

    if not args.path:
        print("Usage: cybersignal scan <path>")
        return

    print("\n🔍 Running CyberSignal scan...\n")

    human = human_signal_analysis()
    drift = process_drift_analysis(args.path)
    shadow = shadow_it_scan(args.path)

    score = compute_risk_score(human, drift, shadow)

    print("=== HUMAN SIGNALS ===")
    print(human)
    print("\n=== PROCESS DRIFT ===")
    print(drift)
    print("\n=== SHADOW IT ===")
    print(shadow)

    print("\n🔥 FINAL RISK SCORE:", score, "/ 100\n")

    if score < 30:
        print("🟢 Low Risk — System stable.")
    elif score < 70:
        print("🟡 Medium Risk — Concerning patterns.")
    else:
        print("🔴 HIGH RISK — Attention required!")

if __name__ == "__main__":
    main()
