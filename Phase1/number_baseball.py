#### 숫자야구 
#### KDT 12기 박성훈

# 프로그램 불러오기
import random
from tkinter import *
from tkinter import messagebox

# 정답 생성
target_list = random.sample("0123456789", 4)
target_text = "".join(target_list)

# 창 만들기
window = Tk()
window.title("숫자야구")
window.geometry("420x840")
# 숫자야구 설명
messagebox.showinfo("숫자야구 룰",
'''
규칙설명
숫자야구는 4자리의 숫자를 맞추는 게임입니다!
10번의 시도를 통해 경우의 수를 줄여나가며 4자리의 숫자를 맞춰주세요!
(각 자리의 숫자는 중복이 안돼요)


맞추는 방법은 간단합니다
out = 숫자와 위치가 전부 틀리면 out(strike 0, ball 0)!
ball = 숫자는 맞지만 위치가 틀렸을때는 ball!
strike =  숫자와 위치가 맞으면 strike!

이 게임을 끝내는 방법은 내가 입력한 숫자와 정답이 일치한 4strike가 정답이라고 할 수 있겠네요!
'''
)

##===========================
# 숫자야구 기록 로그(기회는 10번)
#============================


attemps = 10        #시도 횟수는 10번

def log(guess_list, b, s, o): 
    global attemps 

    if o != 1: #out이 0인지 아닌지에 따라 창에 나오는 결과가 달라짐
        text = f's : {s},   b  : {b}'
    else :
        text = f'o : {o}'

    text_guess = "".join(guess_list)

    row = 10 - attemps   # 로그의 위치조정
    y = 20 + row * 20 
    Label(window, text = f'{11-attemps}.   {text_guess} |   {text}', font = ("함초롱바탕", 10, "bold"), anchor = 'w').place(x = 10, y = y)
    
    

    attemps -= 1 #한번 함수가 돌아간 다음에 시도 횟수 줄이기
    if attemps == 0:
        game_end(s)
##===========================
# 게임 종료 루트
#============================
def game_end(s):
    
    if s == 4: #모두 숫자를 맞추거나
        label_result = messagebox.showinfo("숫자야구", "축하합니다 정답을 맞추셨어요!")
    else: #시도횟수가 다 줄거나
        label_result = messagebox.showinfo("숫자야구", f'아쉬워요 정답은 {target_text}입니다')
    window.destroy()


##===========================
# ball, strike, out 판정
#============================
def judge(guess_text, target_text):
    b, s, o = 0, 0, 0
    for i in range(4): #각 자리 를 비교
        if guess_text[i] in target_text: #숫자가 정답에 있다면 
            if guess_text[i] == target_text[i]: #그 자리의 위치가 동일하다면
                s += 1 # 스트라이크
            else:
                b += 1 # 볼
    if (b == 0) and (s == 0):
        o += 1  # 아웃
    if s == 4:  #만약 스트라이크 4개면 게임 종료로
        game_end(s)
    return b, s, o

### 1번의 시도후 첫번째 숫자 버튼을 누르면 나머지 리스트 삭제
def reset_labels():
    label_guess2.configure(text = "_", font = ("함초롱바탕", 20, "bold"))
    label_guess3.configure(text = "_", font = ("함초롱바탕", 20, "bold"))
    label_guess4.configure(text = "_", font = ("함초롱바탕", 20, "bold"))


#============================
# 라벨을 _에서 숫자로 변경
#============================
def update_guess_labels(guess_list):
    if len(guess_list) == 1:
        label_guess1.configure(text = str(guess_list[0]), font = ("함초롱바탕", 20, "bold"))
        reset_labels()

    
    if len(guess_list) == 2:
        label_guess2.configure(text = str(guess_list[1]), font = ("함초롱바탕", 20, "bold"))
    if len(guess_list) == 3:
        label_guess3.configure(text = str(guess_list[2]), font = ("함초롱바탕", 20, "bold"))
    if len(guess_list) == 4:
        label_guess4.configure(text = str(guess_list[3]), font = ("함초롱바탕", 20, "bold"))



#============================
# 버튼을 누르면 그 값을 입력하고 문자 리스트로 만드는 함수
#============================
guess_list = [] 
def push_button(num):
    global guess_list
    a = str(num)
    
    if a in guess_list: # 만약 입력한 숫자가 이미 있었다면
        messagebox.showinfo("숫자야구", "같은 숫자는 입력할 수 없습니다!")
        return
    
    guess_list.append(a)
    
    update_guess_labels(guess_list) # 

    if len(guess_list) == 4:
        guess_text = "".join(guess_list)
        
        b, s, o = judge(guess_text, target_text)

        log(guess_list, b, s, o)
        guess_list.clear()
        label_s.configure(text=f"Strike: {s}")
        label_b.configure(text=f"Ball: {b}")
        


#============================
# 버튼 만들기
#============================

# 일단 빈 리스트를 만들어서 버튼이 들어갈 리스트를 하나씩 넣는다. 그리고 칸을 조정한다.
button_list = [""]*10
print(button_list)
num = 1
locx, locy= 50,380
for a in range(3):
    for b in range(3):
        button_list[num] = Button(window, text = num, font = ("함초롱바탕", 30, "bold"), command = lambda n = num : push_button(n))
        button_list[num].place(x = locx, y = locy, width = 90, height = 90)
        num += 1
        locx += 115
    locx = 50
    locy += 115
button_list[0] = Button(window, text = "0", font = ("함초롱바탕", 30, "bold"),  command = lambda n = 0 : push_button(0))
button_list[0].place(x = 165, y = locy, width = 90, height = 90)


##============================
# 값을 화면에 출력하고, 결과를 발표하기
#============================
label_s = Label(window, text="Strike: -", font=("함초롱바탕", 20, "bold"))
label_b = Label(window, text="Ball: -", font=("함초롱바탕", 20, "bold"))
label_s.place(x=70, y=310)
label_b.place(x=230, y=310)

label_guess1 = Label(window, text = "_", font = ("함초롱바탕", 20, "bold"))
label_guess2 = Label(window, text = "_", font = ("함초롱바탕", 20, "bold"))
label_guess3 = Label(window, text = "_", font = ("함초롱바탕", 20, "bold"))
label_guess4 = Label(window, text = "_", font = ("함초롱바탕", 20, "bold"))


label_guess1.place(x=120, y=260)
label_guess2.place(x=170, y=260)
label_guess3.place(x=220, y=260)
label_guess4.place(x=270, y=260)



#창 닫기 맨 마지막으로 갈것
window.mainloop()