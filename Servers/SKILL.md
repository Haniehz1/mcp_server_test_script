---
name: mcp-server-configuration
description: Retrieve relevant MCP server information from a curated selection of supported MCP servers. Use when discovering which MCP servers are available for specific functionality needs (email, GitHub, slack, file operations, web requests, etc.) and for subsequent configuration of those servers.
---

# MCP Server Configuration

## Overview

This skill provides specialized knowledge for recommending and configuring MCP servers from the official supported MCP servers list. It helps discover available servers based on functionality requirements, provides properly formatted configuration examples and outlines any manual steps the user must follow for configuring the servers. Each supported server has a local reference doc outlining details about the server.

## When to Use This Skill

Use this skill when:
- Finding MCP servers for specific functionality (email, GitHub, APIs, etc.)
- Users ask "What MCP servers are available for X?"
- Discovering which servers exist for a particular use case
- Providing MCP server configuration examples
- Assisting the user with the necessary manual steps for configuring an MCP server

## Official Supported MCP Servers

**ONLY the following MCP servers are supported:**

### 1. Airweave Search Server
Provides access to the open-source Airweave platform for transforming apps, databases, documents, and productivity tools into searchable knowledge bases.

**Use for:** Searching connected knowledge bases within Airweave.

### 2. Atlassian Server
Provides access to Jira and Confluence data.

**Use for:** Searching, creating and updating Jira issues and projects; accessing and managing Confluence pages and spaces for documentation.

### 3. CircleCI Server
Connects to CircleCI to surface build, pipeline, and test information.

**Use for:** Inspecting pipeline status, build details, test results, and related CI/CD context.

### 4. Fetch Server
For making HTTP requests and fetching web content.

**Use for:** Web scraping, API calls, HTTP requests, fetching URLs

### 5. Figma Server
Connects to Figma to provide design context (frames, components, variables) to AI agents.

**Use for:** Generating code from selected frames, extracting design variables/components, and retrieving FigJam and Make resources for context.

### 6. Filesystem Server
For local file and directory operations.

**Use for:** Reading/writing files, directory operations, file management

### 7. GitHub Server
Provides access to all available GitHub MCP tools for interacting with GitHub.

**Use for:** Interacting with GitHub Issues, Repositories, Actions, workflows, and other GitHub tools.

### 8. Linear Server
Provides access to Linear for managing issues, projects, cycles, and other workspace resources.

**Use for:** Searching and managing Linear issues and accessing comments and discussions associated with issues, interacting with and monitoring projects and cycles, retrieving Linear team information.

### 9. Notion Server
Gives secure access to Notion workspaces.

**Use for:** Accessing and creating Notion workspace content, including: creating documentation, searching and finding answers, managing tasks, building reports and planning campaigns.

### 10. Perplexity Server
Connects to Perplexity search and reasoning APIs.

**Use for:** Real-time web search, conversational answers, deep research, and advanced reasoning via Perplexity tools.

### 11. Sequential Thinking Server
Provides a structured, reflective tool for multi-step problem solving and branching.

**Use for:** Guided reasoning that breaks problems into steps, allows revisions, and tracks branched thought processes.

### 12. Playwright Server
Provides browser automation capabilities for interacting with web pages using Playwright.

**Use for:** Navigating pages, interacting with accessible elements, and extracting structured page context without screenshots.

### 13. Supabase Server
Connects to Supabase projects for database and backend operations.

**Use for:** Interacting with Supabase databases, querying data, managing projects, and accessing Supabase features.

### 14. HubSpot Server
Connects to HubSpot CRM APIs for accessing CRM records (contacts, companies, deals).

**Use for:** Retrieving and managing HubSpot CRM data within agent workflows.

### 15. Google Maps Grounding Lite Server
Exposes Google Maps tools for places search, weather lookup, and route computation.

**Use for:** Grounding AI responses with Maps place summaries/IDs/coords, weather, and basic route distance/duration.

## Search Workflow

### Step 1: Understand the Requirement
Analyze what functionality the user needs:
- File operations → use built-in filesystem server
- Web requests → use built-in fetch server
- Github operations → use github server

### Step 2: Extract Server Information
For the official MCP servers outlined above, retrieve the relevant configuration information from the server's reference doc:
- Server name and description
- Transport type (sse, streamable_http, stdio)
- Authentication requirements (if any)

### Step 3: Present Findings
Format the response using the output format below.

## Output Format

Format responses as:

```md
**Found {N} MCP Server(s) for {use case}:**

1. **{name}**
   - Description: {description}
   - Info URL: {info_url}
   - Transport Type: {transport_type}
   - Configuration:
   ```yaml
   {server_name}:
     url: "{remote_url}" # if remote server
     transport: "{transport_type}"
     headers: # If specified, e.g.
         Authorization: "Bearer {api_key_if_needed}"
   ```
   (if applicable, include the following)
   - Secrets:
   ```yaml
    {path}: {description}
    ```
```

**Configuration format must match MCPServerSettings from:** https://github.com/lastmile-ai/mcp-agent/blob/main/schema/mcp-agent.config.schema.json

For built-in servers (fetch/filesystem), show their command/args configuration instead.

### Step 4: Manual Set Up / Configuration
If the user would like to use a server which requires manual setup or configuration, use the outlined instructions in the reference doc for the server. If secrets are required, you must help the user configure them using the 'secret' boltAction.

## Guidelines

- **ONLY suggest our official supported servers and ONLY when applicable**
- Try multiple search terms (synonyms, related terms)
- Include practical information: language, authentication needs, setup complexity
- Be honest if a server doesn't exist

## Resources

### references/
This skill includes reference documentation:
- `airweave-search.md` - Details about the airweave search mcp server
- `atlassian.md` - Details about the atlassian mcp server
- `circleci.md` - Details about the circleci mcp server
- `fetch.md` - Details about the fetch mcp server
- `figma.md` - Details about the figma mcp server
- `filesystem.md` - Details about the filesystem mcp server
- `github.md` - Details about the github mcp server
- `linear.md` - Details about the linear mcp server
- `notion.md` - Details about the notion mcp server
- `perplexity.md` - Details about the perplexity mcp server
- `playwright.md` - Details about the playwright mcp server
- `supabase.md` - Details about the supabase mcp server
- `sequentialthinking.md` - Details about the sequential thinking mcp server
- `hubspot.md` - Details about the HubSpot mcp server
- `maps-grounding-lite.md` - Details about the Google Maps Grounding Lite mcp server
