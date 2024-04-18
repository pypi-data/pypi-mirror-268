import os
import sys
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from textblob import TextBlob
import logging
import warnings

class tokenizerNLTK:
    def __init__(self, model_name = "humarin/chatgpt_paraphraser_on_T5_base", tokenizerSeq2SeqIntial = "bigscience/mt0-large"):
        self.tokenizer_default = None
        self.model_default = None
        self.secondary_tokenizer = None
        self.model_name = model_name
        self.tokenizerSeq2SeqIntial = tokenizerSeq2SeqIntial
        # Suppress warnings
        warnings.filterwarnings("ignore")
        # Set logging level to error to suppress unnecessary messages
        logging.getLogger("transformers").setLevel(logging.ERROR)
        # Redirect stdout and stderr to /dev/null
        sys.stdout = open(os.devnull, "w")
        sys.stderr = open(os.devnull, "w")
        self.torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
        # Load Pegasus model and tokenizer
        self.load_model_and_tokenizer()

    def load_model_and_tokenizer(self):
        if self.tokenizer_default is None or self.model_default is None or self.secondary_tokenizer is None:
            self.tokenizer_default = AutoTokenizer.from_pretrained(self.model_name)
            self.model_default = AutoModelForSeq2SeqLM.from_pretrained(self.model_name).to(self.torch_device)
            self.secondary_tokenizer = AutoTokenizer.from_pretrained(self.tokenizerSeq2SeqIntial)

    def get_response(
        self,
        input_text,
        num_beams=5,
        num_beam_groups=5,
        num_return_sequences=5,
        repetition_penalty=10.0,
        diversity_penalty=3.0,
        no_repeat_ngram_size=2,
        temperature=0.7,
        max_length=2000
    ):
        input_ids = self.tokenizer_default(
            f'paraphrase: {input_text}',
            return_tensors="pt", padding="longest",
            max_length=max_length,
            truncation=True,
        ).input_ids.to(self.torch_device)
        
        outputs = self.model_default.generate(
            input_ids, temperature=temperature, repetition_penalty=repetition_penalty,
            num_return_sequences=num_return_sequences, no_repeat_ngram_size=no_repeat_ngram_size,
            num_beams=num_beams, num_beam_groups=num_beam_groups,
            max_length=max_length, diversity_penalty=diversity_penalty
        )

        res = self.tokenizer_default.batch_decode(outputs, skip_special_tokens=True)

        return res

    def tokenize_inputs(self, text):
        try:
            english_text = TextBlob(text).translate(from_lang='ur', to='en')
            paraphrased_texts = self.get_response(str(english_text))
            longest_paraphrased_text = max(paraphrased_texts, key=len)
            urdu_text = TextBlob(longest_paraphrased_text).translate(from_lang='en', to='ur')
            
            inputs = self.secondary_tokenizer.encode(f'return as it is: {str(urdu_text)}', return_tensors="pt")
            return [inputs, self.secondary_tokenizer]

        except Exception as e:
            print("Error:", e)
            return None

# Example usage
