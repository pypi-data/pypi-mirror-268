cd `dirname $0`/../src
#MODEL=../local/models/mlx/Mistral-7B-v0.2-Instruct-f16
#MODEL=mlx-community/Mistral-7B-Instruct-v0.2
MODEL=mlx-community/Mistral-7B-v0.2-4bit
#MODEL=mistralai/Mistral-7B-Instruct-v0.2
#MODEL=mlx-community/Mixtral-8x22B-4bit
#MODEL=mlx-community/CodeQwen1.5-7B-Chat-4bit
EVAL_FILE=../../eval/fireworks-ai_function-calling-eval-dataset-v0/single_turn-00000-of-00001.json
#EVAL_FILE=../../eval/fireworks-ai_function-calling-eval-dataset-v0/multi_turn-00000-of-00001.json
python3 -m tests.eval --model $MODEL --dataset $EVAL_FILE $@
