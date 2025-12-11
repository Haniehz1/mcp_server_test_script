# Notion MCP Server Reference

## Overview

The notion mcp server is used for securely interacting with Notion workspaces.

**Use for:** Accessing and creating Notion workspace content, including: creating documentation, searching and finding answers, managing tasks, building reports and planning campaigns.

## Configuration

notion:
   - Description: Used for interacting with Notion workspaces.
   - Info URL: `https://developers.notion.com/docs/mcp`
   - Transport Type: streamable_http
   - Configuration:
   ```yaml
    notion:
      transport: streamable_http
      url: "https://mcp.notion.com/mcp"
   ```
