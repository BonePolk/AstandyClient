# Astandy v0.2 Proxies!
- The main feature is proxy support for the client.
- StandClient is no longer a new thread. [**Check migration guide!**](migration.md)
- StandClient can now automatically reconnect to the server after the connection is closed!
- New parameter for StandClient: **ping_timeout** – Maximum time (in seconds) to wait for a ping response.
- New parameter for StandClient: **alias_name** – The name of the client used in custom logging.
- New parameter for StandClient: **reconnect_enable** – If set to True, the client will try to reconnect after the connection is closed.
- New method for StandClient: **me** – Returns the player's profile.
- Now only 5 latest old logs saved.

## Astandy v0.2.3 
- StandClient will try to reconnect after any exception occured while client connecting.
- StandClient will retry to connect only **max_retry_count** times.
- New parameter for StandClient: **max_retry_count** – Maximum retries of connecting.
- **client.start()** now can throw ConnectionError if max retries number reached.

## Astandy v0.2.3.1
- Fix Event.wait not awaited

## Astandy v0.2.4
- Filters and comparison types fix