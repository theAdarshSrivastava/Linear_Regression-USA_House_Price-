import streamlit as st
import pickle


pickle_in = open('USA_Housing.pkl', 'rb')
model = pickle.load(pickle_in)


def prediction(income, houseage, rooms, bedrooms, population):
   pred = model.predict([[income, houseage, rooms, bedrooms, population]])
   return pred


def main():
   # front end elements of the web page
   html_temp = """
   <body back 
   <div style ="background-color:yellow;padding:13px"> 
   <h1 style ="color:black;text-align:center;">Streamlit House Price Prediction ML App</h1> 
   </div> 
   """

   # display the front end aspect
   st.markdown(html_temp, unsafe_allow_html=True)

   # following lines create boxes in which user can enter data required to make prediction
   income = st.number_input('Avg. Area Income(15000-110000)')
   houseage = st.number_input('Avg. Area House Age(2-10)')
   rooms = st.number_input("Avg. Area number of Rooms(3-11)")
   bedrooms = st.number_input("Avg. Area number of Bedrooms(2-10)")
   population = st.number_input('Area Population(100-70000)')
   result = ""

   # when 'Predict' is clicked, make the prediction and store it
   if st.button("Predict"):
      result = prediction(income, houseage, rooms, bedrooms, population)
      st.success('Estimated Price in $ {}'.format(result))


if __name__ == '__main__':
   main()



