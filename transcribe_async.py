#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Speech API sample application using the REST API for async
batch processing.

Example usage:
    python transcribe_async.py resources/audio.raw
    python transcribe_async.py gs://cloud-samples-tests/speech/vr.flac
"""

import argparse
import io
import os
from pydub import AudioSegment
from google.cloud import speech


file_list = open('file_list.txt', 'w')

# [START speech_transcribe_async_gcs]
def transcribe_gcs(wav_num):

    # load the wav locally
    full_wav = AudioSegment.from_wav(f'./content/audio/{wav_num}.wav')
    
    gcs_uri = f'gs://robo-tim/{wav_num}.wav'
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        #encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code="en-US",
        enable_word_time_offsets=True,
        enable_automatic_punctuation=True
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=200)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    sentence_num = 1
    for result in response.results:
        sentence = ""
        sentence_start = None
        sentence_end = None
        for word_info in result.alternatives[0].words:
            word = word_info.word
            start_time = word_info.start_time
            if sentence_start is None: sentence_start = start_time
            
            sentence = f'{sentence} {word}'   
            if word.endswith('.'):
                sentence_send = word_info.end_time
                sentence = sentence.strip()
                # Create filename
                filename = f'wavs/TM00{wav_num}-{str(sentence_num).rjust(4, "0")}.wav'

                print(f"Sentence: {sentence.strip()}, sentence_start: {sentence_start}, sentence_end: {sentence_end})")
                #use pydub to slice and export in th proper directory structure
                wav_segnment = full_wav[int(sentence_start * 1000):int(sentence_end * 1000)]
                wav_segment.export(filename, format="wav", parameters['-ac', '1', '-ar', '16000'])

                #write file|sentence mapping to file_list
                file_list.write(f'{filename}|sentence{os.lenesep}')

                sentence = ""
                sentence_start = None
                sentence_num = sentence_num + 1

# [END speech_transcribe_async_gcs]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )

    for i in range(1, 10)
        transcribe_gcs(i)

    file_list.close()