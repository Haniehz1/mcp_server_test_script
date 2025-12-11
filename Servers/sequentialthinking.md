# Sequential Thinking MCP Server Reference

## Overview

The Sequential Thinking MCP server provides a structured, reflective tool for breaking down and refining problem-solving steps.

**Use for:** Guided, multi-step reasoning where you want to plan, branch, and revise thoughts as you work toward a solution.

## Configuration

sequential-thinking:
   - Description: Provides structured, iterative thinking and branching.
   - Info URL: `https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking`
   - Transport Type: stdio
   - Configuration (NPX):
   ```yaml
    sequential-thinking:
      command: "npx"
      args:
        - "-y"
        - "@modelcontextprotocol/server-sequential-thinking"
   ```

   - Optional env:
   ```yaml
    mcp.servers.sequential-thinking.env.DISABLE_THOUGHT_LOGGING: "true" # disable logging of thought details
   ```
