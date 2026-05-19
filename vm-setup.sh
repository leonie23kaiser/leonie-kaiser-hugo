#!/bin/bash
# Setup-Skript für leonie-kaiser.exe.xyz VM
# Paste ins Terminal der VM nach erstem Login

set -e

echo "▶ 1/6 Hugo Extended 0.123.7 installieren..."
HUGO_VERSION=0.123.7
cd /tmp
curl -sSL "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz" -o hugo.tar.gz
sudo tar -xzf hugo.tar.gz -C /usr/local/bin hugo
rm hugo.tar.gz
hugo version

echo "▶ 2/6 Node 20 + git + tmux..."
if ! command -v node >/dev/null; then
  curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
fi
sudo apt-get install -y nodejs git tmux >/dev/null

echo "▶ 3/6 Claude Code CLI..."
sudo npm install -g @anthropic-ai/claude-code 2>&1 | tail -3
claude --version || true

echo "▶ 4/6 Repo holen (oder Integration-Mount prüfen)..."
cd ~
if [ -d ~/leonie-kaiser-hugo ]; then
  echo "Repo schon da (Integration-Mount), pulle aktuellen Stand"
  cd ~/leonie-kaiser-hugo && git pull
else
  git clone https://github.com/leonie23kaiser/leonie-kaiser-hugo.git
  cd ~/leonie-kaiser-hugo
fi
echo "Repo-Pfad: $(pwd)"

echo "▶ 5/6 Hugo-Site testweise bauen..."
cd ~/leonie-kaiser-hugo/src/growthtogether.at
hugo --quiet && echo "Build OK"

echo "▶ 6/6 tmux-Session 'hugo' mit Dev-Server auf Port 8000..."
tmux kill-session -t hugo 2>/dev/null || true
tmux new-session -d -s hugo -c ~/leonie-kaiser-hugo/src/growthtogether.at \
  "hugo server -p 8000 --bind 0.0.0.0 --baseURL https://leonie-kaiser.exe.xyz/ --appendPort=false --disableFastRender"
sleep 3
curl -s -o /dev/null -w "Hugo Dev-Server: %{http_code}\n" http://localhost:8000/

cat <<'NOTE'

═══════════════════════════════════════════════════════════════
FERTIG ✓

Vorschau:    https://leonie-kaiser.exe.xyz/
Repo:        ~/leonie-kaiser-hugo
Hugo-Source: ~/leonie-kaiser-hugo/src/growthtogether.at

Claude Code starten:
  cd ~/leonie-kaiser-hugo && claude

Hugo-Server-Logs ansehen:
  tmux attach -t hugo
  (raus: Strg+B, dann D)

Hugo neu starten:
  tmux kill-session -t hugo
  tmux new-session -d -s hugo -c ~/leonie-kaiser-hugo/src/growthtogether.at \
    "hugo server -p 8000 --bind 0.0.0.0 --baseURL https://leonie-kaiser.exe.xyz/ --appendPort=false"
═══════════════════════════════════════════════════════════════
NOTE
