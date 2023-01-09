import time #time 모듈을 import함
import RPi.GPIO as GPIO #RPi.GPIO 모듈을 import함
trig = 20 #trig 핀 번호 20
echo = 16 #echo 핀 번호 16
MAX=10
GPIO.setmode(GPIO.BCM) #BCM 모드로 작동
GPIO.setwarnings(False) #경고글이 출력되지 않게 설정
GPIO.setup(trig, GPIO.OUT) #trig를 출력으로 설정
GPIO.setup(echo, GPIO.IN) #echo를 입력으로 설정
GPIO.output(trig, False) #신호 0 발생(falling edge)

led_red=12  #led_red 핀 번호 12
GPIO.setup(led_red, GPIO.OUT) #GPIO 12번 핀을 출력 선으로 지정

led_green=13 #led_green 핀 번호 13
GPIO.setup(led_green, GPIO.OUT) #GPIO 13번 핀을 출력 선으로 지정

led_white1=4 #led_white1 핀 번호 4
GPIO.setup(led_white1, GPIO.OUT) #GPIO 4번 핀을 출력 선으로 지정
button_white1=20 #button_white1 핀 번호 20
GPIO.setup(button_white1, GPIO.IN, GPIO.PUD_DOWN) #GPIO 핀 20을 입력으로 지정. 풀다운 효과 지정

led_white2=5 #led_white2 핀 번호 5
GPIO.setup(led_white2, GPIO.OUT) #GPIO 5번 핀을 출력 선으로 지정
button_white2=21 #button_white2 핀 번호 21
GPIO.setup(button_white2, GPIO.IN, GPIO.PUD_DOWN) #GPIO 핀 21을 입력으로 지정. 풀다운 효과 지정

led_white3=6 #led_white3 핀 번호 6
GPIO.setup(led_white3, GPIO.OUT) #GPIO 6번 핀을 출력 선으로 지정
button_white3=22 #button_white3 핀 번호 22
GPIO.setup(button_white3, GPIO.IN, GPIO.PUD_DOWN) #GPIO 핀 22을 입력으로 지정. 풀다운 효과 지정

button=[20, 21, 22] #button 배열
record=[0 for i in range(MAX)] #사용자 입력 배열 record

def input(n): #삽입함수
    cnt=0 #인덱스 번호 0부터 시작
    while(cnt<n): #배열의 인덱스 번호가 삽입하는 값 개수보다 작을 때까지 무한 반복
        if(GPIO.input(button[0])==GPIO.HIGH): #버튼을 눌러 GPIO 20번이 입력으로 들어오면
            record[cnt]=4 #사용자 입력 배열에 핀 번호 값 4를 넣음
            light(4, 0.5) #light 함수 호출
            cnt+=1 #인덱스 번호 하나 증가
        elif(GPIO.input(button[1])==GPIO.HIGH): #버튼을 눌러 GPIO 21번이 입력으로 들어오면
            record[cnt]=5 #사용자 입력 배열에 핀 번호 값 5를 넣음
            light(5, 0.5) #ligth 함수 호출
            cnt+=1 #인덱스 번호 하나 증가
        elif(GPIO.input(button[2])==GPIO.HIGH): #버튼을 눌러 GPIO 22번이 입력으로 들어오면
            record[cnt]=6 #사용자 입력 배열에 핀 번호 값 6을 넣음
            light(6, 0.5) #light 함수 호출
            cnt+=1 #인덱스 번호 하나 증가

def light(n, t): #light 함수
    GPIO.output(n, GPIO.HIGH) #핀 번호가 n에 해당하는 led에 불이 들어옴
    time.sleep(t)
    GPIO.output(n, GPIO.LOW) #핀 번호가 n에 해당하는 led의 불이 꺼짐
    time.sleep(t)

count=0 #틀린 횟수
chapter=1 #단계

