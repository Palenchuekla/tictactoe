# Abort execution when failing command
set -e
# Parse arguments
parse_args() {
    DB_URL="sqlite+pysqlite:///./tmp/tictactoe.db"
    show_help() {
        echo -e "Usage: run.sh [options]"
        echo -e "Options:"
        echo -e "\t-u, --url <url>  URL of the server database."
        echo -e "\t-h, --help      Show this help message and exit"
    }
    while [[ $# -gt 0 ]]; do
        case $1 in
            -u|--url)
                DB_URL="$2"
                shift 2
                ;;
            -h|--help)
                show_help
                exit 0
                ;;
            *)
                echo "Unknown argument: $1"
                show_help
                exit 1
                ;;
        esac
    done
}
parse_args "$@"

# Place execution on scrip directory for more flexible execution (can be invoked from anywhere).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $SCRIPT_DIR/..

# Load configuration/environment varibales
export DB_URL

# Run server
echo -e "Running server with the following DB_URL = \"$DB_URL\"".
python -m uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
