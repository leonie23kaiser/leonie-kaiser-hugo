#!/bin/bash

# get-working-time: Calculate actual working hours from git commits, excluding idle periods

THRESHOLD_HOURS=2
VERBOSE=false

while [[ $# -gt 0 ]]; do
  case $1 in
    --threshold) THRESHOLD_HOURS="$2"; shift 2 ;;
    --verbose) VERBOSE=true; shift ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

THRESHOLD_SECS=$((THRESHOLD_HOURS * 3600))

# Get all commits with timestamps, sorted chronologically
mapfile -t COMMITS < <(git log --all --format="%ai|%h|%s" --reverse)

if [[ ${#COMMITS[@]} -eq 0 ]]; then
  echo "No commits found"
  exit 1
fi

# Parse commits and calculate durations
declare -a TIMESTAMPS
declare -a HASHES
for commit in "${COMMITS[@]}"; do
  IFS='|' read -r timestamp hash subject <<< "$commit"
  TIMESTAMPS+=("$timestamp")
  HASHES+=("$hash")
done

# Calculate gaps and sessions
TOTAL_WORK_SECS=0
FIRST_COMMIT="${TIMESTAMPS[0]}"
LAST_COMMIT="${TIMESTAMPS[-1]}"
CURRENT_SESSION_START=0
SESSION_NUM=0
declare -a SESSION_DURATIONS
declare -a SESSION_RANGES

for ((i = 1; i < ${#TIMESTAMPS[@]}; i++)); do
  PREV_TS="${TIMESTAMPS[$((i-1))]}"
  CURR_TS="${TIMESTAMPS[$i]}"

  # Convert to epoch seconds
  PREV_EPOCH=$(date -d "$PREV_TS" +%s 2>/dev/null || gdate -d "$PREV_TS" +%s)
  CURR_EPOCH=$(date -d "$CURR_TS" +%s 2>/dev/null || gdate -d "$CURR_TS" +%s)

  GAP_SECS=$((CURR_EPOCH - PREV_EPOCH))

  if [[ $GAP_SECS -gt $THRESHOLD_SECS ]]; then
    # End of session
    SESSION_SECS=$((PREV_EPOCH - CURRENT_SESSION_START))
    SESSION_DURATIONS+=($SESSION_SECS)
    SESSION_RANGES+=("${TIMESTAMPS[$CURRENT_SESSION_START]:0:16} → ${PREV_TS:0:16}")
    TOTAL_WORK_SECS=$((TOTAL_WORK_SECS + SESSION_SECS))

    # Start new session at next commit
    CURRENT_SESSION_START=$i
  fi
done

# Add final session
FINAL_EPOCH=$(date -d "${TIMESTAMPS[-1]}" +%s 2>/dev/null || gdate -d "${TIMESTAMPS[-1]}" +%s)
START_EPOCH=$(date -d "${TIMESTAMPS[$CURRENT_SESSION_START]}" +%s 2>/dev/null || gdate -d "${TIMESTAMPS[$CURRENT_SESSION_START]}" +%s)
SESSION_SECS=$((FINAL_EPOCH - START_EPOCH))
SESSION_DURATIONS+=($SESSION_SECS)
SESSION_RANGES+=("${TIMESTAMPS[$CURRENT_SESSION_START]:0:16} → ${TIMESTAMPS[-1]:0:16}")
TOTAL_WORK_SECS=$((TOTAL_WORK_SECS + SESSION_SECS))

# Format output
format_duration() {
  local secs=$1
  local hours=$((secs / 3600))
  local mins=$(((secs % 3600) / 60))
  printf "%dh %dm" $hours $mins
}

echo "Total working time:  $(format_duration $TOTAL_WORK_SECS)"
echo "Sessions:            ${#SESSION_DURATIONS[@]}"
echo "First commit:        ${FIRST_COMMIT:0:16}"
echo "Last commit:         ${LAST_COMMIT:0:16}"
echo ""

for ((i = 0; i < ${#SESSION_DURATIONS[@]}; i++)); do
  echo "Session $((i+1)):  $(format_duration ${SESSION_DURATIONS[$i]})  (${SESSION_RANGES[$i]})"
done
