import pytube

url = input()

pytube.YouTube(url).streams.get_highest_resolution().download('C:/Users/rosha/Desktop')