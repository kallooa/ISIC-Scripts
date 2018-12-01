
"""
Create a new study of MSK-3_1 for Metaphoric Consensus features.
"""

import csv
import json
import os
import pandas as pd

from isic_api import ISICApi

# Initialize the API; a login by a study administrator is required
api = ISICApi(
    username='',
    password=''
)

#for study_num in range(1,6):

#study_num = 6

csv_name = ''
study_name = '' #"EASY_STUDY_"+str(study_num)
study = pd.read_csv(csv_name)

# Hardcode user IDs, since they are not public
userIds = [
    '578e64b09fc3c10d6fd12e4f',  # 'konstantinosliopyris'
    '55d4cde89fc3c1490e995086'
]


# Get IDs for all images in the dataset
imageIds = [ image for image in study['_id']] #_id column contains the 24 digit ids from isic
features = [ image for image in study['feature'].unique()] #array of features for study

df = pd.DataFrame(features, columns=["id"])
df = df.sort_values(by=['id'])
features_x = df.to_dict('records') #isic api needs a super specific and pointless formatting

studyResp = api.postJson('study', {
    'name': study_name,
    'features': features_x,
    'questions': qs,
    'userIds': userIds,
    'imageIds': imageIds
})

studyBody = studyResp.json()
if not studyResp.ok:
    raise Exception('Study creation failed, because: %s' % studyBody['message'])

print('Study creation success. New ID: %s' % studyBody['_id'])
