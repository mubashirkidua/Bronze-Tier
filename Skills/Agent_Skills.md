# 🛠️ Agent Skills

## Overview
This file tracks all skills and capabilities that the AI Employee can perform.

---

## Current Skills (Bronze Tier)

### Basic Skills
- [x] **File Management** - Create, read, edit, and organize files
- [x] **Task Tracking** - Log and track tasks in the vault
- [x] **Documentation** - Write clear notes and documentation
- [x] **Local Search** - Search through vault contents

---

## Skill Template (For Future Addition)

When adding a new skill, use this format:

```markdown
### [Skill Name]
- **Status:** [ ] Available / [ ] Disabled / [ ] Requires Approval
- **Description:** What this skill does
- **Triggers:** When to use this skill
- **Permissions:** What access it needs
- **HITL Required:** Yes/No (Human-in-the-Loop)
```

---

## How to Add New Skills

1. **Identify the Need**
   - What task should the AI perform?
   - Is it repetitive or time-consuming?

2. **Define the Skill**
   - Add a new section below using the template
   - Specify any approval requirements

3. **Test the Skill**
   - Try it on a small task first
   - Verify it works as expected

4. **Enable for Production**
   - Mark as "Available" once tested
   - Update the Dashboard if needed

---

## Planned Skills (Silver/Gold Tier)

- [ ] **Email Management** - Draft and send emails
- [ ] **Calendar Integration** - Schedule and manage appointments
- [ ] **Data Analysis** - Process and analyze datasets
- [ ] **Code Generation** - Write and review code
- [ ] **Research** - Web search and summarization
- [ ] **Automation** - Trigger workflows and scripts

---

## Skill Permissions Matrix

| Skill | Read | Write | Execute | External Access |
|-------|------|-------|---------|-----------------|
| File Management | ✅ | ✅ | ❌ | ❌ |
| Task Tracking | ✅ | ✅ | ❌ | ❌ |
| Documentation | ✅ | ✅ | ❌ | ❌ |

---

**Last Updated:** 2026-04-02
