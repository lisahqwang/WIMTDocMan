#!pip install transformers
#!pip install torch 
#!pip install langchain-community
#!pip install pypdf 
#!pip install tensor

import transformers
from transformers import pipeline 
import torch
from langchain_community.document_loaders import PyPDFLoader
from pypdf import PdfReader

raw_text = " "
sequences = ["Microsoft Pushes Off SP2 Release Microsoft will delay the release of its SP2 update for another week to fix software glitches."]
link = r'C:\Users\wangs\OneDrive\Desktop\TRUST_DOC.pdf'

def PDFloader(link):
    pdfreader = PdfReader(link)
    # read text from pdf
    raw_text = ""
    for i, page in enumerate(pdfreader.pages):
        content = page.extract_text()
        if content:
            raw_text += content
    
    num_of_pages = len(pdfreader.pages)
    num_of_words = len(raw_text)
    num_new_lines = raw_text.count("\n")
    period_counts = raw_text.count(".")
    print("Number of pages:", num_of_pages, "\n"
      "Number of words:", num_of_words, "\n"
      "Number of new lines:", num_new_lines, "\n"
      "Number of periods:" ,period_counts)
    print(raw_text[0:100])
    return raw_text[0:100] #first hundred tokens so as to not overwhelm 

def classification(sequences): 
    device = "cuda" if torch.cuda.is_available() else "cpu"
    classifier = pipeline("zero-shot-classification", 
                      model="facebook/bart-large-mnli", 
                      device=device)
    candidate_labels = ["Technology", "Business", "Legal", "Human Resources", "Tax", "Finance"] 
    results = classifier(sequences, candidate_labels)
    print(results)

if __name__ == "__main__":
    #main function
    #classification(["Microsoft Pushes Off SP2 Release Microsoft will delay the release of its SP2 update for another week to fix software glitches."])
    classification(PDFloader(r'C:\Users\wangs\OneDrive\Desktop\TRUST_DOC.pdf'))