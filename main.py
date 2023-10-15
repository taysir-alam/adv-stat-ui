from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Sample data for teams and metrics (replace with your data)
teams = ["Overall","25 in 2", "Raud 50", "30 in 2:30"]
metrics = ["ARES", "AY", "BA", "CASH", "DG", "ELI", "JEREM", "KAZ", "MATT", "MIKE", "MOODY", "NATHAN", "PARKER", "RIAZ", "SEB", "STEVO", "THOMAS", "TYLER", "TYRELLE"]

# Sample data for metrics per team (replace with your data)
team_metrics = {
    "Overall": [55.01, 59.80, 50.62, 63.67, 55.23, 51.16, 55.56, 63.40, 47.46, 44.31, 56.88, 54.17, 60.65, 45.52, 54.94, 53.45, 50.02, 23.81, 54.61],
    "25 in 2": [50.25, 64.24, 48.71, 67.12, 53.71, 45.50, 55.77, 69.38, 48.37, 66.92, 54.96, 51.45, 56.23, 36.98, 52.63, 47.92, 44.06, 71.43, 51.99],
    "Raud 50": ["61/100", "63/100", "29/50", "69/100", "51/100", "54/100", "63/100", "62/100", "22/50", "33/50", "64/100", "50/100", "64/100", "54/100", "55/100", "32/50", "28/50", "0/0", "32/50"],
    "30 in 2:30": [53.79, 52.17, 45.16, 54.88, 60.98, 53.99, 47.90, 58.81, 50.00, 0, 51.67, 61.07, 61.73, 45.59, 57.18, 48.43, 50.00, 47.83],
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected_team = request.form.get("team")

    if selected_team:
        metrics_data = team_metrics.get(selected_team, [])
        metrics_and_values = zip(metrics, metrics_data)
    else:
        metrics_and_values = []

    return render_template("index.html", teams=teams, selected_team=selected_team, metrics_and_values=metrics_and_values)

if __name__ == "__main__":
    app.run(debug=True)
