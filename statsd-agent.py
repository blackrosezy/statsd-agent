import statsd
import time
import psutil
import multiprocessing

def disk():
    c = statsd.StatsClient('localhost', 8125, prefix='system.disk')
    while True:
        disk_usage = psutil.disk_usage('/')
        c.gauge('root.total', disk_usage.total)
        c.gauge('root.used', disk_usage.used)
        c.gauge('root.free', disk_usage.free)
        c.gauge('root.percent', disk_usage.percent)
            
        time.sleep(10)

def cpu_times():
    c = statsd.StatsClient('localhost', 8125, prefix='system.cpu')
    while True:
        cpu_times = psutil.cpu_times()
        c.gauge('system_wide.times.user', cpu_times.user)
        c.gauge('system_wide.times.nice', cpu_times.nice)
        c.gauge('system_wide.times.system', cpu_times.system)
        c.gauge('system_wide.times.idle', cpu_times.idle)
        c.gauge('system_wide.times.iowait', cpu_times.iowait)
        c.gauge('system_wide.times.irq', cpu_times.irq)
        c.gauge('system_wide.times.softirq', cpu_times.softirq)
        c.gauge('system_wide.times.steal', cpu_times.steal)
        c.gauge('system_wide.times.guest', cpu_times.guest)
        c.gauge('system_wide.times.guest_nice', cpu_times.guest_nice)
        
        time.sleep(10)

def cpu_times_percent():
    c = statsd.StatsClient('localhost', 8125, prefix='system.cpu')
    while True:
        value = psutil.cpu_percent(interval=1)
        c.gauge('system_wide.percent', value)

        cpu_times_percent = psutil.cpu_times_percent(interval=1)
        c.gauge('system_wide.times_percent.user', cpu_times_percent.user)
        c.gauge('system_wide.times_percent.nice', cpu_times_percent.nice)
        c.gauge('system_wide.times_percent.system', cpu_times_percent.system)
        c.gauge('system_wide.times_percent.idle', cpu_times_percent.idle)
        c.gauge('system_wide.times_percent.iowait', cpu_times_percent.iowait)
        c.gauge('system_wide.times_percent.irq', cpu_times_percent.irq)
        c.gauge('system_wide.times_percent.softirq', cpu_times_percent.softirq)
        c.gauge('system_wide.times_percent.steal', cpu_times_percent.steal)
        c.gauge('system_wide.times_percent.guest', cpu_times_percent.guest)
        c.gauge('system_wide.times_percent.guest_nice', cpu_times_percent.guest_nice)
        time.sleep(10)

def memory():
    c = statsd.StatsClient('localhost', 8125, prefix='system.memory')
    while True:
        swap = psutil.swap_memory()
        c.gauge('swap.total', swap.total)
        c.gauge('swap.used', swap.used)
        c.gauge('swap.free', swap.free)
        c.gauge('swap.percent', swap.percent)

        virtual = psutil.virtual_memory()
        c.gauge('virtual.total', virtual.total)
        c.gauge('virtual.available', virtual.available)
        c.gauge('virtual.used', virtual.used)
        c.gauge('virtual.free', virtual.free)
        c.gauge('virtual.percent', virtual.percent)
        c.gauge('virtual.active', virtual.active)
        c.gauge('virtual.inactive', virtual.inactive)
        c.gauge('virtual.buffers', virtual.buffers)
        c.gauge('virtual.cached', virtual.cached)
        
        time.sleep(10)
        
if __name__ == '__main__':
    multiprocessing.Process(target=disk).start()
    multiprocessing.Process(target=cpu_times).start()
    multiprocessing.Process(target=cpu_times_percent).start()
    multiprocessing.Process(target=memory).start()


