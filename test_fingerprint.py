#!/usr/bin/env python3
"""
Unit Test Suite for Standalone Phone Fingerprint Engine
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engine import (
    TOTAL_PHONE_PRESETS,
    get_phone_profile,
    generate_crore_fingerprint,
    build_fingerprint_injection_script
)


class TestPhoneFingerprintEngine(unittest.TestCase):

    def test_preset_bounds(self):
        """Verify phone presets are bounded between 1 and 10,000."""
        p1 = get_phone_profile(1)
        self.assertEqual(p1["preset_id"], 1)
        self.assertIn("brand", p1)
        self.assertIn("user_agent", p1)

        p10000 = get_phone_profile(10000)
        self.assertEqual(p10000["preset_id"], 10000)

        # Clamping
        p_clamp_low = get_phone_profile(0)
        self.assertEqual(p_clamp_low["preset_id"], 1)
        p_clamp_high = get_phone_profile(99999)
        self.assertEqual(p_clamp_high["preset_id"], 10000)

    def test_battery_modeling(self):
        """Verify Battery API fields are within authentic physiological specs."""
        for _ in range(50):
            p = generate_crore_fingerprint()
            self.assertGreaterEqual(p["battery_level"], 0.15)
            self.assertLessEqual(p["battery_level"], 1.0)
            self.assertIsInstance(p["battery_charging"], bool)
            self.assertIn(p["charging_time"], (0, "Infinity"))
            self.assertTrue(p["discharging_time"] == "Infinity" or isinstance(p["discharging_time"], int))

    def test_tcp_network_stack(self):
        """Verify TCP MTU, MSS, TTL, and Window math."""
        for _ in range(50):
            p = generate_crore_fingerprint()
            mtu = p["tcp_mtu"]
            mss = p["tcp_mss"]
            ttl = p["tcp_ttl"]
            self.assertIn(mtu, [1500, 1440, 1420])
            self.assertEqual(mss, mtu - 40, "TCP MSS must equal MTU - 40 (IP + TCP header bytes)")
            self.assertEqual(ttl, 64, "Mobile Linux / Android / iOS TTL must be 64")
            self.assertIn(p["tcp_window_size"], [65535, 131072, 262144, 524288])
            self.assertIn(p["tcp_window_scaling"], [7, 8, 9])
            self.assertTrue(p["tcp_syn_packet_hex"].startswith("4500003c"))

    def test_timer_clock_drift(self):
        """Verify high-precision timer and clock drift PPM parameters."""
        for _ in range(50):
            p = generate_crore_fingerprint()
            ppm = p["clock_drift_ppm"]
            jitter = p["timer_jitter_microsec"]
            self.assertGreaterEqual(ppm, -5.5)
            self.assertLessEqual(ppm, 5.5)
            self.assertGreater(jitter, 0.0)
            self.assertLessEqual(jitter, 25.0)

    def test_crores_uniqueness(self):
        """Verify that 1,000 generated crore-level fingerprints produce 1,000 unique UUIDs and hashes."""
        uuids = set()
        hashes = set()
        for _ in range(1000):
            p = generate_crore_fingerprint()
            uuids.add(p["hardware_uuid"])
            hashes.add(p["unique_fingerprint_hash"])

        self.assertEqual(len(uuids), 1000, "All 1,000 generated profiles must have unique 128-bit hardware UUIDs")
        self.assertEqual(len(hashes), 1000, "All 1,000 generated profiles must have unique composite hashes")

    def test_javascript_injection_builder(self):
        """Verify JavaScript injection script builds and contains all key overrides."""
        p = generate_crore_fingerprint()
        js = build_fingerprint_injection_script(p)
        self.assertIn("navigator.getBattery", js)
        self.assertIn("performance.now", js)
        self.assertIn("UNMASKED_RENDERER_WEBGL", js)
        self.assertIn("CanvasRenderingContext2D", js)
        self.assertIn("AudioBuffer", js)
        self.assertIn(p["hardware_uuid"], js)


if __name__ == "__main__":
    unittest.main()
