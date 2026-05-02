import datetime as dt
import hashlib
import html
import random
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Apex Gym Automation",
    page_icon="AG",
    layout="wide",
    initial_sidebar_state="expanded",
)

TODAY = dt.date.today()
# ---------------- THEME ----------------
st.markdown(
    """
<style>
:root {
    --ink: #f7faf8;
    --muted: #b8c3bd;
    --panel: rgba(10, 14, 17, 0.78);
    --panel-strong: rgba(9, 12, 15, 0.92);
    --line: rgba(255, 255, 255, 0.13);
    --teal: #35e0bd;
    --gold: #ffc247;
    --rose: #ff6b6b;
    --green: #76e083;
}
.stApp {
    background:
        linear-gradient(180deg, rgba(5, 8, 10, 0.72), rgba(5, 8, 10, 0.9)),
        url("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=1800&q=80");
    background-attachment: fixed;
    background-position: center;
    background-size: cover;
    color: var(--ink);
}
.block-container {
    padding-top: 1.4rem;
    padding-bottom: 3rem;
}

h1, h2, h3, label, .stMarkdown, .stText, .stCaption {
    color: var(--ink);
}

[data-testid="stMetric"] {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 18px 18px 14px;
    box-shadow: 0 18px 45px rgba(0, 0, 0, 0.24);
}

[data-testid="stMetricLabel"] p {
    color: var(--muted);
}

[data-testid="stMetricValue"] {
    color: var(--ink);
}

section[data-testid="stSidebar"] {
    background: rgba(4, 7, 9, 0.94);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}

section[data-testid="stSidebar"] * {
    color: var(--ink);
}

.stButton > button,
.stFormSubmitButton > button,
button[kind="primary"] {
    background: linear-gradient(135deg, var(--teal), var(--gold));
    border: 0;
    border-radius: 8px;
    color: #07100d;
    font-weight: 800;
    letter-spacing: 0;
    min-height: 42px;
    transition: transform 160ms ease, filter 160ms ease;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover,
button[kind="primary"]:hover {
    color: #07100d;
    filter: brightness(1.08);
    transform: translateY(-1px);
}

.hero {
    min-height: 290px;
    display: flex;
    align-items: end;
    justify-content: space-between;
    gap: 28px;
    padding: 34px;
    margin-bottom: 22px;
    border: 1px solid var(--line);
    border-radius: 8px;
    background:
        linear-gradient(90deg, rgba(7, 11, 13, 0.94) 0%, rgba(7, 11, 13, 0.7) 48%, rgba(7, 11, 13, 0.16) 100%),
        url("https://images.unsplash.com/photo-1593079831268-3381b0db4a77?auto=format&fit=crop&w=1600&q=80");
    background-position: center;
    background-size: cover;
    box-shadow: 0 24px 70px rgba(0, 0, 0, 0.32);
}

.hero-copy {
    max-width: 720px;
}

.eyebrow {
    color: var(--gold);
    font-size: 0.78rem;
    font-weight: 800;
    letter-spacing: 0.16em;
    margin-bottom: 12px;
    text-transform: uppercase;
}

.hero-title {
    color: var(--ink);
    font-size: clamp(2.3rem, 6vw, 5.4rem);
    font-weight: 900;
    letter-spacing: 0;
    line-height: 0.94;
    margin: 0;
}

.hero-text {
    color: #dce4df;
    font-size: 1.04rem;
    line-height: 1.7;
    margin-top: 18px;
    max-width: 680px;
}

.hero-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 22px;
}

.badge {
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid var(--line);
    border-radius: 999px;
    color: #eef6f1;
    display: inline-flex;
    font-size: 0.82rem;
    font-weight: 750;
    padding: 8px 12px;
}

.glass,
.plan-card,
.profile-card {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 8px;
    box-shadow: 0 16px 42px rgba(0, 0, 0, 0.2);
    padding: 20px;
}

.section-title {
    align-items: center;
    display: flex;
    gap: 10px;
    margin: 8px 0 14px;
}

.section-title span {
    background: var(--teal);
    border-radius: 999px;
    display: inline-flex;
    height: 10px;
    width: 10px;
}

.section-title h2,
.section-title h3 {
    margin: 0;
}

.subtle {
    color: var(--muted);
    line-height: 1.65;
}

.plan-card {
    min-height: 158px;
}

.plan-card h3 {
    font-size: 1.08rem;
    margin: 0 0 8px;
}

.plan-card p {
    color: var(--muted);
    line-height: 1.55;
    margin: 0;
}

.tag-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 14px;
}

.tag {
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 999px;
    color: #e9f1ec;
    font-size: 0.78rem;
    padding: 6px 10px;
}

.score {
    color: var(--teal);
    font-size: 2.3rem;
    font-weight: 900;
    line-height: 1;
}

.score-label {
    color: var(--muted);
    font-size: 0.88rem;
    margin-top: 4px;
}

.divider {
    border-top: 1px solid var(--line);
    margin: 18px 0;
}

.login-panel {
    background: var(--panel-strong);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 24px;
}

.small-note {
    color: var(--muted);
    font-size: 0.86rem;
    line-height: 1.55;
}

div[data-testid="stDataFrame"] {
    border: 1px solid var(--line);
    border-radius: 8px;
    overflow: hidden;
}

@media (max-width: 900px) {
    .hero {
        align-items: start;
        flex-direction: column;
        padding: 24px;
    }
}
</style>
""",
    unsafe_allow_html=True,
)


