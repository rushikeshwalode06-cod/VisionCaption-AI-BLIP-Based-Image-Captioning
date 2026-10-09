import streamlit as st
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import html

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="VisionCaption AI",
    page_icon="🌈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# RGB DESIGN
# =====================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at 10% 5%, rgba(168,85,247,.18), transparent 35%),
        radial-gradient(ellipse at 90% 10%, rgba(0,229,255,.13), transparent 35%),
        linear-gradient(135deg, #080b18, #111329 50%, #080b18);
    font-family: 'Inter', sans-serif;
    color: #ffffff;
}

.block-container {
    max-width: 1700px;
    width: 100%;
    padding: 1.5rem clamp(.8rem, 2vw, 2rem) 3rem;
    box-sizing: border-box;
}

@keyframes rgbFlow {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* TITLE WRAPPER: centered on the page */
.title-wrapper {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 8px 0 22px;
}

/* BOX FITS THE TITLE TEXT */
.rgb-title-box {
    display: inline-flex;
    width: fit-content;
    max-width: 100%;
    box-sizing: border-box;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 15px 25px;
    border: 2px solid transparent;
    border-radius: 18px;
    background:
        linear-gradient(135deg, #101329, #17152e) padding-box,
        linear-gradient(
            90deg,
            #ff35c8,
            #a855f7,
            #00e5ff,
            #65ffb7,
            #ff35c8
        ) border-box;
    background-size: 100% 100%, 300% 300%;
    animation: rgbFlow 5s ease infinite;
    box-shadow:
        0 0 18px rgba(0,229,255,.18),
        0 0 24px rgba(255,53,200,.10);
}

.gradient-title {
    display: block;
    width: fit-content;
    max-width: 100%;
    margin: 0;
    padding: 0;
    text-align: center;
    font-size: clamp(25px, 4vw, 46px);
    font-weight: 800;
    line-height: 1.3;
    overflow-wrap: anywhere;
    background: linear-gradient(
        90deg,
        #ff35c8,
        #a855f7,
        #00e5ff,
        #65ffb7,
        #ffe66d,
        #ff35c8
    );
    background-size: 300% 300%;
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: rgbFlow 6s ease infinite;
}

.subtitle {
    color: #e0e7ff !important;
    text-align: center;
    font-size: clamp(14px, 1.5vw, 18px);
    line-height: 1.8;
    margin-bottom: 18px;
}

.section-title {
    color: #ffffff !important;
    font-size: 21px;
    font-weight: 800;
    line-height: 1.5;
    overflow-wrap: anywhere;
    text-shadow: 0 0 12px rgba(0,229,255,.25);
}

.small-text {
    color: #e2e8f0 !important;
    font-size: 14px;
    line-height: 1.8;
}

.stApp p,
.stApp label,
.stApp li,
.stApp [data-testid="stCaptionContainer"] {
    color: #f1f5ff;
}

.stApp h1,
.stApp h2,
.stApp h3 {
    color: #ffffff;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111329, #090d1c);
    border-right: 1px solid rgba(0,229,255,.5);
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: #f8fafc;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #ffffff !important;
}

/* RGB DIVIDER */
.rgb-line {
    height: 3px;
    width: 100%;
    border-radius: 10px;
    margin: 12px 0 22px;
    background: linear-gradient(
        90deg, #ff35c8, #a855f7, #00e5ff, #65ffb7, #ff35c8
    );
    background-size: 300% 100%;
    animation: rgbFlow 5s linear infinite;
}

/* CONTENT CARDS */
.rgb-card {
    background: rgba(18,23,46,.88);
    border: 1px solid rgba(0,229,255,.55);
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 16px;
    box-shadow:
        0 0 16px rgba(0,229,255,.08),
        inset 0 0 16px rgba(168,85,247,.04);
    overflow-wrap: anywhere;
    box-sizing: border-box;
}

.caption-card {
    background: linear-gradient(
        135deg,
        rgba(168,85,247,.18),
        rgba(0,229,255,.09),
        rgba(255,53,200,.09)
    );
    border: 1px solid rgba(255,53,200,.7);
    border-radius: 18px;
    padding: 22px;
    margin-top: 16px;
    box-shadow: 0 0 20px rgba(255,53,200,.12);
    overflow-wrap: anywhere;
}

/* IMAGE PREVIEW */
[data-testid="stImage"] img {
    display: block;
    width: 100%;
    height: auto;
    object-fit: contain;
    border: 1px solid rgba(0,229,255,.65);
    border-radius: 15px;
    box-shadow: 0 0 18px rgba(0,229,255,.14);
}

/* FILE UPLOADER */
[data-testid="stFileUploader"] {
    background: rgba(12,17,35,.65);
    border: 1px dashed #00e5ff;
    border-radius: 14px;
    padding: 12px;
}

[data-testid="stFileUploader"] label,
[data-testid="stFileUploader"] p,
[data-testid="stFileUploader"] span {
    color: #ffffff !important;
}

/* BUTTONS */
.stButton > button,
.stDownloadButton > button {
    width: 100%;
    min-height: 46px;
    color: #ffffff !important;
    background: linear-gradient(90deg, #7c3aed, #db2777, #0891b2);
    border: 1px solid rgba(255,255,255,.3);
    border-radius: 12px;
    font-weight: 800;
    transition: .25s ease;
    box-shadow: 0 0 15px rgba(168,85,247,.18);
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    transform: translateY(-2px);
    border-color: #00e5ff;
    box-shadow: 0 0 22px rgba(0,229,255,.28);
}

.footer {
    text-align: center;
    color: #cbd5e1 !important;
    font-size: 12px;
    line-height: 1.8;
    margin-top: 28px;
}

/* MOBILE */
@media (max-width: 700px) {
    .block-container {
        padding: 1rem .8rem 2rem;
    }

    .rgb-title-box {
        padding: 12px 16px;
    }

    .rgb-card,
    .caption-card {
        padding: 15px;
    }
}
</style>
""", unsafe_allow_html=True)


# =====================================================
# LOAD BLIP MODEL
# =====================================================
@st.cache_resource(show_spinner=False)
def load_caption_model():
    model_options = [
        "rushikeshwalode/blip-image-captioning-base-Indian_celeb_womens-finetuned",
        "Salesforce/blip-image-captioning-base"
    ]

    last_error = None

    for model_name in model_options:
        try:
            processor = BlipProcessor.from_pretrained(model_name)
            model = BlipForConditionalGeneration.from_pretrained(model_name)

            device = "cuda" if torch.cuda.is_available() else "cpu"
            model = model.to(device)
            model.eval()

            return processor, model, device, model_name

        except Exception as error:
            last_error = error

    raise RuntimeError(
        "Could not load a BLIP model. Check your internet connection "
        "and Hugging Face model access. Details: " + str(last_error)
    )


# =====================================================
# CENTERED TITLE: BOX FITS THE TEXT
# =====================================================
st.markdown("""
<div class="title-wrapper">
    <div class="rgb-title-box">
        <div class="gradient-title">🌈 VisionCaption AI</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
    AI-powered image understanding that transforms your image
    into a meaningful natural-language caption.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="rgb-line"></div>', unsafe_allow_html=True)


# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:
    st.markdown("""
    <div class="title-wrapper">
        <div class="rgb-title-box" style="padding:10px 12px;">
            <div class="gradient-title" style="font-size:23px;">
                🌈 VisionCaption AI
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">✨ About the Project</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="small-text">
        VisionCaption AI uses a BLIP image-captioning model to analyze
        images and generate natural-language descriptions.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(
        '<div class="section-title">🧠 AI Model</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="small-text">
        Model family: BLIP<br>
        Task: Image Captioning<br>
        Input: RGB Image<br>
        Output: Text Description
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(
        '<div class="section-title">⚙️ Caption Settings</div>',
        unsafe_allow_html=True
    )

    max_length = st.slider(
        "Maximum caption length",
        min_value=20,
        max_value=100,
        value=50,
        step=5
    )

    num_beams = st.slider(
        "Caption quality (beam search)",
        min_value=1,
        max_value=8,
        value=5,
        step=1,
        help="Higher values may improve captions but can take longer."
    )

    st.markdown("---")

    st.markdown("""
    <div class="small-text">
        💡 Tip: Clear images with recognizable objects usually produce
        more useful captions.
    </div>
    """, unsafe_allow_html=True)


# =====================================================
# SESSION STATE
# =====================================================
if "generated_caption" not in st.session_state:
    st.session_state.generated_caption = None

if "caption_model_name" not in st.session_state:
    st.session_state.caption_model_name = None

if "caption_device" not in st.session_state:
    st.session_state.caption_device = None

if "uploaded_image_id" not in st.session_state:
    st.session_state.uploaded_image_id = None


# =====================================================
# TWO-COLUMN LAYOUT
# =====================================================
left_col, right_col = st.columns([1, 1], gap="large")

with left_col:
    st.markdown(
        '<div class="section-title">🖼️ Upload Your Image</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="small-text">
        Select an image from your computer. Supported formats:
        JPG, JPEG, PNG and WEBP.
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=["jpg", "jpeg", "png", "webp"],
        help="Upload an image to generate its caption."
    )

    image = None

    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file).convert("RGB")

            # Clear old caption if a different image is uploaded
            image_id = (
                uploaded_file.name,
                uploaded_file.size
            )

            if st.session_state.uploaded_image_id != image_id:
                st.session_state.generated_caption = None
                st.session_state.caption_model_name = None
                st.session_state.caption_device = None
                st.session_state.uploaded_image_id = image_id

            st.markdown("""
            <div class="rgb-card">
                <div class="section-title">📷 Image Preview</div>
            """, unsafe_allow_html=True)

            st.image(
                image,
                caption="Uploaded RGB Image",
                use_container_width=True
            )

            st.markdown(f"""
            <div class="small-text">
                Width: {image.width}px<br>
                Height: {image.height}px<br>
                Color mode: RGB
            </div>
            </div>
            """, unsafe_allow_html=True)

        except Exception as error:
            st.error(f"Unable to read image: {error}")

    else:
        st.session_state.generated_caption = None
        st.session_state.uploaded_image_id = None

        st.markdown("""
        <div class="rgb-card">
            <div class="section-title">🌌 Image Preview</div>
            <div class="small-text">
                Your selected image will appear here.
                The image is converted to RGB for processing.
            </div>
        </div>
        """, unsafe_allow_html=True)


# =====================================================
# CAPTION GENERATOR
# =====================================================
with right_col:
    st.markdown(
        '<div class="section-title">🤖 AI Caption Generator</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="small-text">
        The BLIP model analyzes the image and generates a text description.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="rgb-card">
        <div class="section-title">✨ How It Works</div>
        <div class="small-text">
            1. Upload your image.<br>
            2. The AI model analyzes the image.<br>
            3. A natural-language caption is generated.
        </div>
    </div>
    """, unsafe_allow_html=True)

    generate_button = st.button(
        "🚀 Generate Image Caption",
        use_container_width=True
    )

    if generate_button:
        if image is None:
            st.warning("Please upload an image first.")

        else:
            try:
                with st.spinner("🧠 Loading the AI model..."):
                    processor, model, device, model_name = (
                        load_caption_model()
                    )

                with st.spinner("🌈 Analyzing image and generating caption..."):
                    inputs = processor(
                        images=image,
                        return_tensors="pt"
                    )

                    inputs = {
                        key: value.to(device)
                        for key, value in inputs.items()
                    }

                    with torch.inference_mode():
                        output = model.generate(
                            **inputs,
                            max_length=max_length,
                            num_beams=num_beams,
                            early_stopping=True
                        )

                    caption = processor.decode(
                        output[0],
                        skip_special_tokens=True
                    ).strip()

                st.session_state.generated_caption = caption
                st.session_state.caption_model_name = model_name
                st.session_state.caption_device = device

            except Exception as error:
                st.error(
                    "Caption generation failed. Check your internet "
                    "connection, model access and installed libraries."
                )

                with st.expander("View technical error"):
                    st.code(str(error))

    # Display the generated caption
    caption = st.session_state.generated_caption

    if caption:
        st.markdown("""
        <div class="caption-card">
            <div class="section-title">🌟 Generated Caption</div>
        """, unsafe_allow_html=True)

        st.markdown(
            f'<div style="font-size:19px;font-weight:600;'
            f'line-height:1.8;color:#ffffff;overflow-wrap:anywhere;">'
            f'{html.escape(caption)}</div>',
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

        st.success("Caption generated successfully!")

        st.markdown(f"""
        <div class="rgb-card">
            <div class="section-title">🔍 Model Information</div>
            <div class="small-text">
                Model: {html.escape(st.session_state.caption_model_name or "")}<br>
                Device: {html.escape(str(st.session_state.caption_device or "").upper())}<br>
                Input: RGB Image<br>
                Output: Natural-language caption
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.download_button(
            label="📥 Download Caption",
            data=caption,
            file_name="image_caption.txt",
            mime="text/plain",
            use_container_width=True
        )


# =====================================================
# FOOTER
# =====================================================
st.markdown('<div class="rgb-line"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    🌈 VisionCaption AI | BLIP-Based Image Captioning<br>
    Built with Python, Streamlit, PyTorch and Hugging Face Transformers
</div>
""", unsafe_allow_html=True)

