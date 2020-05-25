import pafy
import youtube_dl

# url of video
url = input("input video url :")

#create stream object
mystream = pafy.new(url)

#videostreams object
vidstream = mystream.videostreams
#audiostreams object
audstream = mystream.audiostreams

select = input('For audio download enter "A", for video download enter "V": ').upper()

if select == 'A':
    print('The audiostreams are: \n ', [j for j in enumerate(audstream, start=0)])
    choice = eval(input('Enter audio number: '))     #instantiate your choice of audio quality

    print('Downloading...', audstream[choice])
    audstream[choice].download()                    #download the audio
    print('Download finished.')

elif select == 'V':
    print('The videostreams are: \n', [j for j in enumerate(vidstream, start=0)])
    choice = eval(input('Enter video number: '))     #instantiate your choice of video quality

    print('Downloading...', vidstream[choice])
    vidstream[choice].download(remux_audio=True)                    #download your video
    print('Download finished.')

else:
    print('Invalid entry.')
