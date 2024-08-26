n = int(input())

playlist = {}
tracks = []
for i in range(n):
    k = int(input())
    tracks.append(input().split())
    for j in tracks[i]:
        playlist[j] = 0

for i in tracks:
    for j in i:
        playlist[j] += 1

playlist = dict(sorted(playlist.items(), key=lambda x: x[1], reverse=True))
res = []
count = 0
for track, value in playlist.items():
    if value == n:
        count += 1
        res.append(track)

print(count)
print(*sorted(res))
