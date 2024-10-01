#Inheritance type data 
class Grandfather: 
    jomi = "10 Biga"
    Bari = "10 ta"
    gari = "Parado"
    mot  = "R15"
    def property(self): 
        print(f"My grand father's was {self.jomi} property")
        print(f"My grand father's was {self.Bari} House")
        print(f"My grand father's was {self.gari} in Dhaka")
        print(f"MY grand father's was {self.mot} in Borishal")

class Father(Grandfather): 
      pass
class Son(Father): 
     pass 
class son_child(Son):
     pass 
ob = son_child()
ob.property()

#Do you know how to inheritance 

class YoutubeID: 
     __myvideo = 0 
     def uplodvideo(self, uplod): 
          self.__myvideo += uplod 
          print("Video Uplod Successfull")
     def deletevideo(self, uplod): 
          self.__myvideo -= uplod
          print("Delete successfull")
     def check_video(self): 
          return self.__myvideo
up = YoutubeID()
up.uplodvideo(1)
print(up.check_video())

def setting(self, option): 
     