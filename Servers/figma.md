# Figma MCP Server Reference

## Overview

The figma mcp server connects to Figma to provide design context (frames, components, variables) to AI agents.

**Use for:** Generating code from selected frames, extracting design variables/components, and retrieving FigJam and Make resources for context.

## Configuration

figma:
   - Description: Used for accessing Figma design data via the remote MCP server.
   - Info URL: `https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/`
   - Transport Type: streamable_http
   - Configuration:
   ```yaml
    figma:
      transport: streamable_http
      url: "https://mcp.figma.com/mcp"
   ```