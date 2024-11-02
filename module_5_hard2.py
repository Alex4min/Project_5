import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return hash(self.password)

    def __repr__(self):
        return f'User(nickname = {self.nickname}, age = {self.age})'

class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'Video(title = {self.title}, duration = {self.duration})'

    def __contains__(self, item):
        return item in self.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos= []
        self.current_user = None

    def log_in(self, nickname, password):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
                return
            else:
                print('Ошибка! Неверный логин или пароль.')
                return

    def register(self,nickname, password, age):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *films):
        for film in films:
            if film.title not in [video.title for video in self.videos]:
                self.videos.append(film)

    def get_videos(self, search: str):
        play_list = []
        for video in self.videos:
            if search.lower() in video.title.lower():
                play_list.append(video.title)
        return play_list
        # return (video.title for video in self.videos if search in video.title.lower())

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for video in self.videos:
            if title == video.title:
                if self.current_user and self.current_user.age < 18:
                    print('Вам нет 18. Пожалуйста, покиньте страницу.')
                    return
                else:
                    for second in range(video.time_now, video.duration):
                        print(second, end=' ', flush=True)
                        time.sleep(1)
                        video.time_now += 1
                    video.time_now = 0
                    print('Конец видео')


if __name__ == '__main__':
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
