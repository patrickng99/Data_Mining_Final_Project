import numpy as np
import pandas as pd

session = pd.read_csv('sessions.csv',skipinitialspace=True)

placeholder = session.groupby('user_id', sort = False)['action_type'].mean()

#Handing the NaN values repaceing with mode of column
session['action'].fillna(session['action'].mode()[0], inplace=True)
session['action_type'].fillna(session['action_type'].mode()[0], inplace=True)
session['action_detail'].fillna(session['action_detail'].mode()[0], inplace=True)
session['device_type'].fillna(session['device_type'].mode()[0], inplace=True)
session['secs_elapsed'].fillna(0, inplace=True)

#replacing space with _ in device_type
session.device_type = session.device_type.str.replace(' ',"_")

#Generating new_session with one row for one user_id
action = session.groupby('user_id', sort = False)[['action']].sum()
action_type = session.groupby('user_id', sort = False)[['action_type']].sum()
action_detail = session.groupby('user_id', sort = False)[['action_detail']].sum()

#Taking mean value of particular user
sec_e= session.groupby('user_id', sort = False)[['secs_elapsed']].mean()

#Create new data frame as new_session after using groupby on session data
new_session=pd.DataFrame(columns=['user_id'])
new_session['action']=action['action'].values
new_session['action_type']=action_type['action_type'].values
new_session['action_detail']=action_detail['action_detail'].values
new_session['secs_elapsed']=sec_e['secs_elapsed'].values

new_session.to_csv('trainedSessions.csv', index = False)
print('finished')