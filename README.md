# Smart Student Attendance System by Face Scanning

**Major Academic Project | Academic Year 2025–2026**  
**Institution:** Sharnbasava University, Kalaburagi, Karnataka, India  
**Faculty:** Faculty of Engineering & Technology  
**Department:** Department of Computer Science & Engineering  

## 👥 Project Team Members
- **Harish Biradar** (USN: SG25CSE050) — Team Member • Core Algorithmic Lead
- **Kartik V** (USN: SG25CSE057) — Team Member • Biometric Slicing & DB Lead
- **Adarsh R Patil** (USN: SG25CSE007) — Team Member • UI/UX & Live Scanner Architect
- **Akash S Patil** (USN: SG25CSE016) — Team Member • Security, Testing & Anti-Proxy QA

---

## 🌟 Comprehensive Features

1. **Non-Sticky Title Banner**:
   - The official Sharnbasava University rectangular banner moves naturally with page scroll rather than being fixed.

2. **Sequential Periods & Breaks (No Countdown Clocks)**:
   - Tracks **Period 1**, **Period 2**, **☕ Short Break (15 mins)**, **Period 3**, **🍱 Lunch Break (1 Hour)**, **Period 4**, **Period 5**, plus **Custom Extra Periods**.
   - **Click on Any Period** in the period bar to immediately inspect its Present/Absent attendance list!
   - Advancing periods automatically updates the subject and assigned faculty name.

3. **Curved-Edge Settings Modal (⚙️)**:
   - **Attendance History**: View past attendance sessions archived across periods and dates.
   - **Student Directory & Management**: View enrolled students, add faces, or delete.
   - **Add Extra Period**: Create extra lab sessions or periods with custom subjects and faculty.
   - **Period & Faculty Settings**: Modify faculty names and subjects.
   - **Face Scanner Options**: Adjust recognition sensitivity and audio feedback.
   - **Start New Attendance Session**: Archive current records and start fresh.

4. **Camera Activation State**:
   - Scanner is **inactive** when camera is OFF.
   - Scanner activates only when camera is **ON**.
   - Includes **🔄 Flip Camera** button for switching between front and back camera on mobile phones and tablets.

5. **Empty Initial Student Roster & Live Camera Face Capture**:
   - Database starts with **zero students**.
   - Click **➕ Add Student**: Uses the live camera to capture a face snapshot and save biometrics. No file/image picker needed.

6. **Strict Biometric Recognition & Anti-Proxy Duplicate Prevention**:
   - **Non-Enrolled Face**: Triggers `❌ FACE NOT SAVED IN DATABASE!`.
   - **Enrolled Face (First Scan)**: Marks `✅ VERIFIED PRESENT` with timestamp and chime.
   - **Same Face Scanned Again**: Triggers `⚠️ FACE ALREADY SCANNED!` and rejects duplicate.

7. **Student Profile Modal (Curved-Edge)**:
   - Clicking on any student in the directory or report opens their curved-edge profile card with photo, attendance percentage, classes attended/missed, and exam eligibility status.

8. **Present/Absent Toggles**:
   - Ability to toggle absent students to Present (or present students to Absent) with one click.
