# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

#Image Declarations for game
#Doctor Aysus
image docayscon = "docaysus/docaysus confused.png"
image docaysdisa = "docaysus/docaysus disapproving.png"
image docaysdis = "docaysus/docaysus disgusted.png"
image docaysnorm = "docaysus/docaysus normal.png"
image docayspis = "docaysus/docaysus pissed.png"
image docaysshit = "docaysus/docaysus segrin.png"
image docayssigh = "docaysus/docaysus sigh.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show docaysnorm at right

    e "Game start"

    show docayscon at right

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    show docaysshit at left

    e "Once you add a story, pictures, and music, you can release it to the world!"

    show docayssigh at right

    e "the end"

    # This ends the game.

    return
