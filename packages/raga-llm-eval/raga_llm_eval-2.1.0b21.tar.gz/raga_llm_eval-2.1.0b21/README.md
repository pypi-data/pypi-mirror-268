<p align="center">
    <img src="https://github.com/aristotle-ai/raga-llm-eval/blob/v2/docs/assets/logo-lg_white.png" alt="RagaAI - Logo" width="100%">
</p>

<h1 align="center">
    Raga LLM Hub
</h1>

<h3 align="center">
    <a href="https://raga.ai">Raga AI</a> |
    <a href="https://docs.raga.ai/raga-llm-hub">Documentation</a> |
    <a href="https://docs.raga.ai/raga-llm-hub/quickstart">Getting Started</a> 

</h3>


<div align="center">


[![PyPI - Version](https://img.shields.io/pypi/v/raga-llm-eval?label=PyPI%20Package)](https://badge.fury.io/py/raga-llm-eval) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1PQGqDGdcSUxhSvpSQYX8ZdHf5r90WSYf?usp=sharing)
</a> [![Python Compatibility](https://img.shields.io/pypi/pyversions/raga-llm-eval)](https://pypi.org/project/raga-llm-eval/) []()

</div>


Welcome to Raga LLM Eval, a comprehensive evaluation toolkit for Language and Learning Models (LLMs). This toolkit provides a suite of tests to evaluate various aspects of language model performance, including relevance, understanding, coherence, toxicity, and more.

## Installation

### Using pip

```bash
python -m venv venv
source venv/bin/activate
pip install raga-llm-eval


* `python -m venv venv` - Create a new python environment.
* `source venv/bin/activate` - Activate the environment.
* `pip install raga-llm-eval` - Install the package

### with conda
* `conda create --name myenv` - Create a new python environment.
* `conda activate myenv` - Activate the environment.
* `python -m pip install raga-llm-eval` - Install the package



## Quick Tour
### Setting up
```py
from raga_llm_eval import RagaLLMEval, get_data

# Initialize with API key
evaluator = RagaLLMEval(api_keys={"OPENAI_API_KEY": "xxx"})
```

###  List available
```py
# List available tests
evaluator.list_available_tests()
```

### Adding and Running Tests
#### Using Custom Data
```py
# Add tests with custom data
evaluator.add_test(
    test_names=["relevancy_test", "summarisation_test"],
    data={
        "prompt": ["How are you?", "How do you do?"],
        "context": ["You are a student, answering your teacher."],
        "response": ["I am fine. Thank you", "Doooo do do do doooo..."],
    },
    arguments={"model": "gpt-3.5-turbo-1106", "threshold": 0.6},
).run()

evaluator.print_results()

```

#### Using Provided Test Data
```py
# Add tests with provided test data
evaluator.add_test(
    test_names=["relevancy_test"],
    data=get_data("relevancy_test", num_samples=1),
    arguments={"model": "gpt-3.5-turbo-1106", "threshold": 0.6},
).run()

evaluator.print_results()
```

## Advanced Usage: Piping and Saving Results
The `raga_llm_eval` package supports a fluent interface, allowing you to chain methods together using a piping style. This approach can make your code more readable and concise. Additionally, you can save the evaluation results to a JSON file for further analysis or record-keeping. Below are examples demonstrating these capabilities.

### Piping Method Calls
Piping allows you to chain multiple operations in a single statement. This can simplify your code, making it easier to read and maintain. Here's an example of how to use piping to add a test, run it, and print the results:

```python
# Method piping
evaluator.add_test(
    test_names=["relevancy_test", "summarisation_test"],
    data={
        "prompt": ["What is the capital of France?", "Explain quantum entanglement."],
        "context": ["You are a geography teacher.", "You are a physics professor explaining to a student."],
        "response": ["The capital of France is Paris.", "Quantum entanglement is a phenomenon where particles become interconnected..."],
    },
    arguments={"model": "gpt-3.5-turbo-1106", "threshold": 0.75},
).run()

evaluator.print_results()
```

### Saving Results to a File
```python
# Adding a test, running it, printing, and saving the results to a JSON file
evaluator.add_test(
    test_names=["relevancy_test", "summarisation_test"],
    data={
        "prompt": ["What is the capital of France?", "Explain quantum entanglement."],
        "context": ["You are a geography teacher.", "You are a physics professor explaining to a student."],
        "response": ["The capital of France is Paris.", "Quantum entanglement is a phenomenon where particles become interconnected..."],
    },
    arguments={"model": "gpt-3.5-turbo-1106", "threshold": 0.75},
).run()

evaluator.print_results()

```
This will execute the tests, print the results to the console, and also save the results in a file named `evaluation_results.json` in your current working directory.

Explore these capabilities to get the most out of your language model evaluations with `raga-llm-eval`.

Happy Evaluating!

## Tests Supported

## Relevance & Understanding
In this suite of tests, we focus on the model's ability to provide relevant, accurate, and contextually appropriate responses. This includes evaluating the model's precision, recall, and overall understanding of the given context to generate relevant answers.

1. **Relevancy Test**: Measures the relevance of LLM response to the input prompt

2. **Contextual Precision Test**: Evaluates if relevant nodes in context are ranked higher, resulting in a dictionary with precision score, reason, and details. Higher scores indicate more precise context alignment.

3. **Contextual Recall Test**: Measures alignment of retrieval context with expected response, outputting a dictionary with recall score, reason, and details. Higher scores denote better recall.

4. **Contextual Relevancy Test**: Assesses the overall relevance of context to the input prompt, providing a dictionary with relevancy score, reason, and details. Higher scores mean more relevant context.

5. **Hallucination Test**: Determines the hallucination score of the model's response compared to the context, offering a dictionary with scores and details. Higher scores indicate more hallucinated responses.

6. **Faithfulness Test**: Evaluates if the LLM response aligns with the retrieval context, producing a dictionary with a faithfulness score and details. Higher scores suggest more faithful responses.

7. **Consistency Test**: Provides a score for the consistency of responses, with a dictionary containing scores and evaluation details. Higher scores indicate better consistency.

8. **Conciseness Test**: Checks the conciseness of the LLM response, yielding a dictionary with a conciseness score and related information. Higher scores denote more concise responses.

9. **Coherence Test**: Assesses the coherence of the LLM response, resulting in a dictionary with coherence scores and details. Higher scores suggest more coherent responses.

10. **Correctness Test**: Evaluates the correctness of the LLM response, offering a dictionary with correctness scores and information. Higher scores indicate more correct responses.

11. **Summarization Test**: Determines the quality of summaries generated by the LLM, providing a dictionary with summarization scores and details. Higher scores mean better summary quality.

12. **Grade Score Test**: Provides a grade score indicating the education level required to understand the text, with a dictionary containing scores and details. Higher scores indicate a higher education level needed.

13. **Complexity Test**: Offers a score for the complexity of the text, producing a dictionary with complexity scores and submetrics. Higher scores signify more complex texts.

14. **Readability Test**: Provides a readability score, yielding a dictionary with scores and details. Higher scores indicate more readable texts.

15. **Maliciousness Test**: Evaluates the maliciousness of prompts and responses, resulting in a dictionary with scores and evaluation details. Higher scores indicate more malicious content.

16. **Toxicity Test**: Provides a score for the toxicity of model responses, offering a dictionary with toxicity scores. Higher scores suggest more toxic responses.

17. **Bias Test**: Measures the bias score of model responses, yielding a dictionary with scores. Higher scores indicate more biased responses.

18. **Response Toxicity Test**: Assesses the toxicity of model responses, providing a dictionary with toxicity scores. Higher scores suggest more toxic responses.

19. **Refusal Test**: Evaluates the model's refusal similarity, offering a dictionary with refusal scores. Higher scores indicate a greater likelihood of refusal.

20. **Prompt Injection Test**: Checks for injection issues in prompts, resulting in a dictionary with injection scores. Lower scores indicate better prompts.

21. **Coverage Test**: Assesses whether all concepts are covered by model responses, providing a dictionary with coverage ratios. This test evaluates concept utilization.

22. **POS Test**: Evaluates the accuracy of part-of-speech tagging in model responses, offering a dictionary with accuracy ratios. It checks for correct PoS tag usage.

23. **Length Test**: Measures the number of words in generated responses, yielding a dictionary with length details. This test assesses response length appropriateness.

24. **Winner Test**: Compares responses of two models or between a model and human annotation, providing a dictionary indicating which is better. It evaluates response quality.

25. **Overall Test**: Compares the overall score of two models on a provided task, offering a dictionary with overall scores. This test evaluates model performance comprehensively.

26. **Sentiment Analysis Test**: Provides a score for the sentiment of model responses, yielding a dictionary with sentiment scores. Higher scores indicate more positive responses.

27. **Generic Evaluation Test**: Returns a score based on specific criteria, response, and context, offering a dictionary with evaluation scores. Higher scores indicate better response quality.

28. **Cosine Similarity Test**: Provides a score for the similarity between the prompt and response, resulting in a dictionary with similarity scores. Higher scores indicate greater similarity.



## Learn More
