# 🏢 AI Employee Vault

A local-first, Obsidian-based task and workflow management system for AI-human collaboration with Human-in-the-Loop (HITL) oversight.

---

## 📋 Overview

AI Employee Vault transforms your AI assistant into a structured "digital employee" that can:
- Process incoming tasks and requests automatically
- Maintain clear audit trails for all actions
- Require human approval for sensitive operations
- Work entirely offline with local file storage

**Current Tier:** Bronze (v0.1)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Obsidian (optional, for GUI viewing)

### Installation

1. **Clone or download this repository**
   ```bash
   cd AI_Employee_Vault
   ```

2. **Install Python dependencies**
   ```bash
   pip install watchdog
   ```

3. **Start the file watcher**
   ```bash
   python watchers/filesystem_watcher.py
   ```

4. **Open in Obsidian** (optional)
   - Open Obsidian → "Open folder as vault" → Select `AI_Employee_Vault`

---

## 📁 Project Structure

```
AI_Employee_Vault/
├── Company_Handbook.md          # Core rules & governance
├── Dashboard.md                 # Status dashboard
├── README.md                    # This file
│
├── Skills/
│   ├── Agent_Skills.md          # Master skill registry
│   └── Bronze_Skills.md         # Bronze tier capabilities
│
├── Plans/
│   └── Orchestrator_Instructions.md  # Core workflow rules
│
├── watchers/
│   └── filesystem_watcher.py    # Automated file watcher
│
├── Inbox/                       # Entry point for new files
├── Needs_Action/                # Tasks requiring attention
├── Plans/                       # Strategic planning documents
├── Done/                        # Completed task archive
├── Pending_Approval/            # Awaiting human approval
├── Approved/                    # Approved items
├── Rejected/                    # Declined items
├── Logs/                        # Activity logs
└── Briefings/                   # Daily/weekly briefings
```

---

## 🔄 Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                     WORKFLOW PIPELINE                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [Drop File]                                                │
│       │                                                     │
│       ▼                                                     │
│  ┌─────────┐   (auto)    ┌──────────────┐                  │
│  │  Inbox  │ ──────────→ │ Needs_Action │                  │
│  └─────────┘  watcher.py └──────────────┘                  │
│                              │                              │
│                    ┌─────────┼─────────┐                    │
│                    ▼         ▼         ▼                    │
│              ┌─────────┐ ┌──────────┐ ┌──────┐             │
│              │  Plans  │ │ Pending  │ │ Done │             │
│              │         │ │ Approval │ │      │             │
│              └─────────┘ └──────────┘ └──────┘             │
│                              │                              │
│                    ┌─────────┴─────────┐                    │
│                    ▼                   ▼                    │
│              ┌─────────┐         ┌─────────┐                │
│              │Approved │         │Rejected │                │
│              └─────────┘         └─────────┘                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### How It Works

1. **Drop a file** in `Inbox/`
2. **Watcher auto-copies** it to `Needs_Action/` with `FILE_` prefix
3. **AI reads** the file and creates a plan in `Plans/`
4. **Processing** happens with appropriate skills
5. **Approval gate** if needed (financial >$100, deletions, external actions)
6. **Completion** → file moved to `Done/`, activity logged in `Logs/`

---

## 🛠️ Bronze Tier Skills

| Skill | ID | Description |
|-------|-----|-------------|
| File Management | `bronze.file_mgmt` | Read, write, move, copy files |
| Task Tracking | `bronze.task_track` | Parse and track tasks |
| Documentation | `bronze.docs` | Create docs, logs, briefings |
| Local Search | `bronze.search` | Full-text vault search |

See `Skills/Bronze_Skills.md` for full details.

---

## 🔒 Governance Rules

### Human-in-the-Loop (HITL) Required For:
- Financial transactions >$100
- Deleting important files/data
- Sending external communications
- Making irreversible changes

### Permission Matrix

| Action | Allowed | Requires Approval |
|--------|---------|-------------------|
| Read vault files | ✅ | - |
| Write to workflow folders | ✅ | - |
| Delete files | ❌ | Human only |
| Modify Company_Handbook.md | ❌ | Human only |
| External API calls | ❌ | Not available in Bronze |

---

## 📝 Usage Examples

### Test the System

1. **Start watcher:**
   ```bash
   python watchers/filesystem_watcher.py
   ```

2. **Create a test file** in `Inbox/`:
   ```markdown
   Title: Welcome New User
   Content: Please create an onboarding plan for this user.
   ```

3. **Watch the magic:**
   - File auto-copies to `Needs_Action/`
   - Log entry created in `Logs/`
   - Terminal shows timestamp

### Check Logs

Logs are automatically created in `Logs/activity_YYYY-MM-DD.md`:

```markdown
# Activity Log - 2026-04-03

| Time | Action | Status |
|------|--------|--------|
| 14:25:30 | File detected: test.md → FILE_test.md | ✅ |
```

---

## 📊 Dashboard

Open `Dashboard.md` to see:
- Current tier status
- Watcher status
- Pending tasks
- Bank balance
- Quick action links

---

## 🔮 Upgrade Path

| Tier | New Capabilities |
|------|------------------|
| **Silver** | Email, Calendar, Data Analysis, Code Generation |
| **Gold** | Web Research, Automation Triggers, AI Insights |

See `Skills/Agent_Skills.md` for full roadmap.

---

## 🐛 Troubleshooting

### Watcher not starting?
```bash
pip install watchdog
```

### Files not moving to Needs_Action?
- Ensure watcher is running
- Check file is actually in `Inbox/` folder
- Watcher only triggers on file **creation**, not modification

### Logs not appearing?
- Check `Logs/` folder exists
- Ensure watcher has write permissions
- Log file format: `activity_YYYY-MM-DD.md`

---

## 📄 License

Internal use only. All data stored locally.

---

## 🤝 Contributing

This is a personal AI employee vault. To add new capabilities:
1. Document the skill in `Skills/`
2. Update `Company_Handbook.md` if governance changes needed
3. Test thoroughly before deployment

---

**Built with ❤️ for local-first AI workflows**
