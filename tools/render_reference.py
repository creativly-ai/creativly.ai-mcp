"""Render public tool docs from the committed schema snapshot; no service imports."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def safe(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def kind(schema):
    value = schema.get("type", "value")
    if value == "array":
        value = kind(schema.get("items", {})) + "[]"
    return value


def rows(schema, prefix=""):
    result = []
    required = schema.get("required", [])
    for name, item in schema.get("properties", {}).items():
        path = prefix + name
        required_text = "Required" if name in required else "Optional"
        details = []
        if "default" in item:
            details.append("Default: `" + json.dumps(item["default"]) + "`")
        if "enum" in item:
            details.append("Values: " + ", ".join("`" + json.dumps(v) + "`" for v in item["enum"]))
        for key, label in [("minimum", "Minimum"), ("maximum", "Maximum"), ("minLength", "Min characters"), ("maxLength", "Max characters"), ("minItems", "Min items"), ("maxItems", "Max items"), ("format", "Format"), ("pattern", "Pattern")]:
            if key in item:
                details.append(f"{label}: `{item[key]}`")
        if item.get("description"):
            details.append(item["description"])
        result.append(f"| `{path}` | {safe(kind(item))} | {required_text} | {safe('; '.join(details))} |")
        child = item.get("items", {}) if item.get("type") == "array" else item
        if child.get("properties"):
            result.extend(rows(child, path + ("[]." if item.get("type") == "array" else ".")))
    return result


def render():
    data = json.loads((ROOT / "schemas/tools.json").read_text())
    lines = ["# MCP tool reference", "", f"{len(data['tools'])} tools · Streamable HTTP · OAuth", "", "[Connection guide](setup.md) · [Workflows](workflows.md) · [Full JSON schemas](../schemas/tools.json)", "", "This is a snapshot of the exposed public tool contract. The connected server’s `tools/list` response is authoritative. Required/default columns reproduce that schema: the server applies declared defaults, while strict clients may still supply those fields explicitly. Model parameter values and account access are discovered through `get_model` and quotes.", "", "For `quote_generation`, edit operations impose additional runtime limits: one source, one output, no extra image references for image edits, and at most one first-frame guide for supported video edits.", "", "## Index", ""]
    lines += [f"- [`{tool['name']}`](#{tool['name']})" for tool in data["tools"]]
    for tool in data["tools"]:
        lines += ["", "## " + tool["name"], "", tool["description"], ""]
        fields = rows(tool["inputSchema"])
        lines += ["| Parameter | Type | Required | Details |", "| --- | --- | --- | --- |", *fields] if fields else ["Parameters: none."]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    (ROOT / "docs/tools.md").write_text(render())
