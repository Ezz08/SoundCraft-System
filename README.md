# 🎸 Music Instruments OOP System

A simple Object-Oriented Programming project in Python that simulates a music instruments management system. It demonstrates key OOP concepts like inheritance, abstraction, polymorphism, and class-level data management.

## 📌 Project Idea

This project models different musical instruments such as:
- Guitar 🎸
- Piano 🎹
- Drums 🥁
- Violin 🎻
- Flute 🎶

Each instrument has:
- Name
- Brand
- Price
- Specific attributes (like strings, keys, etc.)

The system allows you to:
- Add instruments
- Display all instruments
- Play instruments
- Repair & clean instruments
- Show material type
- Track total number of instruments

## 🧠 OOP Concepts Used

### 1. Abstraction
- `Instrument` is an abstract base class
- Forces all instruments to implement:
  - `play()`
  - `get_material()`
  - `repair()`
  - `clean()`

### 2. Inheritance
All instruments inherit from `Instrument`:
- Guitar
- Piano
- Drums
- Violin
- Flute

### 3. Polymorphism
Each instrument implements `play()` differently:
```python
inst.play()

4. Class Variables

Tracks total number of instruments:

Instrument.num_of_instruments

Stores all created instruments:

Instrument.instrument
🏗️ Project Structure

Instrument (Abstract Base Class)
│
├── Guitar
├── Piano
├── Drums
├── Violin
└── Flute

⚙️ Features

➕ Add Instrument
Add instruments to the system using:

add_instrument.add_instrument()

📋 Show All Instruments

show_all().show_all()

🎵 Play Instruments

for inst in Instrument.instrument:
    inst.play()

🔧 Repair & Clean

for inst in Instrument.instrument:
    inst.repair()
    inst.clean()

🧱 Show Material

inst.get_material()

📊 Total Instruments

Instrument.num_of_instruments
▶️ Example Output
== adding instruments to the system ==

Guitar added to the system.
Piano added to the system.
Drums added to the system.
Violin added to the system.
Flute added to the system.

== showing all instruments in the system ==

Name: Guitar, Brand: Yamaha, Price: $1000
Name: Piano, Brand: Casio, Price: $5000
...

== playing all instruments ==

Playing the Guitar with 6 strings.
Playing the Piano with 88 keys.
...

== repairing and cleaning all instruments ==

Repairing the Guitar.
Cleaning the Guitar.
...

== total number of instruments in the system ==

Total instruments: 5
🚀 How to Run

Install Python 3
Run the script:

python main.py
🎯 Learning Goals

This project helps you understand:

Object-Oriented Design in Python
Abstract Classes & Methods
Inheritance hierarchy
Polymorphism in real scenarios
Basic system design thinking
💡 Future Improvements
Add search by brand
Add delete instrument feature
Add file saving/loading (JSON)
Build a menu-driven interface
Add GUI version (Tkinter)
👨‍💻 Author
 Ezz Fawzy
Built as an OOP practice project for learning Python design principles.