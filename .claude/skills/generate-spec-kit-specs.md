---
name: generate-spec-kit-specs
description: Generate Spec-Kit Plus compatible Markdown specifications for Python in-memory Todo CLI applications. This skill translates high-level product requirements into detailed, unambiguous specifications that enable AI code generation without manual coding.
tags:
  - spec-driven-development
  - spec-kit-plus
  - markdown-specifications
  - todo-app
  - python-cli
---

# Generate Spec-Kit Plus Specifications

## Purpose

This skill enables the generation of comprehensive, Spec-Kit Plus compatible Markdown specifications for Python in-memory Todo CLI applications. It transforms high-level product requirements into detailed, unambiguous specifications that Claude Code can use to generate implementation code without manual human coding.

## Core Responsibility

Translate high-level product requirements into detailed, unambiguous, and Spec-Kit Plus compatible Markdown specifications. The output enables automated code generation by Claude Code without further clarification needed on the specification side.

## Technology Constraints (MANDATORY)

When using this skill, you must strictly adhere to the following technology constraints:

- Python 3.13+
- In-memory storage only (NO database)
- Console-based interface
- Spec-Kit Plus compatibility
- Claude Code tooling context
- NO manual coding by humans (output enables AI code generation)

## Required Features Coverage

Specifications generated using this skill must fully cover the following features:

1. Add Task
2. Delete Task
3. Update Task
4. View Task List
5. Mark Task as Complete / Incomplete

## Required Outputs

When executing this skill, you MUST generate the following Markdown files within the `specs/todo-app/` directory (or specified feature directory), ensuring they are fully compliant with Spec-Kit Plus standards:

- `specs/<feature>/spec.md`: Detailing the overall requirements and user stories for the Todo application.
- `specs/<feature>/plan.md`: Outlining the architectural design, key decisions, interfaces, and non-functional requirements.
- `specs/<feature>/tasks.md`: Breaking down features into small, testable tasks with acceptance criteria.

## Execution Workflow

### 1. Confirm Surface and Success Criteria

Briefly state your understanding of the current task (generating specifications for the Todo app) and the success criteria (complete, Spec-Kit Plus compliant, covering all features and constraints).

### 2. List Constraints, Invariants, Non-Goals

Explicitly restate the technology constraints, any invariants you identify, and non-goals (e.g., no persistent storage, no GUI).

### 3. Produce the Artifacts

#### Architectural Planning (plan.md)

- Begin by outlining the high-level architecture adhering to clean architecture principles for an in-memory console app.
- Define the core domain entities (e.g., Task), use cases (e.g., AddTask, DeleteTask), and interfaces (e.g., TaskRepository).
- Consider interface contracts: inputs, outputs, error conditions.
- Address non-functional requirements: performance (minimal for in-memory CLI), reliability (basic error handling), security (not applicable beyond basic input validation for CLI).
- Propose a clear structure for the application that supports future extensibility.

#### Feature Specification (spec.md)

- For each of the 5 required features, write detailed user stories and functional requirements.
- Describe expected user interactions for the console interface.
- Specify input parameters, expected behavior, and output format for each command.
- Include acceptance checks inlined where applicable (e.g., checkboxes or pseudo-tests).

#### Task Breakdown (tasks.md)

- Translate the features and architectural plan into a series of small, testable development tasks.
- For each task, clearly define its scope, dependencies, and explicit acceptance criteria.
- Ensure tasks are granular enough for individual implementation and testing.
- Maintain the smallest viable change principle.

### 4. Add Follow-ups and Risks

Identify potential future work, areas requiring more detail, or architectural risks (max 3 bullets).

### 5. Create PHR

After completing the specification generation, you **MUST** create a Prompt History Record (PHR) in `history/prompts/todo-app/<ID>-<slug>.spec.prompt.md` (or `plan.prompt.md`, `tasks.prompt.md` as appropriate) documenting the interaction and outputs, following the process detailed in `CLAUDE.md`.

### 6. ADR Suggestion

When a significant architectural decision is made (e.g., choice of in-memory data structure, command parsing approach, clean architecture layers), test for ADR significance (Impact, Alternatives, Scope). If all true, suggest documenting with: "📋 Architectural decision detected: [brief-description] — Document reasoning and tradeoffs? Run `/sp.adr [decision-title]`". Wait for user consent; never auto-create ADRs.

## Quality Assurance and Self-Correction

- Before finalizing any specification, re-read and verify that every requirement (features, constraints) has been addressed explicitly and unambiguously.
- Ensure all files are complete, internally consistent, and adhere to Spec-Kit Plus Markdown formatting.
- If any user requirement is ambiguous or leads to multiple valid architectural paths with significant tradeoffs, you MUST invoke the user for clarification, presenting options if applicable.
- Do not invent APIs or data structures; specify requirements clearly enough for them to be inferred or ask for clarification.
- Your output must enable automated code generation by Claude Code without further clarification needed on the specification side.

## Usage Context

This skill is designed for use in the context of **Phase I: Todo In-Memory Python Console App** from the document "Hackathon II – Todo Spec-Driven Development". It should be invoked when:

- Starting the specification phase for a Todo In-Memory Python Console App
- Continuing the Spec-Driven Development process for Todo applications
- Generating Spec-Kit Plus compatible specifications from high-level requirements

## Integration with Agents

This skill is the core capability of the `todo-spec-architect` agent. When the agent is invoked, it uses this skill to generate the required specification artifacts.

## Notes

- This skill focuses on **WHAT** needs to be built, not **HOW** to implement it.
- All specifications must be technology-agnostic where possible, focusing on user value and business needs.
- Specifications should be written for non-technical stakeholders while remaining precise enough for AI code generation.


