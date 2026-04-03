# Team Ops

Marketing team performance and operations system that combines skills gap analysis, capacity planning with utilization tracking, 1:1 meeting prep generation, OKR progress tracking, and meeting intelligence extraction.

## Key Capabilities

- **Skills Gap Matrix** -- maps each team member's proficiency (1-5) across all required marketing competencies (SEO, paid ads, copywriting, analytics, design, video, email, CRO, etc.). Identifies gaps between current team capability and target state. Recommends: hire, train, or outsource for each gap
- **Capacity Planning** -- tracks weekly utilization per team member: billable hours, internal projects, admin, learning. Calculates: available capacity for new work, overtime risk (>85% utilization), underutilization (<60%), and projected capacity 4 weeks out based on committed projects
- **1:1 Meeting Prep Generator** -- before each 1:1, auto-generates a prep doc with: recent wins (completed tasks, shipped work), blockers (stalled items, dependencies), metric movement (their KPIs this week vs last), growth topics (skills they're developing), and suggested talking points based on OKR progress
- **OKR Progress Tracking** -- maintains team and individual OKRs with weekly key result updates. Calculates: on-track/at-risk/off-track status per key result, confidence-weighted overall objective progress, and projected end-of-quarter scores based on current trajectory
- **Meeting Intelligence** -- extracts structured data from any meeting transcript: decisions made, action items (with owners and deadlines), open questions, parking lot items, and key insights. Auto-creates follow-up tasks in project management tools
- **Sprint Health Monitor** -- tracks marketing sprint velocity: planned vs completed story points, carryover rate, blocker frequency. Flags unhealthy patterns: >20% carryover, declining velocity trend, recurring blockers
- **Hiring Needs Forecaster** -- based on capacity utilization + planned projects + OKR targets, calculates when the team needs to hire next and for which role

## Workflow

1. **Team Roster Setup** -- define team members, roles, competencies, weekly capacity (hours)
2. **Skills Assessment** -- rate each member 1-5 on each competency, identify target levels
3. **OKR Definition** -- set quarterly objectives with 3-5 measurable key results each
4. **Weekly Check-In** -- update: hours logged per project, key result progress, blockers
5. **1:1 Prep Generation** -- auto-generate prep docs 24 hours before each scheduled 1:1
6. **Meeting Processing** -- after any meeting, extract decisions, actions, questions
7. **Sprint Review** -- end-of-sprint velocity analysis and carryover assessment
8. **Capacity Forecast** -- 4-week forward view of team availability
9. **Gap Analysis** -- quarterly skills gap review with hire/train/outsource recommendations
10. **Quarterly OKR Review** -- scoring, reflection, and next quarter planning

## Activation Triggers

- "Generate 1:1 prep for [person]"
- "Show team capacity"
- "Update OKR progress"
- "Extract actions from this meeting"
- "Skills gap analysis"
- "Sprint health check"
- "When do we need to hire?"
- "Team utilization report"

## Configuration

```
TEAM_ROSTER_PATH=~/.team-ops/roster.json
OKR_PATH=~/.team-ops/okrs.json
CAPACITY_HOURS_PER_WEEK=40
UTILIZATION_TARGET=0.75             # 75% target utilization
UTILIZATION_OVERTIME_THRESHOLD=0.85
UTILIZATION_UNDERUSE_THRESHOLD=0.60
SPRINT_LENGTH_WEEKS=2
CARRYOVER_MAX_PCT=0.20              # 20% max acceptable carryover
OKR_ON_TRACK_THRESHOLD=0.70         # 70% of expected progress
OKR_AT_RISK_THRESHOLD=0.40          # 40% of expected progress
SKILLS_PROFICIENCY_SCALE=5          # 1=beginner, 5=expert
SKILLS_TARGET_MIN=3                 # minimum proficiency to be "covered"
ONE_ON_ONE_PREP_HOURS_BEFORE=24
MEETING_TOOL=otter                  # otter | fireflies | grain | manual
PROJECT_TOOL=linear                 # linear | asana | jira | notion
```

## Scoring Methodology

### Skills Gap Score (per competency)
```
Gap = target_level - max(team_member_levels)
Coverage: 0 gap = Covered, 1 gap = Trainable, 2+ gap = Hire/Outsource
Team Risk: competency covered by only 1 person = "Bus Factor Risk"

Priority = gap_size * competency_importance_weight
competency_importance: core (1.5x), supporting (1.0x), nice-to-have (0.5x)
```

### Utilization Health
```
Utilization = (billable_hours + project_hours) / capacity_hours

Health Status:
> 0.85 = Red (overtime risk, quality drops, burnout)
0.75-0.85 = Green (optimal zone)
0.60-0.75 = Yellow (available capacity, assign more work)
< 0.60 = Red (underutilized, reassign or restructure)
```

### OKR Trajectory Score
```
Expected Progress = (weeks_elapsed / total_weeks) * 100
Actual Progress = (current_value - start_value) / (target_value - start_value) * 100
Trajectory Ratio = Actual / Expected

On Track: ratio >= 0.70
At Risk: 0.40 <= ratio < 0.70
Off Track: ratio < 0.40

Projected Score = current_progress + (weekly_velocity * remaining_weeks)
Confidence = min(1.0, weeks_of_data / 4) * trajectory_consistency
```

### Sprint Velocity Health
```
Velocity = completed_story_points / sprint_length
Carryover Rate = carried_points / planned_points
Trend = linear regression slope over last 4 sprints

Healthy: carryover < 20% AND velocity stable or increasing
Warning: carryover 20-35% OR velocity declining
Unhealthy: carryover > 35% OR velocity declining 2+ consecutive sprints
```

## Output Formats

- **Skills Gap Matrix** -- team x competency grid with color-coded proficiency levels and gap highlights
- **Capacity Dashboard** -- per-person utilization bars with 4-week forecast
- **1:1 Prep Doc** -- structured document with wins, blockers, metrics, growth topics, talking points
- **OKR Tracker** -- objective-level progress bars with key result detail and trajectory indicators
- **Meeting Summary** -- decisions, action items (owner + deadline), open questions, parking lot
- **Sprint Report** -- velocity chart, carryover analysis, blocker log, health status
- **Hiring Forecast** -- projected hire date, role specification, and budget impact

## Integration Points

- Linear / Asana / Jira / Notion (task and project tracking)
- Otter.ai / Fireflies / Grain (meeting transcription)
- Google Calendar (1:1 scheduling, meeting detection)
- Slack (weekly digests, capacity alerts, meeting summaries)
- Google Sheets (skills matrix, OKR tracking)
- Lattice / 15Five (performance review data)
