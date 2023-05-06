import openai


openai.api_key = "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"


def query(prompt):
    model_engine = "text-davinci-003"

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return completion.choices[0].text
