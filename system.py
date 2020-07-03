import shutil

def check(disk,min_gb,min_percent):
    #return true if enough disk space else false
    du = shutil.disk_usage(disk)

    percent_free = 100*du.free / du.total
    gigabytes_free = du.free / 2**30
    if gigabytes_free <min_gb or percent_free <min_percent:
        return False
    return True

def main():
    print("this one is cool")

def check_root_full():
    return check_disk_full(disk='/',min_gb=2,min_percent=10)

if not check_root_full():
    print("ERROR")
    return 1

print("GOOD")
print("VERY good")
main()
return 0
print("yet another line")
