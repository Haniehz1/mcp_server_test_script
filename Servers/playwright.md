# Playwright MCP Server Reference

## Overview

The playwright mcp server provides browser automation using Playwright’s accessibility tree.

**Use for:** Navigating pages, interacting with accessible elements, and extracting structured page context without screenshots.

## Configuration

playwright:
   - Description: Used for browser automation via Playwright.
   - Info URL: `https://github.com/microsoft/playwright-mcp`
   - Transport Type: stdio
   - Configuration:
   ```yaml
    playwright:
      command: "npx"
      args:
        - "@playwright/mcp@latest"
   ```
   - Secrets:
   ```yaml
    # None required; authenticates via normal Playwright flows as needed
   ```

## Manual Setup

- Ensure Node.js 18+ is installed (Playwright requirement).
- Start the server from your client; it will launch Playwright as needed. If sites require auth, log in through the browser context opened by Playwright.
