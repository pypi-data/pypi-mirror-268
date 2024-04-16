import os
import sys
import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer, AutoTokenizer
from textblob import TextBlob
import logging
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Set logging level to error to suppress unnecessary messages
logging.getLogger("transformers").setLevel(logging.ERROR)

# Redirect stdout and stderr to /dev/null
sys.stdout = open(os.devnull, "w")
sys.stderr = open(os.devnull, "w")

# Initialize model and tokenizer as None
tokenizer_default = None
model_default = None
secondary_tokenizer = None

# Function to load model and tokenizer if not already loaded
def load_model_and_tokenizer(model_name, tokenizerSeq2SeqIntial):
    global tokenizer_default, model_default, secondary_tokenizer
    if tokenizer_default is None or model_default is None or secondary_tokenizer is None:
        tokenizer_default = PegasusTokenizer.from_pretrained(model_name)
        model_default = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)
        secondary_tokenizer = AutoTokenizer.from_pretrained(tokenizerSeq2SeqIntial)

# Load Pegasus model and tokenizer
model_name = 'tuner007/pegasus_paraphrase'
checkpoint = "bigscience/mt0-base"

torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
load_model_and_tokenizer(model_name, checkpoint)

# Function to generate paraphrases
def get_response(input_text, num_return_sequences, num_beams):
    # Tokenize input text
    input_ids = tokenizer_default(input_text, return_tensors='pt', max_length=len(input_text), truncation=True).input_ids.to(torch_device)
    input_length = input_ids.shape[-1]

    # Generate paraphrases
    translated = model_default.generate(
        input_ids,
        max_length=input_length,
        num_beams=num_beams,
        num_return_sequences=num_return_sequences,
        temperature=1.5,
        early_stopping=True
    )

    # Decode paraphrases
    paraphrased_texts = tokenizer_default.batch_decode(translated, skip_special_tokens=True)
    return paraphrased_texts

# Function to translate Urdu to English and then back to Urdu after paraphrasing
def tokenized_inputs(text):
    try:
        # Translate Urdu text to English using TextBlob
        english_text = TextBlob(text).translate(from_lang='ur', to='en')
        num_beams = 50
        num_return_sequences = 23
        paraphrased_texts = get_response(str(english_text), num_return_sequences, num_beams)
        longest_paraphrased_text = max(paraphrased_texts, key=len)
        # Translate the longest paraphrased English text back to Urdu using TextBlob
        urdu_text = TextBlob(longest_paraphrased_text).translate(from_lang='en', to='ur')
        
        inputs = secondary_tokenizer.encode(str(urdu_text), return_tensors="pt")
        # secondary_tokenizer_pytorch = secondary_tokenizer.pytorch()  # Renamed variable
        return [inputs, secondary_tokenizer]

    except Exception as e:
        print("Error:", e)
        return None
