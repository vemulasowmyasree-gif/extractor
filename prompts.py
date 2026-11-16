Extract_prompt= """Role: You are an expert in accurately extracting information from customer messages

Task: Extract the details from customer message such as Customer name, Email address

Instructions:
- Present the extracted details with one row per message indicating ":" side by side
if information is not provided mark as not provided

Input: {message}"""