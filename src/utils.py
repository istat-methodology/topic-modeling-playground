# utils.py

import os
import urllib.request
from gensim.models import KeyedVectors
import gensim.downloader as api
import numpy as np


def load_or_download_embedding(model_name, save_dir="models"):
    """
    Loads a pre-trained model from local disk if available,
    otherwise downloads it via gensim API or fastText for specific languages.

    Parameters:
    - model_name: str, either a gensim model (e.g. 'word2vec-google-news-300')
                  or a fastText language code like 'fasttext-it'

    Returns:
    - gensim.models.KeyedVectors
    """
    os.makedirs(save_dir, exist_ok=True)
    model_path = os.path.join(save_dir, f"{model_name}.model")

    # 📦 Check if already saved
    if os.path.exists(model_path):
        print(f"📦 Loading model from {model_path}")
        return KeyedVectors.load(model_path)

    # 📚 Gensim API models
    try:
        print(f"⬇️ Trying to download '{model_name}' from gensim API...")
        model = api.load(model_name)
        model.save(model_path)
        print(f"💾 Saved model to {model_path}")
        return model
    except (ValueError, FileNotFoundError):
        pass  # Not found in Gensim API

    # 🌍 FastText language-specific models
    if model_name.startswith("fasttext-"):
        lang_code = model_name.split("-")[1]
        url = f"https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.{lang_code}.300.bin.gz"
        bin_path = os.path.join(save_dir, f"cc.{lang_code}.300.bin.gz")

        if not os.path.exists(bin_path):
            print(f"⬇️ Downloading FastText model for '{lang_code}'...")
            urllib.request.urlretrieve(url, bin_path)
            print("✅ Download complete.")

        print("🧠 Loading FastText model...")
        model = KeyedVectors.load_word2vec_format(bin_path, binary=True)
        model.save(model_path)
        print(f"💾 Saved model to {model_path}")
        return model

    raise ValueError(f"Model '{model_name}' not found in gensim API or FastText.")


def get_embedding(word, model):
    """
    Returns the embedding vector for a given word from the specified model.
    If the word is not in the vocabulary, returns a zero vector and prints a warning.

    Parameters:
    - word (str): the word to look up
    - model (gensim KeyedVectors): the embedding model

    Returns:
    - numpy.ndarray: embedding vector (or zero vector if word is OOV)
    """
    if word in model.key_to_index:
        return model[word]
    else:
        print(f"⚠️  Warning: '{word}' not found in vocabulary. Returning zero vector.")
        return np.zeros(model.vector_size)
