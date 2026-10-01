import random
import math
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="ARES-1 // MARS CORE", page_icon=None, layout="wide")

CSS = r"""


    /* =======================================================
       ARES-1 // MATRIX TERMINAL UI
       SHARP TEXT PATCH
       ======================================================= */

    /* -------------------------------------------------------
       GLOBAL TERMINAL
       ------------------------------------------------------- */

    html,
    body,
    [class*="css"],
    .stApp,
    .stApp * {
        font-family: 'Lucida Console', Monaco, monospace !important;

        font-smooth: never !important;
        -webkit-font-smoothing: none !important;
        -moz-osx-font-smoothing: none !important;
        text-rendering: optimizeSpeed !important;

        text-shadow: none !important;
    }

    .stApp {
        background-color: #050505 !important;
        color: #00FF33 !important;
    }


    /* -------------------------------------------------------
       ALL TEXT
       ------------------------------------------------------- */

    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    p,
    span,
    label,
    div,
    a,
    .stMarkdown,
    .stCaption,
    [data-testid="stCaptionContainer"] {

        color: #00FF33 !important;

        font-family:
            'Lucida Console',
            Monaco,
            monospace !important;

        font-smooth: never !important;
        -webkit-font-smoothing: none !important;
        -moz-osx-font-smoothing: none !important;
        text-rendering: optimizeSpeed !important;

        text-shadow: none !important;
    }


    /* -------------------------------------------------------
       HEADINGS
       ------------------------------------------------------- */

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {

        color: #00FF33 !important;

        font-family:
            'Lucida Console',
            Monaco,
            monospace !important;

        font-weight: 700 !important;

        font-smooth: never !important;
        -webkit-font-smoothing: none !important;
        -moz-osx-font-smoothing: none !important;
        text-rendering: optimizeSpeed !important;

        text-shadow: none !important;
    }


    /* -------------------------------------------------------
       METRICS
       ------------------------------------------------------- */

    [data-testid="stMetric"] {

        background-color: #050505 !important;

        border: 1px solid #00FF33 !important;
        border-radius: 0px !important;

        padding: 12px !important;
    }


    [data-testid="stMetricValue"],
    [data-testid="stMetricLabel"] {

        color: #00FF33 !important;

        font-family:
            'Lucida Console',
            Monaco,
            monospace !important;

        font-smooth: never !important;
        -webkit-font-smoothing: none !important;
        -moz-osx-font-smoothing: none !important;
        text-rendering: optimizeSpeed !important;

        text-shadow: none !important;
    }


    [data-testid="stMetricValue"] {

        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }


    /* -------------------------------------------------------
       TERMINAL BUTTONS
       ------------------------------------------------------- */

    .stButton > button {

        background-color: #050505 !important;

        color: #00FF33 !important;

        border: 1px solid #00FF33 !important;
        border-radius: 0px !important;

        font-family:
            'Lucida Console',
            Monaco,
            monospace !important;

        font-weight: 700 !important;

        font-smooth: never !important;
        -webkit-font-smoothing: none !important;
        -moz-osx-font-smoothing: none !important;
        text-rendering: optimizeSpeed !important;

        text-shadow: none !important;

        transition:
            background-color 0.10s linear,
            color 0.10s linear;
    }


    .stButton > button:hover {

        background-color: #00FF33 !important;

        color: #050505 !important;

        border: 1px solid #00FF33 !important;

        box-shadow: none !important;
        text-shadow: none !important;
    }


    .stButton > button:focus {

        border: 1px solid #00FF33 !important;

        box-shadow: none !important;
        outline: 1px solid #00FF33 !important;

        text-shadow: none !important;
    }


    /* -------------------------------------------------------
       ALERT / STATUS PANELS
       ------------------------------------------------------- */

    .stAlert {

        background-color: #050505 !important;

        border: 1px solid #00FF33 !important;
        border-radius: 0px !important;

        color: #00FF33 !important;

        box-shadow: none !important;
    }


    .stAlert p,
    .stAlert div,
    .stAlert span {

        color: #00FF33 !important;
        text-shadow: none !important;
    }


    /* -------------------------------------------------------
       PROGRESS BARS
       ------------------------------------------------------- */

    [data-testid="stProgress"] > div > div,
    [data-testid="stProgressBar"] > div > div,
    .stProgress > div > div > div > div {

        background-color: #00FF33 !important;

        border-radius: 0px !important;

        box-shadow: none !important;
    }


    /* -------------------------------------------------------
       LINKS
       ------------------------------------------------------- */

    a {

        color: #00FF33 !important;

        text-decoration: underline !important;

        text-shadow: none !important;
    }


    /* -------------------------------------------------------
       REMOVE STREAMLIT DECORATION
       ------------------------------------------------------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* SIDEBAR TERMINAL */
    [data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid #00FF33 !important;
    }

    [data-testid="stSidebar"] * {
        color: #00FF33 !important;
        text-shadow: none !important;
        font-smooth: never !important;
        -webkit-font-smoothing: none !important;
        -moz-osx-font-smoothing: none !important;
        text-rendering: optimizeSpeed !important;
    }

    .termination-banner {
        text-align: center;
        color: #00FF33 !important;
        font-weight: 700 !important;
        font-size: 1.15rem !important;
        letter-spacing: 0.04em;
        text-shadow: none !important;
        animation: terminal-blink 0.85s steps(1, end) infinite;
    }

    .death-skull {
        width: 180px;
        max-width: 45vw;
        image-rendering: pixelated;
        filter: grayscale(1) sepia(1) saturate(8) hue-rotate(70deg) brightness(1.15);
    }

    @keyframes terminal-blink {
        0%, 49% { opacity: 1; }
        50%, 100% { opacity: 0; }
    }

"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

VERSION = "6.0"
CREW_NAMES = ["CHEN", "MILLER", "WRIGHT", "DAVIS", "CLARK"]
CREW_TRAITS = ["Genius", "Veteran", "Paranoid", "Standard", "Standard"]
CRISIS_TYPES = ["storm", "leak", "trap_signal", "depress"]


def append_log(message):
    st.session_state.log.append(message)


def get_crew_count():
    return len(st.session_state.crew_members)


def get_leader():
    return st.session_state.crew_members[0] if st.session_state.crew_members else None


def has_trait(trait_name):
    return any(member["trait"] == trait_name for member in st.session_state.crew_members)


def get_filter_cost():
    return (20, 8) if has_trait("Genius") else (30, 10)


def normalize_resources():
    st.session_state.ox = max(0.0, min(100.0, st.session_state.ox))
    st.session_state.energy = max(0.0, min(100.0, st.session_state.energy))
    st.session_state.morale = max(0.0, min(100.0, st.session_state.morale))
    st.session_state.metal = max(0, st.session_state.metal)
    st.session_state.crystals = max(0, st.session_state.crystals)


def apply_morale_penalty(base_penalty, crisis=False):
    penalty = base_penalty
    if crisis and has_trait("Paranoid"):
        penalty += 5
    st.session_state.morale -= penalty
    normalize_resources()
    return penalty


def initialize_game(commander_class=None, preserve_high_score=True):
    high_score = st.session_state.get("high_score", 1) if preserve_high_score else 1
    chosen_class = commander_class or st.session_state.get("commander_class")
    traits = CREW_TRAITS.copy()
    random.shuffle(traits)
    crew = [
        {"id": idx + 1, "name": name, "trait": traits[idx]}
        for idx, name in enumerate(CREW_NAMES)
    ]
    values = {
        "game_version": VERSION,
        "game_started": chosen_class is not None,
        "commander_class": chosen_class,
        "day": 1,
        "ox": 100.0,
        "energy": 100.0,
        "morale": 80.0,
        "metal": 20,
        "crystals": 5,
        "upgrade_filter": False,
        "crew_members": crew,
        "weather": "CLEAR",
        "weather_duration": 0,
        "current_event": None,
        "current_cave_event": None,
        "shuttle_open": False,
        "game_over": False,
        "failure_cause": None,
        "log": ["SOL 1: SYSTEM ONLINE // ARES-1 MARS CORE INITIALIZED"],
        "history": {"days": [], "oxygen": [], "energy": [], "morale": []},
        "high_score": high_score,
    }
    for key, value in values.items():
        st.session_state[key] = value
    record_history()


def ensure_state():
    if "high_score" not in st.session_state:
        st.session_state.high_score = 1
    if st.session_state.get("game_version") != VERSION or "crew_members" not in st.session_state:
        initialize_game(commander_class=None, preserve_high_score=True)


def record_history():
    history = st.session_state.history
    day = st.session_state.day
    if history["days"] and history["days"][-1] == day:
        history["oxygen"][-1] = st.session_state.ox
        history["energy"][-1] = st.session_state.energy
        history["morale"][-1] = st.session_state.morale
        return
    history["days"].append(day)
    history["oxygen"].append(st.session_state.ox)
    history["energy"].append(st.session_state.energy)
    history["morale"].append(st.session_state.morale)


def check_game_over():
    if st.session_state.game_over:
        return True
    cause = None
    if get_crew_count() <= 0:
        cause = "CREW LOST"
    elif st.session_state.ox <= 0:
        cause = "SUFFOCATION"
    elif st.session_state.energy <= 0:
        cause = "BLACKOUT"
    if cause:
        st.session_state.game_over = True
        st.session_state.failure_cause = cause
        survived = max(1, st.session_state.day)
        if survived > st.session_state.high_score:
            st.session_state.high_score = survived
        append_log(f"SOL {st.session_state.day}: MISSION FAILURE // {cause}")
        record_history()
        return True
    return False


def kill_random_crew_member(cause):
    if not st.session_state.crew_members:
        check_game_over()
        return None
    old_leader = get_leader()
    index = random.randrange(len(st.session_state.crew_members))
    casualty = st.session_state.crew_members.pop(index)
    st.session_state.morale -= 30
    normalize_resources()
    append_log(
        f"SOL {st.session_state.day}: CATASTROPHE // LOSS OF {casualty['name']} "
        f"({casualty['trait']}) // -30 MORALE"
    )
    append_log(f"SOL {st.session_state.day}: CASUALTY CAUSE // {cause.upper()}")
    if old_leader and casualty["id"] == old_leader["id"] and st.session_state.crew_members:
        new_leader = get_leader()
        append_log(
            f"SOL {st.session_state.day}: SUCCESSION PROTOCOL // NEW LEADER "
            f"{new_leader['name']} ({new_leader['trait']})"
        )
    check_game_over()
    return casualty


def generate_crisis():
    if st.session_state.current_event or st.session_state.game_over:
        return
    if random.random() >= 0.40:
        return
    event = random.choice(CRISIS_TYPES)
    if event == "depress":
        leader = get_leader()
        if leader and leader["trait"] == "Veteran":
            append_log(
                f"SOL {st.session_state.day}: CRISIS AVERTED // LEADER {leader['name']} "
                "(VETERAN) MAINTAINED MENTAL DISCIPLINE"
            )
            return
    st.session_state.current_event = event
    labels = {
        "storm": "EXTERIOR SYSTEM DAMAGE",
        "leak": "PRESSURE LEAK",
        "trap_signal": "UNKNOWN DISTRESS SIGNAL",
        "depress": "ISOLATION PSYCHOSIS",
    }
    append_log(f"SOL {st.session_state.day}: CRISIS // {labels[event]}")


def update_weather(weather_was_active):
    if weather_was_active:
        st.session_state.weather_duration -= 1
        if st.session_state.weather_duration <= 0:
            st.session_state.weather = "CLEAR"
            st.session_state.weather_duration = 0
            append_log(f"SOL {st.session_state.day}: WEATHER UPDATE // DUST STORM CLEARED")
        return
    if st.session_state.weather == "CLEAR" and random.random() < 0.25:
        st.session_state.weather = "DUST STORM"
        st.session_state.weather_duration = 3
        append_log(
            f"SOL {st.session_state.day}: WEATHER WARNING // SEVERE DUST STORM DETECTED "
            "// IMMINENT ENERGY GENERATION COLLAPSE"
        )


def end_of_day_calculation():
    if st.session_state.game_over:
        return
    current_day = st.session_state.day
    weather_was_active = st.session_state.weather == "DUST STORM"

    ox_draw = get_crew_count() * 2
    if current_day > 10 and not st.session_state.upgrade_filter:
        ox_draw += 4
        append_log(f"SOL {current_day}: SYSTEM NOTICE // FILTER CLOGGING INCREASED OXYGEN DRAW BY 4")
    if st.session_state.commander_class == "Biologist":
        ox_draw *= 0.80
    if st.session_state.upgrade_filter:
        ox_draw *= 0.75
    ox_draw = round(ox_draw, 1)

    energy_draw = 2 if st.session_state.commander_class == "Engineer" else 3
    if current_day > 12 and st.session_state.commander_class != "Engineer":
        energy_draw = 4
        append_log(
            f"SOL {current_day}: SYSTEM NOTICE // EXTREME MARTIAN FROST INCREASED BASE POWER DRAW TO 5"
        )
    if weather_was_active:
        energy_draw += 3
        append_log(f"SOL {current_day}: WEATHER LOAD // DUST STORM ADDED 3 ENERGY DRAW")

    st.session_state.ox -= ox_draw
    st.session_state.energy -= energy_draw
    normalize_resources()
    append_log(f"SOL {current_day}: DAILY LOAD // O2 -{ox_draw:g} // ENERGY -{energy_draw}")

    if check_game_over():
        record_history()
        return

    if st.session_state.ox < 40 or st.session_state.energy < 20:
        if st.session_state.commander_class != "Commander":
            panic_penalty = 16 if current_day > 15 else 8
            st.session_state.morale -= panic_penalty
            normalize_resources()
            append_log(f"SOL {current_day}: RESOURCE PANIC // MORALE -{panic_penalty}")
            if current_day > 15:
                append_log(f"SOL {current_day}: CRITICAL // LONG-TERM ISOLATION DOUBLED CREW PANIC PENALTY")
        else:
            append_log(f"SOL {current_day}: COMMAND DISCIPLINE // RESOURCE PANIC SUPPRESSED")

    if st.session_state.morale < 25 and random.random() < 0.40:
        st.session_state.energy -= 20
        st.session_state.morale += 10
        normalize_resources()
        append_log(f"SOL {current_day}: RIOT // POWER GRID SABOTAGED // ENERGY -20 // MORALE +10")
        if check_game_over():
            record_history()
            return

    generate_crisis()
    update_weather(weather_was_active)
    record_history()
    st.session_state.day += 1

    if st.session_state.day % 10 == 0:
        st.session_state.shuttle_open = True
        append_log(f"SOL {st.session_state.day}: SUPPLY SHUTTLE // DOCKING WINDOW OPEN")


def finish_major_action():
    end_of_day_calculation()
    st.rerun()


def resolve_crisis():
    st.session_state.current_event = None
    st.rerun()


def make_telemetry_chart():
    h = st.session_state.history
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=h["days"], y=h["oxygen"], mode="lines+markers", name="OXYGEN", line=dict(color="#00FF33", width=2)))
    fig.add_trace(go.Scatter(x=h["days"], y=h["energy"], mode="lines+markers", name="ENERGY", line=dict(color="#00CC29", width=2)))
    fig.add_trace(go.Scatter(x=h["days"], y=h["morale"], mode="lines+markers", name="MORALE", line=dict(color="#00991F", width=2)))
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#050505",
        plot_bgcolor="#050505",
        font=dict(color="#00FF33", family="Lucida Console, Monaco, monospace"),
        legend=dict(orientation="h"),
        margin=dict(l=20, r=20, t=35, b=20),
        xaxis=dict(title="SOL", gridcolor="#103A18"),
        yaxis=dict(title="LEVEL", range=[0, 105], gridcolor="#103A18"),
        height=360,
    )
    return fig


def render_survival_manual():
    with st.sidebar:
        st.markdown("### === ARES-1: SURVIVAL MANUAL ===")
        st.code(
            """CORE PROCESS DIALS

