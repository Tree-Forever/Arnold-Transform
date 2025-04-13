#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import numpy as np
from PIL import Image

import streamlit as st

from arnold_transform import arnold_transform

# ====================================================================================================
# Main Program
# ====================================================================================================
st.set_page_config(layout="wide")
col1, col2 = st.columns([.5, .5])

st.markdown("""
# Arnold Transformation
""")

in_file = st.sidebar.file_uploader(
    "Images files:",
    type=["png", "jpg", "jpeg", "gif", "webp"]
)
# print(in_file.file_id)    # uuid

if in_file is None:
    st.stop()
# filetype = in_file.type
pil_image = Image.open(in_file).convert("RGB")

run_encrypt = st.sidebar.button("Run Encryption")
run_decrypt = st.sidebar.button("Run Decryption")

if pil_image is None:
    st.stop()

with col1:
    st.image(
        pil_image,
        caption="Uploaded Image",
        # channels="BGR",
        use_container_width=True
    )

# Run Encryption
if run_encrypt:
    type = "encrypt"
elif run_decrypt:
    type = "decrypt"
else:
    st.stop()

s = time.perf_counter()

processed_image = arnold_transform(np.array(pil_image), type=type)

with col2:
    st.image(
        processed_image,
        caption="Encrypted Image",
        # channels="BGR",
        output_format="PNG",
        use_container_width=True
    )

st.toast(f"Processing time: :red[{time.perf_counter() - s:.4f}s]", icon="⏳")


