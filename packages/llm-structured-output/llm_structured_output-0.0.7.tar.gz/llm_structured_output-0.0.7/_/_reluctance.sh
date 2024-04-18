cd `dirname $0`/../src
#MODEL=mistralai/Mistral-7B-Instruct-v0.2
MODEL=mlx-community/Mistral-7B-v0.2-4bit
PROMPT='[INST] Parse the following address into a JSON object: "27 Barrow St, New York, NY 10014". Your answer should be only a JSON object according to this schema: {"type": "object", "properties": {"streetNumber": {"type": "number"}, "streetName": {"type": "string"}, "city": {"type": {"string"}}, "state": {"type": "string"}, "zipCode": {"type": "number"}}}. Do not explain the result, just output it. Do not add any additional information. [/INST]'
SCHEMA='{"type": "object", "properties": {"streetNumber": {"type": "number"}, "streetName": {"type": "string"}, "city": {"type": "string"}, "state": {"type": "string"}, "zipCode": {"type": "number"}}}'
python3 -m examples.reluctance --model-path $MODEL --prompt "$PROMPT" --schema "$SCHEMA" $@
