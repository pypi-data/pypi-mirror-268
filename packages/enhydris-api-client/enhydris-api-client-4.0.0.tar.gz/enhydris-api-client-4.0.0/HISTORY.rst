=======
History
=======

4.0.0 (2024-04-16)
==================

- Requires htimeseries 7.
- When downloading time series data without specifying the time zone, it
  uses the ``display_timezone`` of that Enhydris station, whereas in
  3.x.x it used UTC. The behaviour is now similar to that of 2.x.x.

3.0.1 (2024-04-14)
==================

- Compatible with htimeseries 4 to 7.

3.0.0 (2022-12-04)
==================

- Requires Enhydris 4 and htimeseries 4, and therefore requires aware
  HTimeseries objects.
- Supports specifying time zone when downloading time series data.
- Support for creating, retrieving, updating, and deleting time series
  groups.

2.0.1 (2021-08-31)
==================

- Updated dependences (the version of htimeseries required was too old).

2.0.0 (2020-10-06)
==================

- We now support the time series groups of Enhydris 3. Earlier Enhydris
  versions are unsupported. Use enhydris-api-client v1 for Enhydris v2.
- We now use token authentication. Using a username and password have
  been deprecated and will be removed in a future version. Accordingly,
  the ``.login()`` method has been removed; it has been replaced with
  the deprecated ``.get_token()`` method.

1.0.0 (2020-02-28)
==================

- We now support only Python 3.7 or greater.
- If there is an http error, the error message now includes the response body.

0.5.1 (2020-01-05)
==================

- Minor fix for compatibility with htimeseries 2

0.5.0 (2019-06-13)
==================

- Can now be used as a context manager
- Added post/put/patch/delete station

0.4.1 (2019-06-12)
==================

- Fixed bug where .read_tsdata() was failing to set the metadata
  attributes of the time series.

0.4.0 (2019-06-12)
==================

- .read_tsdata() now accepts optional arguments start_date and end_date.

0.3.0 (2019-06-06)
==================

- Upgrade dependecy htimeseries to 1.0

0.2.0 (2019-04-17)
==================

- Support new API of Enhydris 3

0.1.0 (2019-03-06)
==================

- Initial release
