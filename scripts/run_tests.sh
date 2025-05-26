# Abort execution when failing command
set -e
# Place execution on scrip directory for more flexible execution (can be invoked from anywhere).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $SCRIPT_DIR/..
# Load configration/environment varibales
source ./.config/.env
# Run server
python ./test/test_move.py
python ./test/test_create.py
python ./test/test_status.py