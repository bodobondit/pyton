from time import sleep
class User():
    def __init__(self,nickname,password,age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)
    def __gt__(self, other):
        if isinstance(other, int):
            return True if self.age > other else False
        if isinstance(other, User):
            return True if self.age > other.age else False
    def __str__(self):
        return self.nickname
class Video():
    def __init__(self,title,duration,time_now = 0,adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    def __repr__(self):
        return self.title
    def __str__(self):
        return self.title

class UrTube():
    def __init__(self):
        self.Users = []
        self.Videos = []
        self.current_user = None
    def log_in(self,nickname,password):
        for users_login in self.Users:
            if nickname == users_login.nickname and hash(password) == users_login.password:
                self.current_user = users_login
    def register(self,nickname,password,age):
        if len(self.Users) == 0:
            self.Users.append(User(nickname, password, age))
            self.log_in(nickname, password)
        else:
            no_user = True
            for reg_user in self.Users:
                if reg_user.nickname ==  nickname:
                    print(f'Пользователь {nickname} уже существует')
                    no_user = False
                    break
            if no_user:
                self.Users.append(User(nickname,password,age))
                self.log_in(nickname,password)
    def log_out(self):
        self.current_user = None
    def __contains__(self, item):
        return item in self.Videos
    def add(self, *other):
        for video in other:
             if video is not self.Videos:
                self.Videos.append(video)
    def get_videos(self,search):
        list_video = []
        for video in self.Videos:
            if search.lower() in video.title.lower():
                list_video.append(video)
        return list_video
    def watch_video(self,name_video):
        for video in self.Videos:
            if name_video in video.title:
                if self.current_user:
                    if self.current_user.age > 18:
                        if video.time_now == 0:
                            for i in range(1,video.duration+1):
                                sleep(1)
                                print(i," ",end='')
                        else:
                            for i in range(video.time_now,video.duration+1):
                                sleep(1)
                                print(i," ",end='')
                        video.time_now = 0
                        print(" Конец видео")
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    print("Войдите в аккаунт, чтобы смотреть видео")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



