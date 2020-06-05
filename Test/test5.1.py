def demo(*para):
    avg = sum(para)/len(para)
    g = [i for i in para if i >avg]
    return (avg,) + tuple(g)
print(demo(1,2,3,4,5))