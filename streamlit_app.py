import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
def gauss(x, m, s):
  return 1 / ((2 * np.pi * s) ** .5) * np.exp(- (x - m) ** 2 / (2 * s))
col1, col2 = st.columns(2)
with col1:
    m = st.slider("μ", -10.0, 10.0, step = 0.01, value = 1.0)
with col2:
    s = st.slider("σ", 0.1, 10.0, step = 0.01, value = 1.0)
fig, ax = plt.subplots()
x = np.linspace(m - np.abs(m), m + np.abs(m), 200)
ax.plot(x, gauss(x, m, s))
st.pyplot(fig)