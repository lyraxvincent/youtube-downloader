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
    print('The audiostreams are: \n ', [j for j in enumerate(audstream)])
    for i in range(len(audstream)):
        print('For audio {} enter {}'.format(i+1, i))
    choice = eval(input('Enter your choice: '))     #instantiate your choice of audio quality

    print('Downloading...', audstream[choice])
    audstream[choice].download()                    #download the audio
    print('Download finished.')

elif select == 'V':
    print('The videostreams are: \n', [j for j in enumerate(vidstream)])
    for i in range(len(vidstream)):
        print('For video {} enter {}'.format(i+1, i))
    choice = eval(input('Enter your choice: '))     #instantiate your choice of video quality

    print('Downloading...', vidstream[choice])
    vidstream[choice].download()                    #download your video
    print('Download finished.')

else:
    print('Invalid entry.')