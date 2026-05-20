# ================================
# HAND GESTURE CONTROL SYSTEM
# Main Backend File
# ================================

def main():
    print("================================")
    print(" Hand Gesture Control System ")
    print(" Starting Application... ")
    print("================================")

    try:
        # Import UI module
        import ui

        print("UI module loaded successfully!")

        # If ui has a start function, call it
        if hasattr(ui, "start_ui"):
            ui.start_ui()
        else:
            print("UI imported. Running default execution...")

    except Exception as e:
        print("Error while starting application:")
        print(e)


# Run program
if __name__ == "__main__":
    main()