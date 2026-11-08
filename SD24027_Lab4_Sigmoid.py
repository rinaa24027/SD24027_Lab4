import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sigmoid Activation Function", layout="centered")

st.title("📈 Sigmoid Activation Function Visualiser")
st.caption("BSD3513 Artificial Intelligence — Lab Report 4")

st.markdown("""
The **Sigmoid** function maps input values to a smooth S-shaped curve between 0 and 1, commonly used for probability outputs.
* **Formula:** $f(x) = \frac{1}{1 + e^{-x}}$
* **Range:** $(0, 1)$
""")

# Interactive Slider for Input Range
x_min, x_max = st.slider("Select Input Range (X)", -10.0, 10.0, (-5.0, 5.0), key="sigmoid_slider")
x = np.linspace(x_min, x_max, 300)
y = 1 / (1 + np.exp(-x))

# Plotting the Graph
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot(x, y, color="green", linewidth=2.5, label="Sigmoid(x)")
ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
ax.set_title("Sigmoid Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output f(x)")
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend()

st.pyplot(fig)