#!/bin/bash
# Railway provee PORT, no BACKEND_PORT
if [ -n "$PORT" ]; then
    export BACKEND_PORT=$PORT
else
    export BACKEND_PORT=8080
fi

echo "Starting Reflex on port $BACKEND_PORT"
reflex run --env prod --backend-only