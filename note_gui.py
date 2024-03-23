from tkinter import *
from tkinter.filedialog import *

# 메뉴가 클릭되었을 때 실행될 함수 
def new_file():
    #텍스트 영역 지우기
    text_area.delete(1.0, END)
    
def save_file():
    f = asksaveasfile(mode='w', defaultextension=".txt", filetypes=[('Text files', '.txt')])
    text_save = str(text_area.get(1.0, END))
    f.write(text_save)
    f.close()

def maker():
    #새 창 만들고 내용 적기
    help_view = Toplevel(window)
    help_view.geometry('300x50+850+400')
    help_view.title('만든 이')
    lb = Label(help_view, text ='\n파이썬으로 메모장 만들기')
    lb.pack()

#윈도우 생성하기 
window = Tk()
window.title('Notepad')
window.geometry('400x400+800+300')
window.resizable(0,0)

#아이콘 넣기
window.iconbitmap("D:/바탕화면/4-1/해달/1차시/notepad-icon_34386.ico")
#photo = PhotoImage(file="D:/바탕화면/4-1/해달/1차시/haedal.png")
#window.iconphoto(False, photo)

#메뉴 생성
menuMaker = Menu(window)
#첫번째 메뉴 만들기 
first_menu = Menu(menuMaker, tearoff=0)
#첫번째 메뉴의 세부메뉴 추가 및 함수 연결
first_menu.add_command(label = '새 파일', command = new_file)
first_menu.add_command(label = '저장', command = save_file)

#첫번째 메뉴에 구분선 추가 
first_menu.add_separator()
#종료 옵션 추가하기
first_menu.add_command(label='종료', command=window.destroy)

#메뉴 바 추가 
menuMaker.add_cascade(label='파일', menu=first_menu)

#두번째 메뉴 추가 
second_menu = Menu(menuMaker, tearoff=0)
#세부 메뉴 추가, 함수 연결
second_menu.add_command(label = '만든 이', command = maker)
#메뉴 바 추가
menuMaker.add_cascade(label='정보', menu = second_menu)

#텍스트 창 만들기 
text_area = Text(window)
#공백 설정하기 
window.grid_rowconfigure(0, weight =1)
window.grid_columnconfigure(0, weight = 1)
#텍스트 화면을 윈도우에 동서남북으로 붙인다
text_area.grid(sticky = N+E+S+W)

#메뉴 구성
window.config(menu = menuMaker)

window.mainloop()