from .util import num_tokens_from_messages

def query_gen(user_query, enum, desc, status, verbose, client, gpt4):
    messages = [
        {
            "role": "system",
            "content": 
            '''
            pandas dataframe table, columns = ''' + str(enum) + ''' . ''' +
            '''Your task is to generate pandas code that 
            1. can be executed directly on this pandas dataframe based on users' queries;
            2. the code should produce correct results based on the SAMPLE VALUES AND DESCRPITIONS of each column.''' + desc + '''
            ATTENTION: the values are case-sensitive, and you should strictly follow their provided formats and sample values (if any).
            The code can be of multiple lines, BUT the final assignment has to be assigned to res;
            Example: res = table['case'].count();
            IMPORTANT: Return the code snippets ONLY. You are not allowed to output anything else.
            ATTENTION: When you think there are more than one ways to write code to answer user query OR unsure about how to generate the code OR need some further details OR assumptions, return the entire table as res.
            '''

        },
        {
            "role": "user",
            "content": "I want to generate stories based on summaries."
        },
        {
            "role": "assistant",
            "content": "res = table"
        },
        {
            "role": "user",
            "content": "I am given a table with the following columns and format/values: "+desc+" "+user_query  # Use the user's query
        }
    ]

    if gpt4:
        response = client.chat.completions.create(
            model="gpt-4-0613",
            messages=messages
        )
        if verbose:
            num_token_msg = num_tokens_from_messages(messages, "gpt-4-0613")
            print("Number of tokens of messages for 'query_pd': ", num_token_msg)
            print("******Number of prompt tokens for 'query_pd': ", response.usage.prompt_tokens)
            print("******Number of answer tokens for 'query_pd': ", response.usage.completion_tokens)
            print("******Number of total tokens for 'query_pd': ", response.usage.total_tokens)
    else:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=messages
        )
        if verbose:
            num_token_msg = num_tokens_from_messages(messages, "gpt-3.5-turbo-0125")
            print("Number of tokens of messages for 'query_pd': ", num_token_msg)
            print("******Number of prompt tokens for 'query_pd': ", response.usage.prompt_tokens)
            print("******Number of answer tokens for 'query_pd': ", response.usage.completion_tokens)
            print("******Number of total tokens for 'query_pd': ", response.usage.total_tokens)

    status.append('code generated')

    return response.choices[0].message.content, status