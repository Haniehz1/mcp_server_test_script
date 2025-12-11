# Perplexity MCP Server Reference

## Overview

The perplexity mcp server connects to Perplexity’s search and reasoning APIs.

**Use for:** Real-time web search, conversational answers, deep research, and advanced reasoning via Perplexity tools.

## Configuration

perplexity:
   - Description: Used for Perplexity search, ask, research, and reasoning tools.
   - Info URL: `https://docs.perplexity.ai/guides/mcp-server`
   - Transport Type: stdio
   - Configuration:
   ```yaml
    perplexity:
      command: "npx"
      args:
        - "-y"
        - "@perplexity-ai/mcp-server"
      env:
        PERPLEXITY_API_KEY: "${PERPLEXITY_API_KEY}"
   ```
   - Secrets:
   ```yaml
    mcp.servers.perplexity.env.PERPLEXITY_API_KEY: Perplexity API key
   ```

## Manual Setup

### 1. Generate an API key
Create a key in the Perplexity API portal: `https://www.perplexity.ai/account/api/group`.

###2. Set secrets
Specify the following secret:
- `mcp.servers.perplexity.env.PERPLEXITY_API_KEY`: Perplexity API key
