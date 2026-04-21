#13
def chuan_hoa(s):
    return "\n".join(" ".join(l.strip().split()).replace(" ,", ",").replace(" .", ".") for l in s.split("\n"))