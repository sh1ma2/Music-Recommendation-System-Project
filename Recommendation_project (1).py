import streamlit as st
import pandas as pd


def recommend(Song_title):
    index = songs[songs['Song_title'] == Song_title].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_song_title = []
    for i in distances[1:10]:
        recommended_song_title.append(songs.iloc[i[0]].Song_title)
    return recommended_song_title

st.title('Songs Recommender System')
import pickle
songs_dict = pickle.load(open('song_dict1.pkl','rb'))
songs = pd.DataFrame(songs_dict)

similarity = pickle.load(open('similarity11.pkl','rb'))

selected_song_name = st.selectbox('How would you like to be contacted?',
songs['Song_title'].values)
if st.button('Recommend'):
   recommendation = recommend(selected_song_name)
   for i in recommendation:
    st.write(i)