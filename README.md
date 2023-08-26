# Voice Tally Counter
A tally counter written in Python and operated through voice.

Install dependencies:
```
python -m pip install pyaudio
pip install SpeechRecognition
```

To run:
`python tally_voice.py`

Currently voice is set to recognize Italian speech, available commands are:
- si / yes
- no
- riavvia (reset)
- stop