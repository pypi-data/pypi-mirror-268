from gwtc.gwtc_gracedb import GWTCGraceDB
from .gwtc import smap_from_gracedb_query
import logging
from optparse import OptionParser
import json

# setup verbose logs
logging.basicConfig(level=logging.INFO)


def parse_command_line():
    parser = OptionParser(usage="usage: %prog [options] query")
    parser.add_option(
        "--proxy-path", type="string", help="Set the path to find the proxy file"
    )
    parser.add_option(
        "--service-url",
        type="string",
        default="https://gracedb-test.ligo.org/api/",
        help="Set the gracedb service url. Default: https://gracedb-test.ligo.org/api/",
    )
    parser.add_option(
        "--number", type="str", default="4", help='Set the catalog number: default "4"'
    )
    options, query = parser.parse_args()

    return options, query


def main():
    options, query = parse_command_line()

    client = GWTCGraceDB(service_url=options.service_url, cred=options.proxy_path)
    query = query[0].replace("\\", " ")
    client = GWTCGraceDB(service_url=options.service_url, cred=options.proxy_path)
    query = query[0].replace("\\", " ")

    smap = smap_from_gracedb_query(client, query)

    resp = client.gwtc_create(smap, number=options.number)
    logging.info(f"Created GWTC:\n{json.dumps(resp.json(), indent=4)}")
