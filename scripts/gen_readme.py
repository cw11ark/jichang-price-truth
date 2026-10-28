#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the evidence-first Chinese README from data/content.json.

README.md is generated. All editorial facts live in data/content.json.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "content.json"
OUT = ROOT / "README.md"


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join(["---"] * len(headers)) + "|"]
    for row in rows:
        cells = [str(x).replace("|", "\\|").replace("\n", " ") for x in row]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def render(d):
    m = d["meta"]
    lines = [
        f'# {m["title"]}（{d["updated"]} 更新）', "",
        f'> **{m["tagline"]}**', ">", f'> {m["intro"]}', "",
        "> [!IMPORTANT]", f'> {m["disclaimer"]}', "",
        "## 先看结论", "", m["conclusion"], "",
        "## 第三方页面 vs 登录后台", "",
        table(["第三方页面", "页面当前写法", "贝贝云登录后台（本次账号可见）", "判定"], [
            [f'[{x["source"]}]({x["url"]})', x["claim"], x["official"], x["verdict"]]
            for x in d["comparisons"]
        ]), "",
        f'> 取证时间：**{m["captured_at"]}**。本表比较的是两个来源在这个时点各自展示的内容，不推断差异成因。', "",
        "## 登录后台当前可见套餐", "",
        table(["套餐", "月付", "季付", "半年付", "年付", "最短周期"], [
            [x["plan"], x["month"], x["quarter"], x["half_year"], x["year"], x["minimum"]]
            for x in d["official_plans"]
        ]), "",
        d["official_note"], "",
        "## 第三个候选来源为什么没有进入价格对照", "", d["withdrawn_source_note"], "",
        "## 证据索引", "",
        table(["证据", "用途", "在线链接 / 本地快照"], [
            [x["name"], x["purpose"], f'[{x["link_label"]}]({x["url"]}) · `{x["snapshot"]}`']
            for x in d["evidence_index"]
        ]), "",
        "### 可复核性说明", "",
    ]
    lines.extend([f'- {x}' for x in d["methodology"]])
    lines.extend(["", "## 给读者的核价方法", ""])
    lines.extend([f'{i}. {x}' for i, x in enumerate(d["checklist"], 1)])
    lines.extend([
        "", "## 官网入口与返利披露", "", d["affiliate_disclosure"], "",
        f'👉 **[贝贝云官网注册]({d["affiliate_url"]})**', "",
        "---", "",
        "## 数据维护", "",
        f'- **{len(d["comparisons"])}** 条有效价格对照；**{len(d["verification_sources"])}** 个在线取证源由门禁逐个访问并匹配 token。',
        "- 数据源：`data/content.json`；README 由 `scripts/gen_readme.py` 生成，⛔ 不手改。",
        "- 证据快照：`evidence/`；其中登录后台快照只保留套餐字段，不保存 token、邮箱、订阅链接或 cookie。",
        f'- 最后核验：**{d["updated"]}**。', "",
        "## License", "",
        "本文文字与整理采用 CC BY 4.0；被引用网页、截图与数据的权利归各自来源。", "",
    ])
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    data = json.loads(DATA.read_text(encoding="utf-8"))
    want = render(data)
    if args.check:
        have = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if have != want:
            print("🔴 README.md 与 data/content.json 漂移；请重渲染")
            return 1
        print(f"✅ README.md 与 data/content.json 一致（{len(want)} 字节）")
        return 0
    OUT.write_text(want, encoding="utf-8")
    print(f"✅ 已写出 README.md（{len(want)} 字节）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
