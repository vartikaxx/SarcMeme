# SarcMeme
# 🎭 Sarcasm & Advanced Vocabulary Fun Game

This fun and interactive app takes a single word input from the user, finds an advanced synonym using the Datamuse API, and generates a sarcastic sentence using the DeepSeek-R1 language model. It also fetches a random meme for some extra fun!

## 🔧 How it Works

1. User enters a word.
2. The app fetches a higher-level synonym using **Datamuse API**.
3. A **sarcastic sentence** is generated using **DeepSeek-R1** via **Fireworks.ai**.
4. A random meme is fetched using **Imgflip API**.

---

## 🧠 Model and API Breakdown

| Component         | Purpose                                      |
|------------------|----------------------------------------------|
| **DeepSeek-R1**   | Generates sarcastic sentences                |
| **Fireworks.ai**  | Hosts the DeepSeek model (model provider)    |
| **Huggingface_hub** | Used as a Python client interface to access Fireworks-hosted models |
| **Datamuse API**  | Provides advanced synonyms                   |
| **Imgflip API**   | Fetches a random meme                        |

---

## 🚀 Tech Stack

- Python
- Streamlit
- DeepSeek-R1 (via Fireworks and Hugging Face SDK)
- Datamuse API
- Imgflip API



