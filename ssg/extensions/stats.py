from ssg import hooks
import time

start_time = None
total_written = 0

@hooks.register("start_build")
def start_build():
    global start_time
    start_time = time.clock_gettime

@hooks.register("written")
def written():
    global total_written
    total_written = total_written + 1

@hooks.event("stats")
def stats():
    final_time = time.clock_gettime - start_time
    average = 0 if total_written ==0 else final_time / total_written
    report = "Converted: {} . Time: {:.2f} sec . Avg: {:.4f} sec/file"
    print(report.format(total_written, final_time, average))