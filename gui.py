"""
Phone Fingerprint Engine: Interactive Cyber-Dark GUI with Large Realistic Phone Screen
Provides:
- Massive, Dominant Smartphone Screen Mockup (60-70% width) with Notch, Status Bar & Android Nav
- Sleek, Ultra-Compact Right-Side Telemetry & Settings Panel
- Interactive Screen Size Switcher: Massive (720px), Giant (820px), Cinema (920px), Full Phone Mode (100%)
- Embedded Live WebEngineView with Fingerprint Telemetry & Interactive Mobile OS Dashboard
- 10,000 Deterministic Authentic Phone Models Browser
- Crores (Tens of Millions / Billions) Dynamic Entropy Generator
- Dedicated Compact Tabs: Hardware, Battery API, TCP/MTU, High-Precision Timer, WebGL/Canvas, JS Injector
- Live Battery & Model Synchronization between Controls and Phone Screen
- 1-Click Clipboard Copying & Batch JSON/CSV Export
"""

import sys
import os
import json
import random
import time
from typing import Dict, Any, List

from PyQt6.QtCore import Qt, QTimer, QUrl
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QComboBox, QSpinBox, QTabWidget,
    QTextEdit, QTableWidget, QTableWidgetItem, QHeaderView, QFrame,
    QProgressBar, QFileDialog, QMessageBox, QGroupBox, QSplitter,
    QSlider, QCheckBox, QScrollArea
)
from PyQt6.QtWebEngineWidgets import QWebEngineView

# Ensure engine is importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine import (
    TOTAL_PHONE_PRESETS,
    get_phone_profile,
    generate_crore_fingerprint,
    build_fingerprint_injection_script
)


class FingerprintManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📱 Mobile Phone Fingerprint Engine & Live Smartphone Screen")
        self.resize(1560, 920)
        self.current_profile: Dict[str, Any] = {}
        self.history: List[Dict[str, Any]] = []

        self._apply_theme()
        self._init_ui()
        self.generate_new_crore_profile()

        # Start maximized and set massive phone screen width
        self.showMaximized()
        QTimer.singleShot(150, lambda: self._set_phone_screen_width(740))

        # Clock timer for phone status bar
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self._update_clock)
        self.clock_timer.start(15000)
        self._update_clock()

    def _apply_theme(self):
        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #0d1117;
                color: #c9d1d9;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
            }
            QLabel {
                color: #8b949e;
                font-size: 10px;
            }
            QLineEdit, QSpinBox, QTextEdit {
                background-color: #161b22;
                color: #58a6ff;
                border: 1px solid #30363d;
                border-radius: 5px;
                padding: 4px 8px;
                font-size: 11px;
                font-family: monospace;
            }
            QLineEdit:focus, QSpinBox:focus, QTextEdit:focus {
                border: 1px solid #58a6ff;
            }
            QComboBox {
                background-color: #161b22;
                color: #58a6ff;
                border: 1px solid #30363d;
                border-radius: 5px;
                padding: 4px 8px;
                font-size: 11px;
                font-weight: bold;
            }
            QTabWidget::pane {
                border: 1px solid #30363d;
                background: #161b22;
                border-radius: 6px;
                top: -1px;
            }
            QTabBar::tab {
                background: #0d1117;
                color: #8b949e;
                padding: 6px 12px;
                border: 1px solid #30363d;
                border-bottom: none;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
                margin-right: 2px;
                font-weight: bold;
                font-size: 10px;
            }
            QTabBar::tab:selected {
                background: #161b22;
                color: #58a6ff;
                border-bottom: 2px solid #58a6ff;
            }
            QPushButton {
                background-color: #21262d;
                color: #c9d1d9;
                border: 1px solid #30363d;
                border-radius: 5px;
                padding: 5px 12px;
                font-size: 11px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #30363d;
                color: #ffffff;
            }
            QTableWidget {
                background-color: #0d1117;
                border: 1px solid #30363d;
                border-radius: 6px;
                color: #c9d1d9;
                gridline-color: #21262d;
                font-size: 10px;
            }
            QHeaderView::section {
                background-color: #161b22;
                color: #58a6ff;
                font-weight: bold;
                border: none;
                padding: 3px;
                font-size: 10px;
            }
            QProgressBar {
                border: 1px solid #30363d;
                border-radius: 4px;
                text-align: center;
                color: #ffffff;
                font-weight: bold;
                font-size: 10px;
                background-color: #161b22;
            }
            QProgressBar::chunk {
                background-color: #238636;
                border-radius: 4px;
            }
            QSplitter::handle {
                background-color: #21262d;
                width: 7px;
                border-radius: 3px;
            }
            QSplitter::handle:hover {
                background-color: #58a6ff;
            }
        """)

    def _init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(10, 8, 10, 8)
        main_layout.setSpacing(6)

        # 1. Top Header Bar
        hdr_layout = QHBoxLayout()
        title = QLabel("📱 Mobile Phone Fingerprint Engine & Live Smartphone Screen")
        title.setStyleSheet("font-size: 15px; font-weight: 800; color: #58a6ff;")
        hdr_layout.addWidget(title)
        hdr_layout.addStretch()

        badge_phones = QLabel("✓ 10,000 Real Models")
        badge_phones.setStyleSheet("background: rgba(35, 134, 54, 0.2); color: #3fb950; border: 1px solid #238636; border-radius: 10px; padding: 2px 8px; font-size: 10px; font-weight: bold;")
        hdr_layout.addWidget(badge_phones)

        badge_entropy = QLabel("✓ Crores Entropy (128-bit)")
        badge_entropy.setStyleSheet("background: rgba(88, 166, 255, 0.2); color: #58a6ff; border: 1px solid #1f6feb; border-radius: 10px; padding: 2px 8px; font-size: 10px; font-weight: bold;")
        hdr_layout.addWidget(badge_entropy)
        main_layout.addLayout(hdr_layout)

        # 2. Controls Toolbar
        ctrl_frame = QFrame()
        ctrl_frame.setStyleSheet("background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 5px;")
        ctrl_layout = QHBoxLayout(ctrl_frame)
        ctrl_layout.setContentsMargins(8, 4, 8, 4)
        ctrl_layout.setSpacing(8)

        ctrl_layout.addWidget(QLabel("<b>Model ID (1 - 10,000):</b>"))
        self.spn_model_id = QSpinBox()
        self.spn_model_id.setRange(1, TOTAL_PHONE_PRESETS)
        self.spn_model_id.setValue(random.randint(1, TOTAL_PHONE_PRESETS))
        self.spn_model_id.setFixedWidth(85)
        ctrl_layout.addWidget(self.spn_model_id)

        btn_load_model = QPushButton("🔍 Load Preset")
        btn_load_model.clicked.connect(self._on_load_preset_clicked)
        ctrl_layout.addWidget(btn_load_model)

        ctrl_layout.addSpacing(6)

        self.btn_gen_crore = QPushButton("🎲 Generate 1 in Crores (Unique Phone)")
        self.btn_gen_crore.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_gen_crore.setStyleSheet("""
            QPushButton {
                background: linear-gradient(135deg, #238636, #2ea043);
                color: #ffffff;
                font-weight: 800;
                font-size: 11px;
                padding: 6px 16px;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background: linear-gradient(135deg, #2ea043, #3fb950);
            }
        """)
        self.btn_gen_crore.clicked.connect(self.generate_new_crore_profile)
        ctrl_layout.addWidget(self.btn_gen_crore)

        ctrl_layout.addSpacing(10)

        # Screen Size Switcher (Moti Screen Controller)
        ctrl_layout.addWidget(QLabel("<b>🖥️ Phone Size:</b>"))
        self.cmb_screen_size = QComboBox()
        self.cmb_screen_size.addItem("📱 Massive Screen (740px) [Default]")
        self.cmb_screen_size.addItem("📱 Giant Screen (840px)")
        self.cmb_screen_size.addItem("📱 Cinema Screen (940px)")
        self.cmb_screen_size.addItem("🖥️ Full Phone Mode (100% Screen)")
        self.cmb_screen_size.addItem("📱 Standard Screen (580px)")
        self.cmb_screen_size.currentIndexChanged.connect(self._on_screen_size_changed)
        ctrl_layout.addWidget(self.cmb_screen_size)

        ctrl_layout.addStretch()

        btn_copy_js = QPushButton("📜 Copy JS")
        btn_copy_js.clicked.connect(self._copy_js_script)
        ctrl_layout.addWidget(btn_copy_js)

        btn_export = QPushButton("💾 Export Batch")
        btn_export.clicked.connect(self._export_batch_dialog)
        ctrl_layout.addWidget(btn_export)

        main_layout.addWidget(ctrl_frame)

        # 3. Main Splitter: Left = Massive Phone Screen, Right = Compact Telemetry
        self.splitter = QSplitter(Qt.Orientation.Horizontal)

        # --- LEFT: Massive Smartphone Frame & Screen ---
        self.phone_container = self._build_phone_frame()
        self.splitter.addWidget(self.phone_container)

        # --- RIGHT: Compact Telemetry Controls & Tabs ---
        self.right_container = QWidget()
        self.right_container.setMaximumWidth(520)
        right_layout = QVBoxLayout(self.right_container)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(6)

        self.tabs = QTabWidget()
        self.tab_hardware = self._build_hardware_tab()
        self.tab_battery = self._build_battery_tab()
        self.tab_tcp = self._build_tcp_tab()
        self.tab_timer = self._build_timer_tab()
        self.tab_webgl_canvas = self._build_webgl_canvas_tab()
        self.tab_js = self._build_js_tab()

        self.tabs.addTab(self.tab_hardware, "📱 Device")
        self.tabs.addTab(self.tab_battery, "🔋 Battery")
        self.tabs.addTab(self.tab_tcp, "🌐 TCP/MTU")
        self.tabs.addTab(self.tab_timer, "⏱️ Clock Drift")
        self.tabs.addTab(self.tab_webgl_canvas, "🎨 WebGL")
        self.tabs.addTab(self.tab_js, "📜 JS Code")
        right_layout.addWidget(self.tabs, 1)

        # Compact History Table
        hist_lbl = QLabel("<b>📚 Generated History (Double click to reload):</b>")
        hist_lbl.setStyleSheet("color: #58a6ff; font-size: 10px;")
        right_layout.addWidget(hist_lbl)

        self.table_history = QTableWidget()
        self.table_history.setColumnCount(6)
        self.table_history.setHorizontalHeaderLabels(["ID", "Model Name", "Battery", "MTU", "Drift", "UUID"])
        self.table_history.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.table_history.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.table_history.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.table_history.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        self.table_history.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        self.table_history.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        self.table_history.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table_history.cellDoubleClicked.connect(self._on_history_double_clicked)
        self.table_history.setFixedHeight(95)
        right_layout.addWidget(self.table_history)

        self.splitter.addWidget(self.right_container)

        # Set initial splitter proportions (Massive Phone: 740px, Compact details: 480px)
        self.splitter.setSizes([740, 480])
        main_layout.addWidget(self.splitter, 1)

        # 4. Status Bar
        bot_bar = QHBoxLayout()
        self.lbl_status = QLabel("Ready to synthesize high-entropy phone fingerprints.")
        self.lbl_status.setStyleSheet("color: #3fb950; font-size: 11px;")
        bot_bar.addWidget(self.lbl_status)
        bot_bar.addStretch()

        btn_close = QPushButton("Close")
        btn_close.clicked.connect(self.close)
        bot_bar.addWidget(btn_close)
        main_layout.addLayout(bot_bar)

    # ==============================================================
    # MASSIVE PHONE CHASSIS & SCREEN MOCKUP BUILDER
    # ==============================================================

    def _build_phone_frame(self) -> QWidget:
        container = QWidget()
        lay = QVBoxLayout(container)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        # Massive Realistic Outer Phone Frame
        self.phone_frame = QFrame()
        self.phone_frame.setObjectName("PhoneChassis")
        self.phone_frame.setStyleSheet("""
            QFrame#PhoneChassis {
                background-color: #0b0c10;
                border: 5px solid #30363d;
                border-radius: 38px;
            }
        """)
        phone_vbox = QVBoxLayout(self.phone_frame)
        phone_vbox.setContentsMargins(5, 5, 5, 5)
        phone_vbox.setSpacing(0)

        # 1. Top Earpiece & Status Bar (Large & Crisp)
        self.phone_status_bar = QFrame()
        self.phone_status_bar.setFixedHeight(32)
        self.phone_status_bar.setStyleSheet("background-color: #12141c; border-top-left-radius: 34px; border-top-right-radius: 34px;")
        sb_lay = QHBoxLayout(self.phone_status_bar)
        sb_lay.setContentsMargins(22, 2, 22, 2)
        sb_lay.setSpacing(10)

        self.lbl_phone_time = QLabel("15:30")
        self.lbl_phone_time.setStyleSheet("color: #ffffff; font-size: 13px; font-weight: bold;")

        self.lbl_phone_model_tag = QLabel("Samsung Galaxy S24 Ultra")
        self.lbl_phone_model_tag.setStyleSheet("color: #58a6ff; font-size: 11px; font-weight: bold; background: rgba(88, 166, 255, 0.15); padding: 2px 8px; border-radius: 4px;")

        # Center Punch-Hole Camera Notch
        lbl_notch = QLabel("⚫")
        lbl_notch.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_notch.setStyleSheet("color: #000000; font-size: 15px;")

        self.lbl_phone_indicators = QLabel("5G 📶 🔋 88%")
        self.lbl_phone_indicators.setStyleSheet("color: #3fb950; font-size: 12px; font-weight: 800;")

        sb_lay.addWidget(self.lbl_phone_time)
        sb_lay.addWidget(self.lbl_phone_model_tag)
        sb_lay.addWidget(lbl_notch, 1)
        sb_lay.addWidget(self.lbl_phone_indicators)
        phone_vbox.addWidget(self.phone_status_bar)

        # 2. In-Phone Browser Navigation Bar (Height 38px)
        self.phone_nav_bar = QFrame()
        self.phone_nav_bar.setFixedHeight(38)
        self.phone_nav_bar.setStyleSheet("background-color: #161b22; border-bottom: 1px solid #30363d;")
        nav_lay = QHBoxLayout(self.phone_nav_bar)
        nav_lay.setContentsMargins(10, 2, 10, 2)
        nav_lay.setSpacing(6)

        btn_back = QPushButton("◀")
        btn_back.setFixedSize(30, 28)
        btn_back.setStyleSheet("border: none; background: transparent; color: #58a6ff; font-size: 14px; font-weight: bold;")
        btn_back.clicked.connect(self._phone_nav_back)
        nav_lay.addWidget(btn_back)

        btn_refresh = QPushButton("🔄")
        btn_refresh.setFixedSize(30, 28)
        btn_refresh.setStyleSheet("border: none; background: transparent; color: #58a6ff; font-size: 14px;")
        btn_refresh.clicked.connect(self._phone_nav_refresh)
        nav_lay.addWidget(btn_refresh)

        self.txt_phone_url = QLineEdit()
        self.txt_phone_url.setPlaceholderText("Enter URL or search...")
        self.txt_phone_url.setText("phone://home")
        self.txt_phone_url.setStyleSheet("font-size: 12px; padding: 3px 10px; border-radius: 6px; height: 24px;")
        self.txt_phone_url.returnPressed.connect(self._phone_nav_go)
        nav_lay.addWidget(self.txt_phone_url, 1)

        btn_go = QPushButton("Go")
        btn_go.setFixedSize(42, 28)
        btn_go.setStyleSheet("background-color: #238636; color: #ffffff; border-radius: 4px; font-size: 11px; font-weight: bold; padding: 0;")
        btn_go.clicked.connect(self._phone_nav_go)
        nav_lay.addWidget(btn_go)

        btn_home = QPushButton("🏠")
        btn_home.setFixedSize(30, 28)
        btn_home.setStyleSheet("border: none; background: transparent; color: #f0883e; font-size: 15px;")
        btn_home.clicked.connect(self._phone_nav_home)
        nav_lay.addWidget(btn_home)

        phone_vbox.addWidget(self.phone_nav_bar)

        # 3. Interactive Phone Screen View (QWebEngineView)
        self.web_view = QWebEngineView()
        self.web_view.setStyleSheet("background-color: #0d1117;")
        phone_vbox.addWidget(self.web_view, 1)

        # 4. Phone Bottom Navigation Bar (Android Softkeys - Height 34px)
        self.phone_bottom_bar = QFrame()
        self.phone_bottom_bar.setFixedHeight(34)
        self.phone_bottom_bar.setStyleSheet("background-color: #12141c; border-bottom-left-radius: 34px; border-bottom-right-radius: 34px;")
        bnav_lay = QHBoxLayout(self.phone_bottom_bar)
        bnav_lay.setContentsMargins(50, 2, 50, 2)

        btn_soft_back = QPushButton("◀")
        btn_soft_back.setFixedSize(48, 26)
        btn_soft_back.setStyleSheet("border: none; background: transparent; color: #8b949e; font-size: 16px;")
        btn_soft_back.clicked.connect(self._phone_nav_back)

        btn_soft_home = QPushButton("●")
        btn_soft_home.setFixedSize(48, 26)
        btn_soft_home.setStyleSheet("border: none; background: transparent; color: #ffffff; font-size: 18px;")
        btn_soft_home.clicked.connect(self._phone_nav_home)

        btn_soft_recent = QPushButton("■")
        btn_soft_recent.setFixedSize(48, 26)
        btn_soft_recent.setStyleSheet("border: none; background: transparent; color: #8b949e; font-size: 16px;")
        btn_soft_recent.clicked.connect(self._phone_show_recent_info)

        bnav_lay.addWidget(btn_soft_back)
        bnav_lay.addStretch()
        bnav_lay.addWidget(btn_soft_home)
        bnav_lay.addStretch()
        bnav_lay.addWidget(btn_soft_recent)
        phone_vbox.addWidget(self.phone_bottom_bar)

        lay.addWidget(self.phone_frame, 1)
        return container

    # --- SCREEN SIZE CONTROLLER (Moti Screen Logic) ---

    def _on_screen_size_changed(self, idx: int):
        sizes = [740, 840, 940, -1, 580]
        chosen = sizes[idx]
        self._set_phone_screen_width(chosen)

    def _set_phone_screen_width(self, width: int):
        if width == -1:  # Full Phone Mode
            self.right_container.hide()
            self.splitter.setSizes([self.width(), 0])
            self.lbl_status.setText("🖥️ Full Phone Mode Activated! (Select another size to restore right panel)")
        else:
            self.right_container.show()
            total_w = self.width()
            rem = max(340, total_w - width - 15)
            self.splitter.setSizes([width, rem])
            self.lbl_status.setText(f"📱 Phone Screen resized to {width}px wide!")

    # --- PHONE SCREEN NAVIGATION HANDLERS ---

    def _update_clock(self):
        curr = time.strftime("%H:%M")
        self.lbl_phone_time.setText(curr)

    def _phone_nav_back(self):
        self.web_view.back()

    def _phone_nav_refresh(self):
        self.web_view.reload()

    def _phone_nav_home(self):
        self.txt_phone_url.setText("phone://home")
        self._load_phone_dashboard()

    def _phone_nav_go(self):
        url_text = self.txt_phone_url.text().strip()
        if not url_text or url_text == "phone://home":
            self._load_phone_dashboard()
            return
        if not url_text.startswith("http://") and not url_text.startswith("https://"):
            if "." in url_text and " " not in url_text:
                url_text = "https://" + url_text
            else:
                url_text = f"https://www.google.com/search?q={url_text}"
        self.txt_phone_url.setText(url_text)
        self.web_view.setUrl(QUrl(url_text))

    def _phone_show_recent_info(self):
        p = self.current_profile
        msg = f"📱 Active Phone: {p.get('name')}\nUUID: {p.get('hardware_uuid')}\nBattery: {int(p.get('battery_level',0)*100)}%\nTCP MTU: {p.get('tcp_mtu')} bytes\nClock Drift: {p.get('clock_drift_ppm')} ppm"
        QMessageBox.information(self, "Phone Specs & Fingerprint", msg)

    def _load_phone_dashboard(self):
        """Renders authentic Massive-Screen Smartphone OS Home Dashboard into the phone screen."""
        p = self.current_profile or {}
        b_level = int(p.get("battery_level", 0.85) * 100)
        is_chg = p.get("battery_charging", False)
        chg_str = "⚡ Charging" if is_chg else "🔋 Discharging"

        html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    body {{
        background: linear-gradient(180deg, #080c14 0%, #101726 100%);
        color: #ffffff;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        margin: 0;
        padding: 22px;
        box-sizing: border-box;
    }}
    .search-box {{
        background: #1a2234;
        border: 1px solid #2d3748;
        border-radius: 28px;
        padding: 12px 22px;
        display: flex;
        align-items: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.4);
    }}
    .search-box input {{
        background: transparent;
        border: none;
        color: #fff;
        font-size: 15px;
        width: 100%;
        outline: none;
    }}
    .card {{
        background: rgba(22, 27, 34, 0.95);
        border: 1px solid #30363d;
        border-radius: 16px;
        padding: 18px 20px;
        margin-bottom: 16px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.3);
    }}
    .card-title {{
        font-size: 13px;
        font-weight: 800;
        color: #58a6ff;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 8px;
    }}
    .val-highlight {{
        font-size: 22px;
        font-weight: 900;
        color: #f0883e;
    }}
    .grid-2 {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 14px;
    }}
    .stat-badge {{
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 12px 14px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }}
    .stat-badge .lbl {{
        font-size: 11px;
        color: #8b949e;
        text-transform: uppercase;
        font-weight: 800;
        letter-spacing: 0.5px;
    }}
    .stat-badge .num {{
        font-size: 15px;
        font-weight: 800;
        color: #3fb950;
        margin-top: 4px;
    }}
    .app-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin-top: 24px;
        text-align: center;
    }}
    .app-icon {{
        background: #21262d;
        border: 1px solid #30363d;
        border-radius: 20px;
        width: 72px;
        height: 72px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 34px;
        margin: 0 auto;
        cursor: pointer;
        transition: transform 0.15s, border-color 0.15s;
        box-shadow: 0 4px 14px rgba(0,0,0,0.35);
    }}
    .app-icon:hover {{
        transform: scale(1.08);
        border-color: #58a6ff;
    }}
    .app-label {{
        font-size: 13px;
        font-weight: 700;
        color: #c9d1d9;
        margin-top: 8px;
    }}
</style>
</head>
<body>

    <!-- Large Search Bar -->
    <div class="search-box">
        <span style="margin-right: 12px; font-size: 18px;">🔍</span>
        <input type="text" placeholder="Search Google or enter web URL..." onkeydown="if(event.key==='Enter') window.location='https://www.google.com/search?q='+encodeURIComponent(this.value)">
    </div>

    <!-- Active Device Card -->
    <div class="card">
        <div class="card-title">📱 ACTIVE SMARTPHONE MODEL</div>
        <div class="val-highlight">{p.get('name', 'Smartphone')}</div>
        <div style="font-size: 14px; color: #8b949e; margin-top: 6px;">
            {p.get('brand')} • {p.get('model')} • {p.get('os')} {p.get('os_version')}
        </div>
        <div style="font-size: 12px; color: #d2a8ff; font-family: monospace; margin-top: 6px;">
            UUID: {p.get('hardware_uuid', 'N/A')}
        </div>
    </div>

    <!-- Real Telemetry Stats Grid (Massive) -->
    <div class="grid-2">
        <!-- Battery Widget -->
        <div class="stat-badge">
            <div class="lbl">🔋 Battery API</div>
            <div class="num" style="color: {'#3fb950' if b_level > 25 else '#f85149'};">{b_level}% ({chg_str})</div>
            <div style="font-size: 11px; color: #8b949e; margin-top: 4px;">Temp: {p.get('battery_temperature_c', 31)}°C ({p.get('battery_health', 'Good')})</div>
        </div>

        <!-- TCP MTU Stack -->
        <div class="stat-badge">
            <div class="lbl">🌐 TCP / MTU Stack</div>
            <div class="num" style="color: #58a6ff;">{p.get('tcp_mtu', 1500)} Bytes (MSS: {p.get('tcp_mss', 1460)})</div>
            <div style="font-size: 11px; color: #8b949e; margin-top: 4px;">TTL: {p.get('tcp_ttl', 64)} • Win: {p.get('tcp_window_size', 65535)}</div>
        </div>

        <!-- Timer & Clock Drift -->
        <div class="stat-badge">
            <div class="lbl">⏱️ Clock Drift</div>
            <div class="num" style="color: #f0883e;">{p.get('clock_drift_ppm', 0.0):+.3f} ppm</div>
            <div style="font-size: 11px; color: #8b949e; margin-top: 4px;">Jitter: {p.get('timer_jitter_microsec', 5)} µs</div>
        </div>

        <!-- WebGL GPU -->
        <div class="stat-badge">
            <div class="lbl">🎮 WebGL GPU</div>
            <div class="num" style="color: #79c0ff; font-size: 13px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{p.get('gl_renderer', 'GPU')}</div>
            <div style="font-size: 11px; color: #8b949e; margin-top: 4px;">DPR: {p.get('device_pixel_ratio', 3.0)} ({p.get('screen_width', 393)}x{p.get('screen_height', 873)})</div>
        </div>
    </div>

    <!-- Massive App Launcher Icons -->
    <div class="app-grid">
        <div onclick="window.location='https://whoer.net'">
            <div class="app-icon">🌐</div>
            <div class="app-label">Whoer</div>
        </div>
        <div onclick="window.location='https://browserleaks.com/canvas'">
            <div class="app-icon">🎨</div>
            <div class="app-label">Canvas</div>
        </div>
        <div onclick="window.location='https://iphey.com'">
            <div class="app-icon">🛡️</div>
            <div class="app-label">IPhey</div>
        </div>
        <div onclick="window.location='https://browserleaks.com/webrtc'">
            <div class="app-icon">🔒</div>
            <div class="app-label">WebRTC</div>
        </div>
    </div>

</body>
</html>
"""
        self.web_view.setHtml(html, QUrl("phone://home"))

    # ==============================================================
    # RIGHT PANEL: COMPACT TABS & CONTROLS
    # ==============================================================

    def _build_hardware_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        # Row 1: Name & Brand
        r1 = QHBoxLayout()
        v_name = QVBoxLayout()
        v_name.addWidget(QLabel("📱 Full Marketing Device Name:"))
        self.txt_name = QLineEdit()
        self.txt_name.setStyleSheet("font-weight: bold; color: #f0883e; font-size: 11px;")
        v_name.addWidget(self.txt_name)
        r1.addLayout(v_name, 2)

        v_brand = QVBoxLayout()
        v_brand.addWidget(QLabel("🏷️ Brand & Model Code:"))
        self.txt_brand_model = QLineEdit()
        v_brand.addWidget(self.txt_brand_model)
        r1.addLayout(v_brand, 1)
        layout.addLayout(r1)

        # Row 2: User Agent
        v_ua = QVBoxLayout()
        v_ua.addWidget(QLabel("🌐 User-Agent (navigator.userAgent):"))
        self.txt_ua = QLineEdit()
        self.txt_ua.setStyleSheet("color: #79c0ff; font-size: 10px;")
        v_ua.addWidget(self.txt_ua)
        layout.addLayout(v_ua)

        # Row 3: UUID & Build ID
        r3 = QHBoxLayout()
        v_uuid = QVBoxLayout()
        v_uuid.addWidget(QLabel("🔑 Hardware UUID (128-Bit Unique):"))
        self.txt_uuid = QLineEdit()
        self.txt_uuid.setStyleSheet("color: #d2a8ff; font-weight: bold;")
        v_uuid.addWidget(self.txt_uuid)
        r3.addLayout(v_uuid, 1)

        v_build = QVBoxLayout()
        v_build.addWidget(QLabel("🏗️ Android / iOS Build ID:"))
        self.txt_build_id = QLineEdit()
        v_build.addWidget(self.txt_build_id)
        r3.addLayout(v_build, 1)
        layout.addLayout(r3)

        # Row 4: Viewport & Cores
        r4 = QHBoxLayout()
        v_screen = QVBoxLayout()
        v_screen.addWidget(QLabel("📐 Screen Resolution & DPR:"))
        self.txt_screen = QLineEdit()
        v_screen.addWidget(self.txt_screen)
        r4.addLayout(v_screen, 1)

        v_cores = QVBoxLayout()
        v_cores.addWidget(QLabel("⚙️ CPU Cores / RAM Memory:"))
        self.txt_cores = QLineEdit()
        v_cores.addWidget(self.txt_cores)
        r4.addLayout(v_cores, 1)

        v_touch = QVBoxLayout()
        v_touch.addWidget(QLabel("👆 Touch Points:"))
        self.txt_touch = QLineEdit()
        v_touch.addWidget(self.txt_touch)
        r4.addLayout(v_touch, 1)
        layout.addLayout(r4)

        layout.addStretch()
        return tab

    def _build_battery_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        lbl_desc = QLabel("⚡ <b>Battery API Simulation</b>: Real-time percentage, charging state, and discharge telemetry.")
        lbl_desc.setWordWrap(True)
        lbl_desc.setStyleSheet("color: #8b949e; font-size: 10px;")
        layout.addWidget(lbl_desc)

        # Battery Bar & Live Slider
        b_box = QGroupBox("Live Battery State (Updates Phone Screen Immediately)")
        b_box.setStyleSheet("QGroupBox { font-weight: bold; color: #58a6ff; border: 1px solid #30363d; border-radius: 5px; margin-top: 4px; padding-top: 8px; }")
        b_lay = QVBoxLayout(b_box)

        self.bar_battery = QProgressBar()
        self.bar_battery.setFixedHeight(20)
        b_lay.addWidget(self.bar_battery)

        r_slider = QHBoxLayout()
        r_slider.addWidget(QLabel("Level:"))
        self.slider_battery = QSlider(Qt.Orientation.Horizontal)
        self.slider_battery.setRange(5, 100)
        self.slider_battery.setValue(85)
        self.slider_battery.valueChanged.connect(self._on_battery_slider_changed)
        r_slider.addWidget(self.slider_battery, 1)

        self.chk_charging = QCheckBox("⚡ Charging")
        self.chk_charging.setStyleSheet("color: #3fb950; font-weight: bold;")
        self.chk_charging.toggled.connect(self._on_charging_toggled)
        r_slider.addWidget(self.chk_charging)
        b_lay.addLayout(r_slider)

        r_state = QHBoxLayout()
        self.lbl_charging_state = QLabel("🔋 State: Discharging")
        self.lbl_charging_state.setStyleSheet("font-size: 11px; font-weight: bold; color: #3fb950;")
        r_state.addWidget(self.lbl_charging_state)
        r_state.addStretch()
        self.lbl_battery_temp = QLabel("🌡️ Temp: 31.4°C (Good)")
        self.lbl_battery_temp.setStyleSheet("color: #f0883e; font-weight: bold;")
        r_state.addWidget(self.lbl_battery_temp)
        b_lay.addLayout(r_state)
        layout.addWidget(b_box)

        # Timers
        r_times = QHBoxLayout()
        v_chg_time = QVBoxLayout()
        v_chg_time.addWidget(QLabel("⏱️ Charging Time (s):"))
        self.txt_charging_time = QLineEdit()
        v_chg_time.addWidget(self.txt_charging_time)
        r_times.addLayout(v_chg_time, 1)

        v_dischg_time = QVBoxLayout()
        v_dischg_time.addWidget(QLabel("⏳ Discharging Time (s):"))
        self.txt_discharging_time = QLineEdit()
        v_dischg_time.addWidget(self.txt_discharging_time)
        r_times.addLayout(v_dischg_time, 1)
        layout.addLayout(r_times)

        layout.addStretch()
        return tab

    def _build_tcp_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        lbl_desc = QLabel("🌐 <b>TCP & Network Stack</b>: Emulates MTU, MSS, TTL, Window Size, SACK to bypass p0f/JA4 detection.")
        lbl_desc.setWordWrap(True)
        lbl_desc.setStyleSheet("color: #8b949e; font-size: 10px;")
        layout.addWidget(lbl_desc)

        # Row 1: MTU, MSS, TTL
        r1 = QHBoxLayout()
        v_mtu = QVBoxLayout()
        v_mtu.addWidget(QLabel("📦 TCP MTU:"))
        self.txt_tcp_mtu = QLineEdit()
        self.txt_tcp_mtu.setStyleSheet("color: #58a6ff; font-weight: bold;")
        v_mtu.addWidget(self.txt_tcp_mtu)
        r1.addLayout(v_mtu, 1)

        v_mss = QVBoxLayout()
        v_mss.addWidget(QLabel("📏 TCP MSS:"))
        self.txt_tcp_mss = QLineEdit()
        self.txt_tcp_mss.setStyleSheet("color: #58a6ff; font-weight: bold;")
        v_mss.addWidget(self.txt_tcp_mss)
        r1.addLayout(v_mss, 1)

        v_ttl = QVBoxLayout()
        v_ttl.addWidget(QLabel("⏳ TCP TTL:"))
        self.txt_tcp_ttl = QLineEdit()
        self.txt_tcp_ttl.setStyleSheet("color: #58a6ff; font-weight: bold;")
        v_ttl.addWidget(self.txt_tcp_ttl)
        r1.addLayout(v_ttl, 1)
        layout.addLayout(r1)

        # Row 2: Window Size & Scaling
        r2 = QHBoxLayout()
        v_win = QVBoxLayout()
        v_win.addWidget(QLabel("🪟 TCP Window Size & Scaling:"))
        self.txt_tcp_win = QLineEdit()
        v_win.addWidget(self.txt_tcp_win)
        r2.addLayout(v_win, 1)

        v_conn = QVBoxLayout()
        v_conn.addWidget(QLabel("📶 Connection & Jitter:"))
        self.txt_conn_type = QLineEdit()
        v_conn.addWidget(self.txt_conn_type)
        r2.addLayout(v_conn, 1)
        layout.addLayout(r2)

        # Row 3: SYN Packet Signature
        v_syn = QVBoxLayout()
        v_syn.addWidget(QLabel("🔏 TCP SYN Packet Header Hex Signature:"))
        self.txt_tcp_syn = QLineEdit()
        self.txt_tcp_syn.setStyleSheet("color: #79c0ff; font-family: monospace; font-size: 10px;")
        v_syn.addWidget(self.txt_tcp_syn)
        layout.addLayout(v_syn)

        layout.addStretch()
        return tab

    def _build_timer_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        lbl_desc = QLabel("⏱️ <b>Timer & Clock Drift</b>: Crystal oscillator drift (PPM) & microsecond jitter against Spectre timing attacks.")
        lbl_desc.setWordWrap(True)
        lbl_desc.setStyleSheet("color: #8b949e; font-size: 10px;")
        layout.addWidget(lbl_desc)

        # Row 1: Drift PPM & Jitter
        r1 = QHBoxLayout()
        v_ppm = QVBoxLayout()
        v_ppm.addWidget(QLabel("🧭 Clock Drift (PPM):"))
        self.txt_drift_ppm = QLineEdit()
        self.txt_drift_ppm.setStyleSheet("color: #f0883e; font-weight: bold; font-size: 12px;")
        v_ppm.addWidget(self.txt_drift_ppm)
        r1.addLayout(v_ppm, 1)

        v_jit = QVBoxLayout()
        v_jit.addWidget(QLabel("🛡️ Performance.now Jitter (µs):"))
        self.txt_timer_jit = QLineEdit()
        self.txt_timer_jit.setStyleSheet("color: #3fb950; font-weight: bold; font-size: 12px;")
        v_jit.addWidget(self.txt_timer_jit)
        r1.addLayout(v_jit, 1)
        layout.addLayout(r1)

        # Row 2: TSC Frequency
        v_tsc = QVBoxLayout()
        v_tsc.addWidget(QLabel("⚡ Time Stamp Counter (TSC) Frequency:"))
        self.txt_tsc = QLineEdit()
        v_tsc.addWidget(self.txt_tsc)
        layout.addLayout(v_tsc)

        layout.addStretch()
        return tab

    def _build_webgl_canvas_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        # WebGL
        v_gl = QVBoxLayout()
        v_gl.addWidget(QLabel("🎮 WebGL Unmasked GPU Vendor & Renderer:"))
        self.txt_gl = QLineEdit()
        self.txt_gl.setStyleSheet("color: #58a6ff; font-weight: bold;")
        v_gl.addWidget(self.txt_gl)
        layout.addLayout(v_gl)

        # Seeds
        r_seeds = QHBoxLayout()
        v_cseed = QVBoxLayout()
        v_cseed.addWidget(QLabel("🎨 Canvas Noise Seed:"))
        self.txt_canvas_seed = QLineEdit()
        v_cseed.addWidget(self.txt_canvas_seed)
        r_seeds.addLayout(v_cseed, 1)

        v_aseed = QVBoxLayout()
        v_aseed.addWidget(QLabel("🔊 Audio Noise Seed:"))
        self.txt_audio_seed = QLineEdit()
        v_aseed.addWidget(self.txt_audio_seed)
        r_seeds.addLayout(v_aseed, 1)
        layout.addLayout(r_seeds)

        # Sensors & GPS
        r_sens = QHBoxLayout()
        v_sseed = QVBoxLayout()
        v_sseed.addWidget(QLabel("🧭 Motion Sensor Seed:"))
        self.txt_sensor_seed = QLineEdit()
        v_sseed.addWidget(self.txt_sensor_seed)
        r_sens.addLayout(v_sseed, 1)

        v_gps = QVBoxLayout()
        v_gps.addWidget(QLabel("🛰️ Micro-GPS Offset:"))
        self.txt_gps_drift = QLineEdit()
        v_gps.addWidget(self.txt_gps_drift)
        r_sens.addLayout(v_gps, 1)
        layout.addLayout(r_sens)

        layout.addStretch()
        return tab

    def _build_js_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        hdr = QHBoxLayout()
        hdr.addWidget(QLabel("<b>📜 Client-Side JavaScript Injection Code:</b>"))
        hdr.addStretch()
        btn_copy = QPushButton("📋 Copy JS")
        btn_copy.clicked.connect(self._copy_js_script)
        hdr.addWidget(btn_copy)
        layout.addLayout(hdr)

        self.txt_js_code = QTextEdit()
        self.txt_js_code.setStyleSheet("font-family: monospace; font-size: 10px; background-color: #0d1117; color: #79c0ff;")
        self.txt_js_code.setReadOnly(True)
        layout.addWidget(self.txt_js_code, 1)

        return tab

    # ==============================================================
    # ACTIONS & DATA POPULATION
    # ==============================================================

    def _on_load_preset_clicked(self):
        pid = self.spn_model_id.value()
        prof = get_phone_profile(pid)
        self._populate_profile(prof)
        self.lbl_status.setText(f"📋 Loaded Preset #{pid:04d}: {prof['name']}")

    def generate_new_crore_profile(self):
        pid = self.spn_model_id.value()
        prof = generate_crore_fingerprint(base_seed=pid)
        self._populate_profile(prof)
        self.spn_model_id.setValue(prof["preset_id"])

        # Add to history
        self.history.insert(0, prof)
        self._refresh_history_table()
        self.lbl_status.setText(f"✅ Generated 1-in-Crores Unique Profile: {prof['name']} (UUID: {prof['hardware_uuid'][:8]}...)")

    def _populate_profile(self, p: Dict[str, Any]):
        self.current_profile = p

        # 1. Update Large Phone Frame Mockup
        self.lbl_phone_model_tag.setText(p.get("market_name", p.get("model", "Phone"))[:24])
        b_level = int(p.get("battery_level", 0.85) * 100)
        is_chg = p.get("battery_charging", False)
        chg_symbol = "⚡" if is_chg else "🔋"
        self.lbl_phone_indicators.setText(f"5G 📶 {chg_symbol} {b_level}%")

        # Set User Agent on webview profile
        try:
            profile = self.web_view.page().profile()
            profile.setHttpUserAgent(p.get("user_agent", ""))
        except Exception:
            pass

        # Load Large Phone Dashboard Screen
        self._load_phone_dashboard()

        # 2. Hardware Tab
        self.txt_name.setText(p.get("name", ""))
        self.txt_brand_model.setText(f"{p.get('brand')} • {p.get('model')}")
        self.txt_ua.setText(p.get("user_agent", ""))
        self.txt_uuid.setText(p.get("hardware_uuid", "N/A"))
        self.txt_build_id.setText(p.get("build_id", "N/A"))
        self.txt_screen.setText(f"{p.get('screen_width')} x {p.get('screen_height')} @ DPR {p.get('device_pixel_ratio')}")
        self.txt_cores.setText(f"{p.get('hardware_concurrency')} Cores / {p.get('device_memory')} GB RAM")
        self.txt_touch.setText(str(p.get("max_touch_points", 5)))

        # 3. Battery Tab
        self.bar_battery.setValue(b_level)
        self.slider_battery.blockSignals(True)
        self.slider_battery.setValue(b_level)
        self.slider_battery.blockSignals(False)

        self.chk_charging.blockSignals(True)
        self.chk_charging.setChecked(is_chg)
        self.chk_charging.blockSignals(False)

        self.lbl_charging_state.setText(f"{'⚡ State: Charging' if is_chg else '🔋 State: Discharging'} ({b_level}%)")
        self.lbl_battery_temp.setText(f"🌡️ Temp: {p.get('battery_temperature_c', 31.0)}°C ({p.get('battery_health', 'Good')})")
        self.txt_charging_time.setText(str(p.get("charging_time", "0")))
        self.txt_discharging_time.setText(str(p.get("discharging_time", "Infinity")))

        # 4. TCP Tab
        self.txt_tcp_mtu.setText(f"{p.get('tcp_mtu')} Bytes")
        self.txt_tcp_mss.setText(f"{p.get('tcp_mss')} Bytes")
        self.txt_tcp_ttl.setText(str(p.get("tcp_ttl", 64)))
        self.txt_tcp_win.setText(f"{p.get('tcp_window_size')} (Scaling: {p.get('tcp_window_scaling')})")
        self.txt_conn_type.setText(f"{p.get('connection_type')} ({p.get('effective_type')}) | {p.get('downlink')} Mbps, RTT: {p.get('rtt')}ms")
        self.txt_tcp_syn.setText(p.get("tcp_syn_packet_hex", "N/A"))

        # 5. Timer Tab
        self.txt_drift_ppm.setText(f"{p.get('clock_drift_ppm')} ppm")
        self.txt_timer_jit.setText(f"{p.get('timer_jitter_microsec')} µs")
        self.txt_tsc.setText(f"{p.get('tsc_frequency_ghz', 2.8)} GHz")

        # 6. WebGL & Canvas Tab
        self.txt_gl.setText(f"{p.get('gl_vendor')} - {p.get('gl_renderer')}")
        self.txt_canvas_seed.setText(str(p.get("canvas_noise_seed", 42)))
        self.txt_audio_seed.setText(str(p.get("audio_noise_seed", 101)))
        self.txt_sensor_seed.setText(str(p.get("sensor_noise_seed", 555)))
        self.txt_gps_drift.setText(f"Lat: {p.get('gps_lat_offset', 0.0):+.6f}, Lng: {p.get('gps_lng_offset', 0.0):+.6f}")

        # 7. JS Code Tab
        js_code = build_fingerprint_injection_script(p)
        self.txt_js_code.setPlainText(js_code)

    def _on_battery_slider_changed(self, val: int):
        self.current_profile["battery_level"] = round(val / 100.0, 2)
        self.bar_battery.setValue(val)
        is_chg = self.chk_charging.isChecked()
        chg_sym = "⚡" if is_chg else "🔋"
        self.lbl_charging_state.setText(f"{'⚡ State: Charging' if is_chg else '🔋 State: Discharging'} ({val}%)")
        self.lbl_phone_indicators.setText(f"5G 📶 {chg_sym} {val}%")
        self._load_phone_dashboard()

    def _on_charging_toggled(self, chg: bool):
        self.current_profile["battery_charging"] = chg
        self.current_profile["charging_time"] = 0 if chg else "Infinity"
        self.txt_charging_time.setText(str(self.current_profile["charging_time"]))
        val = self.bar_battery.value()
        chg_sym = "⚡" if chg else "🔋"
        self.lbl_charging_state.setText(f"{'⚡ State: Charging' if chg else '🔋 State: Discharging'} ({val}%)")
        self.lbl_phone_indicators.setText(f"5G 📶 {chg_sym} {val}%")
        self._load_phone_dashboard()

    def _refresh_history_table(self):
        self.table_history.setRowCount(len(self.history))
        for r, p in enumerate(self.history):
            self.table_history.setItem(r, 0, QTableWidgetItem(f"#{p.get('preset_id', 0):04d}"))
            self.table_history.setItem(r, 1, QTableWidgetItem(p.get("name", "")[:24]))
            self.table_history.setItem(r, 2, QTableWidgetItem(f"{int(p.get('battery_level', 0) * 100)}% ({'Chg' if p.get('battery_charging') else 'Dis'})"))
            self.table_history.setItem(r, 3, QTableWidgetItem(f"{p.get('tcp_mtu')} B"))
            self.table_history.setItem(r, 4, QTableWidgetItem(f"{p.get('clock_drift_ppm')} ppm"))
            self.table_history.setItem(r, 5, QTableWidgetItem(p.get("hardware_uuid", "")[:10] + "..."))

    def _on_history_double_clicked(self, row: int, col: int):
        if 0 <= row < len(self.history):
            prof = self.history[row]
            self._populate_profile(prof)
            self.spn_model_id.setValue(prof.get("preset_id", 1))
            self.lbl_status.setText(f"📋 Loaded from History: {prof['name']}")

    def _copy_js_script(self):
        code = self.txt_js_code.toPlainText()
        if code:
            QApplication.clipboard().setText(code)
            self.lbl_status.setText("📋 Copied full JavaScript Injection snippet to clipboard!")
            QMessageBox.information(self, "Copied", "Client-side JavaScript injection snippet copied to clipboard!")

    def _export_batch_dialog(self):
        path, _ = QFileDialog.getSaveFileName(self, "Export Batch Profiles", "phone_fingerprints.json", "JSON Files (*.json)")
        if path:
            try:
                batch = [generate_crore_fingerprint() for _ in range(500)]
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(batch, f, indent=2)
                QMessageBox.information(self, "Exported", f"Successfully exported 500 unique phone fingerprints to {path}!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to export: {e}")


def main():
    app = QApplication(sys.argv)
    win = FingerprintManagerWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