# ---------------- DATA ----------------
EXERCISE_LIBRARY = {
    "Fat Loss": [
        ("Incline treadmill intervals", "cardio", "bodyweight", "8 rounds", "45s fast / 75s walk", "High burn finisher"),
        ("Kettlebell swings", "power", "free weights", "4 sets", "18 reps", "Hip drive and conditioning"),
        ("Battle rope waves", "conditioning", "machines", "5 sets", "40 seconds", "Upper-body endurance"),
        ("Walking lunges", "legs", "bodyweight", "3 sets", "24 steps", "Long stride and tall chest"),
        ("Sled push", "conditioning", "machines", "6 runs", "20 meters", "Explosive lower body"),
    ],
    "Muscle Gain": [
        ("Barbell bench press", "chest", "free weights", "5 sets", "6-10 reps", "Controlled tempo"),
        ("Lat pulldown", "back", "machines", "4 sets", "10-12 reps", "Full stretch at top"),
        ("Romanian deadlift", "posterior chain", "free weights", "4 sets", "8-10 reps", "Hips back, neutral spine"),
        ("Dumbbell shoulder press", "shoulders", "free weights", "4 sets", "8-12 reps", "No bouncing"),
        ("Cable row", "back", "machines", "4 sets", "10-12 reps", "Squeeze shoulder blades"),
    ],
    "Strength": [
        ("Back squat", "legs", "free weights", "5 sets", "3-5 reps", "Heavy and precise"),
        ("Deadlift", "posterior chain", "free weights", "5 sets", "3 reps", "Reset every rep"),
        ("Weighted pull-up", "back", "free weights", "4 sets", "4-6 reps", "Strict range"),
        ("Overhead press", "shoulders", "free weights", "5 sets", "4-6 reps", "Brace hard"),
        ("Farmer carry", "grip", "free weights", "5 carries", "30 meters", "Strong posture"),
    ],
    "Mobility": [
        ("World's greatest stretch", "mobility", "bodyweight", "2 rounds", "6 per side", "Slow breathing"),
        ("Deep squat hold", "hips", "bodyweight", "3 sets", "45 seconds", "Relax into depth"),
        ("Band pull-aparts", "shoulders", "bodyweight", "3 sets", "20 reps", "Scapular control"),
        ("Cossack squat", "adductors", "bodyweight", "3 sets", "8 per side", "Keep heel grounded"),
        ("Thoracic rotations", "spine", "bodyweight", "2 sets", "10 per side", "Move with control"),
    ],
}

MEAL_TEMPLATES = {
    "Fat Loss": [
        "Greek yogurt bowl with berries and chia",
        "Grilled chicken salad with olive oil dressing",
        "Egg white omelette with vegetables",
        "Paneer tikka with cucumber salad",
    ],
    "Muscle Gain": [
        "Oats with banana, peanut butter, and whey",
        "Chicken rice bowl with vegetables",
        "Paneer wrap with curd dip",
        "Egg curry with rice and salad",
    ],
    "Strength": [
        "Rice, dal, curd, and roasted vegetables",
        "Lean meat or paneer with potatoes",
        "Whole eggs, toast, and fruit",
        "High-protein smoothie with oats",
    ],
    "Mobility": [
        "Colorful vegetable bowl with tofu",
        "Dal soup with brown rice",
        "Fruit, nuts, and curd bowl",
        "Paneer salad with seeds",
    ],
}

