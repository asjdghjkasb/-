from  import color
import random

banner_1 = color.yellow("""                   __
                  [  |                              
  _   __  __   _   | |  _ .--..--.   ,--.  _ .--.   
 [ \ [  ][  | | |  | | [ `.-. .-. | `'_\ :[ '/'`\ \ 
  \ \/ /  | \_/ |, | |  | | | | | | // | |,| \__/ | 
   \__/   '.__.'_/[___][___||__||__]\'-;__/| ;.___/  
                                          [__|""")

banner_2 = color.yellow(r'''
                                +---------------+
 How to find vulnerabilities?   |    vulmap     |
                                +---------------+ 
    (╯▔＾▔)╯                        \ (•◡ •) / 
     \   |                            |   /
￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣''')


def banner():
    o_o = random.choice(range(10))
    if o_o == 0:
        return banner_1
    elif o_o == 1:
        return banner_1
    elif o_o == 2:
        return banner_1
    elif o_o == 3:
        return banner_1
    elif o_o == 3:
        return banner_1
    elif o_o == 4:
        return banner_1
    elif o_o == 5:
        return banner_1
    elif o_o == 6:
        return banner_1
    elif o_o == 7:
        return banner_1
    elif o_o == 8:
        return banner_1
    elif o_o == 9:
        return banner_2