import os
import time
import hashlib
import json
from datetime import datetime

HISTORY_FILE = os.path.expanduser("~/.cyber_signal_history.json")

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return {}
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def hash_file(path):
    try:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                h.update(chunk)
        return h.hexdigest()
    except:
        return None

def human_signal_analysis():
    history = load_history()
    now = time.time()

    signals = {
        "scan_frequency": 0,
        "night_activity": 0,
        "irregular_intervals": 0
    }

    if "scans" not in history:
        history["scans"] = []

    history["scans"].append(now)
    scans = history["scans"][-5:]
    save_history(history)

    if len(scans) >= 2:
        diff = scans[-1] - scans[-2]
        if diff < 10:
            signals["scan_frequency"] = 1
        if diff > 10000:
            signals["irregular_intervals"] = 1

    hour = datetime.now().hour
    if hour < 6 or hour > 23:
        signals["night_activity"] = 1

    return signals

def process_drift_analysis(path):
    history = load_history()
    drift = {
        "new_large_files": 0,
        "missing_key_files": 0,
        "structure_changes": 0
    }

    current_files = {}
    for root, _, files in os.walk(path):
        for f in files:
            full = os.path.join(root, f)
            current_files[full] = hash_file(full)

    if "file_state" not in history:
        history["file_state"] = current_files
        save_history(history)
        return drift

    prev_files = history["file_state"]

    for f in current_files:
        if f not in prev_files:
            if os.path.getsize(f) > 5_000_000:
                drift["new_large_files"] = 1

    for f in prev_files:
        if f not in current_files:
            drift["missing_key_files"] = 1

    if len(current_files) != len(prev_files):
        drift["structure_changes"] = 1

    history["file_state"] = current_files
    save_history(history)

    return drift

def shadow_it_scan(path):
    suspicious = [".exe", ".sh", ".bat", ".ps1", ".apk"]
    signals = {"unknown_executables": 0}

    for root, _, files in os.walk(path):
        for f in files:
            if any(f.endswith(ext) for ext in suspicious):
                signals["unknown_executables"] = 1
                return signals
    return signals

def compute_risk_score(human, drift, shadow):
    score = (
        human["scan_frequency"] * 15 +
        human["night_activity"] * 10 +
        drift["new_large_files"] * 30 +
        drift["missing_key_files"] * 30 +
        drift["structure_changes"] * 20 +
        shadow["unknown_executables"] * 40
    )
    return min(score, 100)
