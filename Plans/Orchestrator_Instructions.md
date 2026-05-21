# Orchestrator Instructions

**Tier:** Bronze  
**Version:** 1.0  
**Created:** 2026-04-03

---

## Core Orchestration Rule

> **Whenever a new file appears in `Needs_Action`, read it, create a `Plan.md`, and move the original to `Done` after processing.**

---

## Step-by-Step Workflow

### Step 1: Detect New File
- Monitor `Needs_Action/` folder for new files
- File arrives here automatically via `filesystem_watcher.py` from `Inbox/`

### Step 2: Read and Analyze
- Open and read the file content
- Identify the request/task type
- Determine which Bronze skills are needed:
  - `bronze.file_mgmt` - File operations
  - `bronze.task_track` - Task tracking
  - `bronze.docs` - Documentation
  - `bronze.search` - Search existing files

### Step 3: Create Plan
- Create a new plan file in `Plans/` folder
- Naming format: `Plans/Plan_YYYYMMDD_<description>.md`
- Include in plan:
  - Task description
  - Required skills
  - Step-by-step approach
  - Estimated actions

### Step 4: Execute Plan
- Follow the plan steps
- Use appropriate Bronze skills
- Log each action in `Logs/activity_YYYYMMDD.md`
- **HITL Check:** If task requires approval (financial >$100, deletions, external actions):
  - Move file to `Pending_Approval/`
  - Wait for human decision
  - If approved → continue; If rejected → move to `Rejected/`

### Step 5: Complete and Archive
- Update task status to "Done"
- Move original file from `Needs_Action/` to `Done/`
- Update `Dashboard.md` with completion status
- Log skill usage in format: `[SKILL_USED] bronze.xxx - action details`

---

## File Naming Conventions

| Folder | Format | Example |
|--------|--------|---------|
| Plans | `Plan_YYYYMMDD_<desc>.md` | `Plan_20260403_ProcessRequest.md` |
| Logs | `activity_YYYYMMDD.md` | `activity_20260403.md` |
| Briefings | `briefing_YYYYMMDD.md` | `briefing_20260403.md` |

---

## Logging Format

```markdown
## Activity Log - 2026-04-03

| Time | Action | Skill | Status |
|------|--------|-------|--------|
| 10:00 | Read file: Needs_Action/request.md | bronze.file_mgmt | ✅ |
| 10:01 | Created plan: Plans/Plan_20260403.md | bronze.docs | ✅ |
| 10:05 | Processed request | bronze.task_track | ✅ |
| 10:06 | Moved file to Done | bronze.file_mgmt | ✅ |
```

---

## Error Handling

1. **File unreadable:** Log error, move to `Needs_Action/_errors/`, notify user
2. **Plan execution fails:** Log failure, keep file in `Needs_Action`, add `_FAILED` prefix
3. **Approval needed:** Move to `Pending_Approval/`, wait for human action

---

## Quick Reference

```
Inbox → (watcher) → Needs_Action → (read) → Plans → (execute) → Done
                                         ↓
                              Pending_Approval → Approved/Rejected
```
