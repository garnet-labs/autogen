import asyncio
import os
import shlex

from autogen_ext.tools.mcp import StdioServerParams, mcp_server_tools


async def main() -> None:
    params = StdioServerParams(
        command=os.environ["GARNET_MCP_COMMAND"],
        args=shlex.split(os.environ["GARNET_MCP_ARGS"]),
        read_timeout_seconds=45,
    )
    tools = await mcp_server_tools(params)

    tool_names = {tool.name for tool in tools}
    if "get_current_time" not in tool_names:
        raise RuntimeError(f"Missing expected MCP tool: {sorted(tool_names)}")

    print(f"TOOLS_OK {sorted(tool_names)}")


if __name__ == "__main__":
    asyncio.run(main())
