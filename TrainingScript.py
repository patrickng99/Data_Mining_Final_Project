import numpy as np
import pandas as pd

dfTrainedSessions = pd.read_csv('sessions.csv',skipinitialspace=True)

dfTrainedSessions.groupby(['user_id'])

dfTrainedSessions.to_csv('trainedSessions.csv')
print('finished ok')