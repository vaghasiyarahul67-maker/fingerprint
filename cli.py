#!/usr/bin/env python3
"""
CLI Tool: Phone Fingerprint Engine
Commands:
  python3 cli.py random              -> Generate a random high-entropy crore-level phone fingerprint
  python3 cli.py generate --id 50    -> Generate deterministically from the 10,000 phone models
  python3 cli.py js --id 1           -> Output client-side JavaScript injection code
  python3 cli.py batch -n 1000 -o f.json -> Batch generate 1,000 unique fingerprints
  python3 cli.py benchmark           -> Test engine generation throughput
"""

import sys
import os
import argparse
import json
import time

# Ensure current dir is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engine import (
    TOTAL_PHONE_PRESETS,
    get_phone_profile,
    generate_crore_fingerprint,
    build_fingerprint_injection_script
)


def print_banner():
    print("""
\033[1;36m======================================================================\033[0m
\033[1;32m  📱 MOBILE PHONE FINGERPRINT ENGINE (10,000 PHONES + CRORES ENTROPY)\033[0m
\033[1;34m  Battery API • TCP/MTU Stack • Clock Drift • WebGL • Canvas • Audio\033[0m
\033[1;36m======================================================================\033[0m
""")


def format_profile(p: dict) -> str:
    lines = [
        f"\033[1;33m[DEVICE HARDWARE & IDENTITY]\033[0m",
        f"  Model Name       : \033[1;37m{p.get('name')}\033[0m",
        f"  Brand / Model    : {p.get('brand')} | {p.get('model')}",
        f"  OS & Platform    : {p.get('os')} {p.get('os_version')} ({p.get('platform')})",
        f"  Hardware UUID    : \033[1;35m{p.get('hardware_uuid', 'N/A')}\033[0m",
        f"  OS Build ID      : {p.get('build_id', 'N/A')}",
        f"  User-Agent       : \033[0;36m{p.get('user_agent')}\033[0m",
        f"  Screen Viewport  : {p.get('screen_width')}x{p.get('screen_height')} @ DPR {p.get('device_pixel_ratio')}",
        f"  CPU Cores / RAM  : {p.get('hardware_concurrency')} Cores | {p.get('device_memory')} GB RAM",
        f"  Touch Points     : {p.get('max_touch_points')}",
        "",
        f"\033[1;32m[BATTERY API (navigator.getBattery)]\033[0m",
        f"  Battery Level    : \033[1;32m{int(p.get('battery_level', 0) * 100)}%\033[0m",
        f"  Charging State   : {'⚡ Charging' if p.get('battery_charging') else '🔋 Discharging'}",
        f"  Charging Time    : {p.get('charging_time')}s",
        f"  Discharging Time : {p.get('discharging_time')}s",
        f"  Battery Temp     : {p.get('battery_temperature_c', 30.0)}°C ({p.get('battery_health', 'Good')})",
        "",
        f"\033[1;34m[TCP & NETWORK STACK MODELING]\033[0m",
        f"  TCP MTU          : \033[1;34m{p.get('tcp_mtu')} bytes\033[0m",
        f"  TCP MSS          : {p.get('tcp_mss')} bytes (MTU - 40)",
        f"  TCP TTL          : {p.get('tcp_ttl')} (Standard {p.get('os')})",
        f"  TCP Window Size  : {p.get('tcp_window_size')} (Scaling: {p.get('tcp_window_scaling')})",
        f"  TCP SYN Packet   : {p.get('tcp_syn_packet_hex')}",
        f"  Connection Type  : {p.get('connection_type')} ({p.get('effective_type')})",
        f"  Downlink / RTT   : {p.get('downlink')} Mbps | {p.get('rtt')} ms",
        "",
        f"\033[1;31m[HIGH-PRECISION TIMER & CLOCK DRIFT]\033[0m",
        f"  Clock Drift PPM  : \033[1;31m{p.get('clock_drift_ppm')} ppm\033[0m",
        f"  Timer Jitter     : {p.get('timer_jitter_microsec')} µs (Spectre Shield)",
        f"  TSC Frequency    : {p.get('tsc_frequency_ghz', 2.8)} GHz",
        "",
        f"\033[1;35m[WEBGL, CANVAS & AUDIO NOISE]\033[0m",
        f"  GL Vendor        : {p.get('gl_vendor')}",
        f"  GL Renderer      : \033[1;37m{p.get('gl_renderer')}\033[0m",
        f"  Canvas Noise Seed: {p.get('canvas_noise_seed')}",
        f"  Audio Noise Seed : {p.get('audio_noise_seed')}",
        f"  Sensor Noise Seed: {p.get('sensor_noise_seed')}",
        f"  GPS Micro-Drift  : Lat {p.get('gps_lat_offset', 0.0):+.6f}, Lng {p.get('gps_lng_offset', 0.0):+.6f}",
        f"\033[1;36m======================================================================\033[0m"
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Phone Fingerprint Engine CLI")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Command: random (Crore unique)
    p_rand = subparsers.add_parser("random", help="Generate a random unique crore-level phone fingerprint")
    p_rand.add_argument("--json", action="store_true", help="Output raw JSON")

    # Command: generate (from 10,000 presets)
    p_gen = subparsers.add_parser("generate", help="Generate a phone profile by index (1 to 10,000)")
    p_gen.add_argument("--id", type=int, default=1, help="Phone index (1 - 10000)")
    p_gen.add_argument("--entropy", action="store_true", help="Apply dynamic crore-level entropy")
    p_gen.add_argument("--json", action="store_true", help="Output raw JSON")

    # Command: js
    p_js = subparsers.add_parser("js", help="Generate client-side JavaScript injection snippet")
    p_js.add_argument("--id", type=int, default=1, help="Phone index (1 - 10000)")
    p_js.add_argument("--out", type=str, help="Save to .js file path")

    # Command: batch
    p_batch = subparsers.add_parser("batch", help="Batch generate multiple unique fingerprints")
    p_batch.add_argument("-n", "--count", type=int, default=100, help="Number of fingerprints to generate")
    p_batch.add_argument("-o", "--out", type=str, required=True, help="Output JSON file path")

    # Command: benchmark
    p_bench = subparsers.add_parser("benchmark", help="Benchmark generation speed")
    p_bench.add_argument("-n", "--count", type=int, default=50000, help="Number of iterations")

    args = parser.parse_args()

    if not args.command:
        print_banner()
        print("Generating a fresh, authentic crore-level phone fingerprint:\n")
        prof = generate_crore_fingerprint()
        print(format_profile(prof))
        print("\nTip: Run with --help to see all available CLI options.")
        return

    if args.command == "random":
        prof = generate_crore_fingerprint()
        if args.json:
            print(json.dumps(prof, indent=2))
        else:
            print_banner()
            print(format_profile(prof))

    elif args.command == "generate":
        if args.entropy:
            prof = generate_crore_fingerprint(base_seed=args.id)
        else:
            prof = get_phone_profile(args.id)

        if args.json:
            print(json.dumps(prof, indent=2))
        else:
            print_banner()
            print(format_profile(prof))

    elif args.command == "js":
        prof = generate_crore_fingerprint(base_seed=args.id)
        js = build_fingerprint_injection_script(prof)
        if args.out:
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(js)
            print(f"✅ JavaScript injection snippet saved to {args.out} ({len(js)} bytes)")
        else:
            print(js)

    elif args.command == "batch":
        print(f"Generating {args.count} unique phone fingerprints...")
        t0 = time.time()
        results = [generate_crore_fingerprint() for _ in range(args.count)]
        t1 = time.time()
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
        print(f"✅ Generated and saved {args.count} profiles to {args.out} in {t1 - t0:.2f}s ({args.count / (t1 - t0):.1f} profiles/sec)")

    elif args.command == "benchmark":
        print(f"Benchmarking generation of {args.count:,} crore-level phone fingerprints...")
        t0 = time.time()
        for _ in range(args.count):
            _ = generate_crore_fingerprint()
        t1 = time.time()
        duration = t1 - t0
        speed = args.count / duration
        print(f"✅ Completed {args.count:,} profiles in {duration:.3f} seconds.")
        print(f"🚀 Throughput: \033[1;32m{speed:,.1f} fingerprints / second\033[0m")


if __name__ == "__main__":
    main()
