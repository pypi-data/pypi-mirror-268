cd `dirname $0`/../src

SCHEMA='{"type": "array", "items": { "type": "number" }}'
INPUT='[5, 10, 15, 20, 25]'

python3 -m examples.json_schema_cli "$SCHEMA" "$INPUT" $@
