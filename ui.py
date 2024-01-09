import streamlit as st
from generateImages import generate_images

st.set_page_config(page_title="Streamlit AI Image Generator", layout="wide", initial_sidebar_state="auto", page_icon="streamlit.svg")

# sidebar
with st.sidebar:
    key = st.text_input("OpenAI API Key", type="password")
    
col1, col2 = st.columns(2)
image_list = ["","","","",""]
def check_errors():
    if(key == ""):
        st.toast('Please enter your API key', icon='🔑')
    if(user_prompt == ""):
        st.toast('Please enter your prompt', icon='😶')
    if(number_of_images == 0):
        st.toast("Please select at least one image.", icon="😮‍💨")

    image_list = generate_images(key, user_prompt, image_size, number_of_images)


with col1:
    st.title("OpenAI Image Generator")

    user_prompt = st.text_input("Enter your prompt:", placeholder="a white siamese cat")
    image_size = st.selectbox("Image size:", ('256x256', '512x512', '1024x1024'))
    image_style = st.selectbox("Image style:", ("Realistic", "Cartoonish", "Abstract", "3D Illustration"))
    number_of_images = st.slider("Number of images:", 0, 5, 1)

    submit = st.button("Generate Images", use_container_width=True, type="primary",on_click=check_errors)

with col2:
    st.write("## Images")
    col3, col4 = st.columns(2)

    for i in range(number_of_images):
        if(i%2==0):
            with col3:
                link = image_list[i]
                st.image("https://oaidalleapiprodscus.blob.core.windows.net/private/org-4sjCUh3etirM3gATatWbOTwv/user-aMKt1easuVn7a8YfBI5gygdZ/img-kt4RZrYHuMliLWUe2f0nFiSI.png?st=2024-01-09T08%3A36%3A12Z&se=2024-01-09T10%3A36%3A12Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-01-08T14%3A30%3A04Z&ske=2024-01-09T14%3A30%3A04Z&sks=b&skv=2021-08-06&sig=YpFWO3rWjfjDAb2Xoi49DEzbHIBt01VFligIxeWNu%2BM%3D", use_column_width=True)
        else:
            with col4:
                link = image_list[i]
                # st.write(link)
                st.image("https://oaidalleapiprodscus.blob.core.windows.net/private/org-4sjCUh3etirM3gATatWbOTwv/user-aMKt1easuVn7a8YfBI5gygdZ/img-kt4RZrYHuMliLWUe2f0nFiSI.png?st=2024-01-09T08%3A36%3A12Z&se=2024-01-09T10%3A36%3A12Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-01-08T14%3A30%3A04Z&ske=2024-01-09T14%3A30%3A04Z&sks=b&skv=2021-08-06&sig=YpFWO3rWjfjDAb2Xoi49DEzbHIBt01VFligIxeWNu%2BM%3D", use_column_width=True)










