from dotenv import load_dotenv
import os
from PIL import Image
import streamlit as st
import fireworks.client
from fireworks.client.image import ImageInference, Answer

# Clear the cache before starting
st.cache_data.clear()

# Specify the path to the .env file in the env/ directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'env', '.env')

# Load the .env file from the specified path
load_dotenv(dotenv_path)

# Get the Fireworks API key from the environment variable
fireworks_api_key = os.getenv("FIREWORKS_API_KEY")

if not fireworks_api_key:
    raise ValueError("No API key found in the .env file. Please add your FIREWORKS_API_KEY to the .env file.")

# Load the image
logo_image = Image.open("img/fireworksai_logo.png")
ash_image = Image.open("img/ash.png")
bulbasaur_image = Image.open("img/bulbasaur.png")
squirtel_image = Image.open("img/squirtel.png")
charmander_image = Image.open("img/charmander.png")

# Streamlit app
st.subheader("Fireworks Playground")

# Add Fireworks logo and description
# TODO: Add Fireworks logo and description here

st.write("Fireworks AI is a platform that offers serverless and scalable AI models.")
st.write("Learn more here: [Fireworks Serverless Models](https://fireworks.ai/models?show=Serverless)")

# Placeholder images above the models
# TODO: Add links to placeholder images if necessary
# st.image("path_to_placeholder_image")

with st.sidebar:
    st.image(logo_image)

    st.write("Select three models to compare their outputs:")

    st.image(bulbasaur_image, width=80)
    option_1 = st.selectbox("Select Model 1", [
        "Text: Meta Llama 3 70B Instruct",
        "Text: Google Gemma 2 9B Instruct",
        "Text: Mixtral MoE 8x7B Instruct",
        "Text: 01 Yi Large",
        "Image: Stable Diffusion XL"
    ], index=1)  # Default to Google Gemma 2 9B Instruct

    st.image(charmander_image, width=80)
    option_2 = st.selectbox("Select Model 2", [
        "Text: Meta Llama 3 70B Instruct",
        "Text: Google Gemma 2 9B Instruct",
        "Text: Mixtral MoE 8x7B Instruct",
        "Text: 01 Yi Large",
        "Image: Stable Diffusion XL"
    ], index=2)  # Default to Mixtral MoE 8x7B Instruct

    st.image(squirtel_image, width=80)
    option_3 = st.selectbox("Select Model 3", [
        "Text: Meta Llama 3 70B Instruct",
        "Text: Google Gemma 2 9B Instruct",
        "Text: Mixtral MoE 8x7B Instruct",
        "Text: 01 Yi Large",
        "Image: Stable Diffusion XL"
    ], index=0)  # Default to Meta Llama 3 70B Instruct

    # Dropdown to select the LLM that will perform the comparison
    st.image(ash_image, width=80)
    comparison_llm = st.selectbox("Select Comparison Model", [
        "Text: Meta Llama 3 70B Instruct",
        "Text: Google Gemma 2 9B Instruct",
        "Text: Mixtral MoE 8x7B Instruct",
        "Text: 01 Yi Large"
    ], index=1)

os.environ["FIREWORKS_API_KEY"] = fireworks_api_key

# Helper text for the prompt
st.markdown("### Enter your prompt below to generate responses:")

prompt = st.text_input("Prompt", label_visibility="collapsed")

# Function to generate a response from a text model
def generate_text_response(model_name, prompt):
    return fireworks.client.ChatCompletion.create(
        model=model_name,
        messages=[{
            "role": "user",
            "content": prompt,
        }]
    )

# Function to generate an image response from an image model
def generate_image_response(prompt):
    client = ImageInference(model="stable-diffusion-xl-1024-v1-0")
    return client.text_to_image(
        prompt=prompt,
        cfg_scale=7,
        height=1024,
        width=1024,
        steps=30,
        seed=0,
        safety_check=False,
        output_image_format="PNG"
    )

# Function to compare the three responses using the selected LLM
def compare_responses(response_1, response_2, response_3, comparison_model):
    comparison_prompt = f"Compare the following three responses:\n\nResponse 1: {response_1}\n\nResponse 2: {response_2}\n\nResponse 3: {response_3}\n\nProvide a detailed comparison."
    
    comparison_response = fireworks.client.ChatCompletion.create(
        model=comparison_model,  # Use the selected LLM for comparison
        messages=[{
            "role": "user",
            "content": comparison_prompt,
        }]
    )
    
    return comparison_response.choices[0].message.content


# If Generate button is clicked
if st.button("Generate"):
    if not fireworks_api_key.strip() or not prompt.strip():
        st.error("Please provide the missing fields.")
    else:
        try:
            with st.spinner("Please wait..."):
                fireworks.client.api_key = fireworks_api_key
                
                # Create three columns for side-by-side comparison
                col1, col2, col3 = st.columns(3)
                
                # Model 1
                with col1:
                    st.subheader(f"Model 1: {option_1}")
                    st.image(bulbasaur_image)
                    if option_1.startswith("Text"):
                        model_map = {
                            "Text: Meta Llama 3 70B Instruct": "accounts/fireworks/models/llama-v3-8b-instruct",
                            "Text: Google Gemma 2 9B Instruct": "accounts/fireworks/models/gemma2-9b-it",
                            "Text: Mixtral MoE 8x7B Instruct": "accounts/fireworks/models/mixtral-8x7b-instruct",
                            "Text: 01 Yi Large": "accounts/fireworks/models/yi-large"
                        }
                        response_1 = generate_text_response(model_map[option_1], prompt)
                        st.success(response_1.choices[0].message.content)
                    else:
                        answer_1 = generate_image_response(prompt)
                        st.image(answer_1.image)
                
                # Model 2
                with col2:
                    st.subheader(f"Model 2: {option_2}")
                    st.image(charmander_image)
                    if option_2.startswith("Text"):
                        response_2 = generate_text_response(model_map[option_2], prompt)
                        st.success(response_2.choices[0].message.content)
                    else:
                        answer_2 = generate_image_response(prompt)
                        st.image(answer_2.image)
                
                # Model 3
                with col3:
                    st.subheader(f"Model 3: {option_3}")
                    st.image(squirtel_image)
                    if option_3.startswith("Text"):
                        response_3 = generate_text_response(model_map[option_3], prompt)
                        st.success(response_3.choices[0].message.content)
                    else:
                        answer_3 = generate_image_response(prompt)
                        st.image(answer_3.image)

                # Visual divider between model responses and comparison
                st.markdown("---")

                # Generate a comparison of the three responses using the selected LLM
                comparison = compare_responses(
                    response_1.choices[0].message.content, 
                    response_2.choices[0].message.content, 
                    response_3.choices[0].message.content, 
                    model_map[comparison_llm]
                )
                
                # Display the comparison
                st.subheader("Comparison of the Three Responses:")
                st.image(ash_image)
                st.write(comparison)
                
        except Exception as e:
            st.exception(f"Exception: {e}")