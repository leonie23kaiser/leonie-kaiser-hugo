param(
  [int]$ThresholdHours = 2,
  [switch]$SummaryOnly
)

$ThresholdSeconds = $ThresholdHours * 3600

# Get all commits with full details, sorted chronologically
$commits = git log --all --format="%ai|%h|%an|%s" --reverse | ForEach-Object {
  $parts = $_ -split '\|', 4
  @{
    timestamp = $parts[0]
    hash = $parts[1]
    author = $parts[2]
    subject = $parts[3]
  }
}

if ($commits.Count -eq 0) {
  Write-Host "No commits found"
  exit 1
}

# Convert to array if single commit
if ($commits -isnot [array]) {
  $commits = @($commits)
}

# Parse timestamps to datetime and track contributors
$timestamps = @()
$contributors = @{}
foreach ($commit in $commits) {
  $dt = [DateTime]::Parse($commit.timestamp)
  $timestamps += $dt
  if (-not $contributors[$commit.author]) {
    $contributors[$commit.author] = 0
  }
  $contributors[$commit.author] += 1
}

# Calculate gaps and sessions
$totalWorkSeconds = 0
$firstCommit = $timestamps[0]
$lastCommit = $timestamps[-1]
$currentSessionStart = 0
$sessionDurations = @()
$sessionRanges = @()
$commitToSession = @()

$sessionNum = 1

for ($i = 1; $i -lt $timestamps.Count; $i++) {
  $prevTime = $timestamps[$i - 1]
  $currTime = $timestamps[$i]

  $gapSeconds = [int]($currTime - $prevTime).TotalSeconds

  if ($gapSeconds -gt $ThresholdSeconds) {
    # End of session
    $sessionSeconds = [int]($prevTime - $timestamps[$currentSessionStart]).TotalSeconds
    $sessionDurations += $sessionSeconds
    $sessionRanges += "$($timestamps[$currentSessionStart].ToString('MMM d HH:mm')) → $($prevTime.ToString('HH:mm'))"
    $totalWorkSeconds += $sessionSeconds

    # Mark all commits in this session
    for ($j = $currentSessionStart; $j -lt $i; $j++) {
      $commitToSession += $sessionNum
    }

    # Start new session at next commit
    $currentSessionStart = $i
    $sessionNum++
  }
}

# Add final session
$finalSessionSeconds = [int]($timestamps[-1] - $timestamps[$currentSessionStart]).TotalSeconds
$sessionDurations += $finalSessionSeconds
$sessionRanges += "$($timestamps[$currentSessionStart].ToString('MMM d HH:mm')) → $($timestamps[-1].ToString('HH:mm'))"
$totalWorkSeconds += $finalSessionSeconds

for ($j = $currentSessionStart; $j -lt $commits.Count; $j++) {
  $commitToSession += $sessionNum
}

# Format duration helper
function Format-Duration($seconds) {
  if ($seconds -lt 0) { $seconds = 0 }
  $hours = [int]($seconds / 3600)
  $mins = [int](($seconds % 3600) / 60)
  if ($hours -eq 0 -and $mins -eq 0) { return "0m" }
  if ($hours -eq 0) { return "$($mins)m" }
  return "$($hours)h $($mins)m"
}

# Truncate message for table
function Truncate-Message($msg, $maxLen = 40) {
  if ($msg.Length -gt $maxLen) {
    return $msg.Substring(0, $maxLen - 3) + "..."
  }
  return $msg
}

# Generate markdown table (ALWAYS OUTPUT)
Write-Host "## Chronological Commit Log"
Write-Host ""

$tableHeader = "| Timestamp | Author | Hash | Message | Session | Cumulative |"
$tableSeparator = "|-----------|--------|------|---------|---------|------------|"

Write-Host $tableHeader
Write-Host $tableSeparator

$sessionStartTime = @()
foreach ($session in 1..$sessionNum) {
  $sessionStartTime += $null
}

for ($i = 0; $i -lt $commits.Count; $i++) {
  $commit = $commits[$i]
  $timeStr = $timestamps[$i].ToString('MMM d HH:mm')
  $authorStr = $commit.author
  $hashStr = $commit.hash.Substring(0, 7)
  $messageStr = Truncate-Message $commit.subject

  $session = $commitToSession[$i]

  # Calculate cumulative time within session
  if ($i -eq 0 -or $commitToSession[$i - 1] -ne $session) {
    $sessionStartTime[$session - 1] = $timestamps[$i]
  }

  $cumulativeSeconds = [int]($timestamps[$i] - $sessionStartTime[$session - 1]).TotalSeconds
  $cumulStr = Format-Duration $cumulativeSeconds

  Write-Host "| $timeStr | $authorStr | ``$hashStr`` | $messageStr | $session | $cumulStr |"
}

Write-Host ""

# Session summary table
Write-Host "## Session Summary"
Write-Host ""

$sessionTableHeader = "| Session | Duration | Time Range |"
$sessionTableSeparator = "|---------|----------|-----------|"

Write-Host $sessionTableHeader
Write-Host $sessionTableSeparator

for ($i = 0; $i -lt $sessionDurations.Count; $i++) {
  Write-Host "| $($i + 1) | $(Format-Duration $sessionDurations[$i]) | $($sessionRanges[$i]) |"
}

Write-Host ""

# Stats
Write-Host "## Stats"
Write-Host ""
Write-Host "- **Total working time:** $(Format-Duration $totalWorkSeconds)"
Write-Host "- **Contributors:** $($contributors.Count) ($($contributors.Keys -join ", "))"
Write-Host "- **Total commits:** $($commits.Count)"
Write-Host ""

# Only show summary if not in summary-only mode
if (-not $SummaryOnly) {
  Write-Host "## Session Breakdown"
  Write-Host ""
  for ($i = 0; $i -lt $sessionDurations.Count; $i++) {
    Write-Host "**Session $($i + 1):** $(Format-Duration $sessionDurations[$i])"
  }
}
