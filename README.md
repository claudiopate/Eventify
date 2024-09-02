## Generate the requirements.txt file
Each time you add a package the requirements.txt should be regenerated with this command:

    pipreqs --ignore bin,etc,include,lib,lib64 --force

Previuosly you had to install the package pipreqs, with:

    pip install pipreqs


## LLM Provider - from which we take info from file
[LLMWhisperer](https://pg.llmwhisperer.unstract.com/)