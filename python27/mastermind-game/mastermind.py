import random

def contain_counter(word,guess):
    word_items = set(list(word))
    guess_items = set(list(guess))
    contain_count = 0
    for i in word_items:
        if i in guess_items:
            contain_count += 1
    return contain_count

def pos_counter(word,guess):
    word_list = list(word)
    guess_list = list(guess)
    pos_count = 0 
    for i in xrange(len(word_list)):
        #print word_list[i] + ' ' + guess_list[i]
        if word_list[i] == guess_list[i]:
            pos_count += 1
    return pos_count

def compare(word,guess):
    print pos_counter(word,guess),
    print contain_counter(word,guess)    

def level_range(level):
    low = int('1' + '0'*(level-1))
    high = int('9'*level)
    return {'high': high , 'low' : low} 

def get_level_range():
  u_limit = 10
  l_limit = 3
  in_err = False
  while True:
    if in_err:
      print "Invalid input.."
    level = int(raw_input("Enter Level(3-10): "))
    if l_limit <= level <= u_limit:
      break
    else:
      in_err = True
  
  return level_range(level)

def get_guess(level_range):
  while True:
    guess = raw_input("Enter Guess : ")
    if level_range['low'] <= int(guess) <= level_range['high']:
      break
    else:
      print "Invalid Guess.."
  return guess
    

#-----testing-----

#word = '111'
#guess = '111'

#compare(word,guess)
#print pos_counter(word,guess)



#-------main-----

#level = int(raw_input("Enter level(3-10): "))
level_range = get_level_range()
word = str(random.randint(level_range['low'],level_range['high']))

#word = str(random.randint(100,999))
guess_count = 0
print "Begin MasterMind"
while True:
    guess_count += 1
    guess = get_guess(level_range)
    pos_count = pos_counter(word,guess)
    contain_count = contain_counter(word , guess)

    if pos_count == len(word):
        print "Congrats, you have guessed the word in " + str(guess_count) + " attempts"
        break

    print pos_count, contain_count
