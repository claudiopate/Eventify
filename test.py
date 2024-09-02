from unstract.llmwhisperer.client import LLMWhispererClient

client = LLMWhispererClient(base_url="https://llmwhisperer-api.unstract.com/v1", api_key="11a3621936744c27a1ca43a4e494976c")

# Get usage info
usage_info = client.get_usage_info()

# Process a document
# Extracted text is available in the 'extracted_text' field of the result
whisper = client.whisper(file_path="MAGGIO.pdf")

# Get the status of a whisper operation
# whisper_hash is available in the 'whisper_hash' field of the result of the whisper operation
status = client.whisper_status(whisper['whisper_hash'])

# Retrieve the result of a whisper operation
# whisper_hash is available in the 'whisper_hash' field of the result of the whisper operation
whisper = client.whisper_retrieve(whisper['whisper_hash'])