ACTIVITY_FACTORS = {
    "Desk job": 1.2,
    "Lightly active": 1.375,
    "Training 3-4 days": 1.55,
    "Training 5-6 days": 1.725,
    "Athlete": 1.9,
}

GOAL_ADJUSTMENTS = {
    "Fat Loss": -350,
    "Muscle Gain": 300,
    "Strength": 150,
    "Mobility": 0,
}


# ---------------- HELPERS ----------------
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def generate_demo_history(base_weight: float, days: int = 12) -> list[dict]:
    history = []
    for index in range(days):
        day = TODAY - dt.timedelta(days=days - index - 1)
        weight = base_weight - (index * 0.16) + random.uniform(-0.25, 0.25)
        body_fat = 24.5 - (index * 0.12) + random.uniform(-0.15, 0.15)
        history.append(
            {
                "date": day.isoformat(),
                "weight": round(weight, 1),
                "body_fat": round(body_fat, 1),
                "energy": random.randint(72, 95),
            }
        )
    return history


def make_user(username: str, password: str, name: str, goal: str, level: str, role: str = "member") -> dict:
    return {
        "password_hash": hash_password(password),
        "name": name,
        "goal": goal,
        "level": level,
        "role": role,
        "joined": TODAY.isoformat(),
        "history": [],
        "checkins": [],
        "workouts": [],
        "meals": [],
        "last_plan": [],
    }


def seed_users() -> dict:
    users = {
        "admin": make_user("admin", "admin123", "Admin Coach", "Strength", "Advanced", "admin"),
        "demo": make_user("demo", "demo123", "Demo Member", "Fat Loss", "Intermediate"),
    }

    users["demo"]["history"] = generate_demo_history(78.8)
    users["demo"]["checkins"] = [
        {"date": (TODAY - dt.timedelta(days=offset)).isoformat(), "time": "06:30"}
        for offset in [0, 1, 2, 4, 5, 6]
    ]
    users["demo"]["workouts"] = [
        {"date": (TODAY - dt.timedelta(days=2)).isoformat(), "goal": "Fat Loss", "duration": 45, "score": 88},
        {"date": (TODAY - dt.timedelta(days=1)).isoformat(), "goal": "Strength", "duration": 50, "score": 91},
    ]
    return users


def ensure_state() -> None:
    if "users" not in st.session_state:
        st.session_state.users = seed_users()
    if "current_user" not in st.session_state:
        st.session_state.current_user = None


def ensure_user_shape(user: dict) -> dict:
    user.setdefault("name", "Member")
    user.setdefault("goal", "Fat Loss")
    user.setdefault("level", "Beginner")
    user.setdefault("role", "member")
    user.setdefault("joined", TODAY.isoformat())
    user.setdefault("history", [])
    user.setdefault("checkins", [])
    user.setdefault("workouts", [])
    user.setdefault("meals", [])
    user.setdefault("last_plan", [])
    return user


def register_user(username: str, password: str, name: str, goal: str, level: str) -> tuple[bool, str]:
    username = username.strip().lower()
    if not username or not password or not name.strip():
        return False, "Please fill in name, username, and password."
    if len(password) < 5:
        return False, "Password should be at least 5 characters."
    if username in st.session_state.users:
        return False, "That username already exists."

    st.session_state.users[username] = make_user(username, password, name.strip(), goal, level)
    st.session_state.current_user = username
    return True, "Account created."


def login_user(username: str, password: str) -> tuple[bool, str]:
    username = username.strip().lower()
    user = st.session_state.users.get(username)
    if not user:
        return False, "Invalid username or password."

    saved_hash = user.get("password_hash")
    legacy_password = user.get("password")
    if saved_hash == hash_password(password) or legacy_password == password:
        st.session_state.current_user = username
        ensure_user_shape(user)
        return True, "Welcome back."

    return False, "Invalid username or password."


def current_user() -> dict:
    user = st.session_state.users[st.session_state.current_user]
    return ensure_user_shape(user)


def calculate_streak(checkins: list[dict]) -> int:
    checkin_dates = set()
    for item in checkins:
        try:
            checkin_dates.add(dt.date.fromisoformat(item["date"]))
        except (KeyError, ValueError):
            continue

    cursor = TODAY if TODAY in checkin_dates else TODAY - dt.timedelta(days=1)
    streak = 0
    while cursor in checkin_dates:
        streak += 1
        cursor -= dt.timedelta(days=1)
    return streak


