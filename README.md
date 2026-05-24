# 카드뉴스 with Claude + Figma

Claude Code와 Figma MCP를 연결하여 카드뉴스를 제작하는 프로젝트입니다.

## 환경 설정

### 1. Node.js 설치
```bash
# ~/local 에 Node.js 설치 (ARM64)
curl -L -o /tmp/node.tar.gz "https://nodejs.org/dist/v20.18.3/node-v20.18.3-darwin-arm64.tar.gz"
mkdir -p ~/local && tar -xzf /tmp/node.tar.gz -C ~/local --strip-components=1
export PATH="$HOME/local/bin:$PATH"
```

### 2. Figma MCP 서버 설정
`~/.claude/settings.json` 파일 생성:
```json
{
  "mcpServers": {
    "figma": {
      "command": "/Users/ykr/local/bin/npx",
      "args": ["figma-developer-mcp"],
      "env": {
        "FIGMA_API_KEY": "YOUR_FIGMA_API_KEY"
      }
    }
  }
}
```

### 3. Figma API 키 발급
Figma 앱 → 홈 → 계정 설정 → 보안 → Personal access tokens → Generate new token

## 사용법

Claude Code 재시작 후 Figma 파일 URL을 공유하면 디자인을 직접 읽고 작업합니다.
