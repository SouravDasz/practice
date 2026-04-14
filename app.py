from transformers import pipeline
import torch 
from input import text
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="papluca/xlm-roberta-base-language-detection"
)

# text = "यह एक हिंदी वाक्य है"

result = classifier(text)

print("Your language detected as -->",result["label"])