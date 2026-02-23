import numpy as np

with open("/Users/kushalpatil/Desktop/studious-waffle/md/ss2.dat") as f:
    for line in f:
        line = line.strip()

        # Skip comments or blank lines
        if not line or line.startswith("#") or line.startswith("@"):
            continue

        parts = line.split()
        vals=[]
        # Case 1: Format = time + one long string
        if len(parts) == 2:
            time = float(parts[0])
            ss = parts[1]

        # Case 2: Format = time + 42 separate characters
        elif len(parts) == 43:
            time = float(parts[0])
            ss = "".join(parts[1:])

        # Case 3: Format = ONLY the SS string (no time)
        elif len(parts) == 1 and all(c.isalpha() or c == "~" for c in parts[0]):
            time = None
            ss = parts[0]

        else:
            # If the line is weird, skip it
            continue

        # Count beta-sheet residues
        beta = ss.count("E") + ss.count("B")
        pct = beta / 42 * 100

        if time is not None:
            print(f"{time:.2f} ns: {pct:.2f}% β-sheet")
        else:
            print(f"{pct:.2f}% β-sheet")
            vals.append(pct)
    print("Mean β-sheet %:", np.mean(vals))

