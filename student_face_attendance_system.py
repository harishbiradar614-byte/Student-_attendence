# ==============================================================================
# Institution: Sharnbasava University, Kalaburagi
# Faculty of Engineering & Technology | Department of Computer Science & Engineering
#
# Project Title: Smart Student Attendance System by Face Scanning
# Description: Automated Biometric Facial Recognition Attendance System
#
# Team Members:
#   - Harish Biradar (USN: SG25CSE050)
#   - Kartik V       (USN: SG25CSE057)
#   - Adarsh R Patil (USN: SG25CSE007)
#   - Akash S Patil  (USN: SG25CSE016)
# ==============================================================================

import os
import sys
import sqlite3
import csv
from datetime import datetime

DB_FILE = os.environ.get("ATTENDANCE_DB_FILE", "/tmp/student_attendance_v3.db")

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS students (
            usn TEXT PRIMARY KEY,
            name TEXT,
            semester INTEGER,
            section TEXT,
            department TEXT,
            registered_at TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS attendance_records (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            period_id TEXT,
            usn TEXT,
            status TEXT,
            scan_time TEXT,
            confidence_score REAL
        )
    """)
    conn.commit()
    conn.close()

def print_banner():
    print("=" * 80)
    print("  SHARNBASAVA UNIVERSITY, KALABURAGI")
    print("  Faculty of Engineering & Technology | Department of Computer Science & Engg.")
    print("  PROJECT: SMART STUDENT ATTENDANCE SYSTEM BY FACE SCANNING")
    print("  Team Members:")
    print("    - Harish Biradar (USN: SG25CSE050)")
    print("    - Kartik V       (USN: SG25CSE057)")
    print("    - Adarsh R Patil (USN: SG25CSE007)")
    print("    - Akash S Patil  (USN: SG25CSE016)")
    print("=" * 80)

def main():
    init_db()
    print_banner()
    print("\nBackend initialized.")
    print("Serve web application with: python3 -m http.server 8080")

if __name__ == "__main__":
    main()
