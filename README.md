# MiniProject_Group12_T1_2025
Mini project for Algorithms and Data Structures 2025 by Group 12

## Overview
A simple Python program for managing course data using CSV files.  
Supports adding courses, undoing changes, and processing all records with priority sorting.

---

## Features
- Add course by `CourseCode`
- Undo last changes (up to 3 times)
- Process and display all courses
- Priority sorting (`Sec` before others)

# Most operations:
# Time Complexity = O(n)
# Reason: Full file read/write + linear search

# Undo stack:
# Push/Pop = O(1)
# But file rewrite dominates = O(n)