def latest_value(user: dict, key: str, fallback: str = "Not set") -> str:
    history = user.get("history", [])
    if not history:
        return fallback
    return str(history[-1].get(key, fallback))


def card(title: str, body: str, tags: list[str] | None = None) -> None:
    tag_html = ""
    if tags:
        tag_html = '<div class="tag-row">' + "".join(
            f'<span class="tag">{html.escape(tag)}</span>' for tag in tags
        ) + "</div>"
    st.markdown(
        f"""
<div class="plan-card">
    <h3>{html.escape(title)}</h3>
    <p>{body}</p>
    {tag_html}
</div>
""",
        unsafe_allow_html=True,
    )


def section(title: str) -> None:
    st.markdown(
        f"""
<div class="section-title">
    <span></span>
    <h2>{html.escape(title)}</h2>
</div>
""",
        unsafe_allow_html=True,
    )


def build_workout_plan(goal: str, level: str, equipment: str, days: int, minutes: int) -> list[dict]:
    library = EXERCISE_LIBRARY[goal]
    if equipment != "Any":
        filtered = [item for item in library if item[2] == equipment.lower()]
        library = filtered or library

    exercises_per_day = 3 if minutes <= 35 else 4
    if level == "Advanced":
        exercises_per_day += 1
    if level == "Beginner":
        exercises_per_day = max(3, exercises_per_day - 1)

    plan = []
    for day in range(1, days + 1):
        choices = random.sample(library, min(exercises_per_day, len(library)))
        plan.append(
            {
                "day": f"Day {day}",
                "focus": f"{goal} session",
                "duration": minutes,
                "exercises": [
                    {
                        "name": item[0],
                        "focus": item[1],
                        "sets": item[3],
                        "reps": item[4],
                        "coach_note": item[5],
                    }
                    for item in choices
                ],
            }
        )
    return plan


def macro_plan(weight: float, height: float, age: int, sex: str, activity: str, goal: str) -> dict:
    base = 10 * weight + 6.25 * height - 5 * age
    base += 5 if sex == "Male" else -161
    calories = int(base * ACTIVITY_FACTORS[activity] + GOAL_ADJUSTMENTS[goal])
    protein = int(weight * (2.0 if goal in ["Muscle Gain", "Strength"] else 1.7))
    fats = int(weight * 0.8)
    carbs = int(max((calories - (protein * 4 + fats * 9)) / 4, 80))
    water = round(weight * 0.035, 1)
    return {
        "calories": max(calories, 1200),
        "protein": protein,
        "carbs": carbs,
        "fats": fats,
        "water": water,
    }


def render_hero(user: dict | None = None) -> None:
    name = html.escape(user["name"]) if user else "Apex Gym Automation"
    goal = html.escape(user["goal"]) if user else "Member management, training, nutrition, and progress in one control center"
    st.markdown(
        f"""
<div class="hero">
    <div class="hero-copy">
        <div class="eyebrow">Fitness club operating system</div>
        <h1 class="hero-title">{name}</h1>
        <div class="hero-text">{goal}</div>
        <div class="hero-badges">
            <span class="badge">Smart workouts</span>
            <span class="badge">Nutrition targets</span>
            <span class="badge">Progress analytics</span>
            <span class="badge">Admin overview</span>
        </div>
    </div>
</div>
""",
        unsafe_allow_html=True,
    )


def render_sidebar() -> str:
    if st.session_state.current_user:
        user = current_user()
        st.sidebar.image(f"https://i.pravatar.cc/160?u={st.session_state.current_user}", width=92)
        st.sidebar.markdown(f"**{html.escape(user['name'])}**")
        st.sidebar.caption(f"{user['goal']} | {user['level']}")
        return st.sidebar.radio(
            "Navigation",
            [
                "Command Center",
                "Smart Workout",
                "Nutrition Lab",
                "Progress Studio",
                "Attendance",
                "Admin",
                "Logout",
            ],
        )

    return st.sidebar.radio("Navigation", ["Login", "Register"])


