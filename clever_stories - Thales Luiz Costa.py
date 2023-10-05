a_funny_game = 'a funny game'
print('Please tell me seven words to insert into the story. I need two adjectives, an animal, a verb, an exclamation and then two verbs, can you do it?')

adjective_1 = input('First Adjective = ')
adjective_2 = input('Second Adjective = ')
animal = input('Animal = ')
verb_1 = input('First verb = ')
exclamation = input('Exclamation = ')
verb_2 = input('Second verb = ')
verb_3 = input('Third verb = ')

#adjective_1 = 'weird' - adjective_2 = 'happy' - animal = 'monkey' - verb_1 = 'jump' - exclamation = 'Oh my gosh' - verb_2 = 'smile' - verb_3 = 'laught'
# #I added two sentences, "A weird Day" as a title and " Once upon a time on my street" as a subtitle.

title = (f'A {adjective_1} Day!')
subtitle = ('Once upon a time on my street...')
cleverstories = (f'The other day, I was really in trouble. It all started when I saw a {adjective_2} {animal} {verb_1} down the hallway. "{exclamation}!" I thought. But all I could think to do was to {verb_2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb_3} right in front of my family.')

print('Adject = ' + adjective_1)
print('Animal = ' + animal)
print('Verb = ' + verb_1)
print('Exclamation = ' + exclamation)
print('Verb = ' + verb_2)
print('Verb = ' + verb_3)
print()
print(title)
print(subtitle)
print(cleverstories)
print()
print(title.upper())
print(subtitle.upper())
print(cleverstories.upper())
print()
print(title.lower())
print(subtitle.lower())
print(cleverstories.lower())
print(cleverstories.count('j'))