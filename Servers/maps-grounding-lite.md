# Google Maps Grounding Lite MCP Server Reference

## Overview

Grounding Lite exposes Google Maps geospatial tools (places search, weather lookup, route computation) via MCP.

**Use for:** Searching places with summaries/IDs/coords/links, retrieving weather, and computing driving/walking routes for grounding.

## Configuration

maps-grounding-lite:
   - Description: Provides Maps grounding tools (places, weather, routes) over MCP.
   - Info URL: `https://developers.google.com/maps/ai/grounding-lite`
   - Transport Type: streamable_http
   - Configuration (API key):
   ```yaml
    maps-grounding-lite:
      transport: streamable_http
      url: "https://mapstools.googleapis.com/mcp"
      headers:
        X-Goog-Api-Key: "${GOOGLE_MAPS_API_KEY}"
   ```
   - Secrets:
   ```yaml
    mcp.servers.maps-grounding-lite.headers.X-Goog-Api-Key: API key with Maps Grounding Lite enabled
   ```

## Manual Setup

1) Enable Maps Grounding Lite and MCP endpoint on your Google Cloud project (billing must be enabled, usage is free while experimental):
   ```bash
   gcloud beta services enable mapstools.googleapis.com --project=PROJECT_ID
   gcloud beta services mcp enable mapstools.googleapis.com --project=PROJECT_ID
   ```
2) Create or reuse a Google Maps API key and enable the Grounding Lite API on it. Apply key restrictions per your security posture.
3) Configure your MCP client with the streamable_http endpoint `https://mapstools.googleapis.com/mcp` and set header `X-Goog-Api-Key` to the key above.
4) Optional: If using OAuth instead of an API key, supply the OAuth client credentials to your MCP host and include any required auth headers when calling the MCP endpoint.

Notes:
- Respect Maps Platform Terms: do not cache or use returned data to train/improve models; include required Google Maps source attributions in outputs.
- Quotas (experimental): search_places 100 QPM/1,000 QPD; lookup_weather 300 QPM; compute_routes 300 QPM.
