import screeninfo
import asyncio


def get_alignments(string = " "):
    screen_width = int((screeninfo.get_monitors()[0].width)/(9.2))
    if screen_width < 128 :
        left_align = 0
        gap = int(screen_width/2)
    else :
        gap = 128

        left_align = (int(screen_width/2) - int(gap/2))
        left_gap = (int(gap/2) - int(len(string)/2))
        right_gap = gap - left_gap - len(string)
    
    return {"left_align" : left_align, "left_gap" : left_gap, "right_gap" : right_gap, "default_gap" : gap }

def centre(title='',symbol=" ",left_alignment=None, str_end="\n") :
    #aligns the title in centre with symbols around it
    alignments = get_alignments(title)
    left_align = alignments["left_align"]*" "
    left_gap = alignments["left_gap"]
    right_gap = alignments["right_gap"]
    default_gap = alignments["default_gap"]*" "

    if left_alignment != None and type(left_alignment) == int :
        left_align = left_alignment*" "

    if str_end != '\r' :
        print_string = f"{left_align}|{left_gap*symbol}{title}{right_gap*symbol}|\n{left_align}|{default_gap}|"

    else :
        print_string = f"{left_align}|{left_gap*symbol}{title}{right_gap*symbol}|"

    print(print_string,end=str_end)

def format_input(ques='') : 
    alignments = get_alignments(ques)
    left_align = alignments["left_align"]*" "
    left_gap = alignments["left_gap"]*" "
    right_gap = alignments["right_gap"]*" "

    string = f"{left_align}|{left_gap}{ques}{right_gap}|\n{left_align}| -"
    output = input(string)
    return output

def int_check(answer='') :
    answer = str(answer).strip()
    integer = -1
    while integer < 1 :
        try : 
            int(answer)
            integer = int(answer)
        except : 
            centre("Please enter a valid integer !")
            answer =  format_input("Enter a number - ") 
            continue
    return int(answer)

def ans_check(option_list=[]) :

    if type(option_list) is not list :
        print('please input a list')
    else:
        #prints and detetcs the answers and returns the choose answer
        centre("-","-")
        for i in option_list : 
            centre(symbol=" ", title=(str(option_list.index(i) + 1) + ".) " + str(i)))
        centre("-","-")
        answer = format_input("Choose a option : ") 
        answer = answer.strip()
        answer = int_check(answer)
        while int(answer) > len(option_list) :
                centre("Not a valid answer !")
                answer = format_input("Choose a option")
                try :
                    int(answer) 
                except  :
                    answer = int_check(answer)
            
        return option_list[int(answer) - 1]

async def redirect_function(redirect):
    for i in range(3,0,-1):
        title = f"Redirecting to {redirect} in {i}..."
        symbol = " "
        gap = str(symbol)*(64-int((len(title)/2)))
        gap2 = str(symbol)*(128- len(title) - len(gap))
        centre(title, str_end="\r")
        await asyncio.sleep(1) 

async def redirect(redirect='UNKNOWN'):
    await redirect_function(redirect)