def render_auth(menu: str) -> None:
    render_hero()
    left, right = st.columns([1.05, 0.95], gap="large")

    with left:
        st.markdown('<div class="login-panel">', unsafe_allow_html=True)
        if menu == "Login":
            st.subheader("Member login")
            st.caption("Try demo / demo123 or admin / admin123.")
            with st.form("login_form"):
                username = st.text_input("Username", placeholder="demo")
                password = st.text_input("Password", type="password", placeholder="demo123")
                submitted = st.form_submit_button("Login")
            if submitted:
                ok, message = login_user(username, password)
                if ok:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
        else:
            st.subheader("Create member account")
            with st.form("register_form"):
                name = st.text_input("Full name", placeholder="Riya Sharma")
                username = st.text_input("Username", placeholder="riya")
                password = st.text_input("Password", type="password")
                goal = st.selectbox("Primary goal", list(EXERCISE_LIBRARY.keys()))
                level = st.selectbox("Training level", ["Beginner", "Intermediate", "Advanced"])
                submitted = st.form_submit_button("Create account")
            if submitted:
                ok, message = register_user(username, password, name, goal, level)
                if ok:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        section("What is included")
        card(
            "Automation cockpit",
            "Track check-ins, member progress, generated plans, nutrition targets, and admin numbers without leaving the app.",
            ["Live session data", "Charts", "Role aware"],
        )
        st.write("")
        card(
            "Better member experience",
            "Each member gets a goal-aware dashboard, workout generator, diet calculator, and progress timeline.",
            ["Fat loss", "Muscle gain", "Strength"],
        )


