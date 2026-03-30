from flask import Flask, render_template, request
from agent import run_travel_agent

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    error = None

    if request.method == "POST":

        goal = request.form.get("goal")

        if not goal or goal.strip() == "":
            error = "Please enter a travel request."

        else:
            try:
                result = run_travel_agent(goal)
            except Exception as e:
                error = f"Agent error: {str(e)}"

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)