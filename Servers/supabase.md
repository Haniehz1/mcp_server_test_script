# Supabase MCP Server Reference

## Overview

The supabase mcp server connects to Supabase projects for database and backend operations.

**Use for:** Interacting with Supabase databases, querying data, managing projects, and accessing Supabase features.

## Configuration

supabase:
   - Description: Used for interacting with Supabase projects.
   - Info URL: `https://supabase.com/docs/guides/getting-started/mcp`
   - Transport Type: streamable_http
   - Configuration:
   ```yaml
    supabase:
      transport: streamable_http
      url: "https://mcp.supabase.com/mcp?project_ref=${SUPABASE_PROJECT_REF}"
      headers:
        Authorization: "Bearer ${SUPABASE_ACCESS_TOKEN}"
   ```
   - Secrets:
   ```yaml
    mcp.servers.supabase.headers.Authorization: Auth header with Personal Access Token for Supabase (Bearer prefix, then token)
    mcp.servers.supabase.url: URL with project reference ID, e.g. https://mcp.supabase.com/mcp?project_ref=<ref_id>
    ```

## Manual Setup

### 1. Create a Supabase Personal Access Token
Go to `https://supabase.com/dashboard`, click on your profile icon (top right) → **"Access Tokens"** → **"Generate new token"**. Give it a name (e.g., "MCP Server Token") and copy the token.

### 2. Get Project Reference ID (Optional)
To scope to a specific project: Go to your project dashboard → **"Settings"** → **"General"** → Copy the **"Reference ID"**.

### 3. Secrets Configuration
Specify the following secrets:
- `mcp.servers.supabase.headers.Authorization`: "Bearer <Personal Access Token for Supabase>"; set with the token obtained above and include the Bearer prefix
- `mcp.servers.supabase.url`: If scoping to a specific project reference, set this to the appropriate URL, e.g. https://mcp.supabase.com/mcp?project_ref=<ref_id>