def render_command_center() -> None:
    user = current_user()
    render_hero(user)

    streak = calculate_streak(user["checkins"])
    workouts = user.get("workouts", [])
    history = user.get("history", [])
    latest_weight = latest_value(user, "weight")
    latest_body_fat = latest_value(user, "body_fat")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Current streak", f"{streak} days", "attendance")
    col2.metric("Latest weight", f"{latest_weight} kg", "tracked")
    col3.metric("Body fat", f"{latest_body_fat}%", "optional")
    col4.metric("Completed workouts", len(workouts), "session log")

    st.write("")
    left, right = st.columns([1.15, 0.85], gap="large")

    with left:
        section("Performance trend")
        if history:
            df = pd.DataFrame(history)
            df["date"] = pd.to_datetime(df["date"])
            fig = px.line(
                df,
                x="date",
                y=["weight", "body_fat", "energy"],
                markers=True,
                title=None,
                color_discrete_sequence=["#35e0bd", "#ffc247", "#ff6b6b"],
            )
            fig.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                legend_title_text="Metric",
                height=390,
                margin=dict(l=20, r=20, t=20, b=20),
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Add a progress entry to unlock charts.")

    with right:
        section("Today")
        checked_in_today = any(item.get("date") == TODAY.isoformat() for item in user["checkins"])
        status = "Checked in" if checked_in_today else "Not checked in"
        readiness = min(100, 62 + streak * 4 + len(workouts) * 3)
        st.markdown(
            f"""
<div class="profile-card">
    <div class="score">{readiness}</div>
    <div class="score-label">Readiness score</div>
    <div class="divider"></div>
    <p class="subtle"><b>Status:</b> {status}</p>
    <p class="subtle"><b>Goal:</b> {html.escape(user["goal"])}</p>
    <p class="subtle"><b>Level:</b> {html.escape(user["level"])}</p>
</div>
""",
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("Quick check in", use_container_width=True):
            if checked_in_today:
                st.warning("You are already checked in for today.")
            else:
                user["checkins"].append({"date": TODAY.isoformat(), "time": dt.datetime.now().strftime("%H:%M")})
                st.success("Check-in added.")
                st.rerun()

    st.write("")
    section("Recent activity")
    activity = []
    for item in user.get("workouts", [])[-5:]:
        activity.append(
            {
                "date": item["date"],
                "type": "Workout",
                "detail": item["goal"],
                "score": item.get("score", "-"),
            }
        )
    for item in user.get("checkins", [])[-5:]:
        activity.append(
            {
                "date": item["date"],
                "type": "Check-in",
                "detail": item.get("time", "-"),
                "score": "-",
            }
        )
    if activity:
        activity_df = pd.DataFrame(activity).sort_values("date", ascending=False)
        st.dataframe(activity_df, use_container_width=True, hide_index=True)
    else:
        st.caption("No activity recorded yet.")


def render_workout() -> None:
    user = current_user()
    section("Smart Workout")
    st.markdown('<p class="subtle">Build a coach-style training plan from your goal, level, equipment, and time.</p>', unsafe_allow_html=True)

    with st.form("workout_generator"):
        c1, c2, c3, c4, c5 = st.columns(5)
        goal = c1.selectbox("Goal", list(EXERCISE_LIBRARY.keys()), index=list(EXERCISE_LIBRARY.keys()).index(user["goal"]))
        level = c2.selectbox("Level", ["Beginner", "Intermediate", "Advanced"], index=["Beginner", "Intermediate", "Advanced"].index(user["level"]))
        equipment = c3.selectbox("Equipment", ["Any", "Bodyweight", "Free weights", "Machines"])
        days = c4.slider("Days", 2, 6, 4)
        minutes = c5.slider("Minutes", 25, 75, 45, step=5)
        generate = st.form_submit_button("Generate plan")

    if generate:
        user["goal"] = goal
        user["level"] = level
        user["last_plan"] = build_workout_plan(goal, level, equipment, days, minutes)
        st.success("Workout plan generated.")

    if user.get("last_plan"):
        tabs = st.tabs([item["day"] for item in user["last_plan"]])
        for tab, day_plan in zip(tabs, user["last_plan"]):
            with tab:
                st.caption(f"{day_plan['focus']} | {day_plan['duration']} minutes")
                cols = st.columns(2)
                for index, exercise in enumerate(day_plan["exercises"]):
                    with cols[index % 2]:
                        body = (
                            f"{html.escape(exercise['sets'])} x {html.escape(exercise['reps'])}<br>"
                            f"{html.escape(exercise['coach_note'])}"
                        )
                        card(
                            exercise["name"],
                            body,
                            [exercise["focus"], day_plan["duration"] and f"{day_plan['duration']} min"],
                        )

        c1, c2 = st.columns([0.25, 0.75])
        if c1.button("Log completed workout", use_container_width=True):
            user["workouts"].append(
                {
                    "date": TODAY.isoformat(),
                    "goal": user["last_plan"][0]["focus"].replace(" session", ""),
                    "duration": user["last_plan"][0]["duration"],
                    "score": random.randint(82, 98),
                }
            )
            st.success("Workout saved to your activity log.")
            st.rerun()
        c2.info("Use the log button after completing today's session.")
    else:
        st.info("Generate a plan to see your training split.")


def render_nutrition() -> None:
    user = current_user()
    section("Nutrition Lab")
    st.markdown('<p class="subtle">Calculate calorie, macro, and hydration targets for the member goal.</p>', unsafe_allow_html=True)

    with st.form("nutrition_form"):
        c1, c2, c3 = st.columns(3)
        weight = c1.number_input("Weight (kg)", min_value=30.0, max_value=220.0, value=75.0, step=0.5)
        height = c2.number_input("Height (cm)", min_value=120.0, max_value=230.0, value=172.0, step=0.5)
        age = c3.number_input("Age", min_value=13, max_value=85, value=24)
        c4, c5, c6 = st.columns(3)
        sex = c4.selectbox("Sex", ["Male", "Female"])
        activity = c5.selectbox("Activity", list(ACTIVITY_FACTORS.keys()), index=2)
        goal = c6.selectbox("Goal", list(EXERCISE_LIBRARY.keys()), index=list(EXERCISE_LIBRARY.keys()).index(user["goal"]))
        calculate = st.form_submit_button("Calculate nutrition")

    plan = None
    if calculate:
        plan = macro_plan(weight, height, age, sex, activity, goal)
        user["meals"].append(
            {
                "date": TODAY.isoformat(),
                "goal": goal,
                "calories": plan["calories"],
                "protein": plan["protein"],
                "carbs": plan["carbs"],
                "fats": plan["fats"],
            }
        )
        st.success("Nutrition targets saved.")

    if plan:
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("Calories", f"{plan['calories']} kcal")
        c2.metric("Protein", f"{plan['protein']} g")
        c3.metric("Carbs", f"{plan['carbs']} g")
        c4.metric("Fats", f"{plan['fats']} g")
        c5.metric("Water", f"{plan['water']} L")

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=["Protein", "Carbs", "Fats"],
                    values=[plan["protein"] * 4, plan["carbs"] * 4, plan["fats"] * 9],
                    hole=0.58,
                    marker_colors=["#35e0bd", "#ffc247", "#ff6b6b"],
                )
            ]
        )
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=350,
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=True,
        )
        left, right = st.columns([0.75, 1])
        with left:
            st.plotly_chart(fig, use_container_width=True)
        with right:
            section("Meal ideas")
            for meal in MEAL_TEMPLATES[goal]:
                card(meal, "Pair with water, vegetables, and consistent portion tracking.", [goal])
    elif user.get("meals"):
        st.caption("Last saved nutrition target")
        st.dataframe(pd.DataFrame(user["meals"][-5:]), use_container_width=True, hide_index=True)


