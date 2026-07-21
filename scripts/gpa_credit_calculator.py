#!/usr/bin/env python3
"""
GPA & Credit Transfer Calculator for Academic Planning

Models GPA recovery at Syracuse University and credit transfer limits for NYU/Columbia.
"""

def calculate_gpa(courses):
    total_points = 0.0
    total_credits = 0.0
    for name, grade_pt, credits in courses:
        total_points += grade_pt * credits
        total_credits += credits
    return total_points / total_credits if total_credits > 0 else 0.0

def main():
    print("=== ACADEMIC CREDIT & GPA MODELING TOOL ===")
    
    # Campus Inc Record
    campus_inc_courses = [
        ("Applied AI & Business Admin Core", 4.0, 80)
    ]
    campus_gpa = calculate_gpa(campus_inc_courses)
    print(f"Campus Inc GPA (80 Credits): {campus_gpa:.2f}")

    # Syracuse Initial Record (Before final non-withdrawn term)
    syracuse_initial = [
        ("Creative Writing & Rhetoric Core (As)", 4.0, 58),
        ("Electives (Bs)", 3.0, 12),
    ]
    syracuse_init_gpa = calculate_gpa(syracuse_initial)
    print(f"Syracuse Initial GPA (70 Credits): {syracuse_init_gpa:.2f}")

    # Syracuse Non-Withdrawn Term Impact (3 Fs at 3 credits each)
    syracuse_with_fs = syracuse_initial + [
        ("Non-withdrawn F 1", 0.0, 3),
        ("Non-withdrawn F 2", 0.0, 3),
        ("Non-withdrawn F 3", 0.0, 3),
        ("Non-withdrawn F 4", 0.0, 3),
    ]
    syracuse_f_gpa = calculate_gpa(syracuse_with_fs)
    print(f"Syracuse Current Un-withdrawn GPA: {syracuse_f_gpa:.2f}")

    # Syracuse Post Grade Forgiveness / Retake Model
    syracuse_recovered = syracuse_initial + [
        ("Retaken Course 1", 4.0, 3),
        ("Retaken Course 2", 4.0, 3),
        ("Retaken Course 3", 4.0, 3),
        ("Retaken Course 4", 4.0, 3),
    ]
    syracuse_rec_gpa = calculate_gpa(syracuse_recovered)
    print(f"Syracuse Recovered GPA after Re-entry Retakes: {syracuse_rec_gpa:.2f}")

    print("\n--- TRANSFER SUMMARY & STRATEGY ---")
    print("1. NYU/Columbia Transfer Base: Use Campus Inc 80 Credits (4.0 GPA).")
    print("2. Syracuse Re-entry Vector: Re-enroll -> Petition Fs -> Restore GPA to 3.83.")
    print("3. Maximum Transfer Cap: 60-90 credits accepted by top institutions.")

if __name__ == "__main__":
    main()
