from pathlib import Path
from detect import detect_objects
from speech import speak


# Resolve project root safely
BASE_DIR = Path(__file__).resolve().parent.parent

# Correct image path
IMAGE_PATH = BASE_DIR / "data" / "sample_images" / "room.jpg"


def main():
    # Fail early if image is missing
    if not IMAGE_PATH.exists():
        raise FileNotFoundError(f"Image not found: {IMAGE_PATH}")

    detections = detect_objects(str(IMAGE_PATH))

    # Defensive check
    if detections is None or detections.empty:
        speak("No objects detected")
        return

    # Extract unique object names
    objects = detections["name"].unique()

    # Build natural sentence
    sentence = "I see " + ", ".join(objects)
    speak(sentence)


if __name__ == "__main__":
    main()
