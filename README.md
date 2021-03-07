## robo-tim
A novel neural net to deepfake a former coworker

# Anyone can make can deepfake. Not everyone can do it on a budget

robo-tim aims to explore the possibility of creating fast, lightweight datasets and models by focusing on a particular subject. The research is geared toward producing quality output with far less data and processing than traditional networks demand. It also does not rely on existing datasets ot pretrained models, instead using bespoke datasets that are tailored to a given source.

## How to go about this

### Creating the dataset

Because I am on an accelerated timeline, a lot of brute force is required. Since the dataset is significantly smaller than average, this is feasibile enough to attempt before futher exploration into using existing datasets as a first pass to refduce the burden of manual dataset creation and training. However, it does have the potential advantage of ideal discrimination and validation, becaues synthetic videos can easily be compared to the source. This may result in superior results which would otherwise be much more resource intensive to acheive.

Using videos and keynote speeches downloaded from YouTube with auto closed captioning, the process of STT is trivial, aside from the diligence of manual alignment and correctiom. which will be perfunctory for the sake of time. The TTLM format can easily be converted into LJSpeech format, making for rapid creation of the dataset. It also has the advantage of producing utterances ideal for LJS dataset creation, which can be sliced automatically using wrappers programs such as ffmpeg.

### Training the dataset

Once the dataset is created, the model will learn from existing source data segregated from the dataset. This will make for accurate validation and excellent discrimination.

### Adding the visual component

Once the TTS sytnhesizer is created, the next step will be facial modeling, which will also be drastically lighter than normal becuase we are dealing with a known face captured in ideal situations. From there, facial alignment and phoneme identification will be used to create a lightweight, accurate lip sync.

As I do not have much motion footage, the plan is to focus on mapping a source face to the target and, if possible, real-time vocoding, wich I hope to be resource light enough to host freely on a PaaS provider using Flask.

## More details to come
