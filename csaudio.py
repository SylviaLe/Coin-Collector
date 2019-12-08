# csaudio.py

# import csaudio ; reload(csaudio) ; from csaudio import *

import wave
wave.big_endian=0

def get_data(fileName):
    """ the file needs to be in .wav format
        there are lots of conversion programs online, however,
        to create .wav from .mp3 and other formats
    """
    # this will complain if the file isn't there!
    inputFile = wave.open(fileName, 'rb')
    params = inputFile.getparams()
    #printParams(params)
    rawFrames = inputFile.readframes(params[3])
    # need to extract just one channel of sound data at the right width...
    inputFile.close()
    return params, rawFrames

def printParams(params):
    print('Parameters:')
    print('  nchannels:', params[0])
    print('  sampwidth:', params[1])
    print('  framerate:', params[2])
    print('  nframes  :', params[3])
    print('  comptype :', params[4])
    print('  compname :', params[5])

def transformRawFramesToSamples(params, rawFrames):
    """ transformRawFramesToSamples transforms raw frames to
        floating-point samples.
    """

    samples = rawFrames

    # give parameters nicer names
    numChannels = params[0]
    sampleWidth = params[1]
    numSamples  = params[3]

    if sampleWidth == 1:

        for i in range(numSamples):
            if samples[i] < 128:
                samples[i] *= 256.0       # Convert to 16-bit range, floating
            else:
                samples[i] = (samples[i] - 256) * 256.0

    elif sampleWidth == 2:

        newSamples = numSamples * numChannels * [0]

        for i in range(numSamples * numChannels):
            # The wav package gives us the data in native
            # "endian-ness".  The clever indexing with wave.big_endian
            # makes sure we unpack in the proper byte order.
            sampleValue = samples[2*i + 1 - wave.big_endian] * 256 \
              + samples[2*i + wave.big_endian]
            if sampleValue >= 32768:
                sampleValue -= 65536
            newSamples[i] = float(sampleValue)

        samples = newSamples

    else:
        print('A sample width of', params[1], 'is not supported.')
        print('Returning silence.')
        samples = numSamples * [0.0]

    if numChannels == 2:
        # Mix to mono
        newSamples = numSamples * [0]
        for i in range(numSamples):
            newSamples[i] = (samples[2 * i] + samples[2 * i + 1]) / 2.0
        samples = newSamples

    return samples

def transformSamplesToRawFrames(params, samples):
    """ transformSamplesToRawFrames is transformRawFramesToSamples inverse,
        i.e. from samples to rawframes.
    """
    if params[1] == 1:                 # one byte per sample
        samples = [int(x + 127.5) for x in samples]
        #print('max, min are', max(samples), min(samples))
    elif params[1] == 2:               # two bytes per sample
        bytesamps = (2*params[3])*[0]  # start at all zeros
        for i in range(params[3]):
            # maybe another rounding strategy in the future?
            intval = int(samples[i])
            if intval >  32767: intval = 32767
            if intval < -32767: intval = -32767  # maybe could be -32768

            if intval < 0: intval += 65536 # Handle negative values

            # The wav package wants its data in native "endian-ness".
            # The clever indexing with wave.big_endian makes sure we
            # pack in the proper byte order.
            bytesamps[2*i + 1 - wave.big_endian] = intval // 256
            bytesamps[2*i + wave.big_endian] = intval % 256

        samples = bytesamps
        #print('max, min are', max(samples), min(samples))

    return bytes(samples)

def readWav(fileName):
    """ readWav returns the audio data in the format

            [[d0, d1, d2, ...], sampleRate]

        where each d0, d1, d2, ... is a floating-point value
        and sampling rate is an integer, representing the
        frequency with which audio samples were taken
    """
    params, rawFrames = get_data(fileName)
    samples = transformRawFramesToSamples(params, rawFrames)

    numChannels = params[0]
    dataWidth = params[1]
    sampleRate = params[2]
    numSamples = params[3]

    print()
    print('You opened', fileName, 'which has')
    print('   ', numSamples, 'audio samples, taken at')
    print('   ', sampleRate, 'hertz (samples per second).')
    print()

    return [samples, sampleRate]

def write_data(params=None, rawFrames=None, filename="out.wav"):
    """ back out to .wav format """

    fout = wave.open(filename, 'wb')
    if params:
        fout.setparams(params)
        if rawFrames:
            fout.writeframes(rawFrames)
        else:
            print('no frames')
    else:
        print('no params')

    fout.close()

def writeWav(data, samplingRate, fileName="out.wav"):
    """ writeWav outputs a .wav file whose
            first parameter is the audio data as a list

            second parameter is the integer sampling rate
                the minimum allowed value is 1 hertz (1 sample per second),
                which is well under human hearing range

            third parameter is the output file name
                if no name is specified, this parameter defaults to 'out.wav'
    """
    frameRate = int(samplingRate)
    if frameRate < 0:
        frameRate = -frameRate
    if frameRate < 1:
        frameRate = 1

    # always 1 channel and 2 output bytes per sample
    params = [1, 2, frameRate, len(data), "NONE", "No compression"]

    # convert to raw frames
    rawFrames = transformSamplesToRawFrames(params, data)
    write_data(params, rawFrames, fileName)

    print()
    print('You have written the file', fileName, 'which has')
    print('   ', len(data), 'audio samples, taken at')
    print('   ', samplingRate, 'hertz.')
    print()

# a useful thing to have... can be done all in sw under windows...
import os

if os.name == 'nt':
    import winsound
elif os.uname()[0] == 'Linux':
    import ossaudiodev

def play(filename):
    """ play a .wav file for Windows, Linux, or Mac
        for Mac, you need to have the "play"
        application in the current folder (.)
    """
    if type(filename) != type(''):
        raise(TypeError, 'filename must be a string')
    if os.name == 'nt':
        winsound.PlaySound(filename, winsound.SND_FILENAME)
    elif os.uname()[0] == 'Linux':
        (params, frames) = get_data(filename)
        oss = ossaudiodev.open('w')
        if wave.big_endian:
            if params[1] == 1:
                oss.setfmt(ossaudiodev.AFMT_S8_BE)
            else:
                oss.setfmt(ossaudiodev.AFMT_S16_BE)
        else:
            if params[1] == 1:
                oss.setfmt(ossaudiodev.AFMT_S8_LE)
            else:
                oss.setfmt(ossaudiodev.AFMT_S16_LE)
        oss.channels(params[0])
        oss.speed(params[2])
        oss.writeall(frames)
        oss.close()
    # assume MAC, if not a Windows or Linux machine
    # if you're using another OS, you'll need to adjust this...
    else:
        os.system(('./play ' + filename))

