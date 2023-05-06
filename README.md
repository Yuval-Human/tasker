# tasker

This is a simple tasker service that gets task -> saves the taskId into the DB -> puts the task in a queue -> update the DB when task is done
To create the docker image run "docker build -t yuval_segal/seemplicity ."
The types of tasks that the service currently supports are:
  - sum_two_numbers: calculates the sum of two numbers
  - hello_world: sleep for some time and return "Hello World!"
  - query_chat_gpt: query chat GPT api

To use the service:
  - get the task result: ``curl --location --request GET '<server_address>/tasks/<task_id>' \
--header 'Content-Type: application/json' \``
  - sum_two_numbers: ``curl --location --request POST '<server_address>/sum_two_numbers' \
--header 'Content-Type: application/json' \
--data-raw '{"firstNum":<numer_one>,"secondNum":<numer_two>}'``
  - hello_world: ``curl --location --request POST '<server_address>/hello_world' \
--header 'Content-Type: application/json' \``
  - query_chat_gpt: ``curl --location --request POST '<server_address>/query_chat_gpt' \
--header 'Content-Type: application/json' \
--data-raw '{"prompt":<the_query>}'``

