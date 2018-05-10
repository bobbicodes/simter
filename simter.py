#!/usr/bin/python2.7

#pasting contents of tkinter simterface
import Tkinter as tk

#load dictionary file
import pprint, pickle
pkl_file = open('needed.pkl', 'rb')
needed = pickle.load(pkl_file)
pkl_file.close()

button_flag = True
def click():
    """
    respond to the button click
    """
    global button_flag

def click01():
    global button_flag
    if 'nails' in needed:
        needed["nails"] += 1
    else:
        needed["nails"] = 1
    pprint.pprint(needed)

def click02():
    global button_flag
    if 'boards' in needed:
        needed["boards"] += 1
    else:
        needed["boards"] = 1
    pprint.pprint(needed)

def click03():
    global button_flag
    if 'bricks' in needed:
        needed["bricks"] += 1
    else:
        needed["bricks"] = 1
    pprint.pprint(needed)

def click04():
    global button_flag
    if 'gum' in needed:
        needed["gum"] += 1
    else:
        needed["gum"] = 1
    pprint.pprint(needed)
def click05():
    global button_flag
    if 'glue' in needed:
        needed["glue"] += 1
    else:
        needed["glue"] = 1
    pprint.pprint(needed)
def click06():
    global button_flag
    if 'paint' in needed:
        needed["paint"] += 1
    else:
        needed["paint"] = 1
    pprint.pprint(needed)
def click07():
    global button_flag
    if 'hammers' in needed:
        needed["hammers"] += 1
    else:
        needed["hammers"] = 1
    pprint.pprint(needed)
def click08():
    global button_flag
    if 'tapes' in needed:
        needed["tapes"] += 1
    else:
        needed["tapes"] = 1
    pprint.pprint(needed)
def click09():
    global button_flag
    if 'shovels' in needed:
        needed["shovels"] += 1
    else:
        needed["shovels"] = 1
    pprint.pprint(needed)
def click10():
    global button_flag
    if 'spatulas' in needed:
        needed["spatulas"] += 1
    else:
        needed["spatulas"] = 1
    pprint.pprint(needed)
def click11():
    global button_flag
    if 'ladders' in needed:
        needed["ladders"] += 1
    else:
        needed["ladders"] = 1
    if 'boards' in needed:
        needed["boards"] += 2
    else:
        needed["boards"] = 2
    pprint.pprint(needed)
def click12():
    global button_flag
    if 'drills' in needed:
        needed["drills"] += 1
    else:
        needed["drills"] = 1
    pprint.pprint(needed)
def click13():
    global button_flag
    if 'veggies' in needed:
        needed["veggies"] += 1
    else:
        needed["veggies"] = 1
    pprint.pprint(needed)
def click14():
    global button_flag
    if 'sacks' in needed:
        needed["sacks"] += 1
    else:
        needed["sacks"] = 1
    pprint.pprint(needed)
def click15():
    global button_flag
    if 'melons' in needed:
        needed["melons"] += 1
    else:
        needed["melons"] = 1
    if 'sprouts' in needed:
        needed["sprouts"] += 1
    else:
        needed["sprouts"] = 1
    if 'shovels' in needed:
        needed["shovels"] += 1
    else:
        needed["shovels"] = 1
    pprint.pprint(needed)
def click16():
    global button_flag
    if 'cream' in needed:
        needed["cream"] += 1
    else:
        needed["cream"] = 1
    pprint.pprint(needed)
def click17():
    global button_flag
    if 'corn' in needed:
        needed["corn"] += 1
    else:
        needed["corn"] = 1
    pprint.pprint(needed)
def click18():
    global button_flag
    if 'cheese' in needed:
        needed["cheese"] += 1
    else:
        needed["cheese"] = 1
    pprint.pprint(needed)
def click19():
    global button_flag
    if 'meat' in needed:
        needed["meat"] += 1
    else:
        needed["meat"] = 1
    pprint.pprint(needed)
