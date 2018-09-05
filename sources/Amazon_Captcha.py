# -*- coding: utf-8 -*-
import base64
import requests


# Reference :https://cloud.google.com/vision/docs/detecting-text?hl=zh-TW#vision-text-detection-protocol
# token ken : AIzaSyBwqm82G8S9ZMAAKgv2-RSosOVQmmgX5Og

def detect_text(image_file, access_token=None):

    with open(image_file, 'rb') as image:
        base64_image = base64.b64encode(image.read()).decode()

    #url = 'https://vision.googleapis.com/v1/images:annotate?key={}'.format(access_token)
    #url = 'https://vision.googleapis.com/v1p2beta1/images:annotate?key={}'.format(access_token)
    url = 'https://vision.googleapis.com/v1p3beta1/images:annotate?key={}'.format(access_token)
    header = {'Content-Type': 'application/json'}
    body = {
        'requests': [{
            'image': {
                'content': base64_image,
            },
            'features': [{
                'type': 'TEXT_DETECTION',
                'maxResults': 1,
            }]

        }]
    }
    response = requests.post(url, headers=header, json=body).json()
    text = response['responses'][0]['textAnnotations'][0]['description'] if len(response['responses'][0]) > 0 else ''
    return text