On PSU ICDS I used the following IGWN environment
```
source /cvmfs/oasis.opensciencegrid.org/ligo/sw/conda/etc/profile.d/conda.sh && conda activate igwn-py39 && export PATH=${PATH}:~/.local/bin
```
Consult the README at the top level of the repo to learn how to install this code.

First I reset all of the gwtc information in gracedb test (this has to be done pipeline by pipeline)
```
$ gwtc_update_pipeline_gevents --reset --pipeline gstlal --group CBC --search AllSky --service-url https://gracedb-test.ligo.org/api/ --number 4
$ gwtc_update_pipeline_gevents --reset --pipeline spiir --group CBC --search AllSky --service-url https://gracedb-test.ligo.org/api/ --number 4
$ gwtc_update_pipeline_gevents --reset --pipeline MBTA --group CBC --search AllSky --service-url https://gracedb-test.ligo.org/api/ --number 4
$ gwtc_update_pipeline_gevents --reset --pipeline pycbc --group CBC --search AllSky --service-url https://gracedb-test.ligo.org/api/ --number 4
```

Before the next steps, copy the contents of the examples directory

Upload events

```
$ gwtc_update_pipeline_gevents --pipeline gstlal --group CBC --search AllSky --number 4 --in-yaml gstlalv1.yaml --out-yaml gstlal_processedv1.yaml
INFO:root:Uploaded G651753
INFO:root:Uploaded G651754
INFO:root:associated super event S230522a with gevent G651754
INFO:root:associated super event S230824d with gevent G651753
INFO:root:Uploading
{
    "S230522a": {
        "pipelines": {
            "gstlal": "G651754"
        },
        "far": 3.171756306943489e-16,
        "pastro": null
    },
    "S230824d": {
        "pipelines": {
            "gstlal": "G651753"
        },
        "far": 1.611950746698324e-13,
        "pastro": null
    }
}
INFO:root:Created GWTC:
{
    "number": "4",
    "version": 53,
    "created": "2024-02-28 14:52:25 UTC",
    "submitter": "chad.hanna@ligo.org",
    "gwtc_superevents": {
        "S230824d": {
            "pipelines": {
                "gstlal": "G651753"
            },
            "far": 1.611950746698324e-13,
            "pastro": null
        },
        "S230522a": {
            "pipelines": {
                "gstlal": "G651754"
            },
            "far": 3.171756306943489e-16,
            "pastro": null
        }
    },
    "comment": ""
}
```

You can see that the GIDs were added to the output yaml file (this is just meant as a convenience for the user)

```
$ cat gstlal_processedv1.yaml 
- coinc: H1L1-GSTLAL_AllSky-1376883065-0.xml.gz
  gid: G651753
  pastro: null
- coinc: L1-GSTLAL_AllSky-1368783503-0.xml.gz
  gid: G651754
  pastro: null
```

Check the diff

```
$ gwtc_diff
INFO:root:Calculating catalog diff from versions None to None
INFO:root:
- new s events in version 53: ['S230522a', 'S230824d']
- deleted s events in version 53: []
- changed s events in version 53:
```

Upload a new version of the pipeline events.

```
$ gwtc_update_pipeline_gevents --pipeline gstlal --group CBC --search AllSky --number 4 --in-yaml gstlalv2.yaml --out-yaml gstlal_processedv2.yaml
```

Check the diff

```
$ gwtc_diff
INFO:root:Calculating catalog diff from versions None to None
INFO:root:
- new s events in version 54: ['S230513ar']
- deleted s events in version 54: []
- changed s events in version 54:

	S230824d:
		pipelines: {'gstlal': 'G651753'} -> {'gstlal': 'G651772'}

	S230522a:
		pastro: None -> {'BBH': 1.0, 'BNS': 0.0, 'NSBH': 0.0, 'Terrestrial': 0.0}
		pipelines: {'gstlal': 'G651754'} -> {'gstlal': 'G651773'}
```
