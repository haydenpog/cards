import os
import random
from tkinter import *
from PIL import Image, ImageTk

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]


def createcards():
    deck = []
    for card in values:
        for card2 in suits:
            deck.append(str(card) + " of " + card2)
    return deck

def randomhand(n):
    deck = createcards()
    hand = []
    i = 0
    while i < n:
        card = deck[random.randint(0, len(deck))]
        if card not in hand:
            hand.append(card)
        i+=1
    return hand

def images(hand):
    items = os.listdir(os.path.dirname(__file__) + "\cards")
    clubs = []
    diamonds = []
    spades = []
    hearts = []
    end = []
    for item in items:
        if "k" in item[:1]:
            #clubs
            clubs.append(item)
        if "l" in item[:1]:
            #diamonds
            diamonds.append(item)
        if "p" in item[:1]:
            #spades
            spades.append(item)
        if "s" in item[:1]:
            #hearts
            hearts.append(item)
    for card in hand:
        if "of Clubs" in card:
            #clubs
            card = card.replace(" of Clubs","")
            if card.isdigit():
                end.append("k"+card)
            if "King" in card:
                end.append("kk")
            if "Queen" in card:
                end.append("kq")
            if "Jack" in card:
                end.append("kj")
            if "Ace" in card:
                end.append("ka")
        if "of Diamonds" in card:
            #diamonds
            card = card.replace(" of Diamonds", "")
            if card.isdigit():
                end.append("l" + card)
            if "King" in card:
                end.append("lk")
            if "Queen" in card:
                end.append("lq")
            if "Jack" in card:
                end.append("lj")
            if "Ace" in card:
                end.append("la")
        if "of Spades" in card:
            #spades
            card = card.replace(" of Spades", "")
            if card.isdigit():
                end.append("p" + card)
            if "King" in card:
                end.append("pk")
            if "Queen" in card:
                end.append("pq")
            if "Jack" in card:
                end.append("pj")
            if "Ace" in card:
                end.append("pa")
        if "of Hearts" in card:
            #hearts
            card = card.replace(" of Hearts", "")
            if card.isdigit():
                end.append("s" + card)
            if "King" in card:
                end.append("sk")
            if "Queen" in card:
                end.append("sq")
            if "Jack" in card:
                end.append("sj")
            if "Ace" in card:
                end.append("sa")
    print(end)
    return end

def render(images: list):

    # Create an instance of tkinter frame
    win = Tk()

    # Set the geometry of tkinter frame
    win.geometry("750x270")

    # Create a canvas
    canvas = Canvas(win, width=224*len(images), height=400)
    canvas.pack()

    # Load an image in the script
    img = ImageTk.PhotoImage(Image.open(os.path.dirname(__file__) + "\cards\\" + images[1] + ".png"))

    # Add image to the Canvas Items
    canvas.create_image(0, 0, anchor=NW, image=img)

    win.mainloop()
render(images(randomhand(8)))
