# Define the notes in an octave
NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Chord formulas in semitones (intervals)
CHORDS = {
    'major': [0, 4, 7],
    'minor': [0, 3, 7],
    'diminished': [0, 3, 6]
}

def find_chord_notes(root, chord_type):
    if root not in NOTES:
        return f"Invalid root note: {root}. Please use standard notes like A, B, C, D#, F, you get the picture."
    if chord_type not in CHORDS:
        return f"Invalid chord type: {chord_type}. Choose from major, minor, diminished."

    root_index = NOTES.index(root)
    intervals = CHORDS[chord_type]
    chord_notes = [NOTES[(root_index + i) % len(NOTES)] for i in intervals]
    return chord_notes

def main():
    print("🎶 Music Chord Finder 🎶")
    root = input("Enter root note (example: A, B,  C, D#, F): ").strip().upper()
    chord_type = input("Enter chord type (major, minor, diminished): ").strip().lower()

    result = find_chord_notes(root, chord_type)
    if isinstance(result, list):
        print(f"\nNotes in the {root} {chord_type} chord: {', '.join(result)}")
    else:
        print(result)

if __name__ == "__main__":
    main()
