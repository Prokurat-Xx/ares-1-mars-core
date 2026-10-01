# ARES-1: MARS CORE // PRODUCTION REPOSITORY

**Build 6.0 // Gold Master**

A punishing, turn-based sci-fi survival strategy simulator built with
Python and Streamlit.

ARES-1 places the player in command of a failing Mars colony where
Oxygen, Energy, Morale, crew survival, environmental hazards, and
strategic decisions interact through a progressively degrading survival
system.

## SYSTEM ARCHITECTURE

ARES-1 uses Streamlit session state as the central runtime state
container. Time progression is centralized so normal UI interactions
cannot accidentally advance multiple Sols or apply duplicate resource
consumption.

``` text
PLAYER DECISION -> RESOURCE CHANGES -> END-OF-SOL ENGINE
-> STATION CONSUMPTION -> HUMAN FACTOR -> CRISIS SYSTEM
-> WEATHER LIFECYCLE -> TELEMETRY -> NEXT SOL
```

## CORE SURVIVAL SYSTEMS

Primary resources are **Oxygen, Energy, and Morale**. Additional
strategic systems include Metal, Crystals, Crew, the CO2 Auto-Filter,
Supply Shuttle, Cave Expeditions, dynamic Weather, Mission Log, and
Telemetry.

A mission terminates when critical survival conditions are reached,
including Oxygen depletion, Energy blackout, or complete crew loss.

## COMMANDER CLASSES

-   **Chief Engineer** --- base Energy consumption is **2 Energy/Sol**
    and remains 2 during Extreme Frost.
-   **Astrobiologist** --- Oxygen consumption multiplier **x0.80**.
-   **Station Commander** --- immune to the standard low-resource panic
    Morale penalty.

## PROGRESSIVE DIFFICULTY // DEATH TIMER

-   **Sol 11+ // Station Degradation:** Without the CO2 Auto-Filter,
    Oxygen draw increases by **+4 O2/Sol**. The filter prevents this
    degradation and applies **x0.75 Oxygen consumption**.
-   **Sol 13+ // Extreme Frost:** Astrobiologist and Station Commander
    base Energy consumption increases from **3 to 4 Energy/Sol**. Chief
    Engineer remains at **2 Energy/Sol**.
-   **Sol 16+ // Long-Term Isolation:** Standard low-resource panic
    increases from **-8 to -16 Morale**.

## DYNAMIC WEATHER ENGINE

While weather is CLEAR, there is a **25% chance** to generate a Severe
Dust Storm. Each storm lasts **3 Sols** and adds **+3 Energy draw/Sol**
to every commander class.

The weather lifecycle is synchronized with the centralized turn engine
so newly generated storms are not incorrectly decremented on the same
Sol they appear.

## CREW MANIFEST & TRAITS

Every mission begins with five colonists. Three specialist traits are
randomly distributed among the crew.

-   **Genius** --- reduces CO2 Auto-Filter fabrication cost from 30
    Metal / 10 Crystals to 20 Metal / 8 Crystals while alive.
-   **Veteran** --- when the current Leader is a Veteran, the standard
    isolation depression crisis can be prevented during crisis
    generation.
-   **Paranoid** --- increases supported negative crisis Morale
    penalties by 5.

Crew casualties are handled through a centralized casualty engine. If
the current Leader dies, leadership automatically transfers to the next
surviving colonist.

## STRATEGIC SYSTEMS

-   **CO2 Auto-Filter:** Prevents Sol 11+ degradation and applies
    **x0.75 Oxygen consumption**.
-   **Oxygen Synthesis:** **-10 Energy, +25 Oxygen**.
-   **Recreation Feed:** **-5 Energy, +15 Morale**.
-   **Cave Expedition:** Launch cost **-8 Energy**, followed by
    encounter-specific strategic outcomes.
-   **Supply Shuttle:** Provides periodic trading opportunities. Trading
    itself does not advance the mission clock.

## TELEMETRY

ARES-1 records Sol, Oxygen, Energy, and Morale telemetry. Plotly
visualizes the colony's survival trajectory during and after a mission.

## DATA SCIENCE & BALANCE VALIDATION

The final Build 6.0 balance was evaluated using automated Python
simulation and a Resource-Balanced Heuristic AI agent.

### Diagnostic Control Test

A 3,000-mission diagnostic batch identified a strong late-game Energy
bottleneck:

-   **Global Mean Survival:** 18.21 Sols
-   **Global Blackout Rate:** 86.8%
-   **Missions reaching Sol 20:** 14.4%
-   **Missions reaching Sol 25:** 11.1%
-   **Mission terminations during Sol 16-20:** 67.6%

### Frost A/B Experiment

A second 3,000-mission experiment changed exactly one balance variable:
non-Engineer Extreme Frost Energy draw from **5 to 4 Energy/Sol**. All
other mechanics remained unchanged.

  Metric Indicator                Control   Final v6.0 Balance
  -------------------------- ------------ --------------------
  Engineer Mean Survival       20.33 Sols           20.33 Sols
  Engineer Median (P50)           18 Sols              18 Sols
  Engineer P90                    28 Sols              28 Sols
  Biologist Mean Survival      17.05 Sols           17.97 Sols
  Biologist Median (P50)          17 Sols              18 Sols
  Biologist P90                   19 Sols              25 Sols
  Commander Mean Survival      17.25 Sols           18.76 Sols
  Commander Median (P50)          17 Sols              18 Sols
  Commander P90                   19 Sols              27 Sols
  Global Blackout Rate              86.8%                84.7%
  Missions Reaching Sol 20          14.4%                21.1%
  Missions Reaching Sol 25          11.1%                16.5%

The tested **4 Energy/Sol** value was adopted as the final Build 6.0
Gold Master balance.

## TECHNOLOGY STACK

-   Python
-   Streamlit
-   Plotly
-   Procedural simulation
-   Session-state game architecture
-   Heuristic / Monte Carlo-style balance testing
-   HTML/CSS terminal interface

## LOCAL DEVELOPMENT

``` bash
git clone https://github.com/Prokurat-Xx/ares-1-mars-core.git
cd ares-1-mars-core
pip install -r requirements.txt
streamlit run app.py
```

## PROJECT STATUS

``` text
ARES-1 // MARS CORE
BUILD 6.0 // GOLD MASTER
BALANCE VALIDATED
READY FOR DEPLOYMENT
```

© 2026 Ares-1: Mars Core. Engineered by Alisa Prokurat.
