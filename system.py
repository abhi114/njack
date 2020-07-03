import shutil

def check(disk,min_gb,min_percent):
    #return true if enough disk space else false
    du = shutil.disk_usage(disk)

    percent_free = 100*du.free / du.total
    gigabytes_free = du.free / 2**30
    if gigabytes_free <min_gb or percent_free <min_percent:
        return False
    return True

if not check(disk="/",min_gb=2,min_percent=10):
    print("ERROR")
    return 1

print("GOOD")
print("VERY good")
return 0
print("prevent a three way merge")
