# there's probably a faster way to both of these
def update_data(obj, points):
	obj.daily_points += points
	obj.weekly_points += points

	d = obj.data_points.split(",")
	d.append(str(int(d.pop()) + points))

	obj.data_points = ",".join(d)

	obj.save()

def shift_data(obj, diff):
	d = obj.data_points.split(",")
	for i in range(diff):
		d.append("0")

	obj.data_points = ",".join(d[diff:])
	obj.save()