def render_progress() -> None:
    user = current_user()
    section("Progress Studio")

    with st.form("progress_form"):
        c1, c2, c3 = st.columns(3)
        weight = c1.number_input("Weight (kg)", min_value=30.0, max_value=220.0, value=75.0, step=0.1)
        body_fat = c2.number_input("Body fat (%)", min_value=3.0, max_value=60.0, value=22.0, step=0.1)
        energy = c3.slider("Energy score", 1, 100, 80)
        save = st.form_submit_button("Save progress")

    if save:
        user["history"].append(
            {
                "date": TODAY.isoformat(),
                "weight": round(weight, 1),
                "body_fat": round(body_fat, 1),
                "energy": energy,
            }
        )
        st.success("Progress saved.")
        st.rerun()

    if user["history"]:
        df = pd.DataFrame(user["history"])
        df["date"] = pd.to_datetime(df["date"])

        c1, c2 = st.columns([1.05, 0.95], gap="large")
        with c1:
            fig = px.area(
                df,
                x="date",
                y="weight",
                markers=True,
                color_discrete_sequence=["#35e0bd"],
            )
            fig.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                title="Weight trend",
                height=360,
                margin=dict(l=20, r=20, t=50, b=20),
            )
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            latest = df.iloc[-1]
            first = df.iloc[0]
            weight_delta = latest["weight"] - first["weight"]
            fat_delta = latest["body_fat"] - first["body_fat"]
            col_a, col_b = st.columns(2)
            col_a.metric("Weight change", f"{weight_delta:+.1f} kg")
            col_b.metric("Fat change", f"{fat_delta:+.1f}%")
            st.dataframe(df.sort_values("date", ascending=False), use_container_width=True, hide_index=True)
    else:
        st.info("No progress entries yet.")


def render_attendance() -> None:
    user = current_user()
    section("Attendance")

    checked_in_today = any(item.get("date") == TODAY.isoformat() for item in user["checkins"])
    c1, c2, c3 = st.columns([0.25, 0.25, 0.5])
    if c1.button("Check in today", use_container_width=True):
        if checked_in_today:
            st.warning("Already checked in today.")
        else:
            user["checkins"].append({"date": TODAY.isoformat(), "time": dt.datetime.now().strftime("%H:%M")})
            st.success("Attendance recorded.")
            st.rerun()
    c2.metric("Streak", f"{calculate_streak(user['checkins'])} days")
    c3.info("Attendance powers streak and readiness on the Command Center.")

    if user["checkins"]:
        df = pd.DataFrame(user["checkins"]).sort_values("date", ascending=False)
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.caption("No attendance records yet.")


def render_admin() -> None:
    user = current_user()
    section("Admin")
    if user["role"] != "admin":
        st.error("Access denied. Admin role required.")
        return

    rows = []
    for username, member in st.session_state.users.items():
        ensure_user_shape(member)
        latest_history = member["history"][-1] if member["history"] else {}
        rows.append(
            {
                "username": username,
                "name": member["name"],
                "role": member["role"],
                "goal": member["goal"],
                "level": member["level"],
                "checkins": len(member["checkins"]),
                "workouts": len(member["workouts"]),
                "latest_weight": latest_history.get("weight", "-"),
            }
        )

    df = pd.DataFrame(rows)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Members", len(df))
    c2.metric("Check-ins", int(df["checkins"].sum()))
    c3.metric("Workouts logged", int(df["workouts"].sum()))
    c4.metric("Admin users", int((df["role"] == "admin").sum()))

    st.write("")
    st.dataframe(df, use_container_width=True, hide_index=True)


# ---------------- APP ----------------
ensure_state()
menu = render_sidebar()

if not st.session_state.current_user:
    render_auth(menu)
elif menu == "Command Center":
    render_command_center()
elif menu == "Smart Workout":
    render_workout()
elif menu == "Nutrition Lab":
    render_nutrition()
elif menu == "Progress Studio":
    render_progress()
elif menu == "Attendance":
    render_attendance()
elif menu == "Admin":
    render_admin()
elif menu == "Logout":
    st.session_state.current_user = None
    st.success("Logged out.")
    st.rerun()
