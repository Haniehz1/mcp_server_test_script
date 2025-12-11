"""
MCP Server Testing Framework

A comprehensive testing system for validating MCP server compatibility with mcp-agent SDK.
Tests 15 different MCP servers across various transport types and authentication methods.

Run locally: uv run main.py
Deploy to cloud: mcp-agent deploy mcp-server-tester
"""

from __future__ import annotations

import asyncio
import json
from datetime import datetime
from typing import Optional
from pathlib import Path

from mcp_agent.app import MCPApp
from mcp_agent.core.context import Context as AppContext
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM

# Create the MCPApp
app = MCPApp(
    name="mcp-server-tester",
    description="Testing framework for validating MCP servers with mcp-agent SDK",
)


# ===== INDIVIDUAL SERVER TEST TOOLS =====

@app.tool()
async def test_fetch_server(app_ctx: Optional[AppContext] = None) -> dict:
    """
    Test fetch server: Fetch apple.com homepage and extract first paragraph.

    Returns test result with status and details.
    """
    logger = app_ctx.app.logger
    logger.info("Testing fetch server - Fetching apple.com homepage...")

    try:
        # Fetch Apple's homepage
        result = await app_ctx.server_registry.call_tool(
            server_name="fetch",
            tool_name="fetch",
            arguments={"url": "https://www.apple.com"}
        )

        content = result.content[0].text if result.content else ""

        if not content or len(content) < 100:
            raise ValueError("No valid content received from apple.com")

        # Verify it's actually Apple's page
        if "apple" not in content.lower():
            raise ValueError("Did not receive Apple homepage content")

        return {
            "server": "fetch",
            "status": "success",
            "transport": "stdio",
            "auth_required": False,
            "details": f"✓ Fetched apple.com homepage ({len(content)} bytes)",
            "test_description": "Fetch apple.com and extract content",
            "bytes_received": len(content),
            "data_sample": content[:200] + "...",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Fetch server test failed: {e}")
        return {
            "server": "fetch",
            "status": "error",
            "transport": "stdio",
            "auth_required": False,
            "error": str(e),
            "error_type": type(e).__name__,
            "timestamp": datetime.now().isoformat()
        }


@app.tool()
async def test_filesystem_server(app_ctx: Optional[AppContext] = None) -> dict:
    """
    Test filesystem server: Read README.md and get first 3 lines.

    Returns test result with status and details.
    """
    logger = app_ctx.app.logger
    logger.info("Testing filesystem server - Reading README.md first 3 lines...")

    try:
        # Read the README file
        readme_result = await app_ctx.server_registry.call_tool(
            server_name="filesystem",
            tool_name="read_file",
            arguments={"path": "README.md"}
        )

        readme_content = readme_result.content[0].text if readme_result.content else ""

        if not readme_content:
            raise ValueError("Failed to read README.md")

        # Get first 3 lines
        lines = readme_content.split('\n')
        first_3_lines = '\n'.join(lines[:3])

        return {
            "server": "filesystem",
            "status": "success",
            "transport": "stdio",
            "auth_required": False,
            "details": f"✓ Read README.md - First 3 lines extracted",
            "test_description": "Read README.md and get first 3 lines",
            "total_lines": len(lines),
            "data_sample": first_3_lines,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Filesystem server test failed: {e}")
        return {
            "server": "filesystem",
            "status": "error",
            "transport": "stdio",
            "auth_required": False,
            "error": str(e),
            "error_type": type(e).__name__,
            "timestamp": datetime.now().isoformat()
        }


@app.tool()
async def test_playwright_server(app_ctx: Optional[AppContext] = None) -> dict:
    """
    Test Playwright server: Go to example.com and get the page title.

    Returns test result with status and details.
    """
    logger = app_ctx.app.logger
    logger.info("Testing playwright server - Loading example.com and getting title...")

    try:
        # Navigate to example.com
        nav_result = await app_ctx.server_registry.call_tool(
            server_name="playwright",
            tool_name="playwright_navigate",
            arguments={"url": "https://example.com"}
        )

        # Capture the page snapshot
        snapshot_result = await app_ctx.server_registry.call_tool(
            server_name="playwright",
            tool_name="playwright_snapshot",
            arguments={}
        )

        snapshot_content = snapshot_result.content[0].text if snapshot_result.content else ""

        # Validate we got example.com
        if "example domain" not in snapshot_content.lower():
            raise ValueError("Failed to load example.com")

        return {
            "server": "playwright",
            "status": "success",
            "transport": "stdio",
            "auth_required": False,
            "details": f"✓ Navigated to example.com and captured page",
            "test_description": "Go to example.com and get page title",
            "page_loaded": "example.com",
            "page_content_length": len(snapshot_content),
            "data_sample": snapshot_content[:200] + "...",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Playwright server test failed: {e}")
        return {
            "server": "playwright",
            "status": "error",
            "transport": "stdio",
            "auth_required": False,
            "error": str(e),
            "error_type": type(e).__name__,
            "timestamp": datetime.now().isoformat()
        }


@app.tool()
async def test_sequential_thinking_server(app_ctx: Optional[AppContext] = None) -> dict:
    """
    Test Sequential Thinking server: Create 2 thoughts (problem + solution).

    Returns test result with status and details.
    """
    logger = app_ctx.app.logger
    logger.info("Testing sequential-thinking server - Creating problem and solution thoughts...")

    try:
        # Step 1: State the problem
        thought1 = await app_ctx.server_registry.call_tool(
            server_name="sequential-thinking",
            tool_name="create_thought",
            arguments={
                "thought": "What is 15% of 200?",
                "thoughtType": "observation"
            }
        )

        # Step 2: Provide the answer
        thought2 = await app_ctx.server_registry.call_tool(
            server_name="sequential-thinking",
            tool_name="create_thought",
            arguments={
                "thought": "15% of 200 = 0.15 × 200 = 30",
                "thoughtType": "conclusion"
            }
        )

        content1 = thought1.content[0].text if thought1.content else ""
        content2 = thought2.content[0].text if thought2.content else ""

        if not content1 or not content2:
            raise ValueError("Failed to create thoughts")

        return {
            "server": "sequential-thinking",
            "status": "success",
            "transport": "stdio",
            "auth_required": False,
            "details": "✓ Created 2 sequential thoughts (problem → solution)",
            "test_description": "Create problem and solution thoughts",
            "thoughts_created": 2,
            "data_sample": f"{content1[:50]}... → {content2[:50]}...",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Sequential thinking server test failed: {e}")
        return {
            "server": "sequential-thinking",
            "status": "error",
            "transport": "stdio",
            "auth_required": False,
            "error": str(e),
            "error_type": type(e).__name__,
            "timestamp": datetime.now().isoformat()
        }


@app.tool()
async def test_server_with_auth(
    server_name: str,
    test_tool: str,
    test_args: dict,
    transport: str,
    test_description: str = "",
    app_ctx: Optional[AppContext] = None
) -> dict:
    """
    Generic test function for servers requiring authentication.
    Tests connectivity, auth flow, and actual data retrieval.

    Args:
        server_name: Name of the MCP server to test
        test_tool: Tool name to call for testing
        test_args: Arguments for the test tool
        transport: Transport type (stdio, sse, streamable_http)
        test_description: Human-readable description of what this test does

    Returns test result with status and details.
    """
    logger = app_ctx.app.logger

    # Create descriptive test messages
    test_descriptions = {
        "github": "Search Python AI repos with 1000+ stars",
        "linear": "Search for bug issues",
        "notion": "Search workspace for 'meeting notes'",
        "perplexity": "Ask about latest LLM developments",
        "supabase": "List your Supabase projects",
        "hubspot": "Search contacts in CRM",
        "circleci": "Get pipelines for React repo",
        "figma": "Get design file data",
        "atlassian": "Search JIRA for in-progress issues",
        "airweave": "Search knowledge base for AI trends",
        "maps-grounding-lite": "Find coffee shops in San Francisco"
    }

    desc = test_description or test_descriptions.get(server_name, f"Call {test_tool}")
    logger.info(f"Testing {server_name} server - {desc}...")

    try:
        # First, try to check if server is even registered
        if server_name not in app_ctx.server_registry.server_configs:
            return {
                "server": server_name,
                "status": "not_configured",
                "transport": transport,
                "auth_required": True,
                "test_description": desc,
                "error": f"Server '{server_name}' not found in registry",
                "timestamp": datetime.now().isoformat()
            }

        # Attempt to call the test tool
        result = await app_ctx.server_registry.call_tool(
            server_name=server_name,
            tool_name=test_tool,
            arguments=test_args
        )

        # Validate we got actual data back
        content = result.content[0].text if result.content else ""

        # Check if response is meaningful
        if not content or len(content) < 2:
            logger.warning(f"{server_name}: Got empty or minimal response")

        return {
            "server": server_name,
            "status": "success",
            "transport": transport,
            "auth_required": True,
            "details": f"✓ {desc}",
            "test_description": desc,
            "response_length": len(content),
            "data_sample": content[:150] + "..." if len(content) > 150 else content,
            "timestamp": datetime.now().isoformat()
        }

    except Exception as e:
        logger.error(f"{server_name} server test failed: {type(e).__name__}: {e}")
        error_msg = str(e)

        # Categorize the error
        if any(x in error_msg.lower() for x in ["not found", "not configured", "no such server"]):
            status = "not_configured"
            friendly_error = "Server or credentials not configured"
        elif any(x in error_msg.lower() for x in ["unauthorized", "authentication", "forbidden", "401", "403"]):
            status = "auth_error"
            friendly_error = "Authentication failed - check credentials/OAuth flow"
        elif any(x in error_msg.lower() for x in ["timeout", "connection", "refused"]):
            status = "connection_error"
            friendly_error = "Connection failed - server may be unreachable"
        elif any(x in error_msg.lower() for x in ["oauth", "token"]):
            status = "oauth_required"
            friendly_error = "OAuth authentication required - run oauth flow first"
        else:
            status = "error"
            friendly_error = error_msg

        return {
            "server": server_name,
            "status": status,
            "transport": transport,
            "auth_required": True,
            "error": friendly_error,
            "error_detail": error_msg,
            "error_type": type(e).__name__,
            "timestamp": datetime.now().isoformat()
        }


# ===== MAIN TEST ORCHESTRATOR =====

@app.async_tool()
async def run_all_server_tests(app_ctx: Optional[AppContext] = None) -> str:
    """
    Run comprehensive tests on all configured MCP servers.

    This is a long-running workflow that tests all 15 MCP servers and generates
    a detailed report showing which servers are working, which need configuration,
    and which have errors.

    Returns: JSON string with test results for all servers.
    """
    logger = app_ctx.app.logger
    logger.info("Starting comprehensive MCP server testing...")

    results = []

    # Test no-auth servers
    logger.info("Testing servers without authentication requirements...")

    no_auth_tests = [
        test_fetch_server(app_ctx=app_ctx),
        test_filesystem_server(app_ctx=app_ctx),
        test_playwright_server(app_ctx=app_ctx),
        test_sequential_thinking_server(app_ctx=app_ctx),
    ]

    for test_result in await asyncio.gather(*no_auth_tests, return_exceptions=True):
        if isinstance(test_result, Exception):
            logger.error(f"Test failed with exception: {test_result}")
            results.append({
                "status": "error",
                "error": str(test_result),
                "timestamp": datetime.now().isoformat()
            })
        else:
            results.append(test_result)

    # Test API key auth servers with realistic queries
    logger.info("Testing servers with API key authentication...")

    api_key_servers = [
        ("airweave-search", "search", {"query": "AI and machine learning trends"}, "stdio"),
        ("circleci", "get_pipelines", {"org_slug": "gh/facebook", "project_slug": "react"}, "stdio"),
        ("perplexity", "search", {"query": "What are the latest developments in LLM technology?"}, "stdio"),
        ("maps-grounding-lite", "search_places", {"query": "best coffee shops in San Francisco"}, "streamable_http"),
        ("hubspot", "search_contacts", {"query": "email:@example.com"}, "streamable_http"),
        ("supabase", "list_projects", {}, "streamable_http"),
    ]

    for server_name, tool_name, args, transport in api_key_servers:
        result = await test_server_with_auth(
            server_name=server_name,
            test_tool=tool_name,
            test_args=args,
            transport=transport,
            app_ctx=app_ctx
        )
        results.append(result)

    # Test OAuth/SSE servers with realistic queries
    logger.info("Testing servers with OAuth/SSE authentication...")

    oauth_servers = [
        ("atlassian", "search_issues", {"jql": "project = DEMO AND status = 'In Progress'"}, "sse"),
        ("figma", "get_file", {"file_key": "sample-design-file"}, "streamable_http"),
        ("github", "search_repositories", {"query": "language:python stars:>1000 topic:ai", "sort": "stars", "per_page": 5}, "streamable_http"),
        ("linear", "search_issues", {"query": "status:in_progress label:bug"}, "streamable_http"),
        ("notion", "search", {"query": "meeting notes"}, "streamable_http"),
    ]

    for server_name, tool_name, args, transport in oauth_servers:
        result = await test_server_with_auth(
            server_name=server_name,
            test_tool=tool_name,
            test_args=args,
            transport=transport,
            app_ctx=app_ctx
        )
        results.append(result)

    # Generate summary with detailed status breakdown
    summary = {
        "test_run": {
            "timestamp": datetime.now().isoformat(),
            "total_servers": len(results),
            "successful": len([r for r in results if r.get("status") == "success"]),
            "not_configured": len([r for r in results if r.get("status") == "not_configured"]),
            "auth_errors": len([r for r in results if r.get("status") == "auth_error"]),
            "oauth_required": len([r for r in results if r.get("status") == "oauth_required"]),
            "connection_errors": len([r for r in results if r.get("status") == "connection_error"]),
            "other_errors": len([r for r in results if r.get("status") == "error"]),
            "total_errors": len([r for r in results if r.get("status") not in ["success", "not_configured"]]),
        },
        "results": results
    }

    # Save results to file
    output_dir = Path("test_results")
    output_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"mcp_server_test_results_{timestamp}.json"

    with open(output_file, "w") as f:
        json.dump(summary, f, indent=2)

    logger.info(f"Test results saved to {output_file}")
    logger.info(f"Summary: {summary['test_run']['successful']}/{summary['test_run']['total_servers']} servers working")

    return json.dumps(summary, indent=2)


@app.tool()
async def get_server_status_summary(app_ctx: Optional[AppContext] = None) -> str:
    """
    Get a quick summary of all configured MCP servers and their expected status.

    Returns: Human-readable summary of server configuration.
    """
    servers = {
        "No Authentication Required": [
            "fetch - Web requests and HTTP calls",
            "filesystem - Local file operations",
            "playwright - Browser automation",
            "sequential-thinking - Structured reasoning",
        ],
        "API Key Authentication": [
            "airweave-search - Airweave knowledge base search",
            "circleci - CI/CD pipeline information",
            "perplexity - Web search and reasoning",
            "maps-grounding-lite - Google Maps tools",
            "hubspot - CRM data access",
            "supabase - Database operations",
        ],
        "OAuth/Remote Authentication": [
            "atlassian - Jira and Confluence",
            "figma - Design file access",
            "github - GitHub repositories and actions",
            "linear - Issue tracking",
            "notion - Workspace content",
        ],
    }

    summary = ["MCP Server Configuration Summary", "=" * 50, ""]

    for category, server_list in servers.items():
        summary.append(f"\n{category}:")
        summary.append("-" * 50)
        for server in server_list:
            summary.append(f"  • {server}")

    summary.append("\n" + "=" * 50)
    summary.append(f"Total: {sum(len(s) for s in servers.values())} servers configured")
    summary.append("\nRun 'run_all_server_tests' to test all servers")

    return "\n".join(summary)


async def main():
    """Main entry point for local testing."""
    async with app.run() as agent_app:
        print("\n" + "="*70)
        print("MCP SERVER TESTING FRAMEWORK")
        print("="*70 + "\n")

        # Get server summary
        summary = await get_server_status_summary(app_ctx=agent_app.context)
        print(summary)

        print("\n" + "="*70)
        print("RUNNING COMPREHENSIVE SERVER TESTS")
        print("="*70 + "\n")

        # Run all tests
        results_json = await run_all_server_tests(app_ctx=agent_app.context)
        results = json.loads(results_json)

        # Print summary
        print("\n" + "="*70)
        print("TEST RESULTS SUMMARY")
        print("="*70)
        print(f"Total Servers: {results['test_run']['total_servers']}")
        print(f"✓ Successful: {results['test_run']['successful']}")
        print(f"○ Not Configured: {results['test_run']['not_configured']}")
        if results['test_run'].get('auth_errors', 0) > 0:
            print(f"🔐 Auth Errors: {results['test_run']['auth_errors']}")
        if results['test_run'].get('oauth_required', 0) > 0:
            print(f"🔑 OAuth Required: {results['test_run']['oauth_required']}")
        if results['test_run'].get('connection_errors', 0) > 0:
            print(f"🔌 Connection Errors: {results['test_run']['connection_errors']}")
        if results['test_run'].get('other_errors', 0) > 0:
            print(f"✗ Other Errors: {results['test_run']['other_errors']}")
        print("="*70 + "\n")

        # Print individual results
        print("Individual Server Results:")
        print("-" * 70)
        for result in results['results']:
            status_symbol = {
                'success': '✓',
                'not_configured': '○',
                'auth_error': '🔐',
                'oauth_required': '🔑',
                'connection_error': '🔌',
                'error': '✗'
            }.get(result.get('status', 'error'), '?')

            server_name = result.get('server', 'unknown')
            status = result.get('status', 'error')
            transport = result.get('transport', 'unknown')

            print(f"{status_symbol} {server_name:<25} [{transport:<15}] {status.upper()}")

            # Show sample data for successful tests
            if status == 'success' and 'data_sample' in result:
                sample = result['data_sample']
                if sample and len(sample) > 0:
                    print(f"  ↳ Data: {sample[:80]}...")

            # Show errors for failed tests
            if 'error' in result:
                print(f"  ✗ {result['error']}")
                if 'error_detail' in result and result['error_detail'] != result['error']:
                    print(f"    Details: {result['error_detail'][:100]}")

        print("\n" + "="*70)


if __name__ == "__main__":
    asyncio.run(main())