def click20():
    global button_flag
    if 'chairs' in needed:
        needed["chairs"] += 1
    else:
        needed["chairs"] = 1
    if 'hammers' in needed:
        needed["hammers"] += 1
    else:
        needed["hammers"] = 1
    if 'nails' in needed:
        needed["nails"] += 1
    else:
        needed["nails"] = 1
    pprint.pprint(needed)
def click21():
    global button_flag
    if 'tables' in needed:
        needed["tables"] += 1
    else:
        needed["tables"] = 1
    if 'hammers' in needed:
        needed["hammers"] += 1
    else:
        needed["hammers"] = 1
    if 'nails' in needed:
        needed["nails"] += 2
    else:
        needed["nails"] = 2
    if 'boards' in needed:
        needed["boards"] += 1
    else:
        needed["boards"] = 1
    pprint.pprint(needed)
def click22():
    global button_flag
    if 'towels' in needed:
        needed["towels"] += 1
    else:
        needed["towels"] = 1
    if 'tapes' in needed:
        needed["tapes"] += 1
    else:
        needed["tapes"] = 1
    pprint.pprint(needed)
def click23():
    global button_flag
    if 'cabs' in needed:
        needed["cabs"] += 1
    else:
        needed["cabs"] = 1
    if 'paint' in needed:
        needed["paint"] += 1
    else:
        needed["paint"] = 1
    if 'boards' in needed:
        needed["boards"] += 2
    else:
        needed["boards"] = 2
    pprint.pprint(needed)
def click24():
    global button_flag
    if 'couches' in needed:
        needed["couches"] += 1
    else:
        needed["couches"] = 1
    if 'drills' in needed:
        needed["drills"] += 1
    else:
        needed["drills"] = 1
    if 'glue' in needed:
        needed["glue"] += 1
    else:
        needed["glue"] = 1
    pprint.pprint(needed)
def click25():
    global button_flag
    if 'grass' in needed:
        needed["grass"] += 1
    else:
        needed["grass"] = 1
    if 'shovels' in needed:
        needed["shovels"] += 1
    else:
        needed["shovels"] = 1
    pprint.pprint(needed)
def click26():
    global button_flag
    if 'sprouts' in needed:
        needed["sprouts"] += 1
    else:
        needed["sprouts"] = 1
    if 'shovels' in needed:
        needed["shovels"] += 1
    else:
        needed["shovels"] = 1
    pprint.pprint(needed)
def click27():
    global button_flag
    if 'stch' in needed:
        needed["stch"] += 1
    else:
        needed["stch"] = 1
    if 'boards' in needed:
        needed["boards"] += 1
    else:
        needed["boards"] = 1
    pprint.pprint(needed)
def click28():
    global button_flag
    if 'fires' in needed:
        needed["fires"] += 1
    else:
        needed["fires"] = 1
    if 'gum' in needed:
        needed["gum"] += 2
    else:
        needed["gum"] = 2
    if 'bricks' in needed:
        needed["bricks"] += 2
    else:
        needed["bricks"] = 2
    if 'shovels' in needed:
        needed["shovels"] += 1
    else:
        needed["shovels"] = 1
    pprint.pprint(needed)
def click29():
    global button_flag
    if 'mowers' in needed:
        needed["mowers"] += 1
    else:
        needed["mowers"] = 1
    if 'paint' in needed:
        needed["paint"] += 1
    else:
        needed["paint"] = 1
    pprint.pprint(needed)
def click30():
    global button_flag
    if 'gnomes' in needed:
        needed["gnomes"] += 1
    else:
        needed["gnomes"] = 1
    if 'gum' in needed:
        needed["gum"] += 2
    else:
        needed["gum"] = 2
    if 'glue' in needed:
        needed["glue"] += 1
    else:
        needed["glue"] = 1
    pprint.pprint(needed)
def click31():
    global button_flag
    if 'donuts' in needed:
        needed["donuts"] += 1
    else:
        needed["donuts"] = 1
    if 'sacks' in needed:
        needed["sacks"] += 1
    else:
        needed["sacks"] = 1
    pprint.pprint(needed)