while(chapter<11): #10단계가 되면 빠져나옴
    if(count==3): #틀린 횟수가 3번이면 빠져나옴
        break
    if(chapter==1): #1단계
        #게임 시작을 알려줌
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_white1, GPIO.HIGH)
        GPIO.output(led_white2, GPIO.HIGH)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white1, GPIO.LOW)
        GPIO.output(led_white2, GPIO.LOW)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_white1, GPIO.HIGH)
        GPIO.output(led_white2, GPIO.HIGH)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white1, GPIO.LOW)
        GPIO.output(led_white2, GPIO.LOW)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.2)

        #화면에 1단계 시작 메시지 띄우기
        print("1단계를 시작합니다.\n")
        time.sleep(0.5)
        #1단계에 해당하는 불빛 순서 들어옴
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        #1단계 순서 끝남을 의미
        GPIO.output(led_white1, GPIO.HIGH)
        GPIO.output(led_white2, GPIO.HIGH)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        GPIO.output(led_white2, GPIO.LOW)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        #사용자가 led 순서에 맞게 버튼을 누르도록 화면에 출력
        print("led 순서에 맞게 버튼을 눌러주세요.\n")
        while(chapter<2):
            answer=[4, 0, 0, 0, 0, 0, 0, 0, 0, 0] #정답 배열
            input(1) #1개 입력 받도록 input 함수 실행
            print("-----[1단계 입력]-----")
            print(record) #사용자가 최종 입력한 배열 record 출력
            print("-----[1단계 정답]-----")
            print(answer) #정답 배열 answer 출력

            if(answer==record): #정답 배열과 사용자 배열이 같으면
                print("정답입니다.\n") #정답입니다를 화면에 띄움
                time.sleep(0.5)
                #정답 시 초록색 led를 깜빡임
                GPIO.output(led_green, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_green, GPIO.LOW)
                chapter+=1 #단계 하나 증가

            elif(answer!=record): #정답 배열과 사용자 입력 배열이 같지 않다면
                print("틀렸습니다. 다시 버튼을 눌러주세요.\n") #오답이며, 다시 버튼을 눌러달라고 화면에 띄움
                count+=1 #틀린 횟수 증가
                if(count==3): #틀린 횟수가 3번이 되면 반복문 탈출
                    break
                #오답 시 빨간색 led를 깜빡임
                GPIO.output(led_red, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_red, GPIO.LOW)
                time.sleep(0.5)
                #다시 1단계 led 순서를 알려줌
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                #1단계 led 순서가 끝났음을 의미
                GPIO.output(led_white1, GPIO.HIGH)
                GPIO.output(led_white2, GPIO.HIGH)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                GPIO.output(led_white2, GPIO.LOW)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)

    elif(chapter==2):
        #화면에 2단계 시작 메시지 띄우기
        print("2단계를 시작합니다.\n")
        time.sleep(0.5)
        #2단계에 해당하는 불빛 순서 들어옴
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        #2단계 순서 끝남을 의미
        GPIO.output(led_white1, GPIO.HIGH)
        GPIO.output(led_white2, GPIO.HIGH)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        GPIO.output(led_white2, GPIO.LOW)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        #사용자가 led 순서에 맞게 버튼을 누르도록 화면에 출력
        print("led 순서에 맞게 버튼을 눌러주세요.\n")
        while(chapter<3):
            answer=[5, 6, 0, 0, 0, 0, 0, 0, 0, 0] #정답 배열
            input(2) #2개 입력 받도록 input 함수 실행
            print("-----[2단계 입력]-----")
            print(record) #사용자가 최종 입력한 배열 record 출력
            print("-----[2단계 정답]-----")
            print(answer) #정답 배열 answer 출력

            if(answer==record): #정답 배열과 사용자 배열이 같으면
                print("정답입니다.\n") #정답입니다를 화면에 띄움
                time.sleep(0.5)
                #정답 시 초록색 led를 깜빡임
                GPIO.output(led_green, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_green, GPIO.LOW)
                chapter+=1 #단계 하나 증가

            elif(answer!=record): #정답 배열과 사용자 입력 배열이 같지 않다면
                print("틀렸습니다. 다시 버튼을 눌러주세요.\n") #오답이며, 다시 버튼을 눌러달라고 화면에 띄움
                count+=1 #틀린 횟수 증가
                if(count==3): #틀린 횟수가 3이 되면 반복문 탈출
                    break
                #오답 시 빨간색 led를 깜빡임
                GPIO.output(led_red, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_red, GPIO.LOW)
                time.sleep(0.5)
                #다시 2단계 led 순서를 알려줌
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                #2단계 led 순서가 끝났음을 의미
                GPIO.output(led_white1, GPIO.HIGH)
                GPIO.output(led_white2, GPIO.HIGH)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                GPIO.output(led_white2, GPIO.LOW)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)

    elif(chapter==3):
        #화면에 3단계 시작 메시지 띄우기
        print("3단계를 시작합니다.\n")
        time.sleep(0.5)
        #3단계에 해당하는 불빛 순서 들어옴
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        #3단계 순서 끝남을 의미
        GPIO.output(led_white1, GPIO.HIGH)
        GPIO.output(led_white2, GPIO.HIGH)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        GPIO.output(led_white2, GPIO.LOW)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        #사용자가 led 순서에 맞게 버튼을 누르도록 화면에 출력
        print("led 순서에 맞게 버튼을 눌러주세요.\n")
        while(chapter<4):
            answer=[6, 5, 4, 0, 0, 0, 0, 0, 0, 0] #정답 배열
            input(3) #3개 입력 받도록 input 함수 실행
            print("-----[3단계 입력]-----")
            print(record) #사용자가 최종 입력한 배열 record 출력
            print("-----[3단계 정답]-----")
            print(answer) #정답 배열 answer 출력

            if(answer==record): #정답 배열과 사용자 배열이 같으면
                print("정답입니다.\n") #정답입니다를 화면에 띄움
                time.sleep(0.5)
                #정답 시 초록색 led를 깜빡임
                GPIO.output(led_green, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_green, GPIO.LOW)
                chapter+=1 #단계 하나 증가

            elif(answer!=record): #정답 배열과 사용자 입력 배열이 같지 않다면
                print("틀렸습니다. 다시 버튼을 눌러주세요.\n") #오답이며, 다시 버튼을 눌러달라고 화면에 띄움
                count+=1 #틀린 횟수 증가
                if(count==3): #틀린 횟수가 3번이 되면 반복문 탈출
                    break
                #오답 시 빨간색 led를 깜빡임
                GPIO.output(led_red, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_red, GPIO.LOW)
                time.sleep(0.5)
                #다시 3단계 led 순서를 알려줌
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                #3단계 led 순서가 끝났음을 의미
                GPIO.output(led_white1, GPIO.HIGH)
                GPIO.output(led_white2, GPIO.HIGH)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                GPIO.output(led_white2, GPIO.LOW)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)


    elif(chapter==4):
        #화면에 4단계 시작 메시지 띄우기
        print("4단계를 시작합니다.\n")
        time.sleep(0.5)
        #4단계에 해당하는 불빛 순서 들어옴
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        #4단계 순서 끝남을 의미
        GPIO.output(led_white1, GPIO.HIGH)
        GPIO.output(led_white2, GPIO.HIGH)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        GPIO.output(led_white2, GPIO.LOW)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        #사용자가 led 순서에 맞게 버튼을 누르도록 화면에 출력
        print("led 순서에 맞게 버튼을 눌러주세요.\n")
        while(chapter<5):
            answer=[4, 5, 4, 6, 0, 0, 0, 0, 0, 0] #정답 배열
            input(4) #4개 입력 받도록 input 함수 실행
            print("-----[4단계 입력]-----")
            print(record) #사용자가 최종 입력한 배열 record 출력
            print("-----[4단계 정답]-----")
            print(answer) #정답 배열 answer 출력

            if(answer==record): #정답 배열과 사용자 배열이 같으면
                print("정답입니다.\n") #정답입니다를 화면에 띄움
                time.sleep(0.5)
                #정답 시 초록색 led를 깜빡임
                GPIO.output(led_green, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_green, GPIO.LOW)
                chapter+=1 #단계 하나 증가

            elif(answer!=record): #정답 배열과 사용자 입력 배열이 같지 않다면
                print("틀렸습니다. 다시 버튼을 눌러주세요.\n") #오답이며, 다시 버튼을 눌러달라고 화면에 띄움
                count+=1 #틀린 횟수 증가
                if(count==3): #틀린 횟수가 3번이 되면 반복문 탈출
                    break
                #오답 시 빨간색 led를 깜빡임
                GPIO.output(led_red, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_red, GPIO.LOW)
                time.sleep(0.5)
                #다시 4단계 led 순서를 알려줌
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                #4단계 led 순서가 끝났음을 의미
                GPIO.output(led_white1, GPIO.HIGH)
                GPIO.output(led_white2, GPIO.HIGH)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                GPIO.output(led_white2, GPIO.LOW)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)

    elif(chapter==5):
        #화면에 5단계 시작 메시지 띄우기
        print("5단계를 시작합니다.\n")
        time.sleep(0.5)
        #5단계에 해당하는 불빛 순서 들어옴
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        #5단계 순서 끝남을 의미
        GPIO.output(led_white1, GPIO.HIGH)
        GPIO.output(led_white2, GPIO.HIGH)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        GPIO.output(led_white2, GPIO.LOW)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        #사용자가 led 순서에 맞게 버튼을 누르도록 화면에 출력
        print("led 순서에 맞게 버튼을 눌러주세요.\n")
        while(chapter<6):
            answer=[5, 6, 4, 5, 4, 0, 0, 0, 0, 0] #정답 배열
            input(5) #5개 입력 받도록 input 함수 실행
            print("-----[5단계 입력]-----")
            print(record) #사용자가 최종 입력한 배열 record 출력
            print("-----[5단계 정답]-----")
            print(answer) #정답 배열 answer 출력

            if(answer==record): #정답 배열과 사용자 배열이 같으면
                print("정답입니다.\n") #정답입니다를 화면에 띄움
                time.sleep(0.5)
                #정답 시 초록색 led를 깜빡임
                GPIO.output(led_green, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_green, GPIO.LOW)
                chapter+=1 #단계 하나 증가

            elif(answer!=record): #정답 배열과 사용자 입력 배열이 같지 않다면
                print("틀렸습니다. 다시 버튼을 눌러주세요.\n") #오답이며, 다시 버튼을 눌러달라고 화면에 띄움
                count+=1 #틀린 횟수 증가
                if(count==3): #틀린 횟수가 3번이 되면 반복문 탈출
                    break
                #오답 시 빨간색 led를 깜빡임
                GPIO.output(led_red, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_red, GPIO.LOW)
                time.sleep(0.5)
                #다시 5단계 led 순서를 알려줌
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                #5단계 led 순서가 끝났음을 의미
                GPIO.output(led_white1, GPIO.HIGH)
                GPIO.output(led_white2, GPIO.HIGH)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                GPIO.output(led_white2, GPIO.LOW)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)


    elif(chapter==6):
        #화면에 6단계 시작 메시지 띄우기
        print("6단계를 시작합니다.\n")
        time.sleep(0.5)
        #6단계에 해당하는 불빛 순서 들어옴
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        #6단계 순서 끝남을 의미
        GPIO.output(led_white1, GPIO.HIGH)
        GPIO.output(led_white2, GPIO.HIGH)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        GPIO.output(led_white2, GPIO.LOW)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        #사용자가 led 순서에 맞게 버튼을 누르도록 화면에 출력
        print("led 순서에 맞게 버튼을 눌러주세요.\n")
        while(chapter<7):
            answer=[6, 6, 4, 4, 6, 5, 0, 0, 0, 0] #정답 배열
            input(6) #6개 입력 받도록 input 함수 실행
            print("-----[6단계 입력]-----")
            print(record) #사용자가 최종 입력한 배열 record 출력
            print("-----[6단계 정답]-----")
            print(answer) #정답 배열 answer 출력

            if(answer==record): #정답 배열과 사용자 배열이 같으면
                print("정답입니다.\n") #정답입니다를 화면에 띄움
                time.sleep(0.5)
                #정답 시 초록색 led를 깜빡임
                GPIO.output(led_green, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_green, GPIO.LOW)
                chapter+=1 #단계 하나 증가

            elif(answer!=record): #정답 배열과 사용자 입력 배열이 같지 않다면
                print("틀렸습니다. 다시 버튼을 눌러주세요.\n") #오답이며, 다시 버튼을 눌러달라고 화면에 띄움
                count+=1 #틀린 횟수 증가
                if(count==3): #틀린 횟수가 3번이 되면 반복문 탈출
                    break
                #오답 시 빨간색 led를 깜빡임
                GPIO.output(led_red, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_red, GPIO.LOW)
                time.sleep(0.5)
                #다시 6단계 led 순서를 알려줌
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                #6단계 led 순서가 끝났음을 의미
                GPIO.output(led_white1, GPIO.HIGH)
                GPIO.output(led_white2, GPIO.HIGH)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                GPIO.output(led_white2, GPIO.LOW)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)

    elif(chapter==7):
        #화면에 7단계 시작 메시지 띄우기
        print("7단계를 시작합니다.\n")
        time.sleep(0.5)
        #7단계에 해당하는 불빛 순서 들어옴
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        #7단계 순서 끝남을 의미
        GPIO.output(led_white1, GPIO.HIGH)
        GPIO.output(led_white2, GPIO.HIGH)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        GPIO.output(led_white2, GPIO.LOW)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        #사용자가 led 순서에 맞게 버튼을 누르도록 화면에 출력
        print("led 순서에 맞게 버튼을 눌러주세요.\n")
        while(chapter<8):
            answer=[4, 6, 5, 5, 6, 5, 4, 0, 0, 0] #정답 배열
            input(7) #7개 입력 받도록 input 함수 실행
            print("-----[7단계 입력]-----")
            print(record) #사용자가 최종 입력한 배열 record 출력
            print("-----[7단계 정답]-----")
            print(answer) #정답 배열 answer 출력

            if(answer==record): #정답 배열과 사용자 배열이 같으면
                print("정답입니다.\n") #정답입니다를 화면에 띄움
                time.sleep(0.5)
                #정답 시 초록색 led를 깜빡임
                GPIO.output(led_green, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_green, GPIO.LOW)
                chapter+=1 #단계 하나 증가

            elif(answer!=record): #정답 배열과 사용자 입력 배열이 같지 않다면
                print("틀렸습니다. 다시 버튼을 눌러주세요.\n") #오답이며, 다시 버튼을 눌러달라고 화면에 띄움
                count+=1 #틀린 횟수 증가
                if(count==3): #틀린 횟수가 3번이 되면 반복문 탈출
                    break
                #오답 시 빨간색 led를 깜빡임
                GPIO.output(led_red, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_red, GPIO.LOW)
                time.sleep(0.5)
                #다시 7단계 led 순서를 알려줌
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                #7단계 led 순서가 끝났음을 의미
                GPIO.output(led_white1, GPIO.HIGH)
                GPIO.output(led_white2, GPIO.HIGH)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                GPIO.output(led_white2, GPIO.LOW)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)

    elif(chapter==8):
        #화면에 8단계 시작 메시지 띄우기
        print("8단계를 시작합니다.\n")
        time.sleep(0.5)
        #8단계에 해당하는 불빛 순서 들어옴
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        #8단계 순서 끝남을 의미
        GPIO.output(led_white1, GPIO.HIGH)
        GPIO.output(led_white2, GPIO.HIGH)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        GPIO.output(led_white2, GPIO.LOW)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        #사용자가 led 순서에 맞게 버튼을 누르도록 화면에 출력
        print("led 순서에 맞게 버튼을 눌러주세요.\n")
        while(chapter<9):
            answer=[5, 4, 6, 4, 5, 6, 6, 4, 0, 0] #정답 배열
            input(8) #8개 입력 받도록 input 함수 실행
            print("-----[8단계 입력]-----")
            print(record) #사용자가 최종 입력한 배열 record 출력
            print("-----[8단계 정답]-----")
            print(answer) #정답 배열 answer 출력

            if(answer==record): #정답 배열과 사용자 배열이 같으면
                print("정답입니다.\n") #정답입니다를 화면에 띄움
                time.sleep(0.5)
                #정답 시 초록색 led를 깜빡임
                GPIO.output(led_green, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_green, GPIO.LOW)
                chapter+=1 #단계 하나 증가

            elif(answer!=record): #정답 배열과 사용자 입력 배열이 같지 않다면
                print("틀렸습니다. 다시 버튼을 눌러주세요.\n") #오답이며, 다시 버튼을 눌러달라고 화면에 띄움
                count+=1 #틀린 횟수 증가
                if(count==3): #틀린 횟수가 3번이 되면 반복문 탈출
                    break
                #오답 시 빨간색 led를 깜빡임
                GPIO.output(led_red, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_red, GPIO.LOW)
                time.sleep(0.5)
                #다시 8단계 led 순서를 알려줌
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                #8단계 led 순서가 끝났음을 의미
                GPIO.output(led_white1, GPIO.HIGH)
                GPIO.output(led_white2, GPIO.HIGH)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                GPIO.output(led_white2, GPIO.LOW)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)

    elif(chapter==9):
        #화면에 9단계 시작 메시지 띄우기
        print("9단계를 시작합니다.\n")
        time.sleep(0.5)
        #9단계에 해당하는 불빛 순서 들어옴
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        #9단계 순서 끝남을 의미
        GPIO.output(led_white1, GPIO.HIGH)
        GPIO.output(led_white2, GPIO.HIGH)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        GPIO.output(led_white2, GPIO.LOW)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        #사용자가 led 순서에 맞게 버튼을 누르도록 화면에 출력
        print("led 순서에 맞게 버튼을 눌러주세요.\n")
        while(chapter<10):
            answer=[6, 5, 4, 6, 6, 4, 4, 5, 6, 0] #정답 배열
            input(9) #9개 입력 받도록 input 함수 실행
            print("-----[9단계 입력]-----")
            print(record) #사용자가 최종 입력한 배열 record 출력
            print("-----[9단계 정답]-----")
            print(answer) #정답 배열 answer 출력

            if(answer==record): #정답 배열과 사용자 배열이 같으면
                print("정답입니다.\n") #정답입니다를 화면에 띄움
                time.sleep(0.5)
                #정답 시 초록색 led를 깜빡임
                GPIO.output(led_green, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_green, GPIO.LOW)
                chapter+=1 #단계 하나 증가

            elif(answer!=record): #정답 배열과 사용자 입력 배열이 같지 않다면
                print("틀렸습니다. 다시 버튼을 눌러주세요.\n") #오답이며, 다시 버튼을 눌러달라고 화면에 띄움
                count+=1 #틀린 횟수 증가
                if(count==3): #틀린 횟수가 3번이 되면 반복문 탈출
                    break
                #오답 시 빨간색 led를 깜빡임
                GPIO.output(led_red, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_red, GPIO.LOW)
                time.sleep(0.5)
                #다시 9단계 led 순서를 알려줌
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                #9단계 led 순서가 끝났음을 의미
                GPIO.output(led_white1, GPIO.HIGH)
                GPIO.output(led_white2, GPIO.HIGH)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                GPIO.output(led_white2, GPIO.LOW)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)

    elif(chapter==10):
        #화면에 10단계 시작 메시지 띄우기
        print("10단계를 시작합니다.\n")
        time.sleep(0.5)
        #10단계에 해당하는 불빛 순서 들어옴
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.5)
        #10단계 순서 끝남을 의미
        GPIO.output(led_white1, GPIO.HIGH)
        GPIO.output(led_white2, GPIO.HIGH)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_white1, GPIO.LOW)
        GPIO.output(led_white2, GPIO.LOW)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.5)
        #사용자가 led 순서에 맞게 버튼을 누르도록 화면에 출력
        print("led 순서에 맞게 버튼을 눌러주세요.\n")
        while(chapter<11):
            answer=[4, 4, 6, 5, 5, 4, 6, 5, 5, 4] #정답 배열
            input(10) #10개 입력 받도록 input 함수 실행
            print("-----[10단계 입력]-----")
            print(record) #사용자가 최종 입력한 배열 record 출력
            print("-----[10단계 정답]-----")
            print(answer) #정답 배열 answer 출력

            if(answer==record): #정답 배열과 사용자 배열이 같으면
                print("정답입니다.\n") #정답입니다를 화면에 띄움
                time.sleep(0.5)
                #정답 시 초록색 led를 깜빡임
                GPIO.output(led_green, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_green, GPIO.LOW)
                chapter+=1 #단계 하나 증가 -> 11단계이므로 반복문 탈출

            elif(answer!=record): #정답 배열과 사용자 입력 배열이 같지 않다면
                print("틀렸습니다. 다시 버튼을 눌러주세요.\n") #오답이며, 다시 버튼을 눌러달라고 화면에 띄움
                count+=1 #틀린 횟수 증가
                if(count==3): #틀린 횟수가 3번이 되면 반복문 탈출
                    break
                #오답 시 빨간색 led를 깜빡임
                GPIO.output(led_red, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_red, GPIO.LOW)
                time.sleep(0.5)
                #다시 10단계 led 순서를 알려줌
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white2, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                time.sleep(0.5)
                #10단계 led 순서가 끝났음을 의미
                GPIO.output(led_white1, GPIO.HIGH)
                GPIO.output(led_white2, GPIO.HIGH)
                GPIO.output(led_white3, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_white1, GPIO.LOW)
                GPIO.output(led_white2, GPIO.LOW)
                GPIO.output(led_white3, GPIO.LOW)
                time.sleep(0.5)

        #틀린 횟수가 3번 미만이고, 10단계를 모두 통과했을 떄
        print("축하합니다! 모든 단계를 통과하셨습니다.")
        print("최종 단계: 10단계")
        #흰색 led 3개가 파도 치듯이 깜빡이며 게임 종료
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_white1, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white1, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_white2, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white2, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_white1, GPIO.HIGH)
        GPIO.output(led_white2, GPIO.HIGH)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white1, GPIO.LOW)
        GPIO.output(led_white2, GPIO.LOW)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_white1, GPIO.HIGH)
        GPIO.output(led_white2, GPIO.HIGH)
        GPIO.output(led_white3, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_white1, GPIO.LOW)
        GPIO.output(led_white2, GPIO.LOW)
        GPIO.output(led_white3, GPIO.LOW)
        time.sleep(0.2)


if(count>=3): #틀린 횟수가 3번 이상이면
    print("[게임 실패] 최종 단계: ", chapter-1, "단계") #게임 실패 메시지와 함께 최종 단계 출력
    #빨간색 led를 3번 깜빡이며 게임 종료
    GPIO.output(led_red, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(led_red, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(led_red, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(led_red, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(led_red, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(led_red, GPIO.LOW)
    time.sleep(0.5)