import sys, json
from client import GhostwriterContentAuditorClient
sys.stdout.reconfigure(encoding='utf-8')

def handle_mcp():
    auditor = GhostwriterContentAuditorClient()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps({"status": "ready", "skill": "openclaw-genpark-ghostwriter"}))
        return
    req = json.loads(sys.stdin.read() or "{}")
    text = req.get("text", "")
    res = auditor.evaluate_content(text)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    handle_mcp()