def click32():
    global button_flag
    if 'smoothies' in needed:
        needed["smoothies"] += 1
    else:
        needed["smoothies"] = 1
    if 'melons' in needed:
        needed["melons"] += 1
    else:
        needed["melons"] = 1
    if 'sprouts' in needed:
        needed["sprouts"] += 1
    else:
        needed["sprouts"] = 1
    if 'shovels' in needed:
        needed["shovels"] += 1
    else:
        needed["shovels"] = 1
    pprint.pprint(needed)
def click33():
    global button_flag
    if 'buns' in needed:
        needed["buns"] += 1
    else:
        needed["buns"] = 1
    if 'sacks' in needed:
        needed["sacks"] += 2
    else:
        needed["sacks"] = 2
    if 'cream' in needed:
        needed["cream"] += 1
    else:
        needed["cream"] = 1
    pprint.pprint(needed)
def click34():
    global button_flag
    if 'cheesecakes' in needed:
        needed["cheesecakes"] += 1
    else:
        needed["cheesecakes"] = 1
    if 'cheese' in needed:
        needed["cheese"] += 1
    else:
        needed["cheese"] = 1
    if 'melon' in needed:
        needed["melon"] += 1
    else:
        needed["melon"] = 1
    if 'sprouts' in needed:
        needed["sprouts"] += 1
    else:
        needed["sprouts"] = 1
    if 'shovels' in needed:
        needed["shovels"] += 1
    else:
        needed["shovels"] = 1
    if 'sacks' in needed:
        needed["sacks"] += 1
    else:
        needed["sacks"] = 1
    pprint.pprint(needed)
def click35():
    global button_flag
    if 'yogurt' in needed:
        needed["yogurt"] += 1
    else:
        needed["yogurt"] = 1
    if 'cream' in needed:
        needed["cream"] += 1
    else:
        needed["cream"] = 1
    if 'melons' in needed:
        needed["melons"] += 1
    else:
        needed["melons"] = 1
    if 'sprouts' in needed:
        needed["sprouts"] += 1
    else:
        needed["sprouts"] = 1
    if 'shovels' in needed:
        needed["shovels"] += 1
    else:
        needed["shovels"] = 1
    pprint.pprint(needed)
def click36():
    global button_flag
    if 'coffee' in needed:
        needed["coffee"] += 1
    else:
        needed["coffee"] = 1
    if 'cream' in needed:
        needed["cream"] += 1
    else:
        needed["cream"] = 1
    pprint.pprint(needed)
def click37():
    global button_flag
    if 'hats' in needed:
        needed["hats"] += 1
    else:
        needed["hats"] = 1
    if 'tapes' in needed:
        needed["tapes"] += 1
    else:
        needed["tapes"] = 1
    pprint.pprint(needed)
def click38():
    global button_flag
    if 'shoes' in needed:
        needed["shoes"] += 1
    else:
        needed["shoes"] = 1
    if 'glue' in needed:
        needed["glue"] += 1
    else:
        needed["glue"] = 1
    pprint.pprint(needed)
def click39():
    global button_flag
    if 'watches' in needed:
        needed["watches"] += 1
    else:
        needed["watches"] = 1
    pprint.pprint(needed)
def click40():
    global button_flag
    if 'bs' in needed:
        needed["bs"] += 1
    else:
        needed["bs"] = 1
    if 'tapes' in needed:
        needed["tapes"] += 1
    else:
        needed["tapes"] = 1
    if 'glue' in needed:
        needed["glue"] += 1
    else:
        needed["glue"] = 1
    pprint.pprint(needed)
def click41():
    global button_flag
    if 'bp' in needed:
        needed["bp"] += 1
    else:
        needed["bp"] = 1
    if 'tapes' in needed:
        needed["tapes"] += 1
    else:
        needed["tapes"] = 1
    pprint.pprint(needed)
def click42():
    global button_flag
    if 'icecream' in needed:
        needed["icecream"] += 1
    else:
        needed["icecream"] = 1
    if 'cream' in needed:
        needed["cream"] += 1 * 3
    else:
        needed["cream"] = 1 * 3
    if 'buns' in needed:
        needed["buns"] += 1
    else:
        needed["buns"] = 1
    if 'sacks' in needed:
        needed["sacks"] += 2
    else:
        needed["sacks"] = 2
    pprint.pprint(needed)
