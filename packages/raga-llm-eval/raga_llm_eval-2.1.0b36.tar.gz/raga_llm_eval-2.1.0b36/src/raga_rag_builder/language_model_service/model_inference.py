import torch
from langchain_community.llms import HuggingFacePipeline
from transformers import (AutoModelForCausalLM, AutoTokenizer,
                          BitsAndBytesConfig, pipeline)

from ..retrieval_engine import PromptManager


class ModelInference:
    def __init__(self):
        pass
        # Initialize the configuration for BitsAndBytes
        # bnb_config = BitsAndBytesConfig(
        #     load_in_4bit=True,
        #     bnb_4bit_use_double_quant=True,
        #     bnb_4bit_quant_type="nf4",
        #     bnb_4bit_compute_dtype=torch.bfloat16,
        # )

        # Load the model with the specified configuration
        # self.model = AutoModelForCausalLM.from_pretrained(model_name)

        # # Load the tokenizer
        # self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def initalize_model(self):
        if self.model is None or self.tokenizer is None:
            # Load the model and tokenizer here
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        reader_llm = pipeline(
            model=self.model,
            tokenizer=self.tokenizer,
            task="text-generation",
            do_sample=True,
            temperature=0.2,
            repetition_penalty=1.1,
            return_full_text=False,
            max_new_tokens=500,
        )
        llm = HuggingFacePipeline(pipeline=reader_llm)
        return llm

    def generate_prompt_from_template(self):

        template = PromptManager().prompt_template()
        rag_prompt_template = self.tokenizer.apply_chat_template(
            template, tokenize=False, add_generation_prompt=True
        )
        return rag_prompt_template

    def generate_final_prompt(self, reranked_docs, query):
        rag_prompt_template = self.generate_prompt_from_template()
        retrieved_docs_text = [
            doc for doc in reranked_docs
        ]  # we only need the text of the documents
        context = "\nExtracted documents:\n"
        context += "".join(
            [
                f"Document {str(i)}:::\n" + doc
                for i, doc in enumerate(retrieved_docs_text)
            ]
        )

        final_prompt = rag_prompt_template.format(question=query, context=context)

        # print(final_prompt)
        return final_prompt

    def generate_response(self, llm, final_prompt):
        # Generate a response from the model
        response = llm.invoke(final_prompt)

        # Print the content of the response.
        response = f"Response: \n{response.content} "

        return response

    # def user_interaction(self, query):
