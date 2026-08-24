# Adaptive Filipino Story Reading App
# A simple program that gives you a short story to read, then asks questions and gives tips based on your score and reading speed.

# Rule 1: If your score is below 70 -> give an easier story next time
# Rule 2: If you read slower than average -> turn on "Reading Support Mode"

print("=== Adaptive Filipino Romance Reading App ===")

# level starts at 1 (1 = beginner, 2 = intermediate, 3 = advanced)
level = 1

play_again = "y"

while play_again == "y":

    # Pick the story based on the level
    if level == 1:
        title = "Magkaibigan Kami"
        story = ("Magkaaway ang nanay nina Ella at Sam simula pa noong bata sila, "
                 "pero magkaibigan naman sina Ella at Sam. Tuwing recess, "
                 "magkasama sila kumain, at tuwing may problema si Ella, si Sam "
                 "ang unang tumutulong. Isang araw, nagtanong si Ella, 'Bakit "
                 "kaya ayaw mag-usap ng mga nanay natin?' Sumagot si Sam, "
                 "'Ewan, pero okay lang. Tayo naman, magkaibigan pa rin.'")
        question1 = "Ano ang relasyon nina Ella at Sam?"
        answer1 = "magkaibigan"
        question2 = "Sino ang tumutulong kay Ella tuwing may problema siya?"
        answer2 = "sam"
        average_speed = 100

    elif level == 2:
        title = "Ang Malaking Pangarap"
        story = ("Madalas umiyak si Jomar kapag natutulog na ang lahat, dahil "
                 "mahirap lang ang pamilya nila at wala silang pang-baon "
                 "araw-araw. Pero sa kabila ng luha niya, malaki ang pangarap "
                 "ni Jomar: gusto niyang maging guro balang-araw at makatulong "
                 "sa mga batang tulad niya. Kaya naman, tuwing umaga, pinupunasan "
                 "niya ang mga luha niya at pumapasok pa rin sa paaralan, dahil "
                 "alam niyang ang pangarap niya ay mas malaki kaysa sa hirap na "
                 "kanyang nararamdaman.")
        question1 = "Ano ang gustong maging trabaho ni Jomar balang-araw?"
        answer1 = "guro"
        question2 = "Bakit umiiyak si Jomar?"
        answer2 = "mahirap"
        average_speed = 130

    else:
        title = "Ang Pangarap ni Miko"
        story = ("Anim na taong gulang si Miko nang maghiwalay ang kaniyang mga "
                 "magulang. Iniwan siya sa piling ng kaniyang lola sa isang "
                 "maliit na bahay sa probinsya. Madalas siyang umiyak tuwing "
                 "gabi, gustong makasama ang mama at papa niya. Pero sa halip "
                 "na sumuko, ipinangako ni Miko sa sarili niya na pag-aaralan "
                 "niya nang mabuti at hindi niya uulitin ang pagkakamali ng "
                 "kaniyang mga magulang. Taon-taon, tuwing may mababang grado "
                 "siya, naaalala niya ang pangako niya sa sarili at doon siya "
                 "kumukuha ng lakas na magsikap muli. Nang tumapos siya bilang "
                 "kumaganti sa paaralan, hinawakan niya ang kamay ng kaniyang "
                 "lola at sinabi, 'Salamat po, Lola. Dahil sa inyo, natutunan "
                 "kong hindi ang nakaraan ang bahala sa kinabukasan ko.'")
        question1 = "Sino ang nag-alaga kay Miko matapos maghiwalay ang mga magulang niya?"
        answer1 = "lola"
        question2 = "Ilang taon gulang si Miko nang maghiwalay ang kaniyang mga magulang?"
        answer2 = "6"
        average_speed = 150

    # Show the story 
    print("")
    print("Story: " + title)
    print(story)
    input("Press Enter once you are done reading...")

    # Ask reading time (for this demo, user types it in) 
    reading_time = float(input("Enter your reading time in seconds: "))
    word_count = len(story.split())
    reading_speed = word_count / (reading_time / 60)

    # Ask the questions 
    print("")
    print("Comprehension Check")

    score = 0

    user_answer1 = input(question1 + " ").lower()
    if answer1 in user_answer1:
        print("Tama!")
        score = score + 1
    else:
        print("Mali. Sagot: " + answer1)

    user_answer2 = input(question2 + " ").lower()
    if answer2 in user_answer2:
        print("Tama!")
        score = score + 1
    else:
        print("Mali. Sagot: " + answer2)

    # turn score into a percentage (2 questions total)
    score_percent = (score / 2) * 100

    # Show results
    print("")
    print("--- Results ---")
    print("Comprehension score: " + str(score_percent) + "%")
    print("Reading speed: " + str(round(reading_speed)) + " WPM")

    # Rule 1: score check
    if score_percent < 70:
        print("Rule 1: Your score is below 70%, so the next story will be easier.")
        if level > 1:
            level = level - 1
    else:
        print("Rule 1: Good score! The next story will be harder.")
        if level < 3:
            level = level + 1

    # Rule 2: reading speed check 
    if reading_speed < average_speed:
        print("Rule 2: You read slower than average, so Reading Support Mode is ON.")
        print("(This means: simpler words and a read-aloud option next time.)")
    else:
        print("Rule 2: Your reading speed is good, Reading Support Mode is OFF.")

    # Ask if they want to continue
    play_again = input("Do you want to read another story? (y/n): ").lower()

print("Salamat sa pagbabasa! Ingat lagi.")