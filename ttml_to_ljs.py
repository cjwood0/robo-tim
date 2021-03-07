import re
import json

def time_to_millis(t):
    h, m, s, ms = t
    millis = int(h) * 3600 * 1000 + int(m) * 60 * 1000 + int(s) * 1000 + int(ms)
    return millis

file1 = open('Building a Custom Nerves System Image for the Pi Zero-IeuQW3DRVQ0.en.vtt', 'r')
times_match = re.compile(r"(?<!\<)(\d{2}):(\d{2}):(\d{2})\.(\d{2,3})")
lines = (
    line.rstrip('\n')
    for line in file1
    if line != '\n'
)

ljs = []

for line in file1:    
    m = re.findall(times_match, line)
    if not len(m): continue
    start = time_to_millis(m[0])
    stop = time_to_millis(m[1])
    if stop - start < 500: continue
    text = next(file1).strip()
    if not text: continue
    lj_obj = {
        "Start": start,
        "Stop": stop,
        "Text": text
    }
    ljs.append(lj_obj)
file1.close()

output = open("output.json", "w")
output.write(json.dumps(ljs))
output.close()