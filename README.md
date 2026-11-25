# 📱 Mobile Phone Fingerprint Engine (10,000 Phones + Crores Telemetry)

A complete, standalone anti-detection mobile phone fingerprint generation system and client-side JavaScript injection engine.

---

## 🌟 મુખ્ય વિશેષતાઓ (Key Features)

1. **10,000 અધિકૃત ફોન મોડલ્સ (10,000 Real Phone Models)**:
   - Samsung (Galaxy S24 Ultra, S23, Z Fold 6, Z Flip 6, A55, M55)
   - Vivo & iQOO (Vivo X300, X200 Pro, X100, V40 Pro, V30, iQOO 12)
   - Google Pixel (Pixel 9 Pro XL, Pixel 9, Pixel 8 Pro, Pixel 7a)
   - OnePlus (OnePlus 12, 12R, 11, Nord 4, Nord CE 4)
   - Xiaomi / Redmi / POCO (Xiaomi 14 Ultra, 13T, Redmi Note 13 Pro+, POCO F6 Pro, X6 Pro)
   - Apple (iPhone 16 Pro Max, 16, 15 Pro, 14, 13, iPad Pro M4)
   - Realme (GT 6, 12 Pro+), Motorola (Edge 50 Ultra), Nothing Phone (2, 2a)

2. **કરોડો અનન્ય ફિંગરપ્રિન્ટ્સ (Crores / Billions of Unique Instances)**:
   - 128-bit હાર્ડવેર UUID અને અધિકૃત OS Build ID.
   - શૂન્ય કોલિઝન (Zero collision rate).

3. **બેટરી API સિમ્યુલેશન (Dynamic Battery API)**:
   - `battery_level` (0.15 થી 0.99)
   - `battery_charging` (True/False)
   - `charging_time` & `discharging_time`
   - બેટરી તાપમાન (°C) અને હેલ્થ સ્ટેટસ.

4. **TCP અને નેટવર્ક સ્ટેક મોડેલિંગ (TCP & Network Stack)**:
   - TCP MTU (1500, 1440, 1420 bytes)
   - TCP MSS = MTU - 40 bytes
   - TCP TTL = 64 (Linux / Android / iOS standard)
   - TCP Window Size & Window Scaling Factor (7, 8, 9)
   - TCP SYN Packet Hex Signature (p0f / JA4 પેસિવ ફિંગરપ્રિન્ટિંગ બાયપાસ).

5. **હાઈ-પ્રિસિઝન ટાઈમર અને ક્લોક ડ્રિફ્ટ (High-Precision Timer & Clock Drift)**:
   - હાર્ડવેર ક્રિસ્ટલ ઓસિલેટર ક્લોક ડ્રિફ્ટ: `-5.0 ppm` થી `+5.0 ppm`.
   - `performance.now()` માઇક્રોસેકન્ડ જિટર (Spectre/Timing attacks સામે સુરક્ષા).
   - ટાઇમસ્ટેમ્પ કાઉન્ટર (TSC) ફ્રીક્વન્સી (2.4 - 3.2 GHz).

6. **કેનવાસ અને ઓડિયો સબ-પિક્સેલ અવાજ (Canvas & AudioContext Noise)**:
   - 1 થી 2.1 અબજ યુનિક સીડ્સ (Sub-pixel noise).
   - અનમાસ્ક્ડ WebGL GPU Vendor & Renderer (Adreno 750, Mali-G925, Apple GPU).

---

## 🚀 કેવી રીતે રન કરવું (How to Run)

### 1. ગ્રાફિકલ યુઝર ઇન્ટરફેસ (GUI Mode):
```bash
python3 main.py
# અથવા
./run.sh
```

### 2. કમાન્ડ લાઇન ઇન્ટરફેસ (CLI Mode):
```bash
# ૧ રેન્ડમ કરોડ-લેવલ યુનિક ફોન ફિંગરપ્રિન્ટ જનરેટ કરવા માટે:
python3 cli.py random

# ૧૦,૦૦૦ ફોન પ્રીસેટ્સમાંથી ચોક્કસ ફોન લોડ કરવા માટે (ઉદાહરણ તરીકે ફોન #120):
python3 cli.py generate --id 120

# JavaScript ઇન્જેક્શન સ્ક્રિપ્ટ જનરેટ કરવા માટે:
python3 cli.py js --id 1

# 1,000 યુનિક પ્રોફાઇલ્સ એકસાથે બેચમાં JSON ફાઇલમાં સેવ કરવા માટે:
python3 cli.py batch --count 1000 --out phone_fingerprints.json

# એન્જિન સ્પીડ બેન્ચમાર્ક કરવા માટે (૫૦,૦૦૦+ પ્રોફાઇલ્સ/સેકન્ડ):
python3 cli.py benchmark
```

### 3. યુનિટ ટેસ્ટ રન કરવા માટે:
```bash
python3 test_fingerprint.py
```
