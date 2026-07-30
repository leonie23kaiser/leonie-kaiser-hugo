import re, sys
from pathlib import Path
src = Path(sys.argv[1]).read_text(encoding="utf-8")
src = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", src)
src = src.replace("- [ ] ", "- ☐ ")
tmp, cur = [], None
def flushq():
    global cur
    if cur is not None: tmp.append("> " + cur); cur = None
for line in src.splitlines():
    ls = line.lstrip()
    if ls.startswith(">"):
        content = re.sub(r"^\s*>\s?", "", line)
        if cur is None or content.lstrip().startswith("„"):
            flushq(); cur = content
        else:
            cur += " " + content.strip()
    else:
        flushq(); tmp.append(line)
flushq()
out, cur = [], None
def flush():
    global cur
    if cur is not None: out.append(cur); cur = None
for raw in tmp:
    s = raw.rstrip(); st = s.strip()
    if st == "":
        flush(); out.append(""); continue
    if st.startswith("#") or re.match(r"^---+$", st) or st.startswith("|") or st.startswith(">"):
        flush(); out.append(s); continue
    if re.match(r"^[-*]\s+", st) or re.match(r"^\d+\.\s+", st):
        flush(); cur = st; continue
    cur = st if cur is None else cur + " " + st
flush()
Path(sys.argv[2]).write_text("\n".join(out), encoding="utf-8")
