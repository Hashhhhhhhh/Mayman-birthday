from flask import Flask, render_template
import pennylane as qml
import random

app = Flask(__name__)

dev = qml.device('default.qubit', wires=1, shots=1) 
# List of birthday wish phrases
birthday_wishes = [
    "Wishing you a day filled with love and joy!",
    "May your birthday be as special as you are!",
    "Here's to another year of wonderful you!",
    "May your dreams take flight this year!",
    "Celebrate your day with laughter and joy!",
    "Wishing you a fantastic year ahead!",
    "You are a star! Shine on your birthday!",
    "Have a magical birthday filled with all your favorite things!",
    "O tanjoubi omedetou gozaimasu!",
    "Tanjoubi omedetou!",
    "Happii baasudee!",
    "Shēngrì kuàilè!",
    "Herzlichen Glückwunsch zum Geburtstag!",
    "Alles Gute zum Geburtstag!",
    "All das Beste zum Geburtstag!",
    "Viel Glück zum Geburtstag!",
    "Feliz Cumpleaños!",
    "Gëzuar ditëlindjen!",
    "Sretan rođendan!",
    "Chestit Rozhden den!",
    "Per molts anys!",
    "Všechno nejlepší k narozeninám!",
    "Tillykke med fødselsdagen!",
    "Fijne verjaardag!",
    "Joyeux anniversaire!",
    "Saengil chukahaeyo or Saengil chukahamnida!",
    "With dreams that soar high and laughter that stays! May your year ahead be filled with delight, Happy birthday to you, shine ever so bright!",
    "May your circuits always be powered, your sensors forever sensitive, and your code bug-free! Here’s to another year of building the future, one robot at a time!",
    "On your special day, may you find the perfect balance between coding and celebrating! Here’s to you, the visionary creator, whose robotic creations inspire us all. Happy Birthday!",
    "Happy Birthday! May your day be filled with as much joy as a particle in motion and as bright as the light from a supernova!",
    "May your year be filled with endless possibilities and discoveries as you continue to defy gravity and push the boundaries of science!",
    "Smile. Laugh. Smile. Laugh. Smileeeeeeeeeeeee!",
    "Wishing you a birthday that’s as stellar as the universe—full of energy, light, and cosmic adventures!",
    "May your birthday be as bright as the speed of light and as unforgettable as a supernova—here's to an explosive year ahead!",
    "Happy Birthday! Just like an electron, may you always find your way to the most exciting orbits this year!",
]

# Quantum random number generator function
@qml.qnode(dev)
def qrng():
    qml.Hadamard(wires=0)  # Superposition
    return qml.sample(qml.PauliZ(0))  # Measure

# Generate a random birthday wish
def generate_birthday_wish():
    # Get quantum random number
    rand_bit = qrng()
    rand_bit = rand_bit.item()  # Access the value of the 0-dimensional array
    wish = random.choice(birthday_wishes)
    return wish  # No reversal needed here

@app.route('/')
def home():
    wish = generate_birthday_wish()
    return render_template('index.html', wish=wish)

if __name__ == '__main__':
    app.run(debug=True)
