import plotly
import plotly.graph_objects as go

from awaken.models import Points

def create_graph_div(user):

	user_data = Points.objects.get(user_id = user).data_points.split(',')

	fig_data = {
		"data": [{"type": "bar",
			"x": [i + 1 for i in range(14)],
			"y": [v for v in user_data]}],
	}

	fig = go.Figure(fig_data)
	fig.update_layout(
		autosize=False,
		width=400,
		height=200,
		margin=dict(
			l=25,
			r=25,
			b=25,
			t=25,
			pad=2,
		),
		paper_bgcolor="LightSteelBlue",
	)
	graph_div = plotly.offline.plot(fig, auto_open = False, output_type="div")

	return graph_div
