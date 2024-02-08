import speech_recognition as sr
from googletrans import Translator, LANGUAGES

def recognize_speech_from_mic(recognizer, microphone):
    # Check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # Start listening
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say something or 'stop' to exit:")
        audio = recognizer.listen(source)

    # Recognize speech using Google Web Speech API
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # Speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def load_translations(file_path):
    translations = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            spanish_word, english_word = line.strip().split('->')
            translations[spanish_word.lower()] = english_word.lower()
    return translations

def main():

    custom_translations = load_translations("spanish_words.txt")

    translator = Translator()

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        response = recognize_speech_from_mic(recognizer, microphone)

        spanish_text = response["transcription"]
        if spanish_text:
            english_translation = custom_translations.get(spanish_text.lower(), None)
            if not english_translation:
                english_translation: translator.translate(spanish_text, src='es', dest='en').text

            print(f"Spanish: {spanish_text}")
            print(f"Translated to English: {english_translation}")
        
        english_text = response["transcription"]
        if english_text:
            print(f"English Lnagaue: {english_translation}")
        else:
            raise Exception("Does not translate")

        if not response["success"] or response["error"]:
            continue

        print("You said:", response["transcription"])

        # Check if the transcription contains 'stop' (case insensitive)
        if response["transcription"] and "stop" in response["transcription"].lower():
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
