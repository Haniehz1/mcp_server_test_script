# Atlassian MCP Server Reference

## Overview

The atlassian mcp server is used for securely accessing Jira and Confluence data.

**Use for:** Searching, creating and updating Jira issues and projects; accessing and managing Confluence pages and spaces for documentation.

## Configuration

atlassian:
   - Description: Used for interacting with Jira and Confluence data.
   - Info URL: `https://www.atlassian.com/platform/remote-mcp-server`
   - Transport Type: sse
   - Configuration:
   ```yaml
    notion:
      transport: sse
      url: "https://mcp.atlassian.com/v1/sse"
   ```
