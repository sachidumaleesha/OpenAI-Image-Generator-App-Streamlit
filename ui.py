import streamlit as st
from generateImages import generate_images
from sidebarInfo import show_sidebarInfo

st.set_page_config(page_title="Streamlit AI Image Generator", layout="wide", initial_sidebar_state="auto", page_icon="streamlit.svg")

# sidebar
with st.sidebar:
    key = st.text_input("OpenAI API Key", type="password")
    show_sidebarInfo()
    
col1, col2 = st.columns(2)
def check_errors():
    if(key == ""):
        st.toast('Please enter your API key', icon='🔑')
    if(user_prompt == ""):
        st.toast('Please enter your prompt', icon='😶')
    if(number_of_images == 0):
        st.toast("Please select at least one image.", icon="😮‍💨")

    image_list = generate_images(key, user_prompt, image_size, number_of_images)
    with col2:
        st.write("## Images")
        col3, col4 = st.columns(2)

        for i in range(number_of_images):
            if(i%2==0):
                with col3:
                    link = image_list[i]
                    st.image(link, use_column_width=True)
            else:
                with col4:
                    link = image_list[i]
                    st.image(link, use_column_width=True)
        
        st.balloons()


with col1:
    st.title("OpenAI Image Generator")

    user_prompt = st.text_input("Enter your prompt:", placeholder="a white siamese cat")
    image_size = st.selectbox("Image size:", ('256x256', '512x512', '1024x1024'))
    image_style = st.selectbox("Image style:", ("Realistic", "Cartoonish", "Abstract", "3D Illustration"))
    number_of_images = st.slider("Number of images:", 0, 4, 1)

    submit = st.button("Generate Images", use_container_width=True, type="primary",on_click=check_errors)









