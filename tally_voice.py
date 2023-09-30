import speech_recognition as sr

def tally_counter():
    # Initialize counters
    yes_counter = 0
    no_counter = 0

    # Create a recognizer object
    r = sr.Recognizer()

    print("Calibrating background noise...")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

    while True:
        # Use the microphone as the audio source
        with sr.Microphone() as source:
            print("Commands: [(si, ok, yes) | no | riavvia | stop]. Listening... ")
            audio = r.listen(source)

        try:
            # Use Google Speech Recognition to convert speech to text
            text = r.recognize_google(audio, language="it-IT")
            print("You said:", text)

            # Commands close in time are recognized in a single sentence
            commands = text.split()

            for command in commands:
                match command.lower():
                    case "sì" | "si" | "yes" | "ok":
                        yes_counter += 1
                    case "no":
                        no_counter += 1

            match text.lower():
                case "riavvia":
                    yes_counter = 0
                    no_counter = 0
                case "stop":
                    print_status(yes_counter, no_counter)
                    return
                
            print_status(yes_counter, no_counter)

        except sr.UnknownValueError:
            print("Sorry, I could not understand your speech.")
        except sr.RequestError as e:
            print("Sorry, an error occurred. {0}".format(e))

def print_status(yes_counter, no_counter):

    if yes_counter == 0 and no_counter == 0:
        print("SI: 0, NO: 0, Success rate: --%\n")
    else:
        total = yes_counter + no_counter
        percentage = (yes_counter / total) * 100
        print("SI:", yes_counter, "NO:", no_counter, "Success rate:", str(round(percentage, 2)) + "%\n")


if __name__ == "__main__":
    tally_counter()