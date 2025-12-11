# Airweave Search MCP Server Reference

## Overview

The airweave-search mcp server provides access to the open-source Airweave platform for transforming apps, databases, documents, and productivity tools into searchable knowledge bases.

**Use for:** Searching connected knowledge bases within Airweave.


## Configuration

airweave-search:
   - Description: Used for interacting with Airweave collections.
   - Info URL: `https://docs.airweave.ai/mcp-server`
   - Transport Type: stdio
   - Configuration:
   ```yaml
    airweave-search:
        command: "npx"
        args:
            - "-y"
            - "airweave-mcp-search"
   ```
   - Secrets:
   ```yaml
    mcp.servers.airweave.env.AIRWEAVE_API_KEY: Your Airweave API key
    mcp.servers.airweave.env.AIRWEAVE_COLLECTION: Airweave collection ID to search
    ```

## Manual Setup

### 1. Create Airweave Account & Collection
Register an account in Airweave and create a collection with the desired connected data.

### 2. Obtain an API Key
Create an Airweave API Key at `https://app.airweave.ai/api-keys`.

### 3. Secrets Configuration
Specify the following secrets:
- `mcp.servers.airweave.env.AIRWEAVE_API_KEY`: Your API key from above
- `mcp.servers.airweave.env.AIRWEAVE_COLLECTION`: Collection ID for the desired collection to search