def click43():
    global button_flag
    if 'pizza' in needed:
        needed["pizza"] += 1
    else:
        needed["pizza"] = 1
    if 'cheese' in needed:
        needed["cheese"] += 1
    else:
        needed["cheese"] = 1
    if 'sacks' in needed:
        needed["sacks"] += 1
    else:
        needed["sacks"] = 1
    if 'meat' in needed:
        needed["meat"] += 1
    else:
        needed["meat"] = 1
    pprint.pprint(needed)
def click44():
    global button_flag
    if 'burgers' in needed:
        needed["burgers"] += 1
    else:
        needed["burgers"] = 1
    if 'buns' in needed:
        needed["buns"] += 1
    else:
        needed["buns"] = 1
    if 'meat' in needed:
        needed["meat"] += 1
    else:
        needed["meat"] = 1
    if 'grills' in needed:
        needed["grills"] += 1
    else:
        needed["grills"] = 1
    if 'spats' in needed:
        needed["spats"] += 1
    else:
        needed["spats"] = 1
    pprint.pprint(needed)
def click45():
    global button_flag
    if 'fries' in needed:
        needed["fries"] += 1
    else:
        needed["fries"] = 1
    if 'cheese' in needed:
        needed["cheese"] += 1
    else:
        needed["cheese"] = 1
    if 'veggies' in needed:
        needed["veggies"] += 1
    else:
        needed["veggies"] = 1
    pprint.pprint(needed)
def click46():
    global button_flag
    if 'lemonade' in needed:
        needed["lemonade"] += 1
    else:
        needed["lemonade"] = 1
    if 'melons' in needed:
        needed["melons"] += 1
    else:
        needed["melons"] = 1
    if 'sprouts' in needed:
        needed["sprouts"] += 1
    else:
        needed["sprouts"] = 1
    if 'shovels' in needed:
        needed["shovels"] += 1
    else:
        needed["shovels"] = 1
    pprint.pprint(needed)
def click47():
    global button_flag
    if 'pcorn' in needed:
        needed["pcorn"] += 1
    else:
        needed["pcorn"] = 1
    if 'corn' in needed:
        needed["corn"] += 2
    else:
        needed["corn"] = 2
    if 'mics' in needed:
        needed["mics"] += 1
    else:
        needed["mics"] = 1
    pprint.pprint(needed)
def click48():
    global button_flag
    if 'grills' in needed:
        needed["grills"] += 1
    else:
        needed["grills"] = 1
    if 'spatulas' in needed:
        needed["spatulas"] += 1
    else:
        needed["spatulas"] = 1
    pprint.pprint(needed)
def click49():
    global button_flag
    if 'fridges' in needed:
        needed["fridges"] += 1
    else:
        needed["fridges"] = 1
    pprint.pprint(needed)
def click50():
    global button_flag
    if 'bulbs' in needed:
        needed["bulbs"] += 1
    else:
        needed["bulbs"] = 1
    pprint.pprint(needed)
def click51():
    global button_flag
    if 'tvs' in needed:
        needed["tvs"] += 1
    else:
        needed["tvs"] = 1
    pprint.pprint(needed)
def click52():
    global button_flag
    if 'microwaves' in needed:
        needed["microwaves"] += 1
    else:
        needed["microwaves"] = 1
    pprint.pprint(needed)

root = tk.Tk()
root.title('Simter')
# create a frame and pack it
frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP, fill=tk.X)
# pick a (small) image file you have in the working directory ...
photo1 = tk.PhotoImage(file="nails.gif")
# create the image button, image is above (top) the optional text
button1 = tk.Button(frame1, image=photo1,
    text="optional text", command=click01)
button1.pack(side=tk.LEFT, padx=2, pady=2)
# save the button's image from garbage collection (needed?)
button1.image = photo1

#making second button

