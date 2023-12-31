import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by rizwan ")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    while True:
        text_to_speak = input("Enter what you want me to speak (enter 'q' to quit): ")
        if text_to_speak.lower() == "q":
            break

        # Set the text to be spoken
        engine.say(text_to_speak)

        # Wait for the speech to finish
        engine.runAndWait()

    # Cleanup the engine
    engine.stop()
    engine.quit()

