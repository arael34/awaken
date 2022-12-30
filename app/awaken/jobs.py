from .models import Points
from .util.datahelper import shift_data
import datetime

def reset_points(user):
	obj = Points.objects.get_or_create(user_id = user)[0]
	current_date = datetime.date.today()
	diff = (current_date - obj.last_reset).days

	shift_data(obj, diff)

	# readability over speed . to make this faster,
	# each conditional would need to be nested
	if diff >= 1:
		obj.daily_points = 0
		obj.last_reset = current_date
	if diff >= 7:
		obj.weekly_points = 0
	if diff >= 14:
		obj.data_points = ""
	
	obj.save()
