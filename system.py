import shutil

def check(disk,min_gb,min_percent):
    #return true if enough disk space else false
    du = shutil.disk_usage(disk)

    percent_free = 100*du.free / du.total
    gigabytes_free = du.free / 2**30
    if percent_free <min_percent or gigabytes_free  <min_gb:
        return False
    return True

if not check(disk="/",min_gb=2,min_percent=10):
    print("ERROR")
    return 1

print("GOOD")
return 0
