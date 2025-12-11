# GitHub MCP Server Reference

## Overview

The github mcp server provides access to all available GitHub MCP tools for interacting with GitHub.

**Use for:** Interacting with GitHub Issues, Repositories, Actions, workflows, and other GitHub tools.

## Configuration

github:
   - Description: Used for interacting with GitHub tools.
   - Info URL: `https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/set-up-the-github-mcp-server`
   - Transport Type: streamable_http
   - Configuration:
   ```yaml
    github:
      transport: streamable_http
      url: "https://api.githubcopilot.com/mcp/"
      auth:
        oauth:
          enabled: true
          scopes: ["read:org", "public_repo", "user:email"]
          authorization_server: "https://github.com/login/oauth"
          use_internal_callback: false
          include_resource_parameter: false
   ```
   - Secrets:
   ```yaml
    mcp.servers.github.oauth.client_id: Client ID for GitHub Application
    mcp.servers.github.oauth.client_secret: Client secret for GitHub Application
    ```

## Manual Setup

### 1. Create a new GitHub App
Go to `https://github.com/settings/apps` (i.e. Settings > Developer Settings > GitHub Apps) to register a new GitHub App.

Set the Authorization callback URL to `http://127.0.0.1:33418/callback` to start. For testing in MCP Inspector, add `http://localhost:6274/oauth/callback`

NOTE: Once your server is deployed, you must set the authorization callback URL for your deployed server: `https:<server-id>.deployments.mcp-agent.com/callback`

### 2. Secrets Configuration
Specify the following secrets:
- `mcp.servers.github.oauth.client_id`: Client ID for GitHub Application
- `mcp.servers.github.oauth.client_secret`: Client secret for GitHub Application
