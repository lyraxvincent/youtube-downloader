import pafy
import youtube_dl
from pytube import YouTube # for videos
import ffmpeg # audio - video merging
import os
import shutil # remove non-empty directories

if not 'video' in os.listdir('.'):
    os.mkdir('video/'); os.mkdir('audio/')

# url of video
url = input("input video url: ")

#create stream object
mystream = pafy.new(url)

#audiostreams object
audstream = mystream.audiostreams

select = input('For audio download enter "A", for video download enter "V": ').upper()

if select == 'A':
    print('The audiostreams are: \n ', [audio for audio in enumerate(audstream, start=0)])
    choice = eval(input('Enter audio number: '))     #instantiate your choice of audio quality

    print('Downloading...', audstream[choice])
    audstream[choice].download()                    #download the audio
    print('Download finished.')

elif select == 'V':
    
    yt = YouTube(url)
    title = str(yt.title)
    vidstreams = yt.streams.filter(adaptive=True, file_extension='mp4').order_by('resolution')[7:] # starting from 480p

    print("Available video streams: ", [(tag.itag, tag.resolution) for tag in vidstreams])
    tag_number = input("Enter video tag number: ")
    yt.streams.get_by_itag(tag_number).download(output_path='video/', filename=title+'.mp4')
    yt.streams.filter(abr='128kbps')[0].download(output_path='audio/', filename=title+'.mp4')

    # merge audio to video
    input_video = ffmpeg.input(f'audio/{title}.mp4')
    input_audio = ffmpeg.input(f'video/{title}.mp4')
    ffmpeg.output(input_video, input_audio, f'{yt.title}.mp4', vcodec='copy', acodec='aac', strict='experimental').run()

    # remove created directories
    shutil.rmtree('video'); shutil.rmtree('audio')

    print('Download finished.')

else:
    print('Invalid entry.')
