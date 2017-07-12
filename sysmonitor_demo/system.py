#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import  psutil
#CPU信息
cpu_time = psutil.cpu_times(percpu=True)
cpu_count = psutil.cpu_count()
#MEM信息
mem = psutil.virtual_memory()
mem_total = mem.total
mem_free = mem.free
#print(mem_total,mem_free,"%.2f%%" % (mem_free / mem_total * 100 ) )
#IO信息



print(mem_free)