photo2 = tk.PhotoImage(file="boards.gif")
button2 = tk.Button(frame1, image=photo2, command=click02)
button2.pack(side=tk.LEFT, padx=2, pady=2)
button2.image = photo2

#third button
photo3 = tk.PhotoImage(file="bricks.gif")
button3 = tk.Button(frame1, image=photo3, command=click03)
button3.pack(side=tk.LEFT, padx=2, pady=2)
button3.image = photo3

#gum
photo4 = tk.PhotoImage(file="gum.gif")
button4 = tk.Button(frame1, image=photo4, command=click04)
button4.pack(side=tk.LEFT, padx=2, pady=2)
button4.image = photo4

#glue
photo5 = tk.PhotoImage(file="glue.gif")
button5 = tk.Button(frame1, image=photo5, command=click05)
button5.pack(side=tk.LEFT, padx=2, pady=2)
button5.image = photo5

photo6 = tk.PhotoImage(file="paint.gif")
button6 = tk.Button(frame1, image=photo6, command=click06)
button6.pack(side=tk.LEFT, padx=2, pady=2)
button6.image = photo6

#frame2 for hardware store
frame2 = tk.Frame(root)
frame2.pack(side=tk.TOP, fill=tk.X)
photo7 = tk.PhotoImage(file="hammer.gif")
button7 = tk.Button(frame2, image=photo7, command=click07)
button7.pack(side=tk.LEFT, padx=2, pady=2)
button7.image = photo7

photo8 = tk.PhotoImage(file="tape.gif")
button8 = tk.Button(frame2, image=photo8, command=click08)
button8.pack(side=tk.LEFT, padx=2, pady=2)
button8.image = photo8

photo9 = tk.PhotoImage(file="shovel.gif")
button9 = tk.Button(frame2, image=photo9, command=click09)
button9.pack(side=tk.LEFT, padx=2, pady=2)
button9.image = photo9

photo10 = tk.PhotoImage(file="spat.gif")
button10 = tk.Button(frame2, image=photo10, command=click10)
button10.pack(side=tk.LEFT, padx=2, pady=2)
button10.image = photo10

photo11 = tk.PhotoImage(file="ladder.gif")
button11 = tk.Button(frame2, image=photo11, command=click11)
button11.pack(side=tk.LEFT, padx=2, pady=2)
button11.image = photo11

photo12 = tk.PhotoImage(file="drill.gif")
button12 = tk.Button(frame2, image=photo12, command=click12)
button12.pack(side=tk.LEFT, padx=2, pady=2)
button12.image = photo12

#farmers market
frame3 = tk.Frame(root)
frame3.pack(side=tk.TOP, fill=tk.X)
photo13 = tk.PhotoImage(file="veg.gif")
button13 = tk.Button(frame3, image=photo13, command=click13)
button13.pack(side=tk.LEFT, padx=2, pady=2)
button13.image = photo13

photo14 = tk.PhotoImage(file="sack.gif")
button14 = tk.Button(frame3, image=photo14, command=click14)
button14.pack(side=tk.LEFT, padx=2, pady=2)
button14.image = photo14

photo15 = tk.PhotoImage(file="melon.gif")
button15 = tk.Button(frame3, image=photo15, command=click15)
button15.pack(side=tk.LEFT, padx=2, pady=2)
button15.image = photo15

photo16 = tk.PhotoImage(file="cream.gif")
button16 = tk.Button(frame3, image=photo16, command=click16)
button16.pack(side=tk.LEFT, padx=2, pady=2)
button16.image = photo16

photo17 = tk.PhotoImage(file="corn.gif")
button17 = tk.Button(frame3, image=photo17, command=click17)
button17.pack(side=tk.LEFT, padx=2, pady=2)
button17.image = photo17

photo18 = tk.PhotoImage(file="cheese.gif")
button18 = tk.Button(frame3, image=photo18, command=click18)
button18.pack(side=tk.LEFT, padx=2, pady=2)
button18.image = photo18

photo19 = tk.PhotoImage(file="meat.gif")
button19 = tk.Button(frame3, image=photo19, command=click19)
button19.pack(side=tk.LEFT, padx=2, pady=2)
button19.image = photo19

