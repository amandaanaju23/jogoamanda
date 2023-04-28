# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Lydia")
define b = Character("Stiles")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene paisagem


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show lydia

    # These display lines of dialogue.

    e "As noites em Bacon Hills ainda são frias e assustadoras."

    e "O aparecimento de novas criaturas já não é novidade!"

    e "Está noite resolvi caminhar pela floresta, assim como fazia nos velhos tempos. Sei que não é uma boa ideia, mas alguma coisa me fez vir aqui."

    e "O vento frio batendo sobre o meu rosto, me fazendo arrepiar dos pés a cabeça. Os sons estranhos ecoando pelo local e a escuridão do inverno, me fazem cogitar seriamente em pegar o rumo de volta para casa"

    # This ends the game.

    return
