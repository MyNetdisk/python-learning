import json
import re
import requests
from bs4 import BeautifulSoup


def fetch_html(url, timeout=15):
    """获取页面 HTML"""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    resp = requests.get(url, headers=headers, timeout=timeout)
    resp.raise_for_status()
    resp.encoding = resp.apparent_encoding
    return resp.text


def table_to_list(table):
    """把一个 HTML <table> 转成 list[dict]"""
    rows = table.find_all("tr")
    if not rows:
        return []
    first_row_cells = rows[0].find_all(["th", "td"])
    if rows[0].find_all("th"):
        headers = [c.get_text(strip=True) for c in first_row_cells]
        data_rows = rows[1:]
    else:
        headers = [f"列{i}" for i in range(len(first_row_cells))]
        data_rows = rows
    result = []
    for row in data_rows:
        cells = row.find_all(["td", "th"])
        if not cells:
            continue
        values = [c.get_text(strip=True) for c in cells]
        result.append({h: (values[i] if i < len(values) else "")
                       for i, h in enumerate(headers)})
    return result


def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"已保存：{filename}")


# ===================== 题目 1 =====================
# 抓取以下网站并将数据存储为json文件（bu.edu facts & stats）
def task1():
    url = "http://www.bu.edu/president/boston-university-facts-stats/"
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    all_tables = []
    for i, table in enumerate(soup.find_all("table")):
        rows = table_to_list(table)
        if rows:
            all_tables.append({"table_index": i, "rows": rows})
    if not all_tables:
        print("提示：题目1页面已无 <table>，未抓到表格数据")
    save_json(all_tables, "bu_facts_stats.json")


# ===================== 题目 2 =====================
# 提取此url中的表格并转为json。
# 注意：UCI 已改版，旧地址 /ml/datasets.php 返回 404，新站 https://archive.ics.uci.edu/datasets
# 且新版首页不再有 <table>，数据是卡片式布局，这里改为解析卡片。
def task2():
    url = "https://archive.ics.uci.edu/datasets"
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")

    # 新站没有表格时，降级为解析数据集卡片
    datasets = []
    for row in soup.find_all("div", role="row"):
        link = row.find("a", href=re.compile(r"^/dataset/"))
        if not link:
            continue
        h2 = row.find("h2")
        name = h2.get_text(strip=True) if h2 else ""
        if not name:
            img = row.find("img")
            name = img.get("alt", "") if img else ""
        desc = row.find("p")
        txt = row.get_text(" ", strip=True)
        inst = re.search(r"([\d.,KkMm]+)\s*Instances", txt)
        feat = re.search(r"([\d.,KkMm]+)\s*Features", txt)
        datasets.append({
            "name": name,
            "link": "https://archive.ics.uci.edu" + link.get("href", ""),
            "instances": inst.group(1) if inst else "",
            "features": feat.group(1) if feat else "",
            "description": desc.get_text(strip=True) if desc else "",
        })

    if not datasets:
        print("提示：题目2未解析到数据集卡片，页面可能再次改版")
    save_json(datasets, "uci_datasets.json")


# ===================== 题目 3 =====================
# 抓取美国总统表并存储为json（表格结构不规整）
def task3():
    url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", class_="wikitable")
    if not table:
        tables = soup.find_all("table")
        if not tables:
            raise RuntimeError("未找到表格")
        table = tables[0]
    presidents = table_to_list(table)
    save_json(presidents, "us_presidents.json")


if __name__ == "__main__":
    tasks = [("题目1 BU facts & stats", task1),
             ("题目2 UCI datasets", task2),
             ("题目3 US Presidents", task3)]
    done, failed = [], []
    for name, fn in tasks:
        print(f"开始 {name}")
        try:
            fn()
            done.append(name)
        except Exception as e:
            failed.append((name, repr(e)))
            print(f"  [失败] {name}: {e}")
    print("\n=== 运行汇总 ===")
    print(f"成功：{len(done)} 个 -> {done}")
    print(f"失败：{len(failed)} 个 -> {[f[0] for f in failed]}")
