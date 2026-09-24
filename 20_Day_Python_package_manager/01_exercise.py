# 阅读关于虚拟环境的更多信息，尝试创建虚拟环境并安装至少一个包
# # 进入你的空项目目录
# cd /path/to/your/empty/project
# # 创建名为 .venv 的虚拟环境（加 . 前缀可让文件夹在文件管理器中隐藏）
# python -m venv .venv
# # 激活虚拟环境（当前目录pawershell终端下执行）
# .venv\Scripts\Activate.ps1

import json, os, requests
import sys

# requests 这个包实际被加载的 .py 文件路径
print("requests 来源:", requests.__file__)

# 当前 Python 解释器可执行文件路径
print("解释器路径:", sys.executable)

# 关键判断：在虚拟环境中 sys.prefix 与 base_prefix 不相等
print("在虚拟环境内运行:", sys.prefix != sys.base_prefix)
print("虚拟环境根目录:", sys.prefix)

API_KEY = 'rc_live_3f64d21828f84b988147fa2ac4a2511b'  # 注册后获得
BASE = "https://api.restcountries.com/countries/v5"
CACHE_FILE = "countries.json"


def fetch_all_countries():
    if os.path.exists(CACHE_FILE):
        print("读取本地缓存", CACHE_FILE)
        return json.load(open(CACHE_FILE, encoding="utf-8"))
    headers = {"Authorization": f"Bearer {API_KEY}"}
    out, offset, limit = [], 0, 100
    while True:
        r = requests.get(BASE, headers=headers,
                         params={"limit": limit, "offset": offset}, timeout=10)
        data = r.json()
        if "errors" in data:
            print("请求失败:", data["errors"])
            break
        obj = data["data"]
        out.extend(obj["objects"])
        meta = obj["meta"]
        print(f"已拉取 {len(out)} / {meta[chr(39) + chr(39)]}" if False else f"已拉取 {len(out)} / {meta['total']}")
        if not meta["more"]: break
        offset += limit
    json.dump(out, open(CACHE_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"共 {len(out)} 国, 已缓存 {CACHE_FILE}")
    return out


get_name = lambda c: c["names"]["common"]
get_pop = lambda c: c.get("population") or 0
get_area = lambda c: (c.get("area") or {}).get("kilometers") or 0
get_cap = lambda c: (c.get("capitals") or [{}])[0].get("name", "")
get_codes = lambda c: [l.get("iso639_3") or l.get("iso639_2t") for l in (c.get("languages") or [])]


# 使用一个国家API，获取所有国家信息，并找出前十个人口最多的国家
def task1(cs):
    print("\n===== 题1 人口Top10 =====")
    for i, c in enumerate(sorted(cs, key=get_pop, reverse=True)[:10], 1):
        print(f"  {i:>2}. {get_name(c):<22} {get_pop(c):>13,}")


# 从国家API数据中找出官方语言是英语(eng)的所有国家
def task2(cs):
    res = [get_name(c) for c in cs if "eng" in get_codes(c)]
    print("\n===== 题2 官方语言含 English(eng) 共%d国 =====" % len(res))
    print("  " + ", ".join(res))


# 从国家API数据中获取数据，根据国家的面积找出前十个最大的国家
def task3(cs):
    print("\n===== 题3 面积Top10 =====")
    for i, c in enumerate(sorted(cs, key=get_area, reverse=True)[:10], 1):
        print(f"  {i:>2}. {get_name(c):<22} {get_area(c):>13,.0f} km2")


# 从国家API数据中找出所有从新列出的国家，按他们的首都排序
def task4(cs):
    print("\n===== 题4 按首都排序 =====")
    for c in sorted(cs, key=get_cap):
        print(f"  {get_cap(c):<24} <- {get_name(c)}")


if __name__ == "__main__":
    cs = fetch_all_countries()
    print("\n参与统计:", len(cs))
    task1(cs)
    task2(cs)
    task3(cs)
    task4(cs)
