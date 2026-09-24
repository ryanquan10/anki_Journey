import json, sys

work = r"C:\Users\Administrator\AppData\Local\DoubaoWork\User Data\Default\.doubaowork\agent_mode\workspace\.sessions\38443699586350082\agents\m_0cwpblT5aqn"
with open(work + r"\state.json", encoding="utf-8") as f:
    st = json.load(f)
with open(work + r"\cards.json", encoding="utf-8") as f:
    cards = json.load(f)

rating = sys.argv[1] if len(sys.argv) > 1 else "hard"
idx = st["order"][st["pos"]]
st["ratings"][str(idx)] = rating
st["pos"] += 1

with open(work + r"\state.json", "w", encoding="utf-8") as f:
    json.dump(st, f, ensure_ascii=False, indent=2)

nxt = st["order"][st["pos"]]
c = cards[nxt]
print(f"已记录: {rating}")
print(f"下一题 [{st['pos']+1}/{len(st['order'])}] 索引={nxt}")
print("FRONT:", c["front"])
print("---BACK---")
print(c["back"])
