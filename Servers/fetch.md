# Fetch MCP Server Reference

## Overview

The fetch mcp server is used for making HTTP requests and fetching web content.

**Use for:** Web scraping, API calls, HTTP requests, fetching URLs

## Configuration

fetch:
   - Description: Used for making HTTP requests and fetching web content.
   - Info URL: `https://pypi.org/project/mcp-server-fetch/`
   - Transport Type: stdio
   - Configuration:
   ```yaml
    fetch:
        url: "{remote_url}" # if remote server
        command: "uvx"
        args: ["mcp-server-fetch"]
   ```
