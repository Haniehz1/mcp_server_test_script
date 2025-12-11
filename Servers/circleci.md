# CircleCI MCP Server Reference

## Overview

The circleci mcp server connects to CircleCI to surface build, pipeline, and test information.

**Use for:** Inspecting pipeline status, build details, test results, and related CI/CD context.

## Configuration

circleci:
   - Description: Used for interacting with CircleCI pipelines and builds.
   - Info URL: `https://circleci.com/mcp/`
   - Transport Type: stdio
   - Configuration:
   ```yaml
    circleci:
      command: "npx"
      args:
        - "-y"
        - "@circleci/mcp-server-circleci@latest"
      env:
        CIRCLECI_TOKEN: "${CIRCLECI_TOKEN}"
        CIRCLECI_BASE_URL: "https://circleci.com" # optional override of API host
   ```
   - Secrets:
   ```yaml
    mcp.servers.circleci.env.CIRCLECI_TOKEN: CircleCI personal API token
    mcp.servers.circleci.env.CIRCLECI_BASE_URL: Optional API base URL (defaults to https://circleci.com)
   ```

## Manual Setup

### 1. Generate a CircleCI API token
Create a personal API token in CircleCI user settings (`https://app.circleci.com/settings/user/tokens`) and copy it.

### 2. Set secrets
Specify the following secret:
- `mcp.servers.circleci.env.CIRCLECI_TOKEN`: Your CircleCI personal API token
- `mcp.servers.circleci.env.CIRCLECI_BASE_URL`: Optional API base URL (defaults to https://circleci.com)
