from typing import Dict, Any


class Tool:
    def __init__(self, name: str, description: str, parameters: Dict[str, Any]):
        self.name = name
        self.description = description
        self.parameters = parameters

    def execute(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Должен быть переопределён в потомке"""
        raise NotImplementedError("Execute method not implemented")


class SayHelloTool(Tool):
    def __init__(self):
        super().__init__(
            name="Say Hello",
            description="Simple tool for greeting by name",
            parameters={
                "name": {"description": "Name to be used in greeting", "required": True}
            },
        )

    def execute(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        name = arguments.get("name", "Guest")
        return {
            "content": [
                {"type": "text", "text": f"Hello, {name}! Welcome to MCP Debugger."}
            ],
            "isError": False,
        }
