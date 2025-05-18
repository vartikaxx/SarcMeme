import streamlit as st
import requests
import random
from huggingface_hub import InferenceClient

# Hugging Face token
hf_token ='Replace with your token'

# Set up Hugging Face inference client using Fireworks and DeepSeek
client = InferenceClient(
    model="deepseek-ai/DeepSeek-R1",
    token=hf_token,
    provider="fireworks-ai"
)

# Streamlit App Title
st.title('🎭 Sarcasm & Advanced Vocabulary Fun Game')

# User input
sen = st.text_input("Enter a word:")

# 🔁 Function to get a better-quality synonym using Datamuse API
def get_synonym(word):
    url = f"https://api.datamuse.com/words?rel_syn={word}&max=10"
    response = requests.get(url)
    if response.status_code == 200:
        words = response.json()
        valid_words = [w['word'] for w in words if w['word'].lower() != word.lower()]
        return random.choice(valid_words) if valid_words else word
    return word

# 🎯 Function to generate sarcastic sentence using Fireworks model
def replace_word_with_sarcasm(synonym):
    try:
        prompt = f"Generate a sarcastic and witty sentence using the word: {synonym}"
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# 😹 Function to get a random meme from Imgflip
def get_random_meme():
    meme_api_url = "https://api.imgflip.com/get_memes"
    response = requests.get(meme_api_url)
    if response.status_code == 200:
        memes = response.json()['data']['memes']
        return random.choice(memes)['url']
    return None

# 🚀 Main Action
if st.button("Generate Sarcastic Sentence with Synonym"):
    if sen:
        synonym = get_synonym(sen)
        sarcastic_sentence = replace_word_with_sarcasm(synonym)
        st.write(f"**Synonym used:** `{synonym}`")
        st.markdown(f"**🗯️ Sarcastic Sentence:** {sarcastic_sentence}")

        # Show meme for fun
        meme_url = get_random_meme()
        if meme_url:
            st.image(meme_url, caption="Just for fun!", use_column_width=True)
        else:
            st.write("Couldn't fetch a meme this time 😅.")
    else:
        st.warning("Please enter a word to generate something fun!")
