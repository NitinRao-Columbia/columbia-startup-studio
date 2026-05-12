#!/bin/bash
#
# Export reveal.js presentation to PDF using Decktape
# Usage: ./export-pdf.sh [output-name]
#
# Requires: decktape (npm install -g decktape)
#

set -e

# Default output name based on folder name
DECK_DIR="$(cd "$(dirname "$0")" && pwd)"
FOLDER_NAME="$(basename "$DECK_DIR")"
OUTPUT_NAME="${1:-$FOLDER_NAME}"

# Remove .pdf extension if provided (we'll add it)
OUTPUT_NAME="${OUTPUT_NAME%.pdf}"

# Port for temporary server
PORT=${EXPORT_PORT:-8754}

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Exporting presentation to PDF...${NC}"

# Check if decktape is installed
if ! command -v decktape &> /dev/null; then
    echo -e "${RED}Error: decktape is not installed${NC}"
    echo "Install it with: npm install -g decktape"
    exit 1
fi

# Start a simple HTTP server in the background
cd "$DECK_DIR"
python3 -m http.server $PORT &> /dev/null &
SERVER_PID=$!

# Give the server a moment to start
sleep 1

# Cleanup function to kill server on exit
cleanup() {
    kill $SERVER_PID 2>/dev/null || true
}
trap cleanup EXIT

# Run decktape
echo -e "Rendering slides..."
decktape reveal "http://localhost:$PORT/index.html" "${OUTPUT_NAME}.pdf" \
    --size 1920x1080 \
    --pause 500

echo -e "${GREEN}Done! Created: ${OUTPUT_NAME}.pdf${NC}"
