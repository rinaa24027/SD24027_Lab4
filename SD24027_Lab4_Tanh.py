import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Hyperbolic Tangent (Tanh)", layout="centered")

st.title("📈 Hyperbolic Tangent (Tanh) Visualiser")
st.caption("BSD3513 Artificial Intelligence — Lab Report 4")

st.markdown("""
The **Tanh** function is similar to the sigmoid function, but it is zero-centered and maps inputs to values between -1 and 1.
""")
st.latex(r"f(x) = tanh(x)")
st.markdown("**Range:** $(-1, 1)$")

x_min, x_max = st.slider("Select Input Range (X)", -10.0, 10.0, (-5.0, 5.0), key="tanh_slider")
x = np.linspace(x_min, x_max, 300)
y = np.tanh(x)

fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot(x, y, color="purple", linewidth=2.5, label="Tanh(x)")
ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
ax.set_title("Tanh Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output f(x)")
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend()

st.pyplot(fig)