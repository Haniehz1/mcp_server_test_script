# Linear MCP Server Reference

## Overview

The linear mcp server is used to access Linear for managing issues, projects, cycles, and other workspace resources.

**Use for:** Searching and managing Linear issues and accessing comments and discussions associated with issues, interacting with and monitoring projects and cycles, retrieving Linear team information.

## Configuration

linear:
   - Description: Used for interacting with Linear issues, projects, cycles and workspaces.
   - Info URL: `https://linear.app/docs/mcp`
   - Transport Type: streamable_http
   - Configuration:
   ```yaml
    notion:
      transport: streamable_http
      url: "https://mcp.linear.app/mcp"
   ```
