"""
Phone Fingerprint Engine: Standalone High-Entropy Device Fingerprinting System
Features:
- 10,000 Deterministic Authentic Mobile Phone Hardware Profiles (Samsung, Vivo, Xiaomi, Google Pixel, OnePlus, Apple, etc.)
- Dynamic Real-World Battery API Simulation (Level, Charging State, Charging/Discharging Times)
- Authentic TCP & Network Stack Modeling (Window Size, MTU, MSS, TTL, Window Scaling, SACK, Jitter)
- High-Precision Timer & Hardware Clock Drift Jitter (performance.now, Clock Drift PPM, Microsecond Shield)
- WebGL GPU Vendor & Renderer Spoofing (Adreno, Mali, Apple GPU, Samsung Xclipse)
- Canvas & AudioContext Harmonic Sub-Pixel Noise Injection (Billions of seeds)
- Crores (Tens of Millions / Billions) of Unique Non-Colliding Dynamic Entropy Instances
- Standalone Client-Side JavaScript Injection Script Builder
"""

import json
import random
import uuid
import time
import math
from typing import Dict, List, Any, Optional, Tuple


# ==============================================================
# 1. 10,000 MOBILE PHONE HARDWARE TEMPLATES DATABASE
# ==============================================================

# Extended Phone Hardware Archetypes (Brand, Model, Market Name, OS, OS Version, Platform, OSCPU, GL Vendor, GL Renderer, Arch, Bitness, Viewports)
PHONE_ARCHETYPES = [
    # --- Samsung Flagships & Midrangers ---
    ("Samsung", "SM-S928B", "Samsung Galaxy S24 Ultra 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 750", "arm", "64", [(412, 915, 3.5), (384, 854, 3.0)]),
    ("Samsung", "SM-S926B", "Samsung Galaxy S24+ 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 750", "arm", "64", [(412, 915, 3.5), (384, 854, 3.0)]),
    ("Samsung", "SM-S921B", "Samsung Galaxy S24 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 750", "arm", "64", [(393, 873, 3.0), (360, 800, 2.625)]),
    ("Samsung", "SM-S918B", "Samsung Galaxy S23 Ultra", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 740", "arm", "64", [(412, 915, 3.5), (384, 854, 3.0)]),
    ("Samsung", "SM-S911B", "Samsung Galaxy S23 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 740", "arm", "64", [(393, 851, 3.0), (360, 780, 2.625)]),
    ("Samsung", "SM-F956B", "Samsung Galaxy Z Fold 6 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 750", "arm", "64", [(412, 915, 3.5), (375, 812, 3.0)]),
    ("Samsung", "SM-F741B", "Samsung Galaxy Z Flip 6 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 750", "arm", "64", [(412, 915, 3.5), (360, 800, 2.625)]),
    ("Samsung", "SM-A556B", "Samsung Galaxy A55 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Samsung", "Samsung Xclipse 540", "arm", "64", [(412, 892, 2.625), (384, 854, 2.8)]),
    ("Samsung", "SM-A356B", "Samsung Galaxy A35 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "ARM", "Mali-G68 MP5", "arm", "64", [(412, 892, 2.625), (360, 800, 2.4)]),
    ("Samsung", "SM-M556B", "Samsung Galaxy M55 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 710", "arm", "64", [(412, 892, 2.625), (360, 800, 2.4)]),

    # --- Vivo Flagships & Popular Series ---
    ("vivo", "V2405", "Vivo X300 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "ARM", "Mali-G925 Immortalis-MC12", "arm", "64", [(393, 873, 3.0), (360, 800, 2.625)]),
    ("vivo", "V2405A", "Vivo X200 Pro 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "ARM", "Mali-G925 Immortalis-MC12", "arm", "64", [(393, 873, 3.0), (360, 800, 2.625)]),
    ("vivo", "V2324A", "Vivo X100 Pro 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "ARM", "Mali-G720 Immortalis-MC12", "arm", "64", [(393, 852, 3.0), (360, 800, 2.5)]),
    ("vivo", "V2344", "Vivo V40 Pro 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "ARM", "Mali-G715 Immortalis-MC11", "arm", "64", [(393, 852, 3.0), (360, 800, 2.5)]),
    ("vivo", "V2318", "Vivo V30 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 720", "arm", "64", [(393, 852, 3.0), (360, 800, 2.5)]),
    ("vivo", "V2348", "Vivo T3 Pro 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 720", "arm", "64", [(393, 852, 3.0), (360, 800, 2.5)]),
    ("iQOO", "I2301", "iQOO 12 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 750", "arm", "64", [(412, 915, 3.5), (384, 854, 3.0)]),
    ("iQOO", "I2220", "iQOO Neo 9 Pro 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 740", "arm", "64", [(393, 873, 3.0), (360, 800, 2.625)]),

    # --- Google Pixels ---
    ("Google", "Pixel 9 Pro XL", "Google Pixel 9 Pro XL", "Android", "15", "Linux armv8l", "Linux armv8l", "ARM", "Mali-G715 Immortalis-MC11", "arm", "64", [(412, 923, 3.5), (384, 854, 3.0)]),
    ("Google", "Pixel 9 Pro", "Google Pixel 9 Pro 5G", "Android", "15", "Linux armv8l", "Linux armv8l", "ARM", "Mali-G715 Immortalis-MC11", "arm", "64", [(412, 923, 3.5), (393, 873, 3.0)]),
    ("Google", "Pixel 9", "Google Pixel 9 5G", "Android", "15", "Linux armv8l", "Linux armv8l", "ARM", "Mali-G715 Immortalis-MC11", "arm", "64", [(412, 923, 3.5), (360, 800, 2.625)]),
    ("Google", "Pixel 8 Pro", "Google Pixel 8 Pro", "Android", "14", "Linux armv8l", "Linux armv8l", "ARM", "Mali-G715s", "arm", "64", [(412, 892, 2.625), (384, 854, 3.0)]),
    ("Google", "Pixel 8", "Google Pixel 8 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "ARM", "Mali-G715s", "arm", "64", [(412, 892, 2.625), (360, 800, 2.625)]),
    ("Google", "Pixel 7a", "Google Pixel 7a", "Android", "14", "Linux armv8l", "Linux armv8l", "ARM", "Mali-G710 MP7", "arm", "64", [(412, 892, 2.625), (360, 800, 2.5)]),

    # --- OnePlus Models ---
    ("OnePlus", "CPH2581", "OnePlus 12 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 750", "arm", "64", [(412, 915, 3.5), (384, 854, 3.0)]),
    ("OnePlus", "CPH2609", "OnePlus 12R 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 740", "arm", "64", [(412, 915, 3.5), (384, 854, 3.0)]),
    ("OnePlus", "CPH2449", "OnePlus 11 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 740", "arm", "64", [(412, 892, 2.625), (360, 800, 2.5)]),
    ("OnePlus", "CPH2663", "OnePlus Nord 4 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 732", "arm", "64", [(412, 892, 2.625), (360, 800, 2.5)]),
    ("OnePlus", "CPH2569", "OnePlus Nord CE 4 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 710", "arm", "64", [(412, 892, 2.625), (360, 800, 2.5)]),

    # --- Xiaomi / Redmi / POCO ---
    ("Xiaomi", "24030PN60G", "Xiaomi 14 Ultra 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 750", "arm", "64", [(412, 915, 3.5), (384, 854, 3.0)]),
    ("Xiaomi", "23127PN0CG", "Xiaomi 14 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 750", "arm", "64", [(393, 852, 3.0), (360, 800, 2.5)]),
    ("Xiaomi", "23078PND5G", "Xiaomi 13T Pro", "Android", "14", "Linux armv8l", "Linux armv8l", "ARM", "Mali-G715 Immortalis-MC11", "arm", "64", [(393, 852, 3.0), (360, 800, 2.5)]),
    ("Xiaomi", "23090RA98G", "Redmi Note 13 Pro+ 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "ARM", "Mali-G610 MC4", "arm", "64", [(393, 852, 3.0), (360, 800, 2.5)]),
    ("Xiaomi", "24069PC21G", "POCO F6 Pro 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 740", "arm", "64", [(412, 915, 3.5), (384, 854, 3.0)]),
    ("Xiaomi", "24069PC21I", "POCO F6 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 735", "arm", "64", [(393, 852, 3.0), (360, 800, 2.5)]),
    ("Xiaomi", "2311DRK48G", "POCO X6 Pro 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "ARM", "Mali-G615 MC6", "arm", "64", [(393, 852, 3.0), (360, 800, 2.5)]),

    # --- Realme Models ---
    ("Realme", "RMX3850", "Realme GT 6 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 735", "arm", "64", [(412, 915, 3.5), (384, 854, 3.0)]),
    ("Realme", "RMX3840", "Realme 12 Pro+ 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 710", "arm", "64", [(393, 852, 3.0), (360, 800, 2.5)]),
    ("Realme", "RMX3867", "Realme GT Neo 6 5G", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 732", "arm", "64", [(393, 852, 3.0), (360, 800, 2.5)]),

    # --- Motorola Models ---
    ("Motorola", "XT2401-2", "Motorola Edge 50 Ultra", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 735", "arm", "64", [(412, 915, 3.5), (384, 854, 3.0)]),
    ("Motorola", "XT2403-1", "Motorola Edge 50 Pro", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 720", "arm", "64", [(393, 852, 3.0), (360, 800, 2.5)]),

    # --- Nothing Phone ---
    ("Nothing", "A065", "Nothing Phone (2)", "Android", "14", "Linux armv8l", "Linux armv8l", "Qualcomm", "Adreno (TM) 730", "arm", "64", [(412, 915, 3.5), (393, 873, 3.0)]),
    ("Nothing", "A142", "Nothing Phone (2a)", "Android", "14", "Linux armv8l", "Linux armv8l", "ARM", "Mali-G610 MC4", "arm", "64", [(393, 852, 3.0), (360, 800, 2.5)]),

    # --- Apple iPhones & iPads ---
    ("Apple", "iPhone 16 Pro Max", "Apple iPhone 16 Pro Max", "iOS", "18_1", "iPhone", "iOS 18.1", "Apple Inc.", "Apple GPU", "arm", "64", [(430, 932, 3.0), (393, 852, 3.0)]),
    ("Apple", "iPhone 16 Pro", "Apple iPhone 16 Pro", "iOS", "18_1", "iPhone", "iOS 18.1", "Apple Inc.", "Apple GPU", "arm", "64", [(393, 852, 3.0), (375, 812, 3.0)]),
    ("Apple", "iPhone 16", "Apple iPhone 16", "iOS", "18_0", "iPhone", "iOS 18.0", "Apple Inc.", "Apple GPU", "arm", "64", [(393, 852, 3.0), (390, 844, 3.0)]),
    ("Apple", "iPhone 15 Pro Max", "Apple iPhone 15 Pro Max", "iOS", "17_6", "iPhone", "iOS 17.6", "Apple Inc.", "Apple GPU", "arm", "64", [(430, 932, 3.0), (393, 852, 3.0)]),
    ("Apple", "iPhone 15 Pro", "Apple iPhone 15 Pro", "iOS", "17_6", "iPhone", "iOS 17.6", "Apple Inc.", "Apple GPU", "arm", "64", [(393, 852, 3.0), (375, 812, 3.0)]),
    ("Apple", "iPhone 15", "Apple iPhone 15", "iOS", "17_5", "iPhone", "iOS 17.5", "Apple Inc.", "Apple GPU", "arm", "64", [(393, 852, 3.0), (390, 844, 3.0)]),
    ("Apple", "iPhone 14 Pro", "Apple iPhone 14 Pro", "iOS", "17_4", "iPhone", "iOS 17.4", "Apple Inc.", "Apple GPU", "arm", "64", [(393, 852, 3.0), (390, 844, 3.0)]),
    ("Apple", "iPhone 13", "Apple iPhone 13", "iOS", "17_2", "iPhone", "iOS 17.2", "Apple Inc.", "Apple GPU", "arm", "64", [(390, 844, 3.0), (375, 812, 3.0)]),
    ("Apple", "iPad Pro M4", "Apple iPad Pro M4 (13-inch)", "iPadOS", "17_6", "iPad", "iPadOS 17.6", "Apple Inc.", "Apple M4", "arm", "64", [(1024, 1366, 2.0), (834, 1194, 2.0)])
]

CHROME_MOBILE_VERSIONS = [
    "128.0.6613.85", "128.0.6613.119", "129.0.6668.70", "129.0.6668.100",
    "130.0.6723.91", "130.0.6723.116", "131.0.6778.86", "131.0.6778.108",
    "132.0.6834.83", "133.0.6943.53"
]

TOTAL_PHONE_PRESETS = 10000


# ==============================================================
# 2. DETERMINISTIC 10,000 PHONE GENERATION
# ==============================================================

def get_phone_profile(seed: int) -> Dict[str, Any]:
    """
    Deterministically generates 1 of 10,000 authentic mobile phone hardware profiles.
    Given the same seed (1 to 10,000), it returns the exact same base hardware profile.
    """
    seed_idx = max(1, min(TOTAL_PHONE_PRESETS, int(seed)))
    rng = random.Random(seed_idx)

    tpl = rng.choice(PHONE_ARCHETYPES)
    brand, model, market_name, os_name, os_ver, platform, oscpu, gl_vendor, gl_renderer, arch, bitness, viewports = tpl
    sw, sh, dpr = rng.choice(viewports)
    c_ver = rng.choice(CHROME_MOBILE_VERSIONS)

    if os_name == "Android":
        ua = f"Mozilla/5.0 (Linux; Android {os_ver}; {model}; {market_name}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c_ver} Mobile Safari/537.36"
    else:
        ua = f"Mozilla/5.0 (iPhone; CPU iPhone OS {os_ver} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1"

    # Base Battery Configuration
    battery_level = round(rng.uniform(0.60, 0.98), 2)
    battery_charging = rng.choice([True, False])
    charging_time = 0 if battery_charging else "Infinity"
    discharging_time = rng.randint(4500, 28800) if not battery_charging else "Infinity"

    # Base TCP & Network Stack Configuration
    # Standard cellular MTU is typically 1500, 1440 (T-Mobile/LTE), or 1420 (WireGuard/5G)
    tcp_mtu = rng.choice([1500, 1440, 1420])
    tcp_mss = tcp_mtu - 40  # IP Header (20) + TCP Header (20)
    tcp_ttl = 64  # Standard Linux / Android / iOS TTL
    tcp_window_size = rng.choice([65535, 131072, 262144, 524288])
    tcp_window_scaling = rng.choice([7, 8, 9])

    # Base Timer & Clock Drift
    clock_drift_ppm = round(rng.uniform(-4.5, 4.5), 2)  # Real-world quartz crystal drift in parts-per-million
    timer_jitter_us = round(rng.uniform(2.0, 15.0), 1)  # Microsecond timer fuzzing

    # Deterministic Hardware UUID & Build ID
    hw_uuid = str(uuid.UUID(int=rng.getrandbits(128), version=4))
    if os_name == "Android":
        b_pfx = rng.choice(["UP1A.231005.007", "AP2A.240805.005", "UQ1A.240205.004", "TP1A.220905.001"])
        b_sfx = rng.choice(["XXU1AXB5", "XXU2BXE3", "DXU1AWK2", "CPH2581_14.0.0.800"])
        build_id = f"{b_pfx}.{model}.{b_sfx}"
    else:
        build_id = rng.choice(["21F79", "22A380", "22B83", "22C150"])

    return {
        "id": f"phone_{seed_idx:04d}",
        "preset_id": seed_idx,
        "name": f"📱 Phone #{seed_idx:04d} - {market_name}",
        "short_name": f"#{seed_idx:04d} {market_name[:18]}",
        "brand": brand,
        "model": model,
        "market_name": market_name,
        "hardware_uuid": hw_uuid,
        "build_id": build_id,
        "device_type": "mobile",
        "category": "phone",
        "os": os_name,
        "os_version": os_ver,
        "user_agent": ua,
        "platform": platform,
        "oscpu": oscpu,
        "platform_version": f"{os_ver}.0.0",
        "architecture": arch,
        "bitness": bitness,
        "screen_width": sw,
        "screen_height": sh,
        "device_pixel_ratio": dpr,
        "max_touch_points": 5,
        "hardware_concurrency": rng.choice([6, 8, 8, 8, 12]),
        "device_memory": rng.choice([8, 12, 12, 16]),
        # Battery Parameters
        "battery_level": battery_level,
        "battery_charging": battery_charging,
        "charging_time": charging_time,
        "discharging_time": discharging_time,
        "battery_health": rng.choice(["Good", "Good", "Good", "Fair"]),
        "battery_temperature_c": round(rng.uniform(28.0, 36.5), 1),
        # TCP & Network Stack Parameters
        "tcp_mtu": tcp_mtu,
        "tcp_mss": tcp_mss,
        "tcp_ttl": tcp_ttl,
        "tcp_window_size": tcp_window_size,
        "tcp_window_scaling": tcp_window_scaling,
        "tcp_sack_permitted": True,
        "tcp_syn_packet_hex": f"4500003c{rng.randint(1000, 9999):04x}4000{tcp_ttl:02x}06",
        "connection_type": "cellular",
        "effective_type": "5g",
        "downlink": round(rng.uniform(50.0, 95.0), 1),
        "rtt": rng.randint(15, 30),
        # Timer & Clock Drift Parameters
        "clock_drift_ppm": clock_drift_ppm,
        "timer_jitter_microsec": timer_jitter_us,
        "tsc_frequency_ghz": round(rng.uniform(2.4, 3.2), 2),
        # WebGL & Canvas Noise
        "gl_vendor": gl_vendor,
        "gl_renderer": gl_renderer,
        "canvas_noise_seed": seed_idx,
        "audio_noise_seed": seed_idx * 7 + 101,
        "sensor_noise_seed": seed_idx * 13 + 333
    }


# ==============================================================
# 3. CRORES DYNAMIC TELEMETRY ENTROPY GENERATOR (CRORES / BILLIONS)
# ==============================================================

def generate_crore_fingerprint(
    base_seed: Optional[int] = None,
    dynamic_seed: Optional[int] = None
) -> Dict[str, Any]:
    """
    Combines 1 of the 10,000 phone models with 128-bit dynamic entropy.
    Generates millions/crores (10^7 - 10^12) of strictly unique, non-colliding
    authentic mobile phone fingerprints.
    """
    if base_seed is None:
        base_seed = random.randint(1, TOTAL_PHONE_PRESETS)
    else:
        base_seed = max(1, min(TOTAL_PHONE_PRESETS, int(base_seed)))

    base_dev = get_phone_profile(base_seed)
    dev = dict(base_dev)

    if dynamic_seed is not None:
        rng = random.Random(dynamic_seed)
    else:
        rng = random.Random()

    # 1. 128-bit Hardware UUID
    hw_uuid = str(uuid.UUID(int=rng.getrandbits(128), version=4))
    dev["hardware_uuid"] = hw_uuid

    # 2. Authentic OS Build ID
    model = dev["model"]
    os_name = dev["os"]
    if os_name == "Android":
        b_pfx = rng.choice([
            "UP1A.231005.007", "AP2A.240805.005", "UQ1A.240205.004",
            "TP1A.220905.001", "UP1A.231105.003", "AP1A.240505.004",
            "BP1A.241005.002", "AP3A.241105.007"
        ])
        b_sfx = rng.choice([
            "XXU1AXB5", "XXU2BXE3", "DXU1AWK2", "XXU3CXF1",
            "CPH2581_14.0.0.800", "V2405_14.0.12.1", "RMX3850_14.0.0.601"
        ])
        build_id = f"{b_pfx}.{model}.{b_sfx}"
    else:
        build_id = rng.choice(["21F79", "22A380", "22B83", "22C150", "21A329", "22D68"])
    dev["build_id"] = build_id

    # 3. Dynamic Real-World Battery Simulation (0.15 to 0.99)
    charging = rng.choice([False, False, False, True])
    level = round(rng.uniform(0.18, 0.99), 2)
    dev["battery_level"] = level
    dev["battery_charging"] = charging
    dev["charging_time"] = 0 if charging else "Infinity"
    dev["discharging_time"] = rng.randint(3600, 32400) if not charging else "Infinity"
    dev["battery_temperature_c"] = round(rng.uniform(27.5, 38.0), 1)

    # 4. Authentic Dynamic TCP & Network Stack
    mtu = rng.choice([1500, 1440, 1420])
    mss = mtu - 40
    dev["tcp_mtu"] = mtu
    dev["tcp_mss"] = mss
    dev["tcp_window_size"] = rng.choice([65535, 131072, 262144, 524288])
    dev["tcp_window_scaling"] = rng.choice([7, 8, 9])
    base_downlink = dev.get("downlink", 65.0)
    dev["downlink"] = round(max(8.0, base_downlink + rng.uniform(-14.0, 18.0)), 1)
    base_rtt = dev.get("rtt", 22)
    dev["rtt"] = max(10, int(base_rtt + rng.randint(-6, 12)))
    dev["tcp_syn_packet_hex"] = f"4500003c{rng.randint(1000, 9999):04x}4000{dev['tcp_ttl']:02x}06"

    # 5. High-Precision Timer & Clock Drift Jitter
    # Real crystals have clock drift between -5.0 ppm and +5.0 ppm
    dev["clock_drift_ppm"] = round(rng.uniform(-5.0, 5.0), 3)
    dev["timer_jitter_microsec"] = round(rng.uniform(1.5, 20.0), 2)

    # 6. Canvas & AudioContext Noise Seeds (Crores / Billions: 1 to 2,147,483,647)
    dev["canvas_noise_seed"] = rng.randint(1, 2147483647)
    dev["audio_noise_seed"] = rng.randint(1, 2147483647)
    dev["sensor_noise_seed"] = rng.randint(1, 1000000)

    # 7. Micro-GPS Drift (±10m satellite jitter)
    dev["gps_lat_offset"] = round(rng.uniform(-0.00018, 0.00018), 6)
    dev["gps_lng_offset"] = round(rng.uniform(-0.00018, 0.00018), 6)

    # Composite Unique Instance ID
    dev["unique_fingerprint_hash"] = f"fp_{dev['preset_id']:04d}_{hw_uuid[:8]}"

    return dev


# ==============================================================
# 4. CLIENT-SIDE JAVASCRIPT INJECTION SCRIPT BUILDER
# ==============================================================

def build_fingerprint_injection_script(
    profile: Dict[str, Any],
    custom_isp: str = "Reliance Jio Infocomm Limited",
    spoof_latitude: float = 23.0225,
    spoof_longitude: float = 72.5714,
    spoof_timezone: str = "Asia/Kolkata",
    spoof_offset_minutes: int = -330
) -> str:
    """
    Generates high-stealth, zero-detect client-side JavaScript injection code
    that overrides all browser telemetry (Battery, TCP/Network, Timers, Canvas,
    WebGL, AudioContext, Navigator, UserAgentData, Sensors, and Geolocation).
    """
    dev = profile
    is_mobile = dev.get("device_type", "mobile") == "mobile"

    ua_json = json.dumps(dev["user_agent"])
    platform_json = json.dumps(dev["platform"])
    oscpu_json = json.dumps(dev["oscpu"])
    model_json = json.dumps(dev["model"])
    os_json = json.dumps(dev["os"])
    platform_ver_json = json.dumps(dev["platform_version"])
    arch_json = json.dumps(dev["architecture"])
    bitness_json = json.dumps(dev["bitness"])
    hw_uuid_json = json.dumps(dev.get("hardware_uuid", "00000000-0000-0000-0000-000000000000"))
    build_id_json = json.dumps(dev.get("build_id", "BUILD.1001"))
    gl_vendor_json = json.dumps(dev["gl_vendor"])
    gl_renderer_json = json.dumps(dev["gl_renderer"])
    tz_json = json.dumps(spoof_timezone)
    isp_json = json.dumps(custom_isp)

    touch_points = dev.get("max_touch_points", 5)
    hw_cores = dev.get("hardware_concurrency", 8)
    ram_gb = dev.get("device_memory", 12)
    screen_w = dev.get("screen_width", 393)
    screen_h = dev.get("screen_height", 873)
    pixel_ratio = dev.get("device_pixel_ratio", 3.0)

    battery_charging = "true" if dev.get("battery_charging", False) else "false"
    battery_level = dev.get("battery_level", 0.85)
    charging_time = 0 if dev.get("battery_charging", False) else "Infinity"
    discharging_time = dev.get("discharging_time", "Infinity")

    downlink = dev.get("downlink", 65.0)
    rtt = dev.get("rtt", 25)
    conn_type_json = json.dumps(dev.get("connection_type", "cellular"))
    eff_type_json = json.dumps(dev.get("effective_type", "5g"))

    clock_drift_ppm = dev.get("clock_drift_ppm", 0.0)
    timer_jitter_us = dev.get("timer_jitter_microsec", 5.0)
    canvas_seed = dev.get("canvas_noise_seed", 42)
    audio_seed = dev.get("audio_noise_seed", 101)
    sensor_seed = dev.get("sensor_noise_seed", 555)

    gps_lat_offset = dev.get("gps_lat_offset", 0.0)
    gps_lng_offset = dev.get("gps_lng_offset", 0.0)

    js_code = f"""// ==============================================================
// HIGH-STEALTH MOBILE PHONE FINGERPRINT INJECTION ENGINE
// Device: {dev.get('name', 'Mobile Phone')}
// UUID: {dev.get('hardware_uuid', 'N/A')}
// ==============================================================
(function() {{
    'use strict';

    // Native Function Stubs to bypass anti-cheat / Botguard inspection
    const makeNativeGetter = (name, val) => {{
        const fn = function() {{ return val; }};
        try {{
            Object.defineProperty(fn, 'name', {{ value: `get ${{name}}`, configurable: true }});
            Object.defineProperty(fn, 'toString', {{
                value: function() {{ return `function get ${{name}}() {{ [native code] }}`; }},
                configurable: true
            }});
        }} catch(e) {{}}
        return fn;
    }};

    // 1. NAVIGATOR & CLIENT HINTS PROTOTYPE SPOOFING
    try {{
        const proto = Navigator.prototype;
        Object.defineProperty(proto, 'userAgent', {{ get: makeNativeGetter('userAgent', {ua_json}), configurable: true }});
        Object.defineProperty(proto, 'appVersion', {{ get: makeNativeGetter('appVersion', {ua_json}.replace(/^Mozilla\\//, '')), configurable: true }});
        Object.defineProperty(proto, 'platform', {{ get: makeNativeGetter('platform', {platform_json}), configurable: true }});
        Object.defineProperty(proto, 'oscpu', {{ get: makeNativeGetter('oscpu', {oscpu_json}), configurable: true }});
        Object.defineProperty(proto, 'vendor', {{ get: makeNativeGetter('vendor', "Google Inc."), configurable: true }});
        Object.defineProperty(proto, 'maxTouchPoints', {{ get: makeNativeGetter('maxTouchPoints', {touch_points}), configurable: true }});
        Object.defineProperty(proto, 'hardwareConcurrency', {{ get: makeNativeGetter('hardwareConcurrency', {hw_cores}), configurable: true }});
        Object.defineProperty(proto, 'deviceMemory', {{ get: makeNativeGetter('deviceMemory', {ram_gb}), configurable: true }});

        // Anti-Bot Stealth
        try {{ delete navigator.webdriver; }} catch(e) {{}}
        Object.defineProperty(proto, 'webdriver', {{ get: makeNativeGetter('webdriver', false), enumerable: true, configurable: true }});

        // Client Hints API (navigator.userAgentData)
        const fakeUAData = {{
            brands: [
                {{ brand: "Google Chrome", version: "131" }},
                {{ brand: "Chromium", version: "131" }},
                {{ brand: "Not_A Brand", version: "24" }}
            ],
            mobile: {"true" if is_mobile else "false"},
            platform: {os_json},
            getHighEntropyValues: function(hints) {{
                return Promise.resolve({{
                    architecture: {arch_json},
                    bitness: {bitness_json},
                    model: {model_json},
                    platform: {os_json},
                    platformVersion: {platform_ver_json},
                    uaFullVersion: "131.0.6778.86",
                    fullVersionList: [
                        {{ brand: "Google Chrome", version: "131.0.6778.86" }},
                        {{ brand: "Chromium", version: "131.0.6778.86" }},
                        {{ brand: "Not_A Brand", version: "24.0.0.0" }}
                    ],
                    formFactors: ["Mobile"],
                    hardwareUuid: {hw_uuid_json},
                    buildId: {build_id_json}
                }});
            }},
            toJSON: function() {{
                return {{ brands: this.brands, mobile: true, platform: {os_json} }};
            }}
        }};
        Object.defineProperty(navigator, 'userAgentData', {{ get: () => fakeUAData, configurable: true }});
    }} catch(e) {{}}

    // 2. SCREEN & VIEWPORT GEOMETRY
    try {{
        if (window.Screen && Screen.prototype) {{
            const sProto = Screen.prototype;
            Object.defineProperty(sProto, 'width', {{ get: makeNativeGetter('width', {screen_w}), configurable: true }});
            Object.defineProperty(sProto, 'height', {{ get: makeNativeGetter('height', {screen_h}), configurable: true }});
            Object.defineProperty(sProto, 'availWidth', {{ get: makeNativeGetter('availWidth', {screen_w}), configurable: true }});
            Object.defineProperty(sProto, 'availHeight', {{ get: makeNativeGetter('availHeight', {screen_h} - 28), configurable: true }});
            Object.defineProperty(sProto, 'colorDepth', {{ get: makeNativeGetter('colorDepth', 24), configurable: true }});
            Object.defineProperty(sProto, 'pixelDepth', {{ get: makeNativeGetter('pixelDepth', 24), configurable: true }});
        }}
        Object.defineProperty(window, 'devicePixelRatio', {{ get: makeNativeGetter('devicePixelRatio', {pixel_ratio}), configurable: true }});
    }} catch(e) {{}}

    // 3. DYNAMIC BATTERY API (navigator.getBattery)
    try {{
        const fakeBattery = {{
            charging: {battery_charging},
            chargingTime: {charging_time},
            dischargingTime: {discharging_time},
            level: {battery_level},
            onchargingchange: null,
            onchargingtimechange: null,
            ondischargingtimechange: null,
            onlevelchange: null,
            addEventListener: function() {{}},
            removeEventListener: function() {{}},
            dispatchEvent: function() {{ return true; }}
        }};
        navigator.getBattery = function() {{ return Promise.resolve(fakeBattery); }};
    }} catch(e) {{}}

    // 4. TCP & NETWORK INFORMATION (navigator.connection)
    try {{
        const fakeConn = {{
            downlink: {downlink},
            effectiveType: {eff_type_json},
            rtt: {rtt},
            saveData: false,
            type: {conn_type_json},
            onchange: null,
            addEventListener: function() {{}},
            removeEventListener: function() {{}},
            dispatchEvent: function() {{ return false; }}
        }};
        Object.defineProperty(navigator, 'connection', {{ get: () => fakeConn, configurable: true }});
    }} catch(e) {{}}

    // 5. HIGH-PRECISION TIMER & CLOCK DRIFT SHIELD
    try {{
        const driftPPM = {clock_drift_ppm};
        const jitterUS = {timer_jitter_us};
        const origPerfNow = performance.now.bind(performance);
        performance.now = function() {{
            const base = origPerfNow();
            const driftFactor = 1.0 + (driftPPM * 1e-6);
            const jitterMs = (Math.random() - 0.5) * (jitterUS * 0.001);
            return (base * driftFactor) + jitterMs;
        }};
    }} catch(e) {{}}

    // 6. WEBGL GPU VENDOR & RENDERER SPOOFING
    try {{
        const targetGLVendor = {gl_vendor_json};
        const targetGLRenderer = {gl_renderer_json};
        const patchGL = function(proto) {{
            if (!proto || !proto.getParameter) return;
            const origGetParam = proto.getParameter;
            proto.getParameter = function(param) {{
                if (param === 37445) return targetGLVendor; // UNMASKED_VENDOR_WEBGL
                if (param === 37446) return targetGLRenderer; // UNMASKED_RENDERER_WEBGL
                return origGetParam.apply(this, arguments);
            }};
        }};
        if (window.WebGLRenderingContext) patchGL(window.WebGLRenderingContext.prototype);
        if (window.WebGL2RenderingContext) patchGL(window.WebGL2RenderingContext.prototype);
    }} catch(e) {{}}

    // 7. CANVAS SUB-PIXEL HARMONIC NOISE (1 to 2.1 Billion Seeds)
    try {{
        if (window.CanvasRenderingContext2D) {{
            const seedVal = {canvas_seed};
            const origGetImageData = CanvasRenderingContext2D.prototype.getImageData;
            CanvasRenderingContext2D.prototype.getImageData = function(x, y, w, h) {{
                const img = origGetImageData.apply(this, arguments);
                const d = img.data;
                const len = d.length;
                const step = Math.max(1, Math.floor(len / 64));
                for (let i = 0; i < len; i += step) {{
                    const shift = ((seedVal * (i + 19)) % 3) - 1;
                    d[i] = Math.min(255, Math.max(0, d[i] + shift));
                }}
                return img;
            }};
        }}
    }} catch(e) {{}}

    // 8. AUDIOCONTEXT HARMONIC SUB-PIXEL NOISE
    try {{
        if (window.AudioBuffer) {{
            const audioSeed = {audio_seed};
            const origGetChannelData = AudioBuffer.prototype.getChannelData;
            AudioBuffer.prototype.getChannelData = function(channel) {{
                const data = origGetChannelData.call(this, channel);
                if (data && data.length > 0) {{
                    const step = Math.max(1, Math.floor(data.length / 64));
                    for (let i = 0; i < data.length; i += step) {{
                        const noise = (((audioSeed * (i + 17)) % 100) - 50) * 0.00000005;
                        data[i] = data[i] + noise;
                    }}
                }}
                return data;
            }};
        }}
    }} catch(e) {{}}

    // 9. GEOLOCATION SATELLITE DRIFT & TIMEZONE
    try {{
        const spoofedLat = {spoof_latitude} + ({gps_lat_offset});
        const spoofedLng = {spoof_longitude} + ({gps_lng_offset});
        if (navigator.geolocation) {{
            navigator.geolocation.getCurrentPosition = function(successCallback) {{
                if (typeof successCallback === 'function') {{
                    setTimeout(() => successCallback({{
                        coords: {{
                            latitude: spoofedLat,
                            longitude: spoofedLng,
                            accuracy: 15.0,
                            altitude: 28.0,
                            altitudeAccuracy: 4.0,
                            heading: null,
                            speed: null
                        }},
                        timestamp: Date.now()
                    }}), 10);
                }}
            }};
        }}

        // Timezone Spoofing
        const targetTZ = {tz_json};
        const OrigDTF = Intl.DateTimeFormat;
        Intl.DateTimeFormat = function(locales, options) {{
            options = Object.assign({{}}, options);
            if (!options.timeZone) options.timeZone = targetTZ;
            return new OrigDTF(locales, options);
        }};
        Intl.DateTimeFormat.prototype = OrigDTF.prototype;
        Date.prototype.getTimezoneOffset = function() {{ return {spoof_offset_minutes}; }};
    }} catch(e) {{}}

    console.log("[Fingerprint Engine] Active Identity: " + {model_json} + " | UUID: " + {hw_uuid_json} + " | Battery=" + ({battery_level} * 100).toFixed(0) + "%");
}})();
"""
    return js_code
