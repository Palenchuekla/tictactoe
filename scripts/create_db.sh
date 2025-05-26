# Abort execution when failing command
set -e

# Parse arguments
parse_args() {
    VERBOSE=false
    POPULATE=false
    DB_NAME="tictactoe"
    show_help() {
        echo -e "Usage: run.sh [options]"
        echo -e "Options:"
        echo -e "\t-n, --name <file_name>  Specify the name of the created database. Default = $DB_NAME. Directory will always be ./tmp."
        echo -e "\t-v, --verbose      Pretty Print created table. Default = false."
        echo -e "\t-p, --populate      Populate the database with dummy examples. Default = true."
        echo -e "\t-h, --help      Show this help message and exit"
    }
    while [[ $# -gt 0 ]]; do
        case $1 in
            -v|--verbose)
                VERBOSE=true
                shift
                ;;
            -p|--populate)
                POPULATE=true
                shift
                ;;
            -n|--name)
                DB_NAME="$2"
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

# Create temporal folder for database if it does not exist
# It will always be the same to avoid problems with access priviledges and removing sensitive data
if [[ ! -d "./tmp" ]]; then
    mkdir ./tmp
fi

# Create databse
CMD="python -m src.database.create_db -i ./tmp/$DB_NAME.db"
if [ "$VERBOSE" = true ]; then
    CMD="$CMD -v"
fi
if [ "$POPULATE" = true ]; then
    CMD="$CMD -p"
fi
eval $CMD