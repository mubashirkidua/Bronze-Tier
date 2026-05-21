# Bronze Tier Skills

**Tier Status:** Active  
**Last Updated:** 2026-04-03

---

## Overview

Bronze Tier provides foundational AI employee capabilities for local file operations, task management, and documentation. All skills operate with **Human-in-the-Loop (HITL)** oversight for sensitive actions.

---

## Enabled Skills

### 1. File Management
**Skill ID:** `bronze.file_mgmt`  
**Permissions:** Read, Write, Move, Copy files within vault  
**Restrictions:** Cannot delete files >10MB without approval

**Capabilities:**
- Create new markdown files
- Read existing files
- Move files between folders
- Copy files with metadata preservation
- Organize files by category/date

**Use Cases:**
- Processing incoming files from Inbox
- Archiving completed tasks to Done
- Creating backup copies

---

### 2. Task Tracking
**Skill ID:** `bronze.task_track`  
**Permissions:** Read/Write to Needs_Action, Plans, Done folders  
**Restrictions:** Cannot auto-complete tasks without user confirmation

**Capabilities:**
- Parse task requests from files
- Create task entries with status
- Track task progress (Pending → In Progress → Done)
- Log task completion timestamps
- Generate task summaries

**Use Cases:**
- Converting inbox items to actionable tasks
- Updating task status during processing
- Creating completion records

---

### 3. Documentation
**Skill ID:** `bronze.docs`  
**Permissions:** Read/Write to all markdown files  
**Restrictions:** Cannot modify Company_Handbook.md without approval

**Capabilities:**
- Create structured documentation
- Update dashboard status
- Write activity logs
- Generate briefing documents
- Maintain skill registry

**Use Cases:**
- Creating Plan.md for each task
- Updating Dashboard.md with status changes
- Logging actions in Logs/ folder
- Writing daily/weekly briefings

---

### 4. Local Search
**Skill ID:** `bronze.search`  
**Permissions:** Read-only search across vault  
**Restrictions:** Search only (no external queries)

**Capabilities:**
- Full-text search within vault files
- Pattern-based file discovery
- Content extraction and summarization
- Link/reference discovery

**Use Cases:**
- Finding related tasks in Done folder
- Searching for previous similar requests
- Locating specific information in documentation

---

## Permission Matrix

| Action | Allowed | Requires Approval |
|--------|---------|-------------------|
| Read vault files | ✅ | - |
| Write to Inbox/Needs_Action/Plans/Done | ✅ | - |
| Write to Logs/Briefings | ✅ | - |
| Move files between workflow folders | ✅ | - |
| Delete files | ❌ | Human only |
| Modify Company_Handbook.md | ❌ | Human only |
| External API calls | ❌ | Not available in Bronze |
| Financial transactions | ❌ | Human only |

---

## Upgrade Path

| Skill | Silver Tier | Gold Tier |
|-------|-------------|-----------|
| File Management | Cloud sync | Auto-cleanup rules |
| Task Tracking | Email integration | Auto-prioritization |
| Documentation | Template generation | Auto-briefings |
| Local Search | Web search | AI-powered insights |

---

## Skill Invocation Format

When using skills, log them in this format:

```
[SKILL_USED] bronze.file_mgmt - Read file: Inbox/request.md
[SKILL_USED] bronze.docs - Created: Plans/Plan_20260403.md
[SKILL_USED] bronze.task_track - Status: In Progress
```
