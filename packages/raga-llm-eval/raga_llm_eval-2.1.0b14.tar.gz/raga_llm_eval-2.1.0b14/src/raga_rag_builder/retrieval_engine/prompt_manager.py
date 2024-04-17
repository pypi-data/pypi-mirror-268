import tokenizers
from langchain.prompts import PromptTemplate


class PromptManager:
    def __init__(self):
        # Initialize with a default template
        self.templates = {
            "default": (
                """Using the information contained in the context,
give a comprehensive answer to the question.
Respond only to the question asked, response should be concise and relevant to the question.
Provide the number of the source document when relevant.
If the answer cannot be deduced from the context, do not give an answer.
Context:
{context}
---
Now here is the question you need to answer.

Question: {question}"""
            )
        }
        self.template_variables = {}

    def create_prompt(self, context, query, template_name="default"):
        template = self.templates.get(template_name, "Template not found")
        variables = self.template_variables.get(template_name, {})
        input_variables = {
            "context": context,
            "question": query,
            **variables,  # Include template-specific variables automatically
        }
        prompt = template.format(**input_variables)
        return prompt

    def view_template(self, template_name="default"):
        """
        Returns the template string for the given template name.
        """
        return self.templates.get(template_name, "Template not found")

    def edit_template(self, template_name, new_template):
        """
        Edits an existing template with a new value.
        """
        if template_name in self.templates:
            self.templates[template_name] = new_template
            return "Template updated successfully."
        else:
            return "Template not found."

    def add_template(self, template_name, template_content, **variables):
        if template_name in self.templates:
            return "Template name already exists."
        self.templates[template_name] = template_content
        self.template_variables[template_name] = (
            variables  # Store additional template variables
        )
        return "Template added successfully."
