import argparse

from . import server

parser = argparse.ArgumentParser(
    prog='model_explorer',
    description='A modern model graph visualizer and debugger',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('model_paths',
                    nargs='?',
                    help='comma separated model file paths')
parser.add_argument('--host',
                    default='localhost',
                    help='host of the server')
parser.add_argument('--port',
                    default=8080,
                    type=int,
                    help='port of the server')
parser.add_argument('--no_open_in_browser',
                    action='store_true',
                    help='Don\'t open the web app in browser after server starts')
parser.add_argument('--extensions',
                    help='comma separated extension module names')
parser.add_argument('--cors_host',
                    help='the host of the Access-Control-Allow-Origin header')
args = parser.parse_args()


def main():
  """Entry point for the command line version of model explorer."""

  model_paths: list[str] = []
  if args.model_paths is not None and args.model_paths != '':
    model_paths = [x.strip() for x in args.model_paths.split(',')]

  extensions: list[str] = []
  if args.extensions is not None:
    extensions = [x.strip() for x in args.extensions.split(',')]

  server.start(host=args.host,
               port=args.port,
               model_paths=model_paths,
               extensions=extensions,
               cors_host=args.cors_host,
               no_open_in_browser=args.no_open_in_browser)
