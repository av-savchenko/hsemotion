# HSEmotion Python Library for Facial Emotion Recognition
[![Downloads](https://static.pepy.tech/personalized-badge/hsemotion?period=total&units=international_system&left_color=grey&right_color=blue&left_text=pip%20installs)](https://pepy.tech/project/hsemotion)
[![pypi package](https://img.shields.io/badge/version-v0.2.0-blue)](https://pypi.org/project/hsemotion)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/classifying-emotions-and-engagement-in-online/facial-expression-recognition-on-affectnet)](https://paperswithcode.com/sota/facial-expression-recognition-on-affectnet?p=classifying-emotions-and-engagement-in-online)

## License

The code of HSEmotion Python Library is released under the Apache-2.0 License. There is no limitation for both academic and commercial usage.

## Installing

```
    python setup.py install
```

It is also possible to install it via pip:
```
    pip install hsemotion
```

## Usage

```
    from hsemotion.facial_emotions import HSEmotionRecognizer
    model_name='enet_b0_8_best_afew'
    fer=HSEmotionRecognizer(model_name=model_name,device='cpu') # device is cpu or gpu
    emotion,scores=fer.predict_emotions(face_img,logits=True)
```

The following values of `model_name` parameter are supported:
- enet_b0_8_best_vgaf
- enet_b0_8_best_afew
- enet_b0_8_va_mtl
- enet_b2_8
- enet_b2_7

The method `predict_emotions` returns both the string value of predicted emotions (Anger, Contempt, Disgust, Fear, Happiness, Neutral, Sadness, or Surprise) and scores at the output of the last layer. 
If the `logits` parameter is set to `True` (by default), the logits are returned, otherwise, the posterior probabilities are estimated from the logits using softmax.

In addition, it is possible to extract visual embeddings for classifier learning
```
    features=fer.extract_features(face_img)
```

The versions of these methods for a batch of images are also available
```
    emotions,scores=fer.predict_multi_emotions(face_img_list,logits=False)
    features=fer.extract_multi_features(face_img_list)
```

Complete usage example is available in the [test_hsemotion_package.ipynb](demo/test_hsemotion_package.ipynb). It is necessary to run the following line to run the demo script:
```
run pip install facenet-pytorch
```

The details about training of the models are available in the [main repository](https://github.com/HSE-asavchenko/face-emotion-recognition)
