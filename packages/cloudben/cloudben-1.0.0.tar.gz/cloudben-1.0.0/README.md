# `cloudben`

**Usage**:

```console
$ cloudben [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `create-record`: Create a DNS records for a specific zone.
* `delete-record`: Delete a DNS record given a record id...
* `delete-records`: Delete all the DNS records that match the...
* `export-records`: Export DNS records for a specific zone.
* `get-records`: Get all the DNS records for a specific...

## `cloudben create-record`

Create a DNS records for a specific zone.
Example usage: cloudben create-record $zoneid "cloudben" "my-azure-alb.azure.com" CNAME

**Usage**:

```console
$ cloudben create-record [OPTIONS] ZONE_ID NAME CONTENT TYPE:{A|CNAME|AAAA|TXT|MX}
```

**Arguments**:

* `ZONE_ID`: your zone id  [required]
* `NAME`: name of the Cloudflare record  [required]
* `CONTENT`: value of the Cloudflare record (what the record will resolve to)  [required]
* `TYPE:{A|CNAME|AAAA|TXT|MX}`: type of the Cloudflare record  [required]

**Options**:

* `--priority INTEGER RANGE`: priority of the TXT record  [default: 0; 0<=x<=65535]
* `--json / --no-json`: will output valid JSON. It can we useful when using this command in your script. Vanity logging will be disabled  [default: no-json]
* `--help`: Show this message and exit.

## `cloudben delete-record`

Delete a DNS record given a record id
Example usage: cloudben delete-record $zoneid "<record_id>"

**Usage**:

```console
$ cloudben delete-record [OPTIONS] ZONE_ID RECORD_ID
```

**Arguments**:

* `ZONE_ID`: your zone id  [required]
* `RECORD_ID`: id of the record to delete  [required]

**Options**:

* `--force`: Do not ask for confirmation when deleting.
* `--help`: Show this message and exit.

## `cloudben delete-records`

Delete all the DNS records that match the provided queries. If both --name_query and --content_query are provided the records will match both the criterias (it's an AND not an OR)

Example usage: cloudben delete-record $zoneid "<record_id>" --name_query "benny"

**Usage**:

```console
$ cloudben delete-records [OPTIONS] ZONE_ID
```

**Arguments**:

* `ZONE_ID`: your zone id  [required]

**Options**:

* `--name-query TEXT`: Text to be contained in the record's name.
* `--content-query TEXT`: Text to be contained in the record's value.
* `--force`: Do not ask for confirmation when deleting.
* `--help`: Show this message and exit.

## `cloudben export-records`

Export DNS records for a specific zone.
Example usage: python cloudflare_cli.py export_dns_records --zone_id ZONE_ID

**Usage**:

```console
$ cloudben export-records [OPTIONS] ZONE_ID
```

**Arguments**:

* `ZONE_ID`: [required]

**Options**:

* `--help`: Show this message and exit.

## `cloudben get-records`

Get all the DNS records for a specific zone given a query.
Example usage: cloudben get-records $zoneid --query "ben" --json

**Usage**:

```console
$ cloudben get-records [OPTIONS] ZONE_ID
```

**Arguments**:

* `ZONE_ID`: your zone id  [required]

**Options**:

* `--name-query TEXT`: Text to be contained in the record's name.
* `--content-query TEXT`: Text to be contained in the record's content.
* `--json / --no-json`: will output valid JSON. It can we useful when using this command in your script. Vanity logging will be disabled  [default: no-json]
* `--help`: Show this message and exit.
