import os

# TASK 1

# def read_end(lines, file):
#     with open(file) as f:
#         listF = f.readlines()
#     st = ''
#     if lines < 0:
#         print("Количество строк должно быть положительным")
#     else:
#         for i in range(len(listF) - lines, len(listF)):
#             st += listF[i]
#         return st

# print(read_end(2, './folder1/text.txt'))







# TASK 3

# for path, dirs, files in os.walk('./venv'):
#     for dir in dirs:
#         print(os.path.join(path, dir))
#     for file in files:
#         print(os.path.join(path, file))







#TASK 3

# def longest_word(file):
#     with open(file) as f:
#         listF = f.readlines()
#     maxL = 0
#     listMax = []
#     sepList = ';:,.-!?'
#     clearLs = []
#     for sent in listF:
#         st = ''
#         for w in sent:
#             if w not in sepList:
#                 st += w
#         clearLs.append(st)

#     for sent in clearLs:
#         listSt = sent.split()
#         for item in listSt:
#             if maxL < len(item):
#                 maxL = len(item)
#                 listMax = []
#             if len(item) == maxL:
#                 listMax.append(item)
#     print(listMax)

# longest_word('./folder/text.txt')








# TASK 4

# def get_file_info(file):
#     latAlph = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgijklmnopqrstuvwxyz"
#     symbl = ",.:;!?"
#     with open(file) as f:
#         listF = f.readlines()
#         linesCount = len(listF)
#         newList = []
#         lettersCount = 0
#         wordsCount = 0
#         for sent in listF:
#             word = ''
#             for letter in sent:
#                 if letter not in symbl:
#                     word += letter
#                     lettersCount += 1
#             newList.append(word)
        
#         for i in range(0, linesCount):
#             wordsCount += len(newList[i].split())
#         print(f'{lettersCount} letters\n{wordsCount} words\n{linesCount} lines')
            



# get_file_info('./folderTask4/Muse - Muscle Museum.txt')























#РАБОТА НА ЗАНЯТИИ

# print('dir', os.getcwd())
# dir = 'folder1'
# if not os.path.isdir(dir):
#     os.mkdir(dir)
# else:
#     print("Такая папка уже есть")
#
#
# os.chdir('folder')
# print('dir', os.getcwd())
# os.chdir('..')
# print('dir', os.getcwd())
#
# os.makedirs('f1/f2/f3/f4')



# file = open('text.txt', 'w')
# file.write('bbbbbbbbbbbb\nbbbbbbbbbbbbb')
# os.rename('text.txt', 'new_text.txt')

# os.replace('../OS/folder/new.txt', '../OS/new_text.txt')
# os.remove('./new_text.txt')
#
# print(os.listdir())



#
# for path, dirs, files in os.walk('../venv'):
#     for dir in dirs:
#         print(os.path.join(path,dir))
#     for file in files:
#         print(os.path.join(path, file))



# os.rmdir('folder')

# os.removedirs('f1/f2/f3/f4')


#print(os.stat('text.txt').st_size)


# print(os.name)
#
# with open('./text.txt', 'w') as f:
#     f.write('AAAAAAAAA')









