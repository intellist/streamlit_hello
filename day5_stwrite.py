import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

st.header('st.write')

st.write('Hello, *World* :sunglasses:')

st.write(1234)

df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})
st.write(df)

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

df2 = pd.DataFrame(
     np.random.randn(5, 3),
     columns=['a', 'b', 'c'])
st.write(df2)
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.latex(r'''
    \dfrac{1}{2 \pi}
    ''')

st.latex(r'''
    (a+b)^2 = a^2 + b^2 + 2ab
    ''')

st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')