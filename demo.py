# DEPENDENCIES ------------------

# pip install pillow


# INFO -------------------

# @author: Ivo Lopes =)
# Date: 20/09/2021

from PIL import Image
import os
import time
from os import system

width = 0
height = 0
images = []


def getDims():
    system("cls")
    global width, height

    width = input("Image Width: ")
    height = input("Image Height: ")


def resizeImages(resizeMethod, imageWidth, imageHeight, format):
    system("cls")
    print("\n\tResizing the images, please wait...")

    # compressing images
    for image in images:
        img = Image.open(image)
        # resizing the images
        if resizeMethod == 'thumbnail':
            img.thumbnail((int(imageWidth), int(imageHeight)))
            img.save("finals/" + str(image.lower())
                     [:-4] + f".{format}", optimize=True, quality=60)
        elif resizeMethod == 'resize':
            resized = img.resize((int(imageWidth), int(imageHeight)))
            resized.save("finals/" + str(image.lower())
                         [:-4] + f".{format}", optimize=True, quality=60)

    print("\n\tAll Images Succssefully Resized! Congrats 👏")
    enterToContinue("\n\tENTER to go back...")

    menu()


def enterToContinue(text):
    input(text)


def getImages():
    system("cls")
    global images
    images = [file for file in os.listdir() if file.endswith(('jpg', 'png'))]

    print("\n\tImages Added Successfully")

    enterToContinue("\n\tENTER to go back...")

    menu()


def clearImages():
    system("cls")
    global images
    images = []

    print("\n\tImages Cleared Successfully")

    enterToContinue("\n\tENTER to go back...")

    menu()


def showImageList():
    system("cls")
    print("\n\t### IMAGE LIST ###\n\n")
    for image in images:
        print("\t" + image)

    enterToContinue("\n\tENTER to go back...")

    menu()


def getImageFormat():
    option = 0
    while (option != '1') and (option != '2') and (option != '3'):
        print("""
        ### CHOOSE THE FILE FORMAT ###

        1) PNG
        2) JPG
        3) Cancel
        """)

        option = input("\tOption-> ")

        if option == '1':
            return 'png'
        elif option == '2':
            return 'jpg'
        elif option == '3':
            menu()

    enterToContinue("\n\tENTER to start resizing!")


def menu():
    system("cls")

    optionsList = ['1', '2', '3', '4', '5']

    print("""
        ### MENU ###

        1) Get Image List
        2) Clear Image List
        3) Show Image List
        4) Resizer
        5) Exit
    """)

    option = input("\tOption-> ")

    if option in optionsList:
        if option == '1':
            getImages()
        elif option == '2':
            clearImages()
        elif option == '3':
            showImageList()
        elif option == '4':
            while (option != '1') and (option != '2') and (option != '3'):
                system("cls")
                print("""
        ### RESIZER ###

        1) Maintain Aspect Ratio
        2) Ignore Aspect Ratio
        3) <- Go back
                """)

                option = input("\tOption-> ")

                if option == '1':
                    getDims()
                    format = getImageFormat()
                    resizeImages('thumbnail', width, height, format)
                elif option == '2':
                    getDims()
                    format = getImageFormat()
                    resizeImages('resize', width, height, format)
                elif option == '3':
                    menu()

        elif option == '5':
            system("cls")
            exit()
    else:
        menu()


def hello():
    system("cls")
    print("""
        ##     ## ######## ##       ##        #######  
        ##     ## ##       ##       ##       ##     ## 
        ##     ## ##       ##       ##       ##     ## 
        ######### ######   ##       ##       ##     ## 
        ##     ## ##       ##       ##       ##     ## 
        ##     ## ##       ##       ##       ##     ## 
        ##     ## ######## ######## ########  #######  
    """)

    time.sleep(3)

    menu()


if __name__ == "__main__":
    hello()
