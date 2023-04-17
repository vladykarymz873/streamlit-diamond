import pickle
import streamlit as st

model = pickle.load(open('estimasi_diamond.sav','rb'))

st.title('Estimasi Harga Diamond')

cut_ord     = st.number_input('Input Cut Grading [Ideal=5,Premium=4,Very Good=3,Good=2,Fair=1]')
clarity_ord    = st.number_input('input Clarity Diamond [I1=1,SI2=2.SI1=3,VS1=4,VS2=5,VVS2=6,VVS1=7,]')
carat         = st.number_input('Input berapa karat')


predict = ''


if st.button('Estimasi Harga'):
    predict = model.predict(
        [[cut_ord,clarity_ord,carat]]
    )
    st.write ('Estimasi harga diamond dalam USD:',predict)
    st.write ('Estimasi harga diamond dalam IDR', predict*14760)