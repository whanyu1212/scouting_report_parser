summary_prompt_template = """Write a concise summary of the player's draft report 
                    focusing on the player's offense, defensen, athleticism, 
                    basketball IQ, mentality, and ceiling:
                    "{text}"
                    CONCISE SUMMARY:"""

qna_prompt_template = """Use the following pieces of context to answer the question at the end. 
                    If you don't know the answer, just say that you don't know, don't try to make up an answer. 
                    Use three sentences maximum and keep the answer as concise as possible. 
                    Always say "thanks for asking!" at the end of the answer. 
                    {context}
                    Question: {question}
                    Helpful Answer:"""
