import serial
import rtmidi
import time
import threading

MIDI_PORT = 0
SERIAL_PORT = "/dev/ttyUSB0"

class DrumNotes:
	C2 = [rtmidi.MidiMessage.noteOn(0x80, 36, 112), rtmidi.MidiMessage.noteOff(0x80, 36)]
	A2SHARP = [rtmidi.MidiMessage.noteOn(0x80, 46, 112), rtmidi.MidiMessage.noteOff(0x80, 46)]
	D2 = [rtmidi.MidiMessage.noteOn(0x80, 38, 112), rtmidi.MidiMessage.noteOff(0x80, 38)]
	F2SHARP = [rtmidi.MidiMessage.noteOn(0x80, 42, 112), rtmidi.MidiMessage.noteOff(0x80, 42)]
	G3 = [rtmidi.MidiMessage.noteOn(0x80, 55, 112), rtmidi.MidiMessage.noteOff(0x80, 55)]


NOTE_MAPPING = {
	b"1": DrumNotes.C2,
	b"2": DrumNotes.A2SHARP,
	b"3": DrumNotes.D2,
	b"4": DrumNotes.F2SHARP,
	b"5": DrumNotes.G3,
}

midiout = rtmidi.RtMidiOut()
midiout.openPort(MIDI_PORT)

ser = serial.Serial(SERIAL_PORT)

def press_note(notes):
	midiout.sendMessage(notes[0])
	time.sleep(0.3)
	midiout.sendMessage(notes[1])

def main():
	try:
		while True:
			pressed = ser.read()
			threading.Thread(target=press_note, args=(NOTE_MAPPING[pressed],)).start()
	except KeyboardInterrupt:
		ser.close()
		midiout.closePort()
		exit(0)

if __name__ == "__main__":
	main()