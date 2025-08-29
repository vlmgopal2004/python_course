import os
import re

# Define positive and negative word lists for movie reviews
POSITIVE_WORDS = {
    "amazing", "awesome", "brilliant", "captivating", "delightful",
    "enjoyable", "excellent", "fantastic", "fascinating", "good",
    "great", "impressive", "inspiring", "legendary", "lovable",
    "masterful", "mind-blowing", "outstanding", "powerful", "remarkable",
    "spectacular", "stunning", "superb", "thrilling", "unforgettable", "wonderful"
}

NEGATIVE_WORDS = {
    "awful", "bad", "boring", "confusing", "disappointing", "dull",
    "exaggerated", "flat", "forgettable", "horrible", "lame",
    "mediocre", "messy", "overhyped", "pathetic", "predictable",
    "ridiculous", "slow", "terrible", "trash", "unconvincing", "weak", "worst"
}

# Directory where movie reviews are stored
moviereviews_dir = "Assignments/movie_notes_management/moviereviews"
print("Looking for reviews in:", os.path.abspath(moviereviews_dir))

# Ensure the directory exists
os.makedirs(moviereviews_dir, exist_ok=True)

def sanitize_filename(filename):
    """Clean filename: strip spaces and ensure .txt extension."""
    filename = filename.strip()
    if not filename.endswith(".txt"):
        filename += ".txt"
    return filename

def analyze_sentiment(content):
    """Analyze review content and determine if it has a positive or negative vibe."""
    positive_count = len(re.findall(r'\b(?:' + '|'.join(POSITIVE_WORDS) + r')\b', content, re.IGNORECASE))
    negative_count = len(re.findall(r'\b(?:' + '|'.join(NEGATIVE_WORDS) + r')\b', content, re.IGNORECASE))

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"

def read_and_analyze_note():
    """Read and analyze a specific review or all reviews."""
    choice = input("Do you want to analyze:\n1. A specific review\n2. All reviews\nEnter your choice: ").strip()

    if choice == "1":
        filename = input("Enter the file name: ")
        filename = sanitize_filename(filename)
        file_path = os.path.join(moviereviews_dir, filename)

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                sentiment = analyze_sentiment(content)
                print(f"\nAnalyzing file: {filename}\nDetected Sentiment: {sentiment}\n")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found in {moviereviews_dir}.")
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "2":
        sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
        files = os.listdir(moviereviews_dir)

        if not files:
            print("No reviews found.")
            return

        for filename in files:
            file_path = os.path.join(moviereviews_dir, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                sentiment = analyze_sentiment(content)
                sentiment_counts[sentiment] += 1

        print("\nOverall Sentiment Analysis:")
        for sentiment, count in sentiment_counts.items():
            print(f"{sentiment}: {count} reviews")

def create_note():
    """Create a new review note."""
    filename = input("Enter the name of the new review: ")
    filename = sanitize_filename(filename)
    file_path = os.path.join(moviereviews_dir, filename)

    content = input("Enter your review content:\n")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Review '{filename}' saved successfully.")

def modify_note():
    """Modify an existing review note."""
    files = os.listdir(moviereviews_dir)
    if not files:
        print("No reviews available to modify.")
        return

    print("Existing reviews:", ", ".join(files))
    filename = input("Enter the file name to modify: ")
    filename = sanitize_filename(filename)
    file_path = os.path.join(moviereviews_dir, filename)

    if not os.path.exists(file_path):
        print(f"Error: File '{filename}' not found in {moviereviews_dir}.")
        return

    new_content = input("Enter new content:\n")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_content)

    print(f"Review '{filename}' updated successfully.")

def main():
    """Main function to run the Movie Review Notes Management System."""
    while True:
        print("\n🎬 Intelligent Movie Review Notes Management System")
        print("1. Read & Analyze Reviews")
        print("2. Create a New Review")
        print("3. Modify an Existing Review")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            read_and_analyze_note()
        elif choice == "2":
            create_note()
        elif choice == "3":
            modify_note()
        elif choice == "4":
            print("Exiting program. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
