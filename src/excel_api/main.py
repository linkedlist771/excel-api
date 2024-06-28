from excel_api.core.registarar import register_app
from excel_api.core.arg_parser import get_arg_parser
from excel_api.core.server import start_server

app = register_app()
parser = get_arg_parser()
args = parser.parse_args()

if __name__ == "__main__":
    start_server(args.port, args.host, app)
