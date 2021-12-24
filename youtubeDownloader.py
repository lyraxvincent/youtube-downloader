from pytube import YouTube # for videos
from pytube.cli import on_progress
import ffmpeg # audio - video merging
import os
import shutil # remove non-empty directories
from pydub import AudioSegment # audio conversion to mp3


# url of video
url = input("input video url: ")

# YouTube object
yt = YouTube(url, on_progress_callback=on_progress)
title = str(yt.title)

select = input('For audio download enter "A", for video download enter "V": ').upper()

if select == 'A':

    audio_streams = yt.streams.filter(only_audio=True)
    print("Available audio streams: ", [(tag.itag, '[' + tag.abr + ' : ' + tag.audio_codec + ']') for tag in audio_streams])
    tag_number = input("Enter audio tag number: ")
    yt.streams.get_by_itag(tag_number).download(filename=title+'.mp4')

    # convert to mp3
    mp4_audio = AudioSegment.from_file(f"{title}.mp4", 'mp4')
    mp4_audio.export(f"{title}.mp3", format="mp3")
    # delete previous format
    os.remove(f"{title}.mp4")

elif select == 'V':

    if not ('video' in os.listdir('.')) or ('audio' not in os.listdir('.')):
        os.mkdir('video'); os.mkdir('audio')
    
    vidstreams = yt.streams.filter(adaptive=True, file_extension='mp4').order_by('resolution')

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
