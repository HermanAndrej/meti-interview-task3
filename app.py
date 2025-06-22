import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Handwritten Digit Generator (Demo)")

digit = st.selectbox("Select a digit (0–9):", list(range(10)))

if st.button("Generate 5 images"):
    st.write(f"Showing 5 placeholder images for digit {digit}:")

    for i in range(5):
        # Different random noise image for diversity
        noise_seed = np.random.randint(0, 10000)
        rng = np.random.default_rng(seed=noise_seed)
        fake_image = rng.random((28, 28))

        fig, ax = plt.subplots()
        ax.imshow(fake_image, cmap="gray")
        ax.axis("off")
        st.pyplot(fig)
