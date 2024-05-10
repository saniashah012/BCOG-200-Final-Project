import random
import pronouncing
from PIL import Image, ImageDraw, ImageFont

# Function to find rhyming words for a given word
def find_rhymes(word):
    rhymes = pronouncing.rhymes(word)
    return rhymes

# Function to generate a random rap song
def generate_rap_song():
    # Generate a random word
    random_word = random.choice(pronouncing.cmudict.words())

    # Find rhyming words for the random word
    rhyming_words = find_rhymes(random_word)

    # If no rhyming words found, return None
    if not rhyming_words:
        return None

    # Choose a random rhyming word
    chosen_rhyme = random.choice(rhyming_words)

    # Generate the rap song
    rap_song = f"{random_word.capitalize()} {chosen_rhyme}\n"

    # Add more lines to the rap song
    num_lines = random.randint(4, 8)
    for _ in range(num_lines):
        line = generate_line(chosen_rhyme)
        rap_song += line + "\n"

    return rap_song

def create_meme(text):
    # Load meme template image
    meme_template = Image.open("meme_template.jpg")  # Replace with your meme template image path

    # Create a drawing context
    draw = ImageDraw.Draw(meme_template)

    # Define text position
    text_position = (120, 50)

    lines = text.split("\n")
    text_with_newlines = "\n".join([line + "\n" for line in lines])

    # Add text to the image
    draw.multiline_text(text_position, text_with_newlines, fill="black")


    # Add text to the image
    draw.text(text_position, text, fill="black")

    # Save the meme image
    meme_template.save("rap_meme.jpg")



# Function to generate a line for the rap song
def generate_line(chosen_rhyme):
    # Generate a random word
    random_word = random.choice(pronouncing.cmudict.words())

    # Find rhyming words for the random word
    rhyming_words = find_rhymes(random_word)

    # If no rhyming words found, use the chosen rhyme as a fallback
    if not rhyming_words:
        return f"{random_word.capitalize()} {chosen_rhyme}"

    # Choose a random rhyming word
    chosen_rhyme = random.choice(rhyming_words)

    return f"{random_word.capitalize()} {chosen_rhyme}"

# Generate and print a random rap song
random_rap_song = generate_rap_song()
if random_rap_song:
    print("Random Rap Song:")
    print(random_rap_song)

    create_meme(random_rap_song)
    print("Meme created successfully!")

else:
    print("Sorry, couldn't generate a rap song.")