
def average(points: list):
    x, y = 0, 0
    for i in range(0, len(points)):
        x += points[i][0]
        y += points[i][1]
    #sum_x = sum(points[i][0] for i in range(0, len(points)))
    #sum_y = sum(points[j][1] for j in range(0, len(points)))
    return ([(x / len(points)), (y / len(points))])


#def linear_regression(points: list):
#    averages = average(points)
#    avg_x = averages[0]
#    avg_y = averages[1]
#    b = (sum([(points[i][0] - avg_x) * (points[i][1] - avg_y) for i in range(len(points))])) / (
#        sum([(points[i][0] - avg_x) ** 2 for i in range(len(points))]))
#    a = avg_y - (b * avg_x)
#   return (a, b)


def calculate_r_squared(points: list) -> float:
    averages = average(points)
    avg_x = averages[0]
    avg_y = averages[1]
    b = (sum([(points[i][0] - avg_x) * (points[i][1] - avg_y) for i in range(len(points))])) / (
        sum([(points[i][0] - avg_x) ** 2 for i in range(len(points))]))
    a = avg_y - (b * avg_x)
    avg_y = averages[1]
    c = sum(((points[i][1]) - (avg_y)) ** 2 for i in range(len(points)))
    d = sum(((points[i][1]) - (a + (b * ((points[i][0]))))) ** 2 for i in range(len(points)))
    r_sq = 1 - ((d) / (c))
    return r_sq