#furniture
frame4 = tk.Frame(root)
frame4.pack(side=tk.TOP, fill=tk.X)
photo20 = tk.PhotoImage(file="chair.gif")
button20 = tk.Button(frame4, image=photo20, command=click20)
button20.pack(side=tk.LEFT, padx=2, pady=2)
button20.image = photo20

photo21 = tk.PhotoImage(file="table.gif")
button21 = tk.Button(frame4, image=photo21, command=click21)
button21.pack(side=tk.LEFT, padx=2, pady=2)
button21.image = photo21

photo22 = tk.PhotoImage(file="towel.gif")
button22 = tk.Button(frame4, image=photo22, command=click22)
button22.pack(side=tk.LEFT, padx=2, pady=2)
button22.image = photo22

photo23 = tk.PhotoImage(file="cab.gif")
button23 = tk.Button(frame4, image=photo23, command=click23)
button23.pack(side=tk.LEFT, padx=2, pady=2)
button23.image = photo23

photo24 = tk.PhotoImage(file="couch.gif")
button24 = tk.Button(frame4, image=photo24, command=click24)
button24.pack(side=tk.LEFT, padx=2, pady=2)
button24.image = photo24

#gardening
frame5 = tk.Frame(root)
frame5.pack(side=tk.TOP, fill=tk.X)
photo25 = tk.PhotoImage(file="grass.gif")
button25 = tk.Button(frame5, image=photo25, command=click25)
button25.pack(side=tk.LEFT, padx=2, pady=2)
button25.image = photo25

photo26 = tk.PhotoImage(file="sprout.gif")
button26 = tk.Button(frame5, image=photo26, command=click26)
button26.pack(side=tk.LEFT, padx=2, pady=2)
button26.image = photo26

photo27 = tk.PhotoImage(file="stch.gif")
button27 = tk.Button(frame5, image=photo27, command=click27)
button27.pack(side=tk.LEFT, padx=2, pady=2)
button27.image = photo27

photo28 = tk.PhotoImage(file="fire.gif")
button28 = tk.Button(frame5, image=photo28, command=click28)
button28.pack(side=tk.LEFT, padx=2, pady=2)
button28.image = photo28

photo29 = tk.PhotoImage(file="mower.gif")
button29 = tk.Button(frame5, image=photo29, command=click29)
button29.pack(side=tk.LEFT, padx=2, pady=2)
button29.image = photo29

photo30 = tk.PhotoImage(file="gnome.gif")
button30 = tk.Button(frame5, image=photo30, command=click30)
button30.pack(side=tk.LEFT, padx=2, pady=2)
button30.image = photo30


#donut shop
frame6 = tk.Frame(root)
frame6.pack(side=tk.TOP, fill=tk.X)
photo31 = tk.PhotoImage(file="donut.gif")
button31 = tk.Button(frame6, image=photo31, command=click31)
button31.pack(side=tk.LEFT, padx=2, pady=2)
button31.image = photo31
photo32 = tk.PhotoImage(file="smoothie.gif")
button32 = tk.Button(frame6, image=photo32, command=click32)
button32.pack(side=tk.LEFT, padx=2, pady=2)
button32.image = photo32
photo33 = tk.PhotoImage(file="bun.gif")
button33 = tk.Button(frame6, image=photo33, command=click33)
button33.pack(side=tk.LEFT, padx=2, pady=2)
button33.image = photo33
photo34 = tk.PhotoImage(file="ccake.gif")
button34 = tk.Button(frame6, image=photo34, command=click34)
button34.pack(side=tk.LEFT, padx=2, pady=2)
button34.image = photo34
photo35 = tk.PhotoImage(file="yogurt.gif")
button35 = tk.Button(frame6, image=photo35, command=click35)
button35.pack(side=tk.LEFT, padx=2, pady=2)
button35.image = photo35
photo36 = tk.PhotoImage(file="coffee.gif")
button36 = tk.Button(frame6, image=photo36, command=click36)
button36.pack(side=tk.LEFT, padx=2, pady=2)
button36.image = photo36

