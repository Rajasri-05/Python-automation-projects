from googletrans import Translator, LANGUAGES

# Create translator object
translator = Translator()

def translate_text(text, dest_language):
    """
    Translates text into the specified destination language
    """

    translated = translator.translate(text, dest=dest_language)

    print("\n--- Translation Result ---")
    print("Original Text:", text)
    print(f"Translated ({LANGUAGES[dest_language]}):", translated.text)


def main():
    print("🌍 LANGUAGE TRANSLATION TOOL 🌍\n")

    # User enters text
    text = input("Enter the text you want to translate: ")

    print("\nChoose the language to translate into:")
    print("en - English")
    print("fr - French")
    print("es - Spanish")
    print("hi - Hindi")
    print("ta - Tamil")
    print("te - Telugu")
    print("de - German")

    # User selects language
    dest_language = input("\nEnter language code: ").lower()

    # Check if language code is valid
    if dest_language not in LANGUAGES:
        print("❌ Invalid language code. Please try again.")
        return

    translate_text(text, dest_language)


if __name__ == "__main__":
    main()




