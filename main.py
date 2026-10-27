
import os
import time
from collections import Counter

from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY missing. Check your .env file."
    )

client = genai.Client(api_key=api_key)
MODEL = "gemini-3.5-flash"


def generate_text(prompt):
    """Generate text using the Gemini API."""
    start_time = time.time()

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    elapsed = time.time() - start_time
    generated_text = response.text or ""

    return generated_text, elapsed


def analyze_text(text):
    """Calculate basic text-quality indicators."""
    words = text.split()
    sentences = [
        s for s in text.replace("!", ".").replace("?", ".").split(".")
        if s.strip()
    ]

    return {
        "characters": len(text),
        "words": len(words),
        "sentences": len(sentences),
        "unique_words": len(set(w.lower().strip(".,!?;:") for w in words)),
    }


def show_analysis(text, elapsed):
    stats = analyze_text(text)

    print("\n--- GENERATED TEXT ---")
    print(text)

    print("\n--- TEXT ANALYSIS ---")
    for name, value in stats.items():
        print(f"{name.replace('_', ' ').title()}: {value}")

    print(f"Response time: {elapsed:.2f} seconds")


def compare_outputs(text1, text2):
    """Compare two generated responses."""
    stats1 = analyze_text(text1)
    stats2 = analyze_text(text2)

    print("\n--- OUTPUT COMPARISON ---")
    print(f"{'Metric':<20}{'Output 1':>12}{'Output 2':>12}")
    print("-" * 44)

    for key in ["characters", "words", "sentences", "unique_words"]:
        label = key.replace("_", " ").title()
        print(f"{label:<20}{stats1[key]:>12}{stats2[key]:>12}")

    print("\nNote: More words do not necessarily mean better quality.")


def main():
    print("=" * 48)
    print(" AI-POWERED TEXT GENERATION AND ANALYSIS")
    print("=" * 48)

    prompt = input("\nEnter your prompt: ").strip()

    if not prompt:
        print("Please enter a valid prompt.")
        return

    try:
        print("\nGenerating first response...")
        text1, time1 = generate_text(prompt)
        show_analysis(text1, time1)

        choice = input(
            "\nGenerate a second response for comparison? (y/n): "
        ).strip().lower()

        if choice == "y":
            second_prompt = input(
                "Enter the second prompt: "
            ).strip()

            if not second_prompt:
                print("Second prompt is empty. Comparison skipped.")
                return

            print("\nGenerating second response...")
            text2, time2 = generate_text(second_prompt)
            show_analysis(text2, time2)
            compare_outputs(text1, text2)

    except Exception as error:
        print("\nAn error occurred.")
        print("Check your internet connection, API key,")
        print("model availability, and API quota.")
        print("Error details:", error)


if __name__ == "__main__":
    main()
