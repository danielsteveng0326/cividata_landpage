#!/bin/bash
PORT=${PORT:-3000}
echo "Starting Reflex full stack on port $PORT"
reflex run --env prod --frontend-port $PORT --backend-port $PORT --host 0.0.0.0