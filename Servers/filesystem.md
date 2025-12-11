# Filesystem MCP Server Reference

## Overview

The filesystem mcp server is used for local file and directory operations.

**Use for:** Reading/writing files, directory operations, file management

## Configuration

filesystem:
   - Description: Used for local file and directory operations.
   - Info URL: `https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md`
   - Transport Type: stdio
   - Configuration:
   ```yaml
    filesystem:
        command: "npx"
        args:
            - "-y"
            - "@modelcontextprotocol/server-filesystem"
            - "." # directory
   ```
