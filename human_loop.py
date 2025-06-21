# === human_loop.py ===
def human_feedback(text):
    print("\n==== AI Generated Text ====")
    print(text)
    edited = input("\nMake edits or press Enter to approve as-is:\n")
    return edited if edited else text