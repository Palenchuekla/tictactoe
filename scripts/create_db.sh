# Abort execution when failing command
set -e
# Place execution on scrip directory for more flexible execution (can be invoked from anywhere).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $SCRIPT_DIR/..
# Load configration/environment varibales
source ./.config/.env
# Create temporal folder for database if it does not exist
if [[ ! -d "./tmp" ]]; then
    mkdir ./tmp
fi
# Create dummy databse
python -m src.database.create_example_db -i $DB_PATH