OXYGEN REGENERATOR SYSTEM
COST   // -10 ENERGY
YIELD  // +25 OXYGEN
ACTION // COMPLETES THE CURRENT SOL

RECREATION FEED TRANSMITTER
COST   // -5 ENERGY
YIELD  // +15 MORALE
ACTION // COMPLETES THE CURRENT SOL
RIOT   // BELOW 25 MORALE: 40% CHANCE
         OF -20 ENERGY SABOTAGE

MINIMUM BASE DRAW // STANDBY
COST   // 0 DIRECT ACTION RESOURCES
ACTION // SAFELY PASSES THE SOL
NOTE   // NORMAL DAILY O2 / ENERGY DRAW
         STILL APPLIES
TACTIC // CONSERVE ACTION COSTS DURING
         DUST STORMS OR FROST CYCLES

LAUNCH CAVERN RADAR EXPEDITION
COST   // -8 ENERGY
ACTION // OPENS ONE OF THREE CAVE
         ENCOUNTERS, THEN COMPLETES
         THE SOL AFTER RESOLUTION

ANCIENT VAULT
DETONATE // +40 METAL / +15 CRYSTALS
BYPASS   // 60%: +35 CRYSTALS
            40%: CAVE COLLAPSE,
            RANDOM CASUALTY, -30 MORALE

