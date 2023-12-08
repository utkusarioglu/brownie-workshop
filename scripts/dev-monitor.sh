#!/bin/bash
source ~/venv/main/bin/activate

echo "Starting watchmedo for \`src/main.py\`…"
watchmedo shell-command \
  --patterns "*.py" \
  --recursive \
  --wait \
  --verbose \
  --command '
      if [ "${watch_event_type}" = "closed" ]; then
        src/main.py
      fi
  '\
  src
