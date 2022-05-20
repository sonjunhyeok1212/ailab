#당신의 정보를 적는 곳 
no = ["없음", "아직 없음", "x"]
name = input("당신의 이름은? ")
school = input("당신의 학교 ")
age = input("당신의 나이는?" )
habbit = input("당신의 취미는? ")
dream = input("당신의 꿈은? ")
favoritfood = input("당신이 좋아하는 음식은?")

#자기소개 적는곳
news ="이제부터 자기소개를 시작하겠습니다."
news = news + "저는  "+ school+ "에 다니는 "+name+"입니다."
news = news + "저는 " + age + " 살 입니다."
news = news + "저의 취미는 " + habbit+"이고"
if dream in no :
    news = news + "저의 꿈은 아직은 없고"
else:
    news = news + "저의 꿈은 "+ dream +"이고"
news = news + "제가 좋아하는 음식은 " + favoritfood+"입니다. "
news = news + "이상 자기소개를 마치겠습니다."

print(news)


 #음성으로 들려주는 곳
from gtts import gTTS
import playsound
import os #파일관리 함수
 
tts=gTTS(text=news,lang='ko')
tts.save("my.interduce.mp3") #기존에 같은 이름의 파일이 존재하면 에러가 생김
playsound.playsound("my.interduce.mp3",False) #True 멈춰서 해당 하나만 재생, False 밑에 코드랑 동시재생(배경음악)
playsound.playsound("THURSDAY MORNING CHILL JAZZ Sweet March Morning - Spring Jazz &amp Bossa Nova for Good Mood.mp3",True)
os.remove("my.interduce.mp3")
os.remove("THURSDAY MORNING CHILL JAZZ Sweet March Morning - Spring Jazz &amp Bossa Nova for Good Mood.mp3")