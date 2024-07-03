N = int(input())
candidates = list(map(int, input().split()))
main_viewer_ok, sub_viewer_ok = list(map(int, input().split()))

viewer_number = 0
for candidate in candidates:
    candidate -= main_viewer_ok
    viewer_number += 1

    if candidate <= 0:
        continue

    quitoent = candidate // sub_viewer_ok
    remainder = candidate % sub_viewer_ok
    if remainder > 0:
        viewer_number = viewer_number + quitoent + 1
    else:
        viewer_number += quitoent


print(viewer_number)