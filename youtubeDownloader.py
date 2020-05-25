import pafy
import youtube_dl

# url of video
url = input("input video url :")

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
    print('Available videostreams with sound are: \n', [video for video in enumerate(mystream.streams, start=0)])
    choice = eval(input('Enter videostream number: '))     #instantiate your choice of video quality

    print('Downloading...', mystream.streams[choice])
    mystream.streams[choice].download()                    #download the video
    print('Download finished.')

else:
    print('Invalid entry.')
