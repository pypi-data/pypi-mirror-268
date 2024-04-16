import os
import sys
import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer, AutoTokenizer
from textblob import TextBlob
import logging
import warnings

class tokenizer_blob:
    def __init__(self, model_name='tuner007/pegasus_paraphrase', checkpoint='bigscience/mt0-base'):
        # Suppress warnings
        warnings.filterwarnings("ignore")
        # Set logging level to error to suppress unnecessary messages
        logging.getLogger("transformers").setLevel(logging.ERROR)
        # Redirect stdout and stderr to /dev/null
        sys.stdout = open(os.devnull, "w")
        sys.stderr = open(os.devnull, "w")
        # Initialize model and tokenizer as None
        self.tokenizer_default = None
        self.model_default = None
        self.secondary_tokenizer = None
        # Load Pegasus model and tokenizer
        self.torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.load_model_and_tokenizer(model_name, checkpoint)

    def load_model_and_tokenizer(self, model_name, tokenizerSeq2SeqIntial):
        if self.tokenizer_default is None or self.model_default is None or self.secondary_tokenizer is None:
            self.tokenizer_default = PegasusTokenizer.from_pretrained(model_name)
            self.model_default = PegasusForConditionalGeneration.from_pretrained(model_name).to(self.torch_device)
            self.secondary_tokenizer = AutoTokenizer.from_pretrained(tokenizerSeq2SeqIntial)

    def get_response(self, input_text, num_return_sequences, num_beams):
        input_ids = self.tokenizer_default(input_text, return_tensors='pt', max_length=len(input_text), truncation=True).input_ids.to(self.torch_device)
        input_length = input_ids.shape[-1]
        translated = self.model_default.generate(
            input_ids,
            max_length=input_length,
            num_beams=num_beams,
            num_return_sequences=num_return_sequences,
            temperature=1.5,
            early_stopping=True
        )
        paraphrased_texts = self.tokenizer_default.batch_decode(translated, skip_special_tokens=True)
        return paraphrased_texts

    def tokenized_inputs(self, text):
        try:
            english_text = TextBlob(text).translate(from_lang='ur', to='en')
            num_beams = 50
            num_return_sequences = 23
            paraphrased_texts = self.get_response(str(english_text), num_return_sequences, num_beams)
            longest_paraphrased_text = max(paraphrased_texts, key=len)
            urdu_text = TextBlob(longest_paraphrased_text).translate(from_lang='en', to='ur')
            inputs = self.secondary_tokenizer.encode(str(urdu_text), return_tensors="pt")
            return [inputs, self.secondary_tokenizer]
        except Exception as e:
            print("Error:", e)
            return None

# Example usage
# pegasus_paraphraser = PegasusParaphraser()
# urdu_text = "وہ اپنے وقت کا ایک معروف شخص تھا اس کے گرد ایک ہجوم رہتا وہ جنہیں دوست سمجھتا تھا جونہی اچھا وقت ختم ہوا سب غائب ہوگئے ‘سالوں کی دوستیاں گھنٹوں میں بھلادی گئیں یہاں تک جنہ
