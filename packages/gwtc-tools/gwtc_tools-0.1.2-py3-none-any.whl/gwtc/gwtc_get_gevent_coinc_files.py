from gwtc.gwtc_gracedb import GWTCGraceDB
import logging
from optparse import OptionParser

# setup verbose logs
logging.basicConfig(level=logging.INFO)


def get_super_events(client, g_events):
    out = {}
    retry = set()
    for gid in g_events:
        res = client.event(gid).json()
        if res["superevent"] is not None:
            out[res["superevent"]] = {res["pipeline"]: gid}
            logging.info(
                f"associated super event {res['superevent']} with gevent {gid}"
            )
        else:
            logging.debug(f"No super event found for gevent {gid}")
            retry.add(gid)
    return out, retry


def parse_command_line():
    parser = OptionParser()
    parser.add_option(
        "--pipeline",
        type="string",
        help="Set the pipeline. If not set all pipeline g events will be returned",
    )
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
    parser.add_option(
        "--version",
        type="int",
        help="Set the version. If not given, latest will be used",
    )
    options, _ = parser.parse_args()

    return options


def main():
    options = parse_command_line()

    client = GWTCGraceDB(service_url=options.service_url, cred=options.proxy_path)

    smap = client.gwtc_get(options.number, version=options.version or "latest").json()[
        "gwtc_superevents"
    ]

    for sid in smap:
        for p, gid in smap[sid]["pipelines"].items():
            if options.pipeline is None or p == options.pipeline:
                event = client.event(gid).json()
                cfile = client.files(gid, filename="coinc.xml")
                fname = "%s-%s_%s-%d-0.xml" % (
                    "".join(sorted(event["instruments"].split(","))),
                    p.upper(),
                    gid,
                    int(event["gpstime"]),
                )
                logging.info(
                    "Retrieving g event %s for s event %s and pipeline %s\n\t...saving as %s"
                    % (gid, sid, p, fname)
                )
                with open(fname, "wb") as f:
                    f.write(cfile.read())
