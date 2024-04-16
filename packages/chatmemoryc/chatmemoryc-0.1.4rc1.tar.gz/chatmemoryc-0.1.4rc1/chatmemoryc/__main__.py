import os
from argparse import ArgumentParser
import logging
from .server import ChatMemoryServer

def main():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    log_format = logging.Formatter("%(asctime)s %(levelname)8s %(message)s")
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(log_format)
    logger.addHandler(streamHandler)

    usage = "Usage: python {} [--key <anthropic api key>] [--host <ip address or hostname>] [--port <port_number>] [--help]".format(__file__)
    argparser = ArgumentParser(usage=usage)
    argparser.add_argument("--key", dest="api_key", help="ANTHROPIC API Key. Set here or environment variables with key 'ANTHROPIC_APIKEY'")
    argparser.add_argument("--host", dest="host", default="127.0.0.1", help="IP address to listen. Default is 127.0.0.1")
    argparser.add_argument("--port", dest="port", default=8124, type=int, help="Port numbert to listen. Default is 8124")
    args = argparser.parse_args()

    api_key = args.api_key or os.environ.get("ANTHROPIC_APIKEY")
    if not api_key:
        logger.error("ANTHROPIC API Key is missing")
        return

    host = args.host
    port = args.port

    logger.info("starting sever...")

    server = ChatMemoryServer(api_key=api_key)
    server.start(host=host, port=port)


if __name__ == "__main__":
    main()
