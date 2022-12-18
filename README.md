# Aurora

This bot is used to notify aurora hunters about approaching northern lights.
Data is parsed from [NASA's SWPC](https://www.swpc.noaa.gov/) and [openweather](https://openweathermap.org/)

The notification is based on your location: when you send your location to the bot, it is converted to magnetic coordinates and then
corresponding settings are applied.

Build and deployment:

- Multi-stage build Docker image
- Minimalistic final image without poetry deps installed
- Kubernetes is coming

See Makefile for availiable actions


