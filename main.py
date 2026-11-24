import os

LINE = "Every server is down. I cannot reach any of them, so I do not know what failed or when it will be back. I am still trying to connect."

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