ABANDONED ROVER
SIPHON // -10 OXYGEN / +40 ENERGY
STRIP  // +45 METAL

GLOWING FUNGUS
HARVEST // -20 OXYGEN / +35 CRYSTALS
BURN    // +25 MORALE

SURVIVAL PRESSURE
SOL 11+ // WITHOUT CO2 FILTER:
          +4 DAILY OXYGEN DRAW
SOL 13+ // NON-ENGINEER BASE ENERGY
          DRAW INCREASES TO 5
SOL 16+ // RESOURCE PANIC DOUBLES
          FROM -8 TO -16 MORALE

WEATHER
DUST STORM // +3 DAILY ENERGY DRAW
DURATION   // 3 SOLS

CO2 AUTO-FILTER
STANDARD // 30 METAL / 10 CRYSTALS
GENIUS   // 20 METAL / 8 CRYSTALS
EFFECT   // OXYGEN DRAW x0.75 AND
            BLOCKS SOL 11+ O2 DECAY

CREW TRAITS
GENIUS   // CHEAPER FILTER
VETERAN  // IF LEADER, BLOCKS DEPRESS
PARANOID // +5 TO NEGATIVE MORALE
            EFFECTS FROM STORM / LEAK /
            DEPRESS CRISES

SUPPLY SHUTTLE
WINDOW // EVERY 10 SOLS
WEATHER // AVAILABLE EVEN IN DUST STORM
TRADE   // DOES NOT ADVANCE TIME
""",
            language=None,
        )


def render_start_screen():
    st.title("> ARES-1 // MARS CORE INTERFACE")
    st.markdown("BUILD 6.0 // GOLD MASTER")
    st.markdown("SELECT COMMAND AUTHORIZATION PROFILE")
    cols = st.columns(3)
    choices = [
        ("Engineer", "> CHIEF ENGINEER", "BASE ENERGY DRAW // 2"),
        ("Biologist", "> ASTROBIOLOGIST", "OXYGEN DRAW // x0.80"),
        ("Commander", "> STATION COMMANDER", "RESOURCE PANIC // IMMUNE"),
    ]
    for col, (value, label, desc) in zip(cols, choices):
        with col:
            st.markdown(desc)
            if st.button(label, key=f"class_{value}", use_container_width=True):
                initialize_game(value, preserve_high_score=True)
                st.rerun()


def render_hud():
    st.title("> ARES-1 // MARS CORE INTERFACE")
    st.caption("BUILD 6.0 // GOLD MASTER // MARS COLONY SURVIVAL SYSTEM")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("SOL", st.session_state.day)
    c2.metric("OXYGEN", f"{st.session_state.ox:.1f}")
    c3.metric("ENERGY", f"{st.session_state.energy:.1f}")
    c4.metric("MORALE", f"{st.session_state.morale:.1f}")
    c5.metric("CREW", get_crew_count())
    if st.session_state.weather == "DUST STORM":
        st.markdown(
            f"**WEATHER // DUST STORM**  |  DURATION // {st.session_state.weather_duration} SOLS  |  GRID PENALTY // +3 ENERGY"
        )
    else:
        st.markdown("**WEATHER // CLEAR**")


def render_crew_manifest():
    st.subheader("> CREW MANIFEST")
    lines = []
    for idx, member in enumerate(st.session_state.crew_members):
        status = "LEADER" if idx == 0 else "ACTIVE"
        lines.append(f"- {member['name']} // {status} // {member['trait'].upper()}")
    st.markdown("\n".join(lines) if lines else "NO ACTIVE CREW")


def render_crisis():
    event = st.session_state.current_event
    st.subheader("> CRISIS CONTROL")
    if event == "storm":
        st.markdown("EXTERIOR SYSTEM DAMAGE // EMERGENCY RESPONSE REQUIRED")
        a, b = st.columns(2)
        if a.button("> SEND CREW FOR EMERGENCY REPAIRS", key="storm_repair", use_container_width=True):
            chance = 0.50 if st.session_state.morale < 40 else 0.20
            if random.random() < chance:
                kill_random_crew_member("emergency exterior operations")
                if has_trait("Paranoid") and not st.session_state.game_over:
                    extra = apply_morale_penalty(5, crisis=False)
                    append_log(f"SOL {st.session_state.day}: PARANOID RESPONSE // ADDITIONAL MORALE -{extra}")
            else:
                append_log(f"SOL {st.session_state.day}: CRISIS RESOLVED // EXTERIOR REPAIRS SUCCESSFUL")
            st.session_state.current_event = None
            st.rerun()
        if b.button("> BUNKER LOCKDOWN", key="storm_bunker", use_container_width=True):
            st.session_state.ox -= 30
            normalize_resources()
            append_log(f"SOL {st.session_state.day}: CRISIS RESPONSE // BUNKER LOCKDOWN // OXYGEN -30")
            st.session_state.current_event = None
            check_game_over()
            st.rerun()
    elif event == "leak":
        st.markdown("PRESSURE LEAK // HABITAT INTEGRITY FALLING")
        a, b = st.columns(2)
        if a.button("> MANUAL SEAL", key="leak_manual", use_container_width=True):
            penalty = apply_morale_penalty(15, crisis=True)
            append_log(f"SOL {st.session_state.day}: LEAK SEALED MANUALLY // MORALE -{penalty}")
            st.session_state.current_event = None
            st.rerun()
        if b.button("> PURGE DAMAGED SECTION", key="leak_purge", use_container_width=True):
            st.session_state.ox -= 20
            normalize_resources()
            append_log(f"SOL {st.session_state.day}: DAMAGED SECTION PURGED // OXYGEN -20")
            st.session_state.current_event = None
            check_game_over()
            st.rerun()
    elif event == "trap_signal":
        st.markdown("UNKNOWN DISTRESS SIGNAL // ORIGIN UNVERIFIED")
        a, b = st.columns(2)
        if a.button("> INVESTIGATE SIGNAL", key="signal_accept", use_container_width=True):
            if random.random() < 0.50:
                st.session_state.metal += 25
                append_log(f"SOL {st.session_state.day}: SIGNAL CACHE RECOVERED // METAL +25")
            else:
                st.session_state.energy -= 15
                normalize_resources()
                append_log(f"SOL {st.session_state.day}: SIGNAL TRAP // ENERGY -15")
                check_game_over()
            st.session_state.current_event = None
            st.rerun()
        if b.button("> IGNORE SIGNAL", key="signal_ignore", use_container_width=True):
            append_log(f"SOL {st.session_state.day}: SIGNAL DISMISSED")
            st.session_state.current_event = None
            st.rerun()
    elif event == "depress":
        st.markdown("ISOLATION PSYCHOSIS // CREW COHESION CRITICAL")
        a, b = st.columns(2)
        if a.button("> ENFORCE DUTY ROTATION", key="depress_duty", use_container_width=True):
            penalty = apply_morale_penalty(15, crisis=True)
            append_log(f"SOL {st.session_state.day}: DUTY ROTATION ENFORCED // MORALE -{penalty}")
            st.session_state.current_event = None
            st.rerun()
        if b.button("> RECOVERY SESSION", key="depress_recovery", use_container_width=True):
            st.session_state.ox -= 15
            st.session_state.morale += 20
            normalize_resources()
            append_log(f"SOL {st.session_state.day}: RECOVERY SESSION // OXYGEN -15 // MORALE +20")
            st.session_state.current_event = None
            check_game_over()
            st.rerun()


def render_cave_event():
    event = st.session_state.current_cave_event
    st.subheader("> CAVE EXPEDITION")
    if event == "ancient_vault":
        st.markdown("ANCIENT VAULT // SEALED INDUSTRIAL CHAMBER")
        a, b = st.columns(2)
        if a.button("> DETONATE VAULT", key="vault_opt_a", use_container_width=True):
            st.session_state.metal += 40
            st.session_state.crystals += 15
            append_log(f"SOL {st.session_state.day}: VAULT DETONATED // METAL +40 // CRYSTALS +15")
            st.session_state.current_cave_event = None
            finish_major_action()
        if b.button("> BYPASS SECURITY", key="vault_opt_b", use_container_width=True):
            if random.random() < 0.60:
                st.session_state.crystals += 35
                append_log(f"SOL {st.session_state.day}: VAULT BYPASS SUCCESS // CRYSTALS +35")
            else:
                append_log(f"SOL {st.session_state.day}: VAULT BYPASS FAILURE // CAVE COLLAPSE")
                kill_random_crew_member("ancient vault cave collapse")
            st.session_state.current_cave_event = None
            if not st.session_state.game_over:
                finish_major_action()
            else:
                st.rerun()
    elif event == "abandoned_rover":
        st.markdown("ABANDONED ROVER // REACTOR CORE DETECTED")
        a, b = st.columns(2)
        if a.button("> SIPHON CORE", key="rover_opt_a", use_container_width=True):
            st.session_state.ox -= 10
            st.session_state.energy += 40
            normalize_resources()
            append_log(f"SOL {st.session_state.day}: ROVER CORE SIPHONED // OXYGEN -10 // ENERGY +40")
            st.session_state.current_cave_event = None
            if not check_game_over():
                finish_major_action()
            else:
                st.rerun()
        if b.button("> STRIP CHASSIS", key="rover_opt_b", use_container_width=True):
            st.session_state.metal += 45
            append_log(f"SOL {st.session_state.day}: ROVER STRIPPED // METAL +45")
            st.session_state.current_cave_event = None
            finish_major_action()
    elif event == "glowing_fungus":
        st.markdown("GLOWING FUNGUS // UNKNOWN BIOLOGICAL COLONY")
        a, b = st.columns(2)
        if a.button("> HARVEST", key="fungus_opt_a", use_container_width=True):
            st.session_state.ox -= 20
            st.session_state.crystals += 35
            normalize_resources()
            append_log(f"SOL {st.session_state.day}: FUNGUS HARVESTED // OXYGEN -20 // CRYSTALS +35")
            st.session_state.current_cave_event = None
            if not check_game_over():
                finish_major_action()
            else:
                st.rerun()
        if b.button("> BURN", key="fungus_opt_b", use_container_width=True):
            st.session_state.morale += 25
            normalize_resources()
            append_log(f"SOL {st.session_state.day}: FUNGUS INCINERATED // MORALE +25")
            st.session_state.current_cave_event = None
            finish_major_action()


def render_shuttle():
    st.subheader("> SUPPLY SHUTTLE")
    st.markdown("ORBITAL LOGISTICS WINDOW // AVAILABLE REGARDLESS OF WEATHER")
    st.markdown(f"INVENTORY // METAL {st.session_state.metal} // CRYSTALS {st.session_state.crystals}")
    c1, c2, c3 = st.columns(3)
    if c1.button("> BUY OXYGEN // 10 METAL", key="shuttle_ox", use_container_width=True):
        if st.session_state.metal >= 10:
            st.session_state.metal -= 10
            st.session_state.ox += 25
            normalize_resources()
            append_log(f"SOL {st.session_state.day}: SHUTTLE TRADE // METAL -10 // OXYGEN +25")
        st.rerun()
    if c2.button("> BUY ENERGY // 10 METAL", key="shuttle_energy", use_container_width=True):
        if st.session_state.metal >= 10:
            st.session_state.metal -= 10
            st.session_state.energy += 25
            normalize_resources()
            append_log(f"SOL {st.session_state.day}: SHUTTLE TRADE // METAL -10 // ENERGY +25")
        st.rerun()
    if c3.button("> BUY MORALE // 5 CRYSTALS", key="shuttle_morale", use_container_width=True):
        if st.session_state.crystals >= 5:
            st.session_state.crystals -= 5
            st.session_state.morale += 20
            normalize_resources()
            append_log(f"SOL {st.session_state.day}: SHUTTLE TRADE // CRYSTALS -5 // MORALE +20")
        st.rerun()
    if st.button("> DISMISS SHUTTLE", key="dismiss_shuttle", use_container_width=True):
        st.session_state.shuttle_open = False
        append_log(f"SOL {st.session_state.day}: SUPPLY SHUTTLE // DEPARTED")
        st.rerun()


def render_command_center():
    st.subheader("> COMMAND CENTER")
    a, b, c = st.columns(3)
    if a.button("> OXYGEN SYNTHESIS // 10 ENERGY", key="oxygen_synthesis", use_container_width=True):
        if st.session_state.energy >= 10:
            st.session_state.energy -= 10
            st.session_state.ox += 25
            normalize_resources()
            append_log(f"SOL {st.session_state.day}: OXYGEN SYNTHESIS // ENERGY -10 // OXYGEN +25")
            finish_major_action()
        else:
            st.warning("INSUFFICIENT ENERGY")
    if b.button("> MEDIA SESSION // 5 ENERGY", key="media_session", use_container_width=True):
        if st.session_state.energy >= 5:
            st.session_state.energy -= 5
            st.session_state.morale += 15
            normalize_resources()
            append_log(f"SOL {st.session_state.day}: MEDIA SESSION // ENERGY -5 // MORALE +15")
            finish_major_action()
        else:
            st.warning("INSUFFICIENT ENERGY")
    if c.button("> HOLD POSITION", key="hold_position", use_container_width=True):
        append_log(f"SOL {st.session_state.day}: COMMAND // HOLD POSITION")
        finish_major_action()

    st.subheader("> MANUFACTURING")
    filter_metal, filter_crystals = get_filter_cost()
    if st.session_state.upgrade_filter:
        st.markdown("CO2 AUTO-FILTER // ONLINE // OXYGEN DRAW x0.75 // DEGRADATION BLOCKED")
    else:
        modifier = "GENIUS ACTIVE" if has_trait("Genius") else "STANDARD FABRICATION"
        st.markdown(
            f"CO2 AUTO-FILTER // REQUIRED {filter_metal} METAL / {filter_crystals} CRYSTALS // {modifier}"
        )
        if st.button("> BUILD CO2 AUTO-FILTER", key="build_filter", use_container_width=True):
            if st.session_state.metal >= filter_metal and st.session_state.crystals >= filter_crystals:
                st.session_state.metal -= filter_metal
                st.session_state.crystals -= filter_crystals
                st.session_state.upgrade_filter = True
                append_log(
                    f"SOL {st.session_state.day}: MANUFACTURING // CO2 AUTO-FILTER ONLINE // "
                    f"METAL -{filter_metal} // CRYSTALS -{filter_crystals}"
                )
                st.rerun()
            else:
                st.warning("INSUFFICIENT MATERIALS")

    st.subheader("> EXPEDITION CONTROL")
    if st.button("> LAUNCH CAVE EXPEDITION // 8 ENERGY", key="main_expedition", use_container_width=True):
        if st.session_state.energy > 8:
            st.session_state.energy -= 8
            st.session_state.current_cave_event = random.choice(
                ["ancient_vault", "abandoned_rover", "glowing_fungus"]
            )
            append_log(f"SOL {st.session_state.day}: EXPEDITION LAUNCHED // ENERGY -8")
            st.rerun()
        else:
            st.warning("EXPEDITION ABORTED // ENERGY RESERVE TOO LOW")


def render_inventory():
    st.subheader("> STATION INVENTORY")
    c1, c2, c3 = st.columns(3)
    c1.metric("METAL", st.session_state.metal)
    c2.metric("CRYSTALS", st.session_state.crystals)
    c3.metric("COMMAND", st.session_state.commander_class.upper())
    render_crew_manifest()


def render_log():
    st.subheader("> MISSION LOG")
    entries = list(reversed(st.session_state.log[-16:]))
    st.code("\n".join(entries), language=None)


def render_game_over():
    render_hud()
    st.markdown(
        """
        <div style="text-align: center;">
            <img class="death-skull"
                 src="https://media.giphy.com/media/TiIbhyjqnEhDg4DrXm/giphy.gif"
                 width="180"
                 alt="Retro pixel laughing skull">
        </div>
        <div class="termination-banner">
            === MISSION TERMINATION // YOUR COLONY DIED ===
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.header("> MISSION FAILURE")
    st.markdown(f"FAILURE ANALYSIS // **{st.session_state.failure_cause}**")
    st.markdown(f"CURRENT RUN // SOL {st.session_state.day}")
    st.markdown(f"SESSION HIGH SCORE // SOL {st.session_state.high_score}")
    st.subheader("> POST-MISSION TELEMETRY")
    st.plotly_chart(make_telemetry_chart(), use_container_width=True, config={"displayModeBar": False})
    render_log()
    if st.button("> REBOOT MISSION", key="reboot_game", use_container_width=True):
        initialize_game(commander_class=None, preserve_high_score=True)
        st.rerun()


ensure_state()
render_survival_manual()

if not st.session_state.game_started:
    render_start_screen()
    st.stop()

if st.session_state.game_over:
    render_game_over()
    st.stop()

render_hud()

left, right = st.columns([1.45, 1])
with left:
    if st.session_state.current_event:
        render_crisis()
    elif st.session_state.current_cave_event:
        render_cave_event()
    elif st.session_state.shuttle_open:
        render_shuttle()
    else:
        render_command_center()
with right:
    render_inventory()
    st.subheader("> LIVE TELEMETRY")
    st.plotly_chart(make_telemetry_chart(), use_container_width=True, config={"displayModeBar": False})

render_log()
