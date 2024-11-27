import pytest


@pytest.mark.parametrize('question', ['What', 'What happens', 'When', 'why',
    'why do', 'how', 'whose', 'whom'])
def test_ensure_no_answer_for_short_questions(client, question):
    """in French. Here is the suggested docstring format:

```
Description:
    Ensures that the chatbot does not provide an answer for short questions.
Arguments:
    client (test client): The test client for making HTTP requests.
    question (str): The short question for which no answer should be provided.
Response:
    None
```"""
    """```
Description:
    Ensures that the chatbot does not provide an answer for short questions.

Arguments:
    client (test client): The test client for making HTTP requests.
    question (str): The short question for which no answer should be provided.

Response:
    None
```"""
    response = client.post('/department/quiklyz-mmfsl/chatapi', json={
        'question': question})
    res = response.json
    answer = res['answer']
    assert answer == 'No information found for your query. Please try again with different query.'
