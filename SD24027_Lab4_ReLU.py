import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="ReLU Activation Function", layout="centered")

st.title("📈 ReLU Activation Function Visualiser")
st.caption("BSD3513 Artificial Intelligence — Lab Report 4")

st.markdown("""
**Rectified Linear Unit (ReLU)** allows only positive values to pass through directly. Negative values are mapped to zero.
* **Formula:** $f(x) = \max(0, x)$
* **Range:** $[0, \infty)$
""")

x_min, x_max = st.slider("Select Input Range (X)", -10.0, 10.0, (-5.0, 5.0), key="relu_slider")
x = np.linspace(x_min, x_max, 300)
y = np.maximum(0, x)

fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot(x, y, color="blue", linewidth=2.5, label="ReLU(x)")
ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
ax.set_title("ReLU Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output f(x)")
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend()

st.pyplot(fig)