#fashion
frame7 = tk.Frame(root)
frame7.pack(side=tk.TOP, fill=tk.X)

photo37 = tk.PhotoImage(file="hat.gif")
button37 = tk.Button(frame7, image=photo37, command=click37)
button37.pack(side=tk.LEFT, padx=2, pady=2)
button37.image = photo37
photo38 = tk.PhotoImage(file="shoes.gif")
button38 = tk.Button(frame7, image=photo38, command=click38)
button38.pack(side=tk.LEFT, padx=2, pady=2)
button38.image = photo38
photo39 = tk.PhotoImage(file="watch.gif")
button39 = tk.Button(frame7, image=photo39, command=click39)
button39.pack(side=tk.LEFT, padx=2, pady=2)
button39.image = photo39
photo40 = tk.PhotoImage(file="bs.gif")
button40 = tk.Button(frame7, image=photo40, command=click40)
button40.pack(side=tk.LEFT, padx=2, pady=2)
button40.image = photo40
photo41 = tk.PhotoImage(file="bp.gif")
button41 = tk.Button(frame7, image=photo41, command=click41)
button41.pack(side=tk.LEFT, padx=2, pady=2)
button41.image = photo41

#fast food
frame8 = tk.Frame(root)
frame8.pack(side=tk.TOP, fill=tk.X)
photo42 = tk.PhotoImage(file="icecream.gif")
button42 = tk.Button(frame8, image=photo42, command=click42)
button42.pack(side=tk.LEFT, padx=2, pady=2)
button42.image = photo42
photo43 = tk.PhotoImage(file="pizza.gif")
button43 = tk.Button(frame8, image=photo43, command=click43)
button43.pack(side=tk.LEFT, padx=2, pady=2)
button43.image = photo43
photo44 = tk.PhotoImage(file="burger.gif")
button44 = tk.Button(frame8, image=photo44, command=click44)
button44.pack(side=tk.LEFT, padx=2, pady=2)
button44.image = photo44
photo45 = tk.PhotoImage(file="fries.gif")
button45 = tk.Button(frame8, image=photo45, command=click45)
button45.pack(side=tk.LEFT, padx=2, pady=2)
button45.image = photo45
photo46 = tk.PhotoImage(file="lemonade.gif")
button46 = tk.Button(frame8, image=photo46, command=click46)
button46.pack(side=tk.LEFT, padx=2, pady=2)
button46.image = photo46
photo47 = tk.PhotoImage(file="pcorn.gif")
button47 = tk.Button(frame8, image=photo47, command=click47)
button47.pack(side=tk.LEFT, padx=2, pady=2)
button47.image = photo47

#home appliances
frame9 = tk.Frame(root)
frame9.pack(side=tk.TOP, fill=tk.X)
photo48 = tk.PhotoImage(file="grill.gif")
button48 = tk.Button(frame9, image=photo48, command=click48)
button48.pack(side=tk.LEFT, padx=2, pady=2)
button48.image = photo48
photo49 = tk.PhotoImage(file="fridge.gif")
button49 = tk.Button(frame9, image=photo49, command=click49)
button49.pack(side=tk.LEFT, padx=2, pady=2)
button49.image = photo49
photo50 = tk.PhotoImage(file="bulb.gif")
button50 = tk.Button(frame9, image=photo50, command=click50)
button50.pack(side=tk.LEFT, padx=2, pady=2)
button50.image = photo50

photo51 = tk.PhotoImage(file="tv.gif")
button51 = tk.Button(frame9, image=photo51, command=click51)
button51.pack(side=tk.LEFT, padx=2, pady=2)
button51.image = photo51
photo52 = tk.PhotoImage(file="mic.gif")
button52 = tk.Button(frame9, image=photo52, command=click52)
button52.pack(side=tk.LEFT, padx=2, pady=2)
button52.image = photo52



# start the event loop
root.mainloop()

#save dictionary
output = open('needed.pkl', 'wb')
pickle.dump(needed, output)
output